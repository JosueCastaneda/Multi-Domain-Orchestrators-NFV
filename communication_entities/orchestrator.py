import asyncio
import json
import logging
import os
import random
import sys
import time

import aiohttp

from communication_entities.generic_service import GenericService
from communication_entities.life_cycle_management import LifeCycleManagement
from communication_entities.matching_attribute import MatchingAttribute
from communication_entities.messages.lcm_messages.notification_lcm_operation import NotificationLCMOperation
from communication_entities.messages.vnf_forwarding_graph.corrective_negative_message import CorrectiveNegativeMessage
from communication_entities.messages.vnf_forwarding_graph.proposed_vnf_forwarding_graph_update_message import \
    ProposedVNFForwardingGraphUpdateMessage
from communication_entities.messages.vnf_forwarding_graph.reply_proposed_vnf_forwarding_graph_update_message import \
    ReplyProposedVNFForwardingGraphUpdateMessage
from communication_entities.messages.vnf_forwarding_graph.update_vnf_forwarding_graph import UpdateVNFForwardingGraph
from communication_entities.messages.vnf_forwarding_graph.vnf_forwarding_graph_update_message_corrective import \
    VNFForwardingGraphUpdateMessageCorrective
from communication_entities.orchestrator_classes.pending_lcm_scaling_operation import PendingLCMScalingOperation
from communication_entities.vector_clock import VectorClock
from communication_entities.vnf_connection_point_reference import ConnectionPointReference
from communication_entities.vnf_forwarding_graph import VNFForwardingGraph
from definitions import ROOT_DIR
from utilities.life_cycle_management_update import return_success, return_failure, return_in_process, send_message, \
    generate_random_number_between_zero_one_hundred

sys.path.append('../')


def is_orchestrator_included_for_notification(id_orchestrator, excluding_list):
    for orchestrator in excluding_list:
        if isinstance(orchestrator, str):
            if id_orchestrator == orchestrator:
                return False
        elif id_orchestrator == orchestrator['id']:
            return False
    return True


class Orchestrator:

    def __init__(self, experiment_index, orchestrator_index, server_host, server_port, random_seed,
                 causal_delivery=False, algorithm_type='causal', waiting_time=30, probability_repeated_messages=30):
        self.waiting_time = waiting_time
        self.log = None
        self.probability_repeated_message = probability_repeated_messages
        print('Waiting time: ' + str(self.waiting_time) + ' Probability: ' + str(self.probability_repeated_message))
        self.experiment_name = 'experiment_' + experiment_index
        self.experiment_index = experiment_index
        self.name = 'orch_' + orchestrator_index
        self.orchestrator_index = orchestrator_index
        self.orchestrator_counter = 0
        self.directory_path = 'experiments/experiment_' + self.experiment_index + '/'
        self.id = ''
        self.location = ''
        self.orchestrators_ids = []
        self.ip = server_host
        self.port = server_port
        self.list_vnf = dict()
        self.list_orchestrator = list()
        self.pending_lcm_operations = list()
        self.topology = None
        self.services = list()
        self.set_up_my_logger()
        self.vnfs = list()
        self.vnf_forwarding_graphs = list()
        self.inconsistencies = 0
        self.messages_sent = 0
        self.load_server_information()
        self.add_service_information()
        self.life_cycle_manager = LifeCycleManagement(self, self.vnfs, self.services)
        self.vector_clock = VectorClock(self.id)
        self.causal_delivery = False
        self.causal_delivery = causal_delivery
        self.random_seed = random_seed
        # self.random_seed = 11240
        self.pending_operations_repetitions = 0
        self.time_elapsed_in_reconfiguration = 0.0
        self.algorithm_type = algorithm_type
        random.seed(self.random_seed)
        self.total_time_for_experimentation = 0.0
        self.list_pending_vnf_forwarding_updates = []
        # self.log.info('My orchestrator index is: ' + str(self.orchestrator_index))
        # self.log.info('Orchestrator is running')

    def add_vnf_forwarding_graph(self, vnf_forwarding_graphs):
        string_1 = ROOT_DIR + '/' + 'experiments/experiment_'
        directory_path = string_1 + str(self.experiment_index) + '/' + 'experiment_' + str(self.experiment_index)
        with open(directory_path + '.json') as json_file:
            raw_data = json.load(json_file)
        for orchestrator in raw_data['orchestrators']:
            self.orchestrators_ids.append(orchestrator['id'])

        for vnf_fg_entry in vnf_forwarding_graphs:
            new_vnf_fg = VNFForwardingGraph(identifier=vnf_fg_entry['identifier'],
                                            name=vnf_fg_entry['name'],
                                            short_name=vnf_fg_entry['short_name'],
                                            is_shared=vnf_fg_entry['is_shared'],
                                            service_identifier=vnf_fg_entry['service_identifier'],
                                            my_orchestrator=self.id)

            new_vnf_fg.instantiate_classification_rules(vnf_fg_entry, self.orchestrators_ids)
            new_vnf_fg.instantiate_rendered_service_path(vnf_fg_entry, self.orchestrators_ids)
            new_vnf_fg.add_unique_orchestrators(vnf_fg_entry['unique_orchestrators'])
            self.vnf_forwarding_graphs.append(new_vnf_fg)

    def load_server_information(self):
        all_route = ROOT_DIR + '/' + self.directory_path + self.experiment_name + '.json'
        with open(all_route) as json_file:
            raw_data = json.load(json_file)

        orchestrator_number = self.name.find('_')
        orchestrator_index = int(self.name[orchestrator_number + 1:])
        self.id = raw_data['orchestrators'][orchestrator_index]['id']
        self.location = raw_data['orchestrators'][orchestrator_index]['location']

    def find_orchestrator_by_id(self, id_orchestrator):
        for orchestrator in self.list_orchestrator:
            if orchestrator['id'] == id_orchestrator:
                return orchestrator
        my_orchestrator = dict()
        my_orchestrator['ip'] = self.ip
        my_orchestrator['port'] = self.port
        my_orchestrator['name'] = self.name
        my_orchestrator['id'] = self.id
        return my_orchestrator

    def add_service_information(self):
        self.load_vnf_components()

    async def get_inconsistencies(self):
        return self.inconsistencies

    async def get_messages_sent(self):
        return self.messages_sent

    async def get_time_elapsed_reconfiguration(self):
        return self.time_elapsed_in_reconfiguration

    async def request_service_scale(self, service_id) -> json:
        self.time_elapsed_in_reconfiguration = 0.0
        self.inconsistencies = 0
        self.life_cycle_manager.are_VNFs_scaled = False
        self.vector_clock.increment_clock(self.id)
        self.pending_operations_repetitions = 0
        for service in self.services:
            if service.id == service_id:
                service_as_dictionary = service.create_service_as_dictionary_and_add_pending_operations_to_service()
                self.life_cycle_manager.add_new_service_to_scale(service.id, service_as_dictionary)
                await service.scale()
                return return_success()
        return return_failure('Service requested to scale not found')

    async def get_services(self):
        list_of_services = list()
        for service in self.services:
            list_of_services.append(service.as_string())
        return list_of_services

    async def get_vnf_forwarding_graphs(self):
        vnf_forwarding_graphs = list()
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            vnf_forwarding_graphs.append(vnf_forwarding_graph.as_dictionary())
        return vnf_forwarding_graphs

    def get_orchestrator_information_by_id(self, orchestrator_id):
        for orchestrator in self.list_orchestrator:
            if orchestrator['id'] == orchestrator_id:
                return orchestrator
        return self.entry_as_dictionary()

    def entry_as_dictionary(self):
        orchestrator_format = dict()
        orchestrator_format['ip'] = self.ip
        orchestrator_format['port'] = self.port
        orchestrator_format['id'] = self.id
        orchestrator_format['name'] = self.name
        orchestrator_format['experiment_name'] = self.experiment_name
        orchestrator_format['experiment_index'] = self.experiment_index
        orchestrator_format['is_causal'] = self.causal_delivery
        orchestrator_format['algorithm_type'] = self.algorithm_type
        orchestrator_format['vector_clock'] = self.vector_clock.as_string()
        orchestrator_format['inconsistencies'] = self.inconsistencies
        orchestrator_format['random_seed'] = self.random_seed
        orchestrator_format['messages_sent'] = self.messages_sent
        orchestrator_format['pending_operations'] = len(self.pending_lcm_operations)
        orchestrator_format['time_elapsed_in_last_reconfiguration'] = self.time_elapsed_in_reconfiguration
        orchestrator_format['total_time_for_experimentation'] = self.total_time_for_experimentation
        return orchestrator_format

    def get_service_by_id(self, service_id):
        for service in self.services:
            if service.id == service_id:
                return service

    async def wait_before_notification(self, data):
        wait_period = random.randint(0, self.waiting_time)
        await asyncio.sleep(wait_period)
        await self.notification_of_lcm(data)

    def set_up_my_logger(self):
        file_name = 'logs/file_' + self.name + '_' + self.experiment_index + '.log'
        other_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', file_name))
        logging.basicConfig(filename=other_folder)
        self.log = logging.getLogger('logger')
        self.log.propagate = False
        self.log.setLevel(logging.DEBUG)
        log_str = '%(asctime)s - %(filename)s - %(lineno)s - %(message)s'
        formatter = logging.Formatter(log_str)
        fh = logging.FileHandler(other_folder, mode='w', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.log.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        self.log.addHandler(ch)

    def add_inconsistency(self):
        self.inconsistencies += 1

    async def notification_of_lcm(self, data):
        my_clock_is_greater = False
        vector_clock_string = data['vector_clock']
        sender_id = data['orchestrator_sender_id']
        other_clock = VectorClock()
        other_clock.create_from_list(vector_clock_string)
        causality = False
        my_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(data)
        if self.algorithm_type == 'causal':
            causality = True
        if sender_id == self.id:
            vector_difference = 0
        else:
            vector_difference = self.compute_vector_clock_difference(my_clock, other_clock, sender_id, causality)
            my_clock_is_greater = my_clock.is_greater_than_other(other_clock)
        if my_clock_is_greater and self.algorithm_type == 'causal':
            pass
        else:
            await self.apply_notification_of_lifecycle_management_operation(vector_difference, other_clock, sender_id, data, my_clock_is_greater)
            self.pending_operations_repetitions = 0
        return_success()

    def get_clock_from_entry_of_vnf_forwarding_graph(self, data) -> VectorClock:
        clock = None
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if vnf_forwarding_graph.get_identifier() == data['vnffg_identifier']:
                if data['type_of_change_attribute'] == 'connection_point':
                    path = vnf_forwarding_graph.get_first_rendered_service_path()
                    clock = path.get_clock_from_connection_point_entry(data['identifier'])
                else:
                    rule = vnf_forwarding_graph.get_first_classifier_rule()
                    clock = rule.get_clock_from_matching_attribute_entry(data['identifier'])
        return clock

    def compute_vector_clock_difference(self, first_clock, second_clock, sender_id, causal_delivery):
        difference_in_vectors = first_clock.compare_clocks(second_clock, sender_id, causal_delivery, self.log)
        return difference_in_vectors

    async def apply_notification_of_lifecycle_management_operation(self, vector_difference, vector_clock, sender, data=None, my_clock_is_greater=False):
        if self.algorithm_type == 'causal':
            await self.notification_of_lcm_causal(vector_difference, vector_clock, sender, data)
        elif self.algorithm_type == 'standard':
            if vector_difference > 1 or my_clock_is_greater:
                self.log.info('Adding inconsistency, so far: ' + str(self.inconsistencies))
                self.add_inconsistency()
            await self.notification_of_lcm_normal(vector_difference, vector_clock, sender)
        elif self.algorithm_type == 'last_writer_wins':
            await self.notification_of_lcm_last_writer_wins(vector_difference, vector_clock, sender)
        elif self.algorithm_type == 'multi_value':
            await self.notification_of_lcm_multi_value(vector_difference, vector_clock, sender)

    async def notification_of_lcm_last_writer_wins(self, difference_in_vectors, vector_clock, sender):
        pass

    async def notification_of_lcm_multi_value(self, difference_in_vectors, vector_clock, sender):
        pass

    async def notification_of_lcm_causal(self, difference_in_vectors, vector_clock, orchestrator_sender_id, data=None):
        if difference_in_vectors <= 1:
            await self.apply_notification_of_lcm_operation(vector_clock, orchestrator_sender_id, data)
        else:
            if data:
                my_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(data)
                if my_clock.are_different(vector_clock.clock_list):
                    start = time.time()
                    data['buffer_time'] += start
                    new_pending_operation = PendingLCMScalingOperation(vnf_component_to_scale_id='',
                                                                       operation='notification',
                                                                       original_service_id='',
                                                                       orchestrator_sender_id=orchestrator_sender_id,
                                                                       original_orchestrator_id='',
                                                                       sender_vector_clock=vector_clock,
                                                                       service_sender_id='',
                                                                       vnffg_data=data)
                    self.add_pending_operation(new_pending_operation)

    async def notification_of_lcm_normal(self, difference_in_vectors, vector_clock, orchestrator_sender_id):
        if difference_in_vectors > 1:
            self.log.info('Adding inconsistency, so far: ' + str(self.inconsistencies))
            self.add_inconsistency()
        await self.apply_notification_of_lcm_operation(vector_clock, orchestrator_sender_id)

    async def apply_notification_of_lcm_operation(self, vector_clock, orchestrator_sender_id, data=None):
        my_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(data)
        if not my_clock.is_equal(vector_clock):
            start = time.time()
            my_clock.update_clock(vector_clock, orchestrator_sender_id, self.log)
            end_time = time.time()
            time_difference = end_time - start
            self.total_time_for_experimentation += time_difference
        total_pending_operations = len(self.pending_lcm_operations)
        if total_pending_operations > 0:
            await self.do_pending_lcm_notifications_notifications()

    async def notify_all_orchestrators_of_change(self, result):
        list_of_replicas_to_notify = result['replicas']
        list_of_replicas_to_notify.append(self.id)
        data = dict()
        data['vector_clock'] = result['vector_clock']
        data['orchestrator_sender_id'] = self.id
        data['type'] = self.algorithm_type
        data['orchestrator_counter'] = self.orchestrator_counter
        data['orchestrator_index'] = self.orchestrator_index
        data['identifier'] = result['identifier']
        data['vnffg_identifier'] = result['vnffg_identifier']
        data['vnffg_name'] = result['vnffg_name']
        data['vnffg_short_name'] = result['vnffg_short_name']
        data['type_of_change_attribute'] = result['type_of_change_attribute']
        for orchestrator in self.list_orchestrator:
            if is_orchestrator_included_for_notification(orchestrator['id'], list_of_replicas_to_notify):
                new_message = NotificationLCMOperation(orchestrator['ip'], str(orchestrator['port']), data)
                self.increment_sent_messages()
                await asyncio.create_task(send_message(new_message))

    def increment_sent_messages(self):
        self.messages_sent += 1

    async def do_pending_lcm_notifications_notifications(self):
        at_least_one_clock_changed = True
        while at_least_one_clock_changed:
            change_took_place = await self.repeat_lcm_operations()
            at_least_one_clock_changed = change_took_place

    async def repeat_lcm_operations(self):
        change_took_place = False
        repetitions_message = 0
        total_pending_operations = len(self.pending_lcm_operations)

        my_repetitions_are_lesser = self.pending_operations_repetitions < total_pending_operations
        message_repetitions_are_lesser = repetitions_message < total_pending_operations

        while self.pending_lcm_operations and message_repetitions_are_lesser and my_repetitions_are_lesser:
            repetitions_message += 1
            pending_operation = self.pending_lcm_operations.pop(0)

            if type(pending_operation.sender_vector_clock) == str:
                new_vector_clock = VectorClock()
                new_vector_clock.create_from_list(pending_operation.sender_vector_clock)
                pending_operation.set_vector_clock(new_vector_clock)

            difference_in_clocks = self.compute_clock_difference(pending_operation)
            change_result = False
            if self.algorithm_type == 'causal':
                change_result = await self.repeat_lcm_operations_causal(difference_in_clocks, pending_operation)
            elif self.algorithm_type == 'normal':
                change_result = await self.repeat_lcm_operations_normal(difference_in_clocks, pending_operation)
            change_took_place = change_result
            if change_took_place:
                repetitions_message = 0
            my_repetitions_are_lesser = self.pending_operations_repetitions < total_pending_operations
            message_repetitions_are_lesser = repetitions_message < total_pending_operations
        return change_took_place

    async def repeat_lcm_operations_causal(self, difference_in_clocks, pending_operation):
        change_took_place = False
        if difference_in_clocks <= 1 and pending_operation.is_not_done:
            change_took_place = await self.apply_lcm_operation(pending_operation)
            if change_took_place:
                end_time = time.time()
                self.total_time_for_experimentation += (end_time - pending_operation.vnffg_data['buffer_time'])
        else:
            self.add_pending_operation(pending_operation)
        return change_took_place

    async def repeat_lcm_operations_normal(self, difference_in_clocks, pending_operation):
        if difference_in_clocks > 1:
            self.log.info('Adding inconsistency, so far: ' + str(self.inconsistencies))
            self.add_inconsistency()
        return await self.apply_lcm_operation(pending_operation)

    def compute_clock_difference(self, pending_operation):
        causal_delivery = False
        if self.algorithm_type == 'causal':
            causal_delivery = True
        my_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(pending_operation.vnffg_data)
        other_clock = pending_operation.sender_vector_clock
        sender_id = pending_operation.orchestrator_sender_id
        difference_in_clocks = self.compute_vector_clock_difference(my_clock, other_clock, sender_id, causal_delivery)
        return difference_in_clocks

    async def apply_lcm_operation(self, pending_operation):
        change_result = True
        if pending_operation.operation == 'notification':
            pending_operation.is_not_done = False
            await self.apply_notification_operation(pending_operation)
        elif pending_operation.operation == 'scale' or pending_operation.operation == 'scaling':
            pending_operation.is_not_done = False
            await self.apply_scaling_operation(pending_operation)
        elif pending_operation.operation == 'vnf_fg_update':
            pending_operation.is_not_done = False
            my_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(pending_operation.vnffg_data)
            my_clock.update_clock_with_a_string(pending_operation.sender_vector_clock, self.log)
            await self.apply_vnf_fg_update_notification(pending_operation.data)
        else:
            change_result = False
        return change_result

    async def apply_notification_operation(self, pending_operation):
        my_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(pending_operation.vnffg_data)
        my_clock.update_clock(pending_operation.sender_vector_clock, pending_operation.orchestrator_sender_id, self.log)
        pending_operation.is_not_done = False

    async def apply_scaling_operation(self, pending_operation):
        pending_operation.is_not_done = False
        await self.life_cycle_manager.scale_confirmation(pending_operation.vnf_component_to_scale_id,
                                                         pending_operation.original_service_id,
                                                         pending_operation.orchestrator_sender_id,
                                                         pending_operation.original_orchestrator_id,
                                                         pending_operation.sender_vector_clock,
                                                         pending_operation.service_sender_id)

    async def wait_before_delivery_grant(self, vnf_component_to_scale_id, operation, original_service,
                                         sender_vector_clock=None):
        wait_period = random.randint(0, self.waiting_time)
        await asyncio.sleep(wait_period)
        await self.grant_lcm_operation_of_service(vnf_component_to_scale_id, operation, original_service,
                                                  sender_vector_clock)
        return return_in_process('Grant in process')

    async def grant_lcm_operation_of_service(self, vnf_component_to_scale_id, operation, original_service,
                                             sender_vector_clock=None):
        if self.causal_delivery:
            await self.grant_lcm_operation_causal(vnf_component_to_scale_id, operation, original_service,
                                                  sender_vector_clock)
        else:
            await self.grant_lcm_operation_normal(vnf_component_to_scale_id, operation, original_service,
                                                  sender_vector_clock)

    def compute_difference_in_vectors(self, original_service, sender_vector_clock) -> int:
        causal_delivery = False
        if self.algorithm_type == 'causal':
            causal_delivery = True

        if original_service['orchestrator_id'] != self.id:
            return self.vector_clock.compare_clocks(sender_vector_clock,
                                                    original_service['orchestrator_id'],
                                                    causal_delivery,
                                                    self.log)
        return 100

    async def do_lcm_operation(self, service, sender_vector_clock, operation, vnf_component):
        if service['orchestrator_id'] != self.id:
            self.vector_clock.update_clock(sender_vector_clock, service['orchestrator_id'], self.log)
        await asyncio.gather(self.scale_vnf_component_operation(vnf_component, service), self.do_pending_operations())

    async def grant_lcm_operation_causal(self, vnf_component_to_scale_id, operation, original_service,
                                         sender_vector_clock=None):
        difference_in_vectors = self.compute_difference_in_vectors(original_service, sender_vector_clock)
        if difference_in_vectors <= 1 or self.vector_clock.is_equal(sender_vector_clock):
            await self.do_lcm_operation(original_service, sender_vector_clock, operation, vnf_component_to_scale_id)
        else:
            new_operation = PendingLCMScalingOperation(vnf_component_to_scale_id,
                                                       operation,
                                                       original_service['original_service_id'],
                                                       self.id,
                                                       original_service['orchestrator_id'],
                                                       sender_vector_clock,
                                                       original_service['id'],
                                                       original_service)
            self.add_pending_operation(new_operation)

    async def grant_lcm_operation_normal(self, vnf_component_to_scale_id, operation, original_service,
                                         sender_vector_clock=None):
        difference_in_vectors = self.compute_difference_in_vectors(original_service, sender_vector_clock)
        if difference_in_vectors > 1:
            self.log.info('Adding inconsistency, so far: ' + str(self.inconsistencies))
            self.add_inconsistency()
        await self.do_lcm_operation(original_service, sender_vector_clock, operation, vnf_component_to_scale_id)

    def add_pending_operation(self, new_operation) -> None:
        self.pending_lcm_operations.append(new_operation)

    async def scale_vnf_component_operation(self, vnf_component_to_scale_id, original_service):
        service_to_scale = self.get_service_by_id(vnf_component_to_scale_id)
        self.life_cycle_manager.add_new_service_to_scale(vnf_component_to_scale_id, original_service)
        is_ok_to_scale, no_dependencies = service_to_scale.validate_scaling()
        if is_ok_to_scale:
            await service_to_scale.independent_scale_causal(vnf_component_to_scale_id,
                                                            original_service['original_service_id'],
                                                            original_service['orchestrator_id'])

    async def do_pending_operations(self):
        self.pending_operations_repetitions += 1
        clock_was_updated = True
        while clock_was_updated:
            at_least_one_clock_changed = await self.repeat_operation_store_clock()
            clock_was_updated = at_least_one_clock_changed
        self.pending_operations_repetitions = 0

    async def repeat_operation_store_clock(self):
        at_least_one_clock_changed = False
        repetitions_message = 0
        total_pending_operations = len(self.pending_lcm_operations)
        message_repetitions_are_lesser = repetitions_message < total_pending_operations
        my_repetitions_are_lesser = self.pending_operations_repetitions < total_pending_operations

        while self.pending_lcm_operations and message_repetitions_are_lesser and my_repetitions_are_lesser:
            repetitions_message += 1
            operation = self.pending_lcm_operations.pop(0)
            if operation.is_not_done and self.vector_clock.compare_stored_clock(operation.sender_vector_clock,
                                                                                self.causal_delivery):
                if operation.operation == 'scale' or operation.operation == 'scaling':
                    operation.is_not_done = False
                    at_least_one_clock_changed = True
                    await self.grant_lcm_operation_causal(operation.vnf_component_to_scale_id, 'scale',
                                                          operation.original_service, operation.sender_vector_clock)
            else:
                self.add_pending_operation(operation)
            message_repetitions_are_lesser = repetitions_message < total_pending_operations
            my_repetitions_are_lesser = self.pending_operations_repetitions < total_pending_operations
        return at_least_one_clock_changed

    def load_vnf_components(self):
        all_route = ROOT_DIR + '/' + self.directory_path + self.experiment_name + '.json'
        with open(all_route) as json_file:
            raw_data = json.load(json_file)
        orchestrator_number = self.name.find('_')
        orchestrator_index = int(self.name[orchestrator_number + 1:])
        my_orchestrator = raw_data['orchestrators'][orchestrator_index]
        self.vnfs = raw_data['orchestrators'][orchestrator_index]['vnfs']
        if self.ip == '127.0.0.1':
            my_ip = self.ip
            for vnf in self.vnfs:
                vnf['server'] = self.ip
        else:
            my_ip = str(my_orchestrator['ip'])
        self.instantiate_services(my_orchestrator['services'], my_ip)
        self.add_vnf_forwarding_graph(my_orchestrator['vnf-forwarding_graphs'])

    async def get_pending_operations(self):
        pending_operations = self.life_cycle_manager.pending_operations
        for operation in pending_operations:
            operation['start_time'] = ''
        return pending_operations

    def instantiate_services(self, services, ip):
        for service in services:
            new_service = GenericService(service['id'],
                                         self,
                                         service['dependencies'],
                                         ip,
                                         self.port)
            self.services.append(new_service)

    def print_state_vnf(self):
        self.log.info(''.join(["VNF name: ", self.name]))

    def get_local_vnf(self, vnf_name):
        return self.list_vnf.get(vnf_name)

    async def add_orchestrator(self, orchestrator_information) -> json:
        try:
            new_orchestrator = dict()
            new_orchestrator['ip'] = orchestrator_information['ip']
            new_orchestrator['port'] = int(orchestrator_information['port'])
            new_orchestrator['name'] = orchestrator_information['name']
            new_orchestrator['id'] = orchestrator_information['id']
            self.list_orchestrator.append(new_orchestrator)
            self.vector_clock.add_clock(orchestrator_information['id'])
            return return_success()
        except Exception as e:
            return return_failure(str(e))

    async def add_vnf(self, vnf_information):
        self.list_vnf[vnf_information.name] = vnf_information
        return return_success()

    async def get_vnfs(self):
        return self.vnfs

    async def get_orchestrators(self):
        return self.list_orchestrator

    async def get_log_file(self) -> str:
        file_name = 'test.log'
        with open(file_name, 'r') as file:
            data = file.read()
        return data

    async def update_unique_vnf_forwarding_graph_rendered_service_path(self, connection_point: ConnectionPointReference):
        if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
            await self.update_unique_vnf_forwarding_graph_connection_point_causal_standard(connection_point)
        elif self.algorithm_type == 'preventive':
            await self.update_unique_vnf_forwarding_graph_connection_point_preventive(connection_point)
        elif self.algorithm_type == 'corrective':
            # self.log.info('Doing corrective')
            await self.update_unique_vnf_forwarding_graph_connection_point_corrective(connection_point)

    async def update_unique_vnf_forwarding_graph_connection_point_corrective(self, connection_point: ConnectionPointReference):
        pass
        # # Fix later concentrate on the attribute
        # self.log.info('Doing this part :)')
        # self.log.info('Doing corrective unique for attribute ' + str(connection_point.get_vnf_identifier()[0:8]))
        # data = dict()
        # how_many_vnfs_have_it = 0
        # for vnf_forwarding_graph in self.vnf_forwarding_graphs:
        #     if vnf_forwarding_graph.has_connection_point(connection_point):
        #         # CHECK THIS FUNCTION
        #         data = connection_point.as_dictionary()
        #         data['type'] = 'connection_point'
        #         data['update'] = 'corrective'
        #         data['attribute_id'] = connection_point.vnf_identifier
        #         data['current_max_orchestrator_index'] = self.orchestrator_index
        #         new_entry = await vnf_forwarding_graph.update_data(data, self.log)
        #         how_many_vnfs_have_it += 1
        #
        #         self.log.info('How many VNF-FGs have it ' + str(how_many_vnfs_have_it))
        #         # self.log.info('Trying to send to alls')
        #         # data = self.get_vnf_forwarding_graph_by_connection_point(connection_point)
        #         entry = new_entry.as_dictionary()
        #         entry['attribute_id'] = connection_point.vnf_identifier
        #         entry['update'] = 'corrective'
        #         entry['type'] = 'connection_point'
        #         entry['affected_orchestrators'] = vnf_forwarding_graph.get_affected_orchestrators()
        #         entry['sender_id'] = self.port
        #         await self.send_update_vnf_forwarding_graph_notification_to_affected_orchestrators(entry, entry['affected_orchestrators'])
        #
        #         # self.log.info(vnf_forwarding_graph.as_dictionary())
        #         # ERROR: Here it could be repeated for some reason...
        #         break
        # self.log.info('How many VNF-FGs have it ' + str(how_many_vnfs_have_it))


    async def update_unique_vnf_forwarding_graph_connection_point_causal_standard(self, connection_point: ConnectionPointReference):
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if len(connection_point.list_of_orchestrator_id) == 0:
                connection_point.list_of_orchestrator_id = self.orchestrators_ids
                connection_point.add_clocks()

            list_caller = dict()
            list_caller['caller'] = self.id
            list_caller['first_call'] = True
            update_result = await vnf_forwarding_graph.update_unique_rendered_service_path(connection_point, self.log, self.orchestrator_index, list_caller)
            if update_result['is_positive_result']:
                result = await self.notify_all_replicas_and_orchestrators_of_positive_change(update_result)
                return result
        return return_failure('No VNF ID FOUND! ' + str(connection_point.get_vnf_identifier()))

    # TODO: Change this quick fix function by separating in each orchestrator
    async def update_unique_vnf_forwarding_graph_classifier_rule_causal_standard(self, attribute: MatchingAttribute):
        if len(attribute.list_of_orchestrator_id) == 0:
            attribute.list_of_orchestrator_id = self.orchestrators_ids
            attribute.add_clocks()

        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            list_caller = dict()
            list_caller['caller'] = self.id
            list_caller['first_call'] = True
            update_result = await vnf_forwarding_graph.update_unique_classifier_rule(attribute, self.log, list_caller)

            if update_result['is_positive_result']:
                result = await self.notify_all_replicas_and_orchestrators_of_positive_change(update_result)
                return result
        return return_failure('No Matching attribute with ID found! ' + str(attribute.get_identifier()))

    def get_vnf_forwarding_graph_by_attribute(self, attribute: MatchingAttribute):
        data = dict()
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if vnf_forwarding_graph.has_matching_attribute(attribute):
                vnf_forwarding_graph.increase_message_for_attribute(attribute)
                counter_data = vnf_forwarding_graph.get_counter_for_attribute(attribute)
                data = self.fill_data_of_vnf_forwarding_graph(vnf_forwarding_graph, counter_data)
                break
        return data

    def get_vnf_forwarding_graph_by_connection_point(self, connection_point: ConnectionPointReference):
        data = dict()
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if vnf_forwarding_graph.has_connection_point(connection_point):
                vnf_forwarding_graph.increase_message_for_connection_point(connection_point)
                counter_data = vnf_forwarding_graph.get_counter_for_connection_point(connection_point)
                data = self.fill_data_of_vnf_forwarding_graph(vnf_forwarding_graph, counter_data)
                break
        return data

    def fill_data_of_vnf_forwarding_graph(self, vnf_forwarding_graph, counter_data):
        data = dict()
        data['vnf_forwarding_graph_identifier'] = vnf_forwarding_graph.identifier
        data['affected_orchestrators_replicas'] = vnf_forwarding_graph.set_unique_orchestrators
        data['affected_orchestrators_dependencies'] = vnf_forwarding_graph.set_unique_dependencies
        data['attribute_counter'] = counter_data['attribute_counter']
        data['current_max_orchestrator_index'] = counter_data['current_max_orchestrator_index']
        data['messages_sent'] = counter_data['messages_sent']
        data['affected_orchestrators'] = vnf_forwarding_graph.get_affected_orchestrators()
        list_orchestrators_id = dict()
        list_orchestrators_id[self.id] = False
        for orchestrator in vnf_forwarding_graph.set_unique_orchestrators:
            list_orchestrators_id[orchestrator] = False
        for orchestrator in vnf_forwarding_graph.set_unique_dependencies:
            list_orchestrators_id[orchestrator] = False
        data['affected_vnf_forwarding_graphs'] = list_orchestrators_id
        return data

    # TODO: Change this quick fix function by separating in each orchestrator
    async def update_unique_vnf_forwarding_graph_classifier_rule_preventive(self, attribute: MatchingAttribute):
        # self.log.info('First update of matching attribute')
        data = self.get_vnf_forwarding_graph_by_attribute(attribute)
        entry = await self.fill_entry_with_data(data)
        entry['attribute_id'] = attribute.identifier
        entry['type'] = 'matching_attribute'
        await self.add_to_pending_list_and_send_message(entry, attribute)

    async def update_unique_vnf_forwarding_graph_connection_point_preventive(self, connection_point: ConnectionPointReference):
        # self.log.info('First update of connection point')
        data = self.get_vnf_forwarding_graph_by_connection_point(connection_point)
        entry = await self.fill_entry_with_data(data)
        entry['attribute_id'] = connection_point.vnf_identifier
        entry['type'] = 'connection_point'
        await self.add_to_pending_list_and_send_message(entry, connection_point)

    async def add_to_pending_list_and_send_message(self, entry, item):
        entry['value'] = item.as_dictionary()
        entry_as_json = json.dumps(entry)
        self.list_pending_vnf_forwarding_updates.append(entry)
        # self.log.info(entry)
        str_log = str(entry['attribute_id'][0:8]) + ' Counter: ' + str(entry['attribute_counter']) + ' Max.' + str(entry['current_max_orchestrator_index']) + ' Messages ' + str(entry['messages_sent'])
        self.log.info('New value: ' + str_log)
        # my_status = GODZI
        # self.list_pending_vnf_forwarding_updates.append(data)
        str_my_status=''
        for pending in self.list_pending_vnf_forwarding_updates:
            if pending['attribute_id'] == entry['attribute_id']:
                str_my_status = ' ['
                for affected_orch, value in pending['affected_vnf_forwarding_graphs'].items():
                    my_orch = self.find_orchestrator_by_id(affected_orch)
                    str_my_status += '('+str(my_orch['port']) + ' ' + str(value) + '), '
                str_my_status += ']'

        # self.log.info('My status')
        # self.log.info(self.list_pending_vnf_forwarding_updates[0])

        for orch in entry['affected_orchestrators']:
            orch_def = self.find_orchestrator_by_id(orch)
            self.log.info('Sending to: ' + str(orch_def['ip']) + ':' + str(orch_def['port']) + str(str_my_status))
        await self.send_json_encoded_message(entry['affected_orchestrators'], entry_as_json)

    async def send_json_encoded_message(self, orchestrator_identifiers, entry):
        for orchestrator in orchestrator_identifiers:
            if orchestrator != self.id:
                my_orch = self.find_orchestrator_by_id(orchestrator)
                new_message = ProposedVNFForwardingGraphUpdateMessage(my_orch['ip'], str(my_orch['port']), entry)
                self.increment_sent_messages()
                await asyncio.create_task(self.send_message_with_json(new_message))

    async def fill_entry_with_data(self, data) -> dict:
        entry = dict()
        entry['orchestrator_id'] = self.id
        entry['vnf_forwarding_graph_id'] = data['vnf_forwarding_graph_identifier']
        entry['attribute_counter'] = data['attribute_counter'] + 1
        entry['current_max_orchestrator_index'] = self.orchestrator_index
        entry['affected_vnf_forwarding_graphs'] = data['affected_vnf_forwarding_graphs']
        entry['affected_vnf_forwarding_graphs'][self.id] = True
        entry['affected_orchestrators_replicas'] = data['affected_orchestrators_replicas']
        entry['affected_orchestrators_dependencies'] = data['affected_orchestrators_dependencies']
        entry['messages_sent'] = data['messages_sent']
        entry['affected_orchestrators'] = data['affected_orchestrators']
        entry['type'] = 'matching_attribute'
        return entry

    async def   send_message_with_json(self, message):
        url = 'http://' + message.host + ':' + str(message.port) + '/' + message.type
        # self.log.info(url)
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=message.data) as resp:
                str_log_encoded = await (resp.text())

    def get_entry_from_list(self, data):
        for entry in self.list_pending_vnf_forwarding_updates:
            is_same_vnf_forwarding_graph = entry['vnf_forwarding_graph_id'] == data['vnf_forwarding_graph_id']
            is_same_attribute = entry['attribute_id'] == data['attribute_id']
            is_same_counter = entry['attribute_counter'] == data['attribute_counter']
            is_same_max_index = entry['current_max_orchestrator_index'] == data['current_max_orchestrator_index']
            is_same_messages = entry['messages_sent'] == data['messages_sent']
            if is_same_vnf_forwarding_graph and is_same_attribute and is_same_counter and is_same_max_index and is_same_messages:
                return entry

    # TODO: Update this function to pass. Now is a stub
    def check_is_valid_change(self, data):
        # random.seed(1324)
        random_number = random.randint(0, 100)
        # random_number = generate_random_number_between_zero_one_hundred()
        if random_number > 70:
            self.log.info('Negated ' + data['attribute_id'][0:8])
            return False
        return True

    def are_all_positive(self, data):
        answer = False
        for entry in self.list_pending_vnf_forwarding_updates:
            is_same_vnf_forwarding_graph = entry['vnf_forwarding_graph_id'] == data['vnf_forwarding_graph_id']
            is_same_attribute = entry['attribute_id'] == data['attribute_id']
            is_same_counter = entry['attribute_counter'] == data['attribute_counter']
            is_same_max_index = entry['current_max_orchestrator_index'] == data['current_max_orchestrator_index']
            is_same_messages = entry['messages_sent'] == data['messages_sent']
            if is_same_vnf_forwarding_graph and is_same_attribute and is_same_counter and is_same_max_index and is_same_messages:
                my_answer = True
                for vnf_fg_entry, value in entry['affected_vnf_forwarding_graphs'].items():
                    if not value:
                        my_answer = False
                answer = my_answer
                return answer
        return answer

    async def mark_as_positive_update_and_apply_if_full(self, data):
        my_entry = self.get_entry_from_list(data)
        # self.log.info('MARK A')
        self.log.info('Before update: ' + data['attribute_id'][0:8] + ' ' + str(my_entry['affected_vnf_forwarding_graphs']))
        my_entry['affected_vnf_forwarding_graphs'][self.id] = True
        my_entry['affected_vnf_forwarding_graphs'][data['orchestrator_id']] = True
        # self.log.info('MARK B')
        self.log.info('After update: ' + data['attribute_id'][0:8] + ' ' + str(my_entry['affected_vnf_forwarding_graphs']))
        all_positive_entries = self.are_all_positive(my_entry)
        # self.log.info('All positive entries? ' + str(all_positive_entries))
        if all_positive_entries:
            # self.log.info('All positive entries, updating...')
            for vnf_forwarding_graph in self.vnf_forwarding_graphs:
                if vnf_forwarding_graph.identifier == data['vnf_forwarding_graph_id']:
                    self.log.info('CHECKING A')
                    await vnf_forwarding_graph.update_data(data, self.log)
                    self.log.info('Finished updating hehe')
        # else:
        #     self.log.info('No all positive, waiting until all')
        # self.log.info('MARK ENDED')

    def check_if_entry_in_my_list(self, data):
        for entry in self.list_pending_vnf_forwarding_updates:
            is_same_vnf_forwarding_graph = entry['vnf_forwarding_graph_id'] == data['vnf_forwarding_graph_id']
            is_same_attribute = entry['attribute_id'] == data['attribute_id']
            is_same_counter = entry['attribute_counter'] == data['attribute_counter']
            is_same_max_index = entry['current_max_orchestrator_index'] == data['current_max_orchestrator_index']
            is_same_messages = entry['messages_sent'] == data['messages_sent']
            if is_same_vnf_forwarding_graph and is_same_attribute and is_same_counter and is_same_max_index and is_same_messages:
                return True
        return False

    async def notify_proposal_for_vnf_forwarding_graph(self, data):
        my_orch_debug = self.get_orchestrator_information_by_id(data['orchestrator_id'])
        str_log_1 = 'Notify proposal: ' + str(my_orch_debug['ip']) + ':' + str(my_orch_debug['port'])
        str_log_2 = ' ID: ' + data['attribute_id'][0:8] + ' Counter: ' + str(data['attribute_counter']) + ' Max. ' + str(data['current_max_orchestrator_index']) + ' Messgaes. ' + str(data['messages_sent'])
        self.log.info(str_log_1 + str_log_2)
        answer = False
        is_entry_in_my_list = self.check_if_entry_in_my_list(data)
        if not is_entry_in_my_list:
            self.log.info('Add to my pending list not ready')
            self.list_pending_vnf_forwarding_updates.append(data)

        if self.id in data['affected_orchestrators_replicas']:
            # TEST HERE:
            is_valid = self.check_is_valid_change(data)
            if is_valid:
                await self.mark_as_positive_update_and_apply_if_full(data)
                # ERROR: CHECK WHY THE MESSAGES ARE NOT SENT BY REPLICAS>>> GODZILLA
                answer = True
            else:
                my_entry = self.get_entry_from_list(data)
                my_entry[self.id] = False
                my_entry[data['orchestrator_id']] = False
                str_log = 'Negated: ' + data['attribute_id'][0:8] + ' Counter: ' + str(
                    data['attribute_counter']) + ' Max. ' + str(
                    data['current_max_orchestrator_index'])
                self.log.info(str_log)

            # self.log.info('Yes, I am marking as positive and doing all Notify')
            # await self.mark_as_positive_update_and_apply_if_full(data)
            # answer = True
        elif self.id in data['affected_orchestrators_dependencies']:
            is_valid = self.check_is_valid_change(data)
            if is_valid:
                await self.mark_as_positive_update_and_apply_if_full(data)
                answer = True
            else:
                my_entry = self.get_entry_from_list(data)
                my_entry[self.id] = False
                my_entry[data['orchestrator_id']] = False
                str_log = 'Negated: ' + data['attribute_id'] + ' Counter: ' + str(
                    data['attribute_counter']) + ' Max. ' + str(
                    data['current_max_orchestrator_index'])
                self.log.info(str_log)

        data['answer'] = answer
        data['reply_id'] = self.id
        entry_as_json = json.dumps(data)

        str_my_status = ''
        # same_attributes_log = pending['attribute_counter'] == data['attribute_counter']
        # same_attributes_log = pending['current_max_orchestrator_index'] == data['current_max_orchestrator_index']
        # same_attributes_log = pending['messages_sent'] == data['messages_sent']

        for pending in self.list_pending_vnf_forwarding_updates:
            same_attributes = pending['attribute_counter'] == data['attribute_counter']
            same_max = pending['current_max_orchestrator_index'] == data['current_max_orchestrator_index']
            same_messages = pending['messages_sent'] == data['messages_sent']
            same_id = pending['attribute_id'] == data['attribute_id']

            if same_id and same_attributes and same_max and same_messages:
                str_my_status = ' ['
                for affected_orch, value in pending['affected_vnf_forwarding_graphs'].items():
                    my_orch = self.find_orchestrator_by_id(affected_orch)
                    str_my_status += '(' + str(my_orch['port']) + ' ' + str(value) + '), '
                str_my_status += ']'

        for orchestrator in data['affected_orchestrators']:
            my_orch = self.get_orchestrator_information_by_id(orchestrator)
            first_condition = self.ip != my_orch['ip'] and self.port != my_orch['port']
            second_condition = self.ip == '127.0.0.1' and self.port != my_orch['port']
            if first_condition or second_condition:
                # self.log.info('REPLYINGS')
                # self.log.info(my_orch)
                # self.log.info(str_my_status)
                # self.log.info(data['answer'])
                # str_log = 'Sending reply to: ' + str(my_orch['ip']) + ':' + str(my_orch['port']) + ' answer: ' + data['answer']
                if str_my_status == '':
                    self.log.info('Status is empty...')
                    powa = self.get_entry_from_list(data)
                    str_my_status = ' ['
                    for item, value in powa['affected_vnf_forwarding_graphs'].items():
                        orch_log_debug = self.get_orchestrator_information_by_id(item)
                        str_my_status += '(' + str(orch_log_debug['port']) + ' ' + str(value) + '), '
                    str_my_status += ']'


                str_log = 'Sending reply to: ' + str(my_orch['ip']) + ':'+ str(my_orch['port']) + ' for ' + data['attribute_id'][0:8] + ' answer: ' + str(data['answer']) + ' my status: ' + str(str_my_status)
                self.log.info(str_log)
                new_message = ReplyProposedVNFForwardingGraphUpdateMessage(my_orch['ip'], str(my_orch['port']), entry_as_json)
                self.increment_sent_messages()
                await asyncio.create_task(self.send_message_with_json(new_message))

    async def reply_notify_proposal_for_vnf_forwarding_graph(self, data):
        # self.log.info('REPLY NOTIFIY....')
        my_orch_debug = self.get_orchestrator_information_by_id(data['reply_id'])
        # self.log.info('REPLY NOTIFIY....')
        str_log_1= 'Reply notify proposal: ' + str(my_orch_debug['ip']) + ':'+str(my_orch_debug['port'])
        str_log_2 = ' ID: ' + data['attribute_id'][0:8] + ' Counter: ' + str(data['attribute_counter']) + ' Max. ' + str(
            data['current_max_orchestrator_index']) + ' Messages. ' + str(data['messages_sent']) + ' Answer: ' + str(data['answer'])
        self.log.info(str_log_1 + str_log_2)

        is_entry_in_my_list = self.check_if_entry_in_my_list(data)
        if not is_entry_in_my_list:
            self.list_pending_vnf_forwarding_updates.append(data)

        my_entry = self.get_entry_from_list(data)
        str_affected_log = '['
        for item,value in my_entry['affected_vnf_forwarding_graphs'].items():
            my_orch_affected = self.find_orchestrator_by_id(item)
            str_affected_log += '(' + str(my_orch_affected['port']) + ' ' + str(value) + '), '
        str_affected_log += ']'
        # self.log.info('Before update..')
        # str_log_old = 'Before update: ' + data['attribute_id'][0:8] + ' ' + str(my_entry['affected_vnf_forwarding_graphs']) + ' Answer: ' + str(data['answer'])
        str_log_old = 'Before update: ' + data['attribute_id'][0:8] + ' ' + str_affected_log + ' Answer: ' + str(data['answer'])

        self.log.info(str_log_old)
        my_entry['affected_vnf_forwarding_graphs'][data['reply_id']] = data['answer']

        str_affected_log = '['
        for item, value in my_entry['affected_vnf_forwarding_graphs'].items():
            my_orch_affected = self.find_orchestrator_by_id(item)
            str_affected_log += '(' + str(my_orch_affected['port']) + ' ' + str(value) + '), '
        str_affected_log += ']'

        # str_log_old = 'After update: ' + data['attribute_id'][0:8] + ' ' + str(my_entry['affected_vnf_forwarding_graphs'])
        str_log_old = 'After update: ' + data['attribute_id'][0:8] + ' ' + str(str_affected_log)

        self.log.info(str_log_old)
        all_positive_entries = self.are_all_positive(my_entry)
        if all_positive_entries:
            for vnf_forwarding_graph in self.vnf_forwarding_graphs:
                if vnf_forwarding_graph.identifier == data['vnf_forwarding_graph_id']:
                    self.log.info('B')
                    await vnf_forwarding_graph.update_data(data, self.log)
                    self.log.info('END B')
                    break

    # TODO: Change this quick fix function by separating in each orchestrator
    async def update_unique_vnf_forwarding_graph_classifier_rule_corrective(self, attribute: MatchingAttribute):
        self.log.info('Doing first update for attribute ' + str(attribute.get_identifier()[0:8]))
        data = dict()
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if vnf_forwarding_graph.has_matching_attribute(attribute):
                data = attribute.as_dictionary()
                data['type'] = 'matching_attribute'
                data['update'] = 'corrective'
                data['first_update'] = 'True'
                data['attribute_id'] = attribute.identifier
                data['current_max_orchestrator_index'] = self.orchestrator_index
                new_entry = await vnf_forwarding_graph.update_data(data, self.log)
                break
        data = self.get_vnf_forwarding_graph_by_attribute(attribute)
        entry = new_entry.as_dictionary()
        entry['attribute_id'] = attribute.identifier
        entry['update'] = 'corrective'
        entry['type'] = 'matching_attribute'
        entry['affected_orchestrators'] = data['affected_orchestrators']
        entry['op_sender_id'] = self.port
        entry['sender_id'] = self.port
        entry['first_update'] = 'False'
        await self.send_update_vnf_forwarding_graph_notification_to_affected_orchestrators(entry, data['affected_orchestrators'])

        # for orchestrator in data['affected_orchestrators']:
        #     my_orch = self.get_orchestrator_information_by_id(orchestrator)
        #     first_condition = self.ip != my_orch['ip'] and self.port != my_orch['port']
        #     second_condition = self.ip == '127.0.0.1' and self.port != my_orch['port']
        #     if first_condition or second_condition:
        #         str_log = 'Sending First Notification to: ' + str(my_orch['ip']) + ':' + str(my_orch['port']) + ' for ' + str(entry['attribute_id'][0:8])
        #         self.log.info(str_log)
        #         new_message = VNFForwardingGraphUpdateMessageCorrective(my_orch['ip'], str(my_orch['port']), entry_as_json)
        #         self.increment_sent_messages()
        #         await asyncio.create_task(self.send_message_with_json(new_message))

    async def send_update_vnf_forwarding_graph_notification_to_affected_orchestrators(self, entry, affected):
        entry_as_json = json.dumps(entry)
        for orchestrator in affected:
            my_orch = self.get_orchestrator_information_by_id(orchestrator)
            first_condition = self.ip != my_orch['ip'] and self.port != my_orch['port']
            second_condition = self.ip == '127.0.0.1' and self.port != my_orch['port']
            if first_condition or second_condition:
                # str_log = 'Sending First Notification to: ' + str(my_orch['ip']) + ':' + str(my_orch['port']) + ' for ' + str(entry['attribute_id'][0:8])
                str_log_1 = 'Sending First Notification to: ' + str(my_orch['ip'])
                str_log_2 = ':' + str(my_orch['port']) + ' for ' + str(entry['attribute_id'][0:8]) + ' ['
                str_log_3 = str(entry['counter']) + ',' + str(entry['current_max_orchestrator_index']) + ']'
                str_log = str_log_1 + str_log_2 + str_log_3
                self.log.info(str_log)
                new_message = VNFForwardingGraphUpdateMessageCorrective(my_orch['ip'], str(my_orch['port']), entry_as_json)
                self.increment_sent_messages()
                await asyncio.create_task(self.send_message_with_json(new_message))

    async def notify_update_vnf_forwarding_graph_corrective(self, data):
        self.log.info('Notify corrective update from: ' + str(data['attribute_id'][0:8]) + ' [' + str(data['counter']) + ', ' + str(data['current_max_orchestrator_index']) + ']' + ' from ' + str(data['op_sender_id']))
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if vnf_forwarding_graph.has_item(data, self.log):
                await self.check_and_apply_not_negated(vnf_forwarding_graph, data)
                # #ERROR: Do not break because is possible to have the same
                break

    async def check_and_apply_not_negated(self, vnf_forwarding_graph, data):
        is_negated = vnf_forwarding_graph.has_item_negated(data, self.log)
        if not is_negated:
            is_valid = self.check_is_valid_change(data)
            if is_valid:
                await vnf_forwarding_graph.update_data(data, self.log)
            else:
                await self.handle_invalid_corrective_update(vnf_forwarding_graph, data)
        else:
            self.log.info('Element is negated ' + str(data['attribute_id'][0:8]) + ' ignoring...')

    async def handle_invalid_corrective_update(self, vnf_forwarding_graph, data):
        # self.log.info('Adding the data to my negated...')
        rule = vnf_forwarding_graph.classification_rules[0]
        if data['type'] == 'matching_attribute':
            new_matching_attribute = None
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == data['attribute_id']:
                    # self.log.info('Adding matching attribute to incorrect things')
                    new_matching_attribute = matching_attribute.add_invalid_corrective_update(data, self.log)

        elif data['type'] == 'connection_point':
            # ERROR: Godzilla poder
            self.log.info('IMPLEMENT connection point')

        # await vnf_forwarding_graph.update_data(data, self.log)

        # Send negative answer to all affected
        for orchestrator in data['affected_orchestrators']:
            my_orch = self.get_orchestrator_information_by_id(orchestrator)
            first_condition = self.ip != my_orch['ip'] and self.port != my_orch['port']
            second_condition = self.ip == '127.0.0.1' and self.port != my_orch['port']
            if first_condition or second_condition:
                # str(data['current_max_orchestrator_index']) + ']')
                str_log_1 = 'Sending Negative Answer to: ' + str(my_orch['ip'])
                str_log_2 = ':' + str(my_orch['port']) + ' for ' + str(data['attribute_id'][0:8]) + ' ['
                str_log_3 = str(data['counter']) + ',' + str(data['current_max_orchestrator_index']) + ']'
                str_log = str_log_1 + str_log_2 + str_log_3
                self.log.info(str_log)
                data['sender_id'] = self.port
                entry_as_json = json.dumps(data)
                new_message = CorrectiveNegativeMessage(my_orch['ip'], str(my_orch['port']),
                                                        entry_as_json)
                self.increment_sent_messages()
                await asyncio.create_task(self.send_message_with_json(new_message))

    async def notify_reject_corrective(self, data):
        self.log.info('Notify negative corrective update: ' + str(data['attribute_id'][0:8]) + ' [' + str(data['counter']) + ', ' + str(data['current_max_orchestrator_index']) + ']' + ' from ' + str(data['sender_id']))
        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            if vnf_forwarding_graph.has_item(data):
                is_element_in_negative = vnf_forwarding_graph.check_item_is_negated(data, self.log)
                is_element_in_positive = vnf_forwarding_graph.check_item_is_accepted(data, self.log)
                self.log.info('Is element ' + str(data['attribute_id'][0:8]) + ' accepted? ' + str(is_element_in_positive) + ', negated? ' + str(is_element_in_negative))
                if is_element_in_positive:
                    self.log.info('Removing item from heap and reconfigure ' + str(data['attribute_id'][0:8]))
                    await vnf_forwarding_graph.remove_item_from_heap_and_reconfigure(data, self.log)
                if is_element_in_negative:
                    self.log.info('Already negative pass ' + str(data['attribute_id'][0:8]))
                    pass
                if not is_element_in_negative and not is_element_in_positive:
                    self.log.info('Negation arrived first '+ str(data['attribute_id'][0:8]))
                    await vnf_forwarding_graph.add_item_to_negated_list(data, self.log)
        self.log.info('Finished negative corrective update for ' + str(data['attribute_id'][0:8]) + ' [' + str(
            data['counter']) + ', ' + str(data['current_max_orchestrator_index']) + ']' + ' from ' + str(
            data['sender_id']))

    async def update_unique_vnf_forwarding_graph_classifier_rule(self, attribute: MatchingAttribute):
        if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
            await self.update_unique_vnf_forwarding_graph_classifier_rule_causal_standard(attribute)
        elif self.algorithm_type == 'preventive':
            await self.update_unique_vnf_forwarding_graph_classifier_rule_preventive(attribute)
        elif self.algorithm_type == 'corrective':
            await self.update_unique_vnf_forwarding_graph_classifier_rule_corrective(attribute)

    async def notify_all_replicas_and_orchestrators_of_positive_change(self, result):
        if self.algorithm_type == 'causal':
            await self.notify_all_orchestrators_of_change(result)
        self.total_time_for_experimentation += result['running_time']
        return return_success()

    def increase_my_counter(self):
        self.orchestrator_counter += 1

    async def notify_replicas_of_vnf_forwarding_graph_update(self, data):
        vnf_forwarding_graph = data['vnffg']
        result = ""
        for replica in data['replicas']:
            for orchestrator in self.list_orchestrator:
                if orchestrator['id'] == replica:
                    vnf_forwarding_graph['vector_clock'] = data['vector_clock']
                    vnf_forwarding_graph['orchestrator_id'] = self.id
                    vnf_forwarding_graph['type'] = self.algorithm_type
                    vnf_forwarding_graph['orchestrator_index'] = self.orchestrator_index
                    vnf_forwarding_graph['identifier'] = data['identifier']
                    vnf_forwarding_graph['vnffg_identifier'] = data['vnffg_identifier']
                    vnf_forwarding_graph['vnffg_name'] = data['vnffg_name']
                    vnf_forwarding_graph['vnffg_short_name'] = data['vnffg_short_name']
                    vnf_forwarding_graph['type_of_change_attribute'] = data['type_of_change_attribute']
                    new_message = UpdateVNFForwardingGraph(host=orchestrator['ip'],
                                                           port=orchestrator['port'],
                                                           data=vnf_forwarding_graph)

                    random_number = generate_random_number_between_zero_one_hundred()
                    if self.probability_repeated_message >= random_number:
                        concurrent_updates = []
                        self.increment_sent_messages()
                        concurrent_updates.append(send_message(new_message))
                        while self.probability_repeated_message >= random_number:
                            concurrent_updates.append(self.wait_before_repeated(new_message))
                            random_number = generate_random_number_between_zero_one_hundred()
                        await asyncio.gather(*concurrent_updates)
                    else:
                        self.increment_sent_messages()
                        result = await send_message(new_message)
                    # ERROR: POSSIBLE TO UNCOMMENT
                    # if self.algorithm_type == 'last_writer_wins':
                    #     self.increment_sent_messages()
        return result

    async def wait_before_repeated(self, message):
        wait_period = random.randint(0, self.waiting_time)
        await asyncio.sleep(wait_period)
        await send_message(message)

    async def wait_before_notify_update_of_vnf_forwarding_graph(self, vnf_forwarding_graph):
        wait_period = random.randint(0, self.waiting_time)
        await asyncio.sleep(wait_period)
        await self.notify_update_of_vnf_forwarding_graph(vnf_forwarding_graph)

    async def notify_update_of_vnf_forwarding_graph(self, vnf_forwarding_graph):
        vector_clock = VectorClock()
        vector_clock.create_from_list(vnf_forwarding_graph['vector_clock'])
        sender_id = vnf_forwarding_graph['orchestrator_id']
        my_vector_clock = self.get_clock_from_entry_of_vnf_forwarding_graph(vnf_forwarding_graph)
        difference_in_vectors = my_vector_clock.compare_with_list_of_values(vector_clock, sender_id, self.log)
        my_clock_greater = my_vector_clock.is_greater_than_other(vector_clock)
        are_clocks_equal = my_vector_clock.is_equal(vector_clock)
        if vnf_forwarding_graph['type'] == 'causal':
            if difference_in_vectors <= 1:
                my_vector_clock.update_clock(vector_clock, sender_id, self.log)
                await self.apply_vnf_fg_update_notification(vnf_forwarding_graph)
                if len(self.pending_lcm_operations) > 0:
                    await self.do_pending_lcm_notifications_notifications()
            else:
                self.save_vnf_fg_update(vnf_forwarding_graph)
        elif vnf_forwarding_graph['type'] == 'standard':
            if difference_in_vectors > 1 or my_clock_greater or are_clocks_equal:
                self.add_inconsistency()
            my_vector_clock.update_clock(vector_clock, sender_id, self.log)
            await self.apply_notification_using_standard_algorithm(vnf_forwarding_graph)
        elif vnf_forwarding_graph['type'] == 'last_writer_wins':
            await self.apply_notification_using_last_writer_win_algorithm(vnf_forwarding_graph)

    async def apply_notification_using_standard_algorithm(self, vnf_forwarding_graph):
        await self.apply_vnf_fg_update_notification(vnf_forwarding_graph)

    async def apply_notification_using_last_writer_win_algorithm(self, vnf_forwarding_graph):
        other_counter = int(vnf_forwarding_graph['vnffg_counter'])
        other_index = int(vnf_forwarding_graph['orchestrator_index'])
        for vnf_fg_entry in self.vnf_forwarding_graphs:
            is_same_identifier = vnf_fg_entry.get_identifier() == vnf_forwarding_graph['identifier']
            is_same_identifier_alternate = vnf_fg_entry.get_identifier() == vnf_forwarding_graph['vnffg_identifier']
            if is_same_identifier or is_same_identifier_alternate:
                my_counter = vnf_fg_entry.get_counter_of_entry(vnf_forwarding_graph, self.log)
                my_current_max_index = vnf_fg_entry.get_current_max_index_of_entry(vnf_forwarding_graph, self.log)
                if my_current_max_index == -1:
                    my_current_max_index = self.orchestrator_index
                debug_first_condition = other_counter > my_counter
                debug_second_first_condition = other_counter == my_counter
                debug_second_second_condition = other_index > int(my_current_max_index)
                debug_second_condition = debug_second_first_condition and debug_second_second_condition
                if debug_first_condition or debug_second_condition:
                    await self.apply_vnf_fg_update_notification(vnf_forwarding_graph)

    def save_vnf_fg_update(self, data):
        new_vector_clock = VectorClock()
        if type(data['vector_clock']) == str:
            new_vector_clock.create_from_list(data['vector_clock'])
        else:
            new_vector_clock.create_from_list(data['vector_clock'].as_string())

        start = time.time()
        data['buffer_time'] = start
        new_pending_operation = PendingLCMScalingOperation(vnf_component_to_scale_id='',
                                                           operation='vnf_fg_update',
                                                           orchestrator_sender_id=data['orchestrator_id'],
                                                           sender_vector_clock=new_vector_clock,
                                                           data=data,
                                                           vnffg_data=data)
        self.add_pending_operation(new_pending_operation)

    async def apply_vnf_fg_update_notification(self, vnf_forwarding_graph):
        for vnf_fg_entry in self.vnf_forwarding_graphs:
            is_same_identifier = vnf_fg_entry.get_identifier() == vnf_forwarding_graph['identifier']
            is_same_identifier_alternate = vnf_fg_entry.get_identifier() == vnf_forwarding_graph['vnffg_identifier']
            if is_same_identifier or is_same_identifier_alternate:
                start = time.time()
                if vnf_forwarding_graph['type_of_change'] == 'rsp':
                    new_change = self.create_vnf_fg_update_entry_rsp(vnf_forwarding_graph)
                    await self.update_vnf_forwarding_graph_unique_rsp(vnf_fg_entry, new_change)
                if vnf_forwarding_graph['type_of_change'] == 'classifier_rule':
                    new_change = self.create_vnf_fg_update_entry_classifier(vnf_forwarding_graph)
                    await self.update_vnf_forwarding_graph_unique_classifier(vnf_fg_entry, new_change)
                end = time.time()
                self.total_time_for_experimentation += (end - start)
                break

        total_pending_operations = len(self.pending_lcm_operations)
        if total_pending_operations > 0:
            self.log.info('Total pending operations: ' + str(total_pending_operations))

    def create_vnf_fg_update_entry_classifier(self, new_vnf_forwarding_graph):
        new_matching_attributed = MatchingAttribute(
            identifier=new_vnf_forwarding_graph['change_identifier'],
            ip_proto=new_vnf_forwarding_graph['change_ip_proto'],
            source_ip=new_vnf_forwarding_graph['change_source_ip'],
            destination_ip=new_vnf_forwarding_graph['change_destination_ip'],
            source_port=new_vnf_forwarding_graph['change_source_port'],
            destination_port=new_vnf_forwarding_graph['change_destination_port'],
            counter=new_vnf_forwarding_graph['vnffg_counter'],
            current_max_orchestrator_index=new_vnf_forwarding_graph['orchestrator_index'],
            orchestrator_sender_id=new_vnf_forwarding_graph['orchestrator_id'],
            list_of_orchestrator_id=self.orchestrators_ids)
        return new_matching_attributed

    def create_vnf_fg_update_entry_rsp(self, new_vnf_forwarding_graph):
        new_vnf_connection_point_reference = ConnectionPointReference(
            identifier=new_vnf_forwarding_graph['change_identifier'],
            order=new_vnf_forwarding_graph['change_order'],
            ingress_connection_point=new_vnf_forwarding_graph['change_ingress_connection_point'],
            egress_connection_point=new_vnf_forwarding_graph['change_egress_connection_point'],
            counter=new_vnf_forwarding_graph['vnffg_counter'],
            current_max_orchestrator_index=new_vnf_forwarding_graph['orchestrator_index'],
            orchestrator_sender_id=new_vnf_forwarding_graph['orchestrator_id'],
            list_of_orchestrator_id=self.orchestrators_ids)
        return new_vnf_connection_point_reference

    async def update_vnf_forwarding_graph_unique_rsp(self,
                                                     old_vnf_fg: VNFForwardingGraph,
                                                     new_cp: ConnectionPointReference):
        result = await old_vnf_fg.update_unique_rendered_service_path(new_cp, self.log, self.orchestrator_index)
        if self.algorithm_type == 'last_writer_wins':
            self.log.info(
                'After update: {' + str(self.orchestrator_index) + ',' + str(result['new_counter']) + ',' + str(
                    result['new_max_counter']) + '}')
        return result

    async def update_vnf_forwarding_graph_unique_classifier(self,
                                                            old_vnf_fg: VNFForwardingGraph,
                                                            new_matching_attribute: MatchingAttribute):
        result = await old_vnf_fg.update_unique_classifier_rule(new_matching_attribute, self.log)
        if self.algorithm_type == 'last_writer_wins':
            self.log.info(
                'After update: {' + str(self.orchestrator_index) + ',' + str(result['new_counter']) + ',' + str(
                    result['new_max_counter']) + '}')
        return result

    async def wait_before_vnf_fg_update(self, update):
        wait_period = random.randint(0, self.waiting_time)
        await asyncio.sleep(wait_period)
        if update['type'] == 'update_vnffg_classifier':
            await self.update_unique_vnf_forwarding_graph_classifier_rule(update['data'])
        elif update['type'] == 'update_vnffg_rsp':
            await self.update_unique_vnf_forwarding_graph_rendered_service_path(update['data'])

    async def apply_concurrent_updates(self):
        vnf_forwarding_graph_updates = self.read_vnf_forwarding_graph_updates()
        coroutines = []
        my_updates = 0
        for update in vnf_forwarding_graph_updates:
            if update['host'] == self.ip and update['port'] == str(self.port) and update['type'] != 'update_all_vnffg':
                coroutines.append(self.wait_before_vnf_fg_update(update))
                my_updates += 1
        await asyncio.gather(*coroutines)
        print('Number of updates: ' + str(my_updates))

    async def apply_sequential_updates(self):
        vnf_forwarding_graph_updates = self.read_vnf_forwarding_graph_updates()
        my_updates = 0
        for update in vnf_forwarding_graph_updates:
            if update['host'] == self.ip and update['port'] == str(self.port) and update['type'] != 'update_all_vnffg':
                await self.wait_before_vnf_fg_update(update)
                my_updates += 1
        print('Number of updates: ' + str(my_updates))

    def read_vnf_forwarding_graph_updates(self):
        updates = []
        string_1 = ROOT_DIR + '/experiments/experiment_'
        directory_path = string_1 + str(self.experiment_index) + '/' + 'updates_vnf_forwarding_graphs.sh'
        print(directory_path)
        file1 = open(directory_path, 'r')
        lines = file1.readlines()
        for current_line in lines:
            line = current_line.split()
            if len(line) > 0:
                update = dict()
                update['type'] = line[3]
                update['host'] = line[5]
                update['port'] = line[7]
                if update['type'] == 'update_vnffg_classifier':
                    data = MatchingAttribute(line[9], line[11], line[13], line[15], line[17], line[19])
                elif update['type'] == 'update_vnffg_rsp':
                    data = ConnectionPointReference(line[9], line[11], line[13], line[15])
                else:
                    data = None
                update['data'] = data
                updates.append(update)
        return updates
