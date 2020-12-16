import asyncio
import json
import logging
import os
import random
import sys

from communication_entities.generic_service import GenericService
from communication_entities.life_cycle_management import LifeCycleManagement
from communication_entities.matching_attribute import MatchingAttribute
from communication_entities.messages.lcm_messages.notification_lcm_operation import NotificationLCMOperation
from communication_entities.messages.vnf_forwarding_graph.update_vnf_forwarding_graph import UpdateVNFForwardingGraph
from communication_entities.orchestrator_classes.pending_lcm_scaling_operation import PendingLCMScalingOperation
from communication_entities.vector_clock import VectorClock
from communication_entities.vnf_connection_point_reference import VNFConnectionPointReference
from communication_entities.vnf_forwarding_graph import VNFForwardingGraph
from definitions import ROOT_DIR
from utilities.life_cycle_management_update import return_success, return_failure, return_in_process, send_message
from utilities.random_integer_generation import generate_random_integer

sys.path.append('../')

def is_orchestrator_included_for_notification(id_orch, excluding_list):
    for orchestrator in excluding_list:
        if isinstance(orchestrator, str):
            if id_orch == orchestrator:
                return False
        elif id_orch == orchestrator['id']:
            return False
    return True


class Orchestrator:

    def __init__(self, experiment_index, orchestrator_index, server_host, server_port, random_seed,
                 causal_delivery=False, algorithm_type='causal'):
        self.experiment_name = 'experiment_' + experiment_index
        self.experiment_index = experiment_index
        self.name = 'orch_' + orchestrator_index
        self.orchestrator_index = orchestrator_index
        self.orchestrator_counter = 0
        self.directory_path = 'experiments/experiment_generator/experiments/experiment_' + self.experiment_index + '/'
        self.id = ''
        self.location = ''
        self.ip = server_host
        self.port = server_port
        self.list_vnf = dict()
        self.list_orchestrator = list()
        self.pending_lcm_operations = list()
        self.topology = None
        self.services = list()
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
        self.pending_operations_repetitions = 0
        self.time_elapsed_in_reconfiguration = 0.0
        self.algorithm_type = algorithm_type
        self.set_up_my_logger()
        random.seed(self.random_seed)

    def add_vnf_forwarding_graph(self, vnf_forwarding_graphs):
        for vnf_fg_entry in vnf_forwarding_graphs:
            new_vnf_fg = VNFForwardingGraph(identifier=vnf_fg_entry['identifier'],
                                            name=vnf_fg_entry['name'],
                                            short_name=vnf_fg_entry['short_name'],
                                            is_shared=vnf_fg_entry['is_shared'],
                                            service_identifier=vnf_fg_entry['service_identifier'],
                                            my_orchestrator=self.id)

            new_vnf_fg.instantiate_rendered_service_path(vnf_fg_entry)
            new_vnf_fg.instantiate_classification_rules(vnf_fg_entry)
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

    def find_orchestrator_by_id(self, orch_id):
        for orchestrator in self.list_orchestrator:
            if orchestrator['id'] == orch_id:
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
        self.log.info('Please scale service: ' + str(service_id))
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
        orchestrator_format['is_causal'] = self.causal_delivery
        orchestrator_format['algorithm_type'] = self.algorithm_type
        orchestrator_format['vector_clock'] = self.vector_clock.as_string()
        orchestrator_format['inconsistencies'] = self.inconsistencies
        orchestrator_format['random_seed'] = self.random_seed
        orchestrator_format['messages_sent'] = self.messages_sent
        orchestrator_format['pending_operations'] = len(self.pending_lcm_operations)
        orchestrator_format['time_elapsed_in_last_reconfiguration'] = self.time_elapsed_in_reconfiguration
        return orchestrator_format

    def get_service_by_id(self, service_id):
        for service in self.services:
            if service.id == service_id:
                return service

    async def wait_before_notification(self, vector_clock, orchestrator_sender_id):
        wait_period = random.randint(0, 10)
        await asyncio.sleep(wait_period)
        await self.notification_of_lcm(vector_clock, orchestrator_sender_id)

    def set_up_my_logger(self):
        file_name = 'logs/file_' + self.name + '_' + self.experiment_index + '.log'
        other_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', file_name))
        logging.basicConfig(filename=other_folder)
        self.log = logging.getLogger('logger')
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

    def add_inconsistency(self, vector_clock):
        str_log = 'A new inconsistency because Sender ' + vector_clock.as_string() + ' > '
        str_log_2 = str_log + self.vector_clock.as_string()
        self.log.info(str_log_2)
        self.inconsistencies += 1

    async def notification_of_lcm(self, vector_clock_string, orchestrator_sender_id):
        self.log.info('notification_of_lcm -- Update')
        vector_clock = VectorClock()
        vector_clock.create_from_list(vector_clock_string)
        self.log.info('Received ' + vector_clock.as_string() + ' from: ' + str(
            orchestrator_sender_id[0:8]) + ' My clock ' + self.vector_clock.as_string())
        causal_delivery = False
        if self.algorithm_type == 'causal':
            causal_delivery = True
        if orchestrator_sender_id == self.id:
            difference_in_vectors = 0
        else:
            difference_in_vectors = self.vector_clock.compare_clocks(vector_clock,
                                                                     orchestrator_sender_id,
                                                                     causal_delivery,
                                                                     self.log)
        await self.apply_notification_of_lifecycle_management_operation(difference_in_vectors,
                                                                        vector_clock,
                                                                        orchestrator_sender_id)
        self.log.info('Orch operations in ' + str(
            len(self.pending_lcm_operations)) + ' LCM operations: ' + str(
            len(self.life_cycle_manager.pending_operations)) + ' My ' + self.vector_clock.as_string())
        self.pending_operations_repetitions = 0
        return_success()

    async def apply_notification_of_lifecycle_management_operation(self, difference_in_vectors, vector_clock, sender):
        if self.algorithm_type == 'causal':
            await self.notification_of_lcm_causal(difference_in_vectors, vector_clock, sender)
        elif self.algorithm_type == 'standard':
            await self.notification_of_lcm_normal(difference_in_vectors, vector_clock, sender)
        elif self.algorithm_type == 'last_writer_wins':
            await self.notification_of_lcm_last_writer_wins(difference_in_vectors, vector_clock, sender)
        elif self.algorithm_type == 'multi_value':
            await self.notification_of_lcm_multi_value(difference_in_vectors, vector_clock, sender)

    async def notification_of_lcm_last_writer_wins(self, difference_in_vectors, vector_clock, sender):
        pass

    async def notification_of_lcm_multi_value(self, difference_in_vectors, vector_clock, sender):
        pass

    async def notification_of_lcm_causal(self, difference_in_vectors, vector_clock, orchestrator_sender_id):
        if difference_in_vectors <= 1:
            await self.apply_notification_of_lcm_operation(vector_clock, orchestrator_sender_id)
        else:
            if self.vector_clock.are_different(vector_clock.clock_list):
                self.log.info('Saving notification as a pending operation')
                new_pending_operation = PendingLCMScalingOperation(vnf_component_to_scale_id='',
                                                                   operation='notification',
                                                                   original_service_id='',
                                                                   orchestrator_sender_id=orchestrator_sender_id,
                                                                   original_orchestrator_id='',
                                                                   sender_vector_clock=vector_clock,
                                                                   service_sender_id='')
                self.add_pending_operation(new_pending_operation)

    async def notification_of_lcm_normal(self, difference_in_vectors, vector_clock, orchestrator_sender_id):
        if difference_in_vectors > 1:
            self.add_inconsistency(vector_clock)
        await self.apply_notification_of_lcm_operation(vector_clock, orchestrator_sender_id)

    async def apply_notification_of_lcm_operation(self, vector_clock, orchestrator_sender_id):
        if not self.vector_clock.is_equal(vector_clock):
            self.log.info('Before update: ' + str(self.vector_clock.as_string()))
            self.vector_clock.update_clock(vector_clock,
                                           orchestrator_sender_id,
                                           self.log)
            self.log.info('After update: ' + str(self.vector_clock.as_string()) + ' Pending operations: ' + str(
                len(self.pending_lcm_operations)))
        total_pending_operations = len(self.pending_lcm_operations)
        if total_pending_operations > 0:
            await self.do_pending_lcm_notifications_notifications()

    async def notify_all_orchestrators_of_change(self, exclude_list_of_orchestrators, current_vector_clock, operation='scaling'):
        exclude_list_of_orchestrators.append(self.id)
        data = dict()
        data['vector_clock'] = current_vector_clock
        data['orchestrator_sender_id'] = self.id
        data['type'] = self.algorithm_type
        data['orchestrator_counter'] = self.orchestrator_counter
        data['orchestrator_index'] = self.orchestrator_index
        for orchestrator in self.list_orchestrator:
            if is_orchestrator_included_for_notification(orchestrator['id'], exclude_list_of_orchestrators):
                new_message = NotificationLCMOperation(host=orchestrator['ip'],
                                                       port=str(orchestrator['port']),
                                                       data=data)
                self.increment_sent_messages()
                await asyncio.create_task(send_message(new_message))

    def increment_sent_messages(self):
        self.messages_sent += 1

    async def do_pending_lcm_notifications_notifications(self):
        self.log.info('Do pending LCM NOTIFICATION')
        at_least_one_clock_changed = True
        while at_least_one_clock_changed:
            change_took_place = await self.repeat_lcm_operations()
            at_least_one_clock_changed = change_took_place
        self.log.info('Finish doing LCM notifications!')

    async def repeat_lcm_operations(self):
        change_took_place = False
        repetitions_message = 0
        total_pending_operations = len(self.pending_lcm_operations)
        self.log.info('Total operatins: ' + str(total_pending_operations))
        while self.pending_lcm_operations and repetitions_message < total_pending_operations and self.pending_operations_repetitions < total_pending_operations:
            self.log.info('Current repetitions: ' + str(repetitions_message))
            repetitions_message += 1
            pending_operation = self.pending_lcm_operations.pop(0)

            if type(pending_operation.sender_vector_clock) == str:
                new_vector_clock = VectorClock()
                new_vector_clock.create_from_list(pending_operation.sender_vector_clock)
                self.log.info(new_vector_clock.to_json())
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
        return change_took_place

    async def repeat_lcm_operations_causal(self, difference_in_clocks, pending_operation):
        change_took_place = False
        if difference_in_clocks <= 1 and pending_operation.is_not_done:
            self.log.info('Applying operation')
            change_took_place = await self.apply_lcm_operation(pending_operation)
        else:
            self.add_pending_operation(pending_operation)
        return change_took_place

    async def repeat_lcm_operations_normal(self, difference_in_clocks, pending_operation):
        if difference_in_clocks > 1:
            self.add_inconsistency(pending_operation.sender_vector_clock)
        return await self.apply_lcm_operation(pending_operation)

    def compute_clock_difference(self, pending_operation):
        causal_delivery = False
        if self.algorithm_type == 'causal':
            causal_delivery = True

        difference_in_clocks = self.vector_clock.compare_clocks(pending_operation.sender_vector_clock,
                                                                pending_operation.orchestrator_sender_id,
                                                                causal_delivery,
                                                                self.log)
        self.log.info('Difference in clocks: ' + str(difference_in_clocks))
        return difference_in_clocks

    async def apply_lcm_operation(self, pending_operation):
        self.log.info('Appliging LCM operation')
        change_result = True
        if pending_operation.operation == 'notification':
            pending_operation.is_not_done = False
            await self.apply_notification_operation(pending_operation)
        elif pending_operation.operation == 'scale' or pending_operation.operation == 'scaling':
            pending_operation.is_not_done = False
            await self.apply_scaling_operation(pending_operation)
        elif pending_operation.operation == 'vnf_fg_update':
            self.log.info('Appliying VNF FG UPDATE')
            pending_operation.is_not_done = False
            self.vector_clock.update_clock_with_a_string(pending_operation.sender_vector_clock,
                                                         self.log)
            await self.apply_vnf_fg_update_notification(pending_operation.data)
        else:
            self.log.info('Something went horribly wrong')
            change_result = False
        return change_result

    async def apply_notification_operation(self, pending_operation):
        self.log.info('Notification and pending operation is not done')
        self.vector_clock.update_clock(pending_operation.sender_vector_clock,
                                       pending_operation.orchestrator_sender_id,
                                       self.log)
        pending_operation.is_not_done = False

    async def apply_scaling_operation(self, pending_operation):
        self.log.info('Scaling operation and pending operation is not done')
        pending_operation.is_not_done = False
        await self.life_cycle_manager.scale_confirmation(pending_operation.vnf_component_to_scale_id,
                                                         pending_operation.original_service_id,
                                                         pending_operation.orchestrator_sender_id,
                                                         pending_operation.original_orchestrator_id,
                                                         pending_operation.sender_vector_clock,
                                                         pending_operation.service_sender_id)

    async def wait_before_delivery_grant(self, vnf_component_to_scale_id, operation, original_service,
                                         sender_vector_clock=None):
        wait_period = random.randint(0, 10)
        await asyncio.sleep(wait_period)
        await self.grant_lcm_operation_of_service(vnf_component_to_scale_id, operation, original_service,
                                                  sender_vector_clock)
        return return_in_process('Grant in process')

    async def grant_lcm_operation_of_service(self, vnf_component_to_scale_id, operation, original_service,
                                             sender_vector_clock=None):
        self.log.info('Can you please scale: ' + str(vnf_component_to_scale_id)[0:8] + ' originally from ' + str(
            original_service['original_service_id'][0:8]))
        self.log.info('Received ' + sender_vector_clock.as_string() + ' My clock ' + self.vector_clock.as_string())
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

    async def do_lcm_operation(self, original_service, sender_vector_clock, operation, vnf_component_to_scale_id):
        self.log.info('Doing LCM operations')
        if original_service['orchestrator_id'] != self.id:
            self.vector_clock.update_clock(sender_vector_clock,
                                           original_service['orchestrator_id'],
                                           self.log)
        await asyncio.gather(self.scale_vnfc_operation(vnf_component_to_scale_id, original_service),
                             self.do_pending_operations())

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
            self.add_inconsistency(sender_vector_clock)
        await self.do_lcm_operation(original_service, sender_vector_clock, operation, vnf_component_to_scale_id)

    def add_pending_operation(self, new_operation) -> None:
        self.log.info('Adding operation to pending LCM')
        self.pending_lcm_operations.append(new_operation)

    async def scale_vnfc_operation(self, vnf_component_to_scale_id, original_service):
        service_to_scale = self.get_service_by_id(vnf_component_to_scale_id)
        self.life_cycle_manager.add_new_service_to_scale(vnf_component_to_scale_id, original_service)
        is_ok_to_scale, no_dependencies = service_to_scale.validate_scaling()
        if is_ok_to_scale:
            await service_to_scale.independent_scale_causal(vnf_component_to_scale_id,
                                                            original_service['original_service_id'],
                                                            original_service['orchestrator_id'])

    async def do_pending_operations(self):
        self.log.info('Grant Pending Operations ' + str(
            self.pending_operations_repetitions) + ' are VNFs SCALED? ' + str(self.life_cycle_manager.are_VNFs_scaled))
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
        while self.pending_lcm_operations and repetitions_message < total_pending_operations and self.pending_operations_repetitions < total_pending_operations:
            repetitions_message += 1
            operation = self.pending_lcm_operations.pop(0)
            if operation.is_not_done and self.vector_clock.compare_stored_clock(operation.sender_vector_clock,
                                                                                self.causal_delivery):
                if operation.operation == 'scale' or operation.operation == 'scaling':
                    operation.is_not_done = False
                    at_least_one_clock_changed = True
                    self.log.info('Doing pending operation ' + str(
                        operation.vnf_component_to_scale_id) + ' originally from: ' + str(
                        operation.original_service_id))
                    await self.grant_lcm_operation_causal(operation.vnf_component_to_scale_id, 'scale',
                                                          operation.original_service, operation.sender_vector_clock)
            else:
                self.add_pending_operation(operation)
        return at_least_one_clock_changed

    def load_vnf_components(self):
        all_route = ROOT_DIR + '/' + self.directory_path + self.experiment_name + '.json'
        with open(all_route) as json_file:
            raw_data = json.load(json_file)
        orchestrator_number = self.name.find('_')
        orchestrator_index = int(self.name[orchestrator_number + 1:])
        my_orchestrator = raw_data['orchestrators'][orchestrator_index]
        my_ip = my_orchestrator['ip']
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

    async def update_unique_vnf_forwarding_graph_rendered_service_path(self, connection_point:VNFConnectionPointReference):
        for vnffg in self.vnf_forwarding_graphs:
            update_result = await vnffg.update_unique_rendered_service_path(connection_point,
                                                                            self.log,
                                                                            self.orchestrator_index,
                                                                            was_called_by_caller=True)
            if update_result['is_positive_result']:
                oi = str(self.orchestrator_index)
                nc = str(update_result['new_counter'])
                mc = str(update_result['new_max_counter'])
                id = str(update_result['vnffg_identifier'])
                ci = str(update_result['change_identifier'])

                if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
                    self.log.info(
                        'Call from Handler... My clock after update: ' + self.vector_clock.as_string() + ' Pending operations: ' + str(
                            len(self.pending_lcm_operations)))
                elif self.algorithm_type == 'last_writer_wins':
                    self.log.info('Call from Handler... After update: {' + oi + ',' + nc + ','+mc+'} for VNFFG ' + id + ' val: ' + ci)
                return await self.notify_all_replicas_and_orchestrators_of_positive_change(update_result)
        return return_failure('No VNF ID FOUND! ' + str(connection_point.get_vnf_identifier()))

    async def update_unique_vnf_forwarding_graph_classifier_rule(self, matching_attribute:MatchingAttribute):
        for vnffg in self.vnf_forwarding_graphs:
            update_result = await vnffg.update_unique_classifier_rule(matching_attribute,
                                                                      self.log,
                                                                      was_called_by_caller=True)
            if update_result['is_positive_result']:
                oi = str(self.orchestrator_index)
                nc = str(update_result['new_counter'])
                mc = str(update_result['new_max_counter'])
                id = str(update_result['vnffg_identifier'])
                ci = str(update_result['change_identifier'])
                if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
                    self.log.info(
                        'Call from Handler... My clock after update: ' + self.vector_clock.as_string() + ' Pending operations: ' + str(
                            len(self.pending_lcm_operations)))
                elif self.algorithm_type == 'last_writer_wins':
                    self.log.info('Call from Handler... After update: {' + oi + ',' + nc + ','+mc+'} for VNFFG ' + id + ' val: ' + ci)
                return await self.notify_all_replicas_and_orchestrators_of_positive_change(update_result)
        return return_failure('No Matching attribute with ID found! ' + str(matching_attribute.get_identifier()))

    async def notify_all_replicas_and_orchestrators_of_positive_change(self, update_result):
        list_of_replicas_to_notify = update_result['replicas']
        vnf_fg_as_dictionary = update_result['vnffg']
        self.vector_clock.increment_clock(self.id)
        my_clock_as_json = self.vector_clock.to_json()
        await self.notify_replicas_of_vnf_forwarding_graph_update(list_of_replicas_to_notify, vnf_fg_as_dictionary, my_clock_as_json)
        if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
            await self.notify_all_orchestrators_of_change(list_of_replicas_to_notify, my_clock_as_json)
        return return_success()

    def increase_my_counter(self):
        self.orchestrator_counter +=1

    async def notify_replicas_of_vnf_forwarding_graph_update(self, replicas, vnf_forwarding_graph, vector_clock_as_json):
        # self.log.info('Notifying replicas of VNFFG Update....')
        for replica in replicas:
            for orchestrator in self.list_orchestrator:
                if orchestrator['id'] == replica:
                    vnf_forwarding_graph['vector_clock'] = vector_clock_as_json
                    vnf_forwarding_graph['orchestrator_id'] = self.id
                    vnf_forwarding_graph['type'] = self.algorithm_type
                    vnf_forwarding_graph['orchestrator_index'] = self.orchestrator_index
                    new_message = UpdateVNFForwardingGraph(host=orchestrator['ip'],
                                                           port=orchestrator['port'],
                                                           data=vnf_forwarding_graph)
                    await send_message(new_message)

    async def notify_update_of_vnf_forwarding_graph(self, vnf_forwarding_graph):
        self.log.info('Received Notification for: ' + str(vnf_forwarding_graph['identifier'][0:8]) + ' ' + str(vnf_forwarding_graph['change_identifier'][0:8]) )
        vector_clock = VectorClock()
        vector_clock.create_from_list(vnf_forwarding_graph['vector_clock'])
        sender_id = vnf_forwarding_graph['orchestrator_id']
        difference_in_vectors = self.vector_clock.compare_with_list_of_values(vector_clock, sender_id, self.log)
        if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
            self.log.info('Difference in Vectors: ' + str(difference_in_vectors))
        await self.apply_notification_using_type(difference_in_vectors, vector_clock, vnf_forwarding_graph)
        if self.algorithm_type == 'causal' or self.algorithm_type == 'standard':
            self.log.info('My clock after notification: ' + self.vector_clock.as_string() + ' Pending operations: ' + str(len(self.pending_lcm_operations)))

    async def apply_notification_using_type(self, difference_in_vectors, vector_clock, vnf_forwarding_graph):
        if vnf_forwarding_graph['type'] == 'causal':
            await self.apply_notification_using_causal_algorithm(difference_in_vectors, vector_clock, vnf_forwarding_graph)
        elif vnf_forwarding_graph['type'] == 'standard':
            await self.apply_notification_using_standard_algorithm(vector_clock, vnf_forwarding_graph)
        elif vnf_forwarding_graph['type'] == 'last_writer_wins':
            await self.apply_notification_using_last_writer_win_algorithm(vnf_forwarding_graph)
        elif vnf_forwarding_graph['type'] == 'multi_value':
            self.log.info('Applying multi-value')
            await self.apply_notification_using_multi_value_algorithm()
        else:
            self.log.info('ERROR!')

    async def apply_notification_using_causal_algorithm(self, difference_in_vectors, vector_clock, vnf_forwarding_graph):
        if difference_in_vectors <= 1:
            self.log.info('Updating....')
            self.vector_clock.update_clock_with_a_string(vector_clock, self.log)
            await self.apply_vnf_fg_update_notification(vnf_forwarding_graph)
            total_pending_operations = len(self.pending_lcm_operations)
            self.log.info('Total pelding operations: ' + str(total_pending_operations))
            if total_pending_operations > 0:
                await self.do_pending_lcm_notifications_notifications()
        else:
            self.save_vnf_fg_update_notification(vnf_forwarding_graph)

    async def apply_notification_using_standard_algorithm(self, vector_clock, vnf_forwarding_graph):
        # self.log.info('Updating using standard algorithm....')
        self.vector_clock.update_clock_with_a_string(vector_clock, self.log)
        await self.apply_vnf_fg_update_notification(vnf_forwarding_graph)

    async def apply_notification_using_last_writer_win_algorithm(self, vnf_forwarding_graph):
        other_counter = int(vnf_forwarding_graph['vnffg_counter'])
        other_index = int(vnf_forwarding_graph['orchestrator_index'])
        # other_max_index = int(vnf_forwarding_graph['orchestrator_index'])
        # self.log.info('OP Value: {' + str(other_index) + ',' + str(other_counter) + '}')
        debug_change = False
        for vnf_fg_entry in self.vnf_forwarding_graphs:
            if vnf_fg_entry.get_identifier() == vnf_forwarding_graph['identifier']:
                my_counter = vnf_fg_entry.get_counter_of_entry(vnf_forwarding_graph, self.log)
                my_current_max_index = vnf_fg_entry.get_current_max_index_of_entry(vnf_forwarding_graph, self.log)
                if my_current_max_index == -1:
                    my_current_max_index = self.orchestrator_index
                debug_string = 'Received Notification for: ' + str(vnf_forwarding_graph['identifier'][0:8]) + ' ' + str(
                    vnf_forwarding_graph['change_identifier'][0:8])
                op_string = ' OP Value: {' + str(other_index) + ',' + str(other_counter) + '}'
                my_string = ' My Value: {' + str(self.orchestrator_index) + ',' + str(my_counter) + ', ' + str(my_current_max_index) + '}'
                self.log.info(debug_string + op_string + my_string)
                debug_first_condition = other_counter > my_counter
                debug_second_first_condition = other_counter == my_counter
                debug_second_second_condition = other_index > int(my_current_max_index)
                debug_second_condition = debug_second_first_condition and debug_second_second_condition
                # self.log.info('First condition is: ' + str(debug_first_condition))
                # self.log.info('Second condition is: ' + str(debug_second_condition))
                if debug_first_condition or debug_second_condition:
                    self.log.info('Applying update because First condition is ' + str(debug_first_condition) + ' Second condition is: ' + str(debug_second_condition))
                    debug_change = True
                    await self.apply_vnf_fg_update_notification(vnf_forwarding_graph)

        self.log.info('Applying notification or not?: ' + str(debug_change))

    async def apply_notification_using_multi_value_algorithm(self):
        print('apply_notification_using_multi_value_algorithm')

    def save_vnf_fg_update_notification(self, new_vnf_forwarding_graph):
        new_vector_clock = VectorClock()
        if type(new_vnf_forwarding_graph['vector_clock']) == str:
            new_vector_clock.create_from_list(new_vnf_forwarding_graph['vector_clock'])
        else:
            new_vector_clock.create_from_list(new_vnf_forwarding_graph['vector_clock'].as_string())

        new_pending_operation = PendingLCMScalingOperation(vnf_component_to_scale_id='',
                                                           operation='vnf_fg_update',
                                                           orchestrator_sender_id=new_vnf_forwarding_graph['orchestrator_id'],
                                                           sender_vector_clock=new_vector_clock,
                                                           data=new_vnf_forwarding_graph)
        self.add_pending_operation(new_pending_operation)

    async def apply_vnf_fg_update_notification(self, new_vnf_forwarding_graph):
        for vnf_fg_entry in self.vnf_forwarding_graphs:
            if vnf_fg_entry.get_identifier() == new_vnf_forwarding_graph['identifier']:
                if new_vnf_forwarding_graph['type_of_change'] == 'rsp':
                    new_change = self.create_vnf_fg_update_entry_rsp(new_vnf_forwarding_graph)
                    result = await self.update_vnf_forwarding_graph_unique_rsp(vnf_fg_entry, new_change)
                if new_vnf_forwarding_graph['type_of_change'] == 'classifier_rule':
                    new_change = self.create_vnf_fg_update_entry_classifier(new_vnf_forwarding_graph)
                    result = await self.update_vnf_forwarding_graph_unique_classifier(vnf_fg_entry, new_change)
                if self.algorithm_type == 'last_writer_wins':
                    self.log.info('After update {' + str(self.orchestrator_index) + ',' + str(result['vnffg'][['vnffg_counter']]) +'}')
        total_pending_operations = len(self.pending_lcm_operations)
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
            current_max_orchestrator_index=new_vnf_forwarding_graph['orchestrator_index']
            )
        return new_matching_attributed

    def create_vnf_fg_update_entry_rsp(self, new_vnf_forwarding_graph):
        new_vnf_connection_point_reference = VNFConnectionPointReference(
            identifier=new_vnf_forwarding_graph['change_identifier'],
            order=new_vnf_forwarding_graph['change_order'],
            ingress_connection_point=new_vnf_forwarding_graph['change_ingress_connection_point'],
            egress_connection_point=new_vnf_forwarding_graph['change_egress_connection_point'],
            counter=new_vnf_forwarding_graph['vnffg_counter'],
            current_max_orchestrator_index=new_vnf_forwarding_graph['orchestrator_index'])
        return new_vnf_connection_point_reference

    # DEBUG: Only to test if the inconsistency code is valid
    async def update_random_vnf_forwarding_graph(self):
        random_index_vnf_fg_entry = generate_random_integer(0, len(self.vnf_forwarding_graphs) - 1)
        random_index_connection_point = generate_random_integer(0, len(self.vnf_forwarding_graphs) - 1)
        service_path = self.vnf_forwarding_graphs[random_index_vnf_fg_entry].rendered_service_paths[0]
        connection_point = service_path.vnf_descriptor_connection_points[random_index_connection_point]
        print(connection_point)
        connection_point.order = -999

    async def update_vnf_forwarding_graph_unique_rsp(self,
                                                     old_vnf_fg: VNFForwardingGraph,
                                                     new_cp:VNFConnectionPointReference):
        self.log.info('Updating VNF-FG: ' + str(old_vnf_fg.identifier[0:8]) + ' RSP: ' + str(new_cp.vnf_identifier[0:8]))
        result = await old_vnf_fg.update_unique_rendered_service_path(new_cp, self.log, self.orchestrator_index)
        if self.algorithm_type == 'last_writer_wins':
            self.log.info('After update: {' + str(self.orchestrator_index) + ',' + str(result['new_counter']) + ',' + str(result['new_max_counter']) + '}')
        return result

    async def update_vnf_forwarding_graph_unique_classifier(self,
                                                            old_vnf_fg: VNFForwardingGraph,
                                                            new_matching_attribute: MatchingAttribute):
        self.log.info('Updating VNF-FG: ' + str(old_vnf_fg.identifier[0:8]) + ' CLA: ' + str(new_matching_attribute.identifier[0:8]))
        result = await old_vnf_fg.update_unique_classifier_rule(new_matching_attribute, self.log)
        if self.algorithm_type == 'last_writer_wins':
            self.log.info('After update: {' + str(self.orchestrator_index) + ',' + str(result['new_counter']) + ',' + str(result['new_max_couter']) + '}')
        return result
