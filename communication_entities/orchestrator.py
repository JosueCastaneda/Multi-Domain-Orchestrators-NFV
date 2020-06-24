import asyncio
import json
import random
import sys

from communication_entities.generic_service import GenericService
from communication_entities.life_cycle_management import LifeCycleManagement
from communication_entities.messages.lcm_messages.notification_lcm_operation import NotificationLCMOperation
from communication_entities.orchestrator_classes.pending_lcm_scaling_operation import PendingLCMScalingOperation
from communication_entities.vector_clock import VectorClock
from utilities.life_cycle_management_update import return_success, return_failure, return_in_process, send_message

sys.path.append('../')

from utilities.logger import *


def is_orchestrator_included_for_notification(id_orch, excluding_list):
    for orchestrator in excluding_list:
        if isinstance(orchestrator, str):
            if id_orch == orchestrator:
                return False
        elif id_orch == orchestrator['id']:
            return False
    return True


class Orchestrator:

    def __init__(self, experiment_index, orchestrator_index, server_host, server_port, causal_delivery=True):
        self.experiment_name = 'experiment_' + experiment_index + '.json'
        self.name = 'orch_' + orchestrator_index
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
        self.inconsistencies = 0
        self.messages_sent = 0
        self.load_server_information()
        self.add_service_information()
        self.life_cycle_manager = LifeCycleManagement(self, self.vnfs, self.services)
        self.vector_clock = VectorClock(self.id)
        self.causal_delivery = causal_delivery
        self.random_seed = 1000
        self.pending_operations_repetitions = 0
        random.seed(self.random_seed)
        log.info(''.join(["Orchestrator: ", self.name, " is running on host ", self.ip, ' port: ', str(self.port)]))

    def load_server_information(self):
        str_new_file_name = 'experiments/experiment_generator/experiments/' + self.experiment_name
        with open(str_new_file_name) as json_file:
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

    async def request_service_scale(self, service_id) -> json:
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
        return orchestrator_format

    def get_service_by_id(self, service_id):
        log.info('Get service id: ' + str(service_id))
        for service in self.services:
            log.info('Service id: ' + str(service.id))
            if service.id == service_id:
                return service

    async def wait_before_notification(self, vector_clock, orchestrator_sender_id):
        wait_period = random.randint(0, 10)
        await asyncio.sleep(wait_period)
        await self.notification_of_lcm(vector_clock, orchestrator_sender_id)

    async def notification_of_lcm(self, vector_clock_string, orchestrator_sender_id):
        vector_clock = VectorClock()
        vector_clock.create_from_list(vector_clock_string)
        log.info('Received ' + vector_clock.as_string() + ' from orchestrator: ' + str(
            orchestrator_sender_id) + ' My clock ' + self.vector_clock.as_string())
        if orchestrator_sender_id == self.id:
            difference_in_vectors = 0
        else:
            difference_in_vectors = self.vector_clock.compare_clocks(vector_clock, orchestrator_sender_id,
                                                                     self.causal_delivery)
        if difference_in_vectors <= 1:
            if not self.vector_clock.is_equal(vector_clock):
                self.vector_clock.update_clock(vector_clock, orchestrator_sender_id, self.causal_delivery)
            await self.do_pending_lcm_notifications_notifications()
        else:
            if self.vector_clock.are_different(vector_clock.clock_list):
                log.info('Saving notification as a pending operation')
                new_pending_operation = PendingLCMScalingOperation(vnf_component_to_scale_id='',
                                                                   operation='notification',
                                                                   original_service_id='',
                                                                   orchestrator_sender_id=orchestrator_sender_id,
                                                                   original_orchestrator_id='',
                                                                   sender_vector_clock=vector_clock,
                                                                   service_sender_id='')
                self.pending_lcm_operations.append(new_pending_operation)
        log.info('Orchestrator Pending Operations in ' + str(
            len(self.pending_lcm_operations)) + ' Lifecycle management pending operations: ' + str(
            len(self.life_cycle_manager.pending_operations)))
        log.info('Vector Clock: ' + self.vector_clock.as_string())
        self.pending_operations_repetitions = 0
        return_success()

    async def notify_all_orchestrators_of_change(self, exclude_list_of_orchestrators, current_vector_clock):
        exclude_list_of_orchestrators.append(self.id)
        data = dict()
        data['vector_clock'] = current_vector_clock.to_json()
        data['orchestrator_sender_id'] = self.id
        for orchestrator in self.list_orchestrator:
            if is_orchestrator_included_for_notification(orchestrator['id'], exclude_list_of_orchestrators):
                new_message = NotificationLCMOperation(host=orchestrator['ip'],
                                                       port=str(orchestrator['port']),
                                                       data=data)
                await asyncio.create_task(send_message(new_message))

    async def do_pending_lcm_notifications_notifications(self):
        log.info('Do pending LCM NOTIFICATION')
        at_least_one_clock_changed = True
        while at_least_one_clock_changed:
            change_took_place = False
            repetitions_message = 0
            total_pending_operations = len(self.pending_lcm_operations)
            log.info('Total pending operations: ' + str(total_pending_operations) + ' Pending LCM operations' + str(
                len(self.pending_lcm_operations)))
            while self.pending_lcm_operations and repetitions_message < total_pending_operations and self.pending_operations_repetitions < total_pending_operations:
                repetitions_message += 1
                pending_operation = self.pending_lcm_operations.pop(0)
                if type(pending_operation.sender_vector_clock) == str:
                    new_vector_clock = VectorClock()
                    new_vector_clock.create_from_list(pending_operation.sender_vector_clock)
                    pending_operation.sender_vector_clock = new_vector_clock
                log.info('Pending operation' + str(pending_operation) + ' Repetition: ' + str(
                    self.pending_operations_repetitions) + ' Total pending: ' + str(total_pending_operations))
                log.info('Orchestrator sender ID: ' + str(
                    pending_operation.orchestrator_sender_id) + ' VT: ' + pending_operation.sender_vector_clock.as_string())
                log.info('My vector clock: ' + self.vector_clock.as_string())
                difference_in_clocks = self.vector_clock.compare_clocks(pending_operation.sender_vector_clock,
                                                                        pending_operation.orchestrator_sender_id,
                                                                        self.causal_delivery)
                if difference_in_clocks == 2:
                    difference_in_clocks, real_orchestrator_sender_id = self.vector_clock.check_single_difference(
                        pending_operation.sender_vector_clock)
                    if difference_in_clocks == 1:
                        pending_operation.orchestrator_sender_id = real_orchestrator_sender_id

                log.info('Difference in clocks: ' + str(difference_in_clocks))
                if difference_in_clocks <= 1:
                    if pending_operation.operation == 'notification' and pending_operation.is_not_done:
                        log.info('Notification and pending operation is not done')
                        self.vector_clock.update_clock(pending_operation.sender_vector_clock,
                                                       pending_operation.orchestrator_sender_id)
                        pending_operation.is_not_done = False
                        change_took_place = True

                    elif pending_operation.operation == 'scale' or pending_operation.operation == 'scaling' and pending_operation.is_not_done:
                        log.info('Scaling operation and pending operation is not done')
                        pending_operation.is_not_done = False
                        change_took_place = True
                        await self.life_cycle_manager.scale_confirmation(pending_operation.vnf_component_to_scale_id,
                                                                         pending_operation.original_service_id,
                                                                         pending_operation.orchestrator_sender_id,
                                                                         pending_operation.original_orchestrator_id,
                                                                         pending_operation.sender_vector_clock,
                                                                         pending_operation.service_sender_id)
                    else:
                        log.info('Something went horribly wrong')

                else:
                    self.pending_lcm_operations.append(pending_operation)
            at_least_one_clock_changed = change_took_place

    async def wait_before_delivery_grant(self, vnf_component_to_scale_id, operation, original_service,
                                         sender_vector_clock=None):
        wait_period = random.randint(0, 10)
        await asyncio.sleep(wait_period)
        await self.grant_lcm_operation_of_service(vnf_component_to_scale_id, operation, original_service,
                                                  sender_vector_clock)
        return return_in_process('Grant in process')

    async def grant_lcm_operation_of_service(self, vnf_component_to_scale_id, operation, original_service,
                                             sender_vector_clock=None):
        log.info('Can you please scale: ' + str(vnf_component_to_scale_id) + ' originally from ' + str(
            original_service['original_service_id']))
        log.info('Received ' + sender_vector_clock.as_string() + ' My clock ' + self.vector_clock.as_string())
        if self.causal_delivery:
            await self.grant_lcm_operation_causal(vnf_component_to_scale_id, operation, original_service,
                                                  sender_vector_clock)

    # async def grant_lcm_operation_normal(self, vnf_component_to_scale_id, operation, original_service,
    #                                      sender_vector_clock=None):
    #     difference_in_vectors = self.vector_clock.compare_clocks(sender_vector_clock,
    #                                                              original_service['orchestrator_id'],
    #                                                              self.causal_delivery)
    #     if difference_in_vectors > 1:
    #         self.inconsistencies += 1
    #
    #     if original_service['orchestrator_id'] != self.id:
    #         self.vector_clock.update_clock(sender_vector_clock, original_service['orchestrator_id'],
    #                                        self.causal_delivery)
    #     if operation == 'scaling':
    #         service_to_scale = self.get_service_by_id(vnf_component_to_scale_id)
    #         self.life_cycle_manager.add_new_service_to_scale(vnf_component_to_scale_id, original_service)
    #         is_ok_to_scale, no_dependencies = service_to_scale.validate_scaling()
    #         if is_ok_to_scale:
    #             service_to_scale.independent_scale_normal(vnf_component_to_scale_id,
    #                                                       original_service['original_service_id'],
    #                                                       original_service['orchestrator_id'])
    #         else:
    #             print('ERROR IN SCALING :(')

    def compute_difference_in_vectors(self, original_service, sender_vector_clock) -> int:
        if original_service['orchestrator_id'] != self.id:
            return self.vector_clock.compare_clocks(sender_vector_clock, original_service['orchestrator_id'],
                                                    self.causal_delivery)
        return 100

    async def do_lcm_operation(self, original_service, sender_vector_clock, operation, vnf_component_to_scale_id):
        if original_service['orchestrator_id'] != self.id:
            self.vector_clock.update_clock(sender_vector_clock, original_service['orchestrator_id'],
                                           self.causal_delivery)
        await asyncio.gather(self.scale_vnfc_operation(vnf_component_to_scale_id, original_service),
                             self.do_pending_operations())

    async def grant_lcm_operation_causal(self, vnf_component_to_scale_id, operation, original_service,
                                         sender_vector_clock=None):
        difference_in_vectors = self.compute_difference_in_vectors(original_service, sender_vector_clock)
        if difference_in_vectors <= 1:
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

    def add_pending_operation(self, new_operation) -> None:
        log.info('Adding operation to pending LCM')
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
        log.info('Grant LCM Causal Entry Pending Operations ' + str(
            self.pending_operations_repetitions) + 'Are VNFs SCALED? ' + str(self.life_cycle_manager.are_VNFs_scaled))
        self.pending_operations_repetitions += 1
        clock_was_updated = True
        while clock_was_updated:
            at_least_one_clock_changed = False
            repetitions_message = 0
            total_pending_operations = len(self.pending_lcm_operations)
            while self.pending_lcm_operations and repetitions_message < total_pending_operations and self.pending_operations_repetitions < total_pending_operations:
                repetitions_message += 1
                operation = self.pending_lcm_operations.pop(0)
                clock_difference = self.vector_clock.compare_stored_clock(operation.sender_vector_clock,
                                                                          self.causal_delivery)
                log.info('My Clock: ' + str(self.vector_clock.as_string()) + 'Sender Vector clock: ' + str(
                    operation.sender_vector_clock.as_string()))
                log.info('Clock difference: ' + str(clock_difference))
                if operation.is_not_done and self.vector_clock.compare_stored_clock(operation.sender_vector_clock,
                                                                                    self.causal_delivery):
                    if operation.operation != 'notification':
                        operation.is_not_done = False
                        at_least_one_clock_changed = True
                        log.info('Doing pending operation ' + str(
                            operation.vnf_component_to_scale_id) + ' originally from: ' + str(
                            operation.original_service_id))
                        await self.grant_lcm_operation_causal(operation.vnf_component_to_scale_id, 'scale',
                                                              operation.original_service, operation.sender_vector_clock)
                else:
                    log.info('Adding operation to LCM Operations')
                    self.pending_lcm_operations.append(operation)
            clock_was_updated = at_least_one_clock_changed
        self.pending_operations_repetitions = 0
        log.info('End pending operations')

    def load_vnf_components(self):
        str_new_file_name = 'experiments/experiment_generator/experiments/' + self.experiment_name
        with open(str_new_file_name) as json_file:
            raw_data = json.load(json_file)
        orchestrator_number = self.name.find('_')
        orchestrator_index = int(self.name[orchestrator_number + 1:])
        self.instantiate_services(raw_data['orchestrators'][orchestrator_index]['services'])
        self.vnfs = raw_data['orchestrators'][orchestrator_index]['vnfs']

    def instantiate_services(self, services):
        for service in services:
            new_service = GenericService(service['id'], self, service['dependencies'])
            self.services.append(new_service)

    def print_state_vnf(self):
        log.info(''.join(["VNF name: ", self.name]))

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
