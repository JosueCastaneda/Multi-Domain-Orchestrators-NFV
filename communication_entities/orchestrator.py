import json
import pickle
import random
import sys
import threading
import time

from communication_entities.generic_service import GenericService
from communication_entities.life_cycle_management import LifeCycleManagement
from communication_entities.messages.all_dependencies_are_registered import AllDependenciesAreRegistered
from communication_entities.messages.lcm_messages.notification_lcm_operation import NotificationLCMOperation
from communication_entities.messages.vnf_information.update_vnf_info_after_internal_operation import \
    UpdateVnfInfoAfterInternalOperation
from communication_entities.orchestrator_classes.pending_lcm_scaling_operation import PendingLCMScalingOperation
from communication_entities.vector_clock import VectorClock

sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.vnf_information.vnf_found_message import VNFFound
from utilities.logger import *


class Orchestrator:

    def __init__(self, experiment_index, orchestrator_index, causal_delivery=True):
        self.experiment_name = 'experiment_' + experiment_index + '.json'
        self.name = 'orch_' + orchestrator_index
        self.list_vnf = dict()
        self.list_old_vnfs = []
        self.list_orchestrator = list()
        self.pending_lcm_operations = list()
        if self.list_orchestrator is None:
            self.list_orchestrator = []
        self.topology = None
        communication_entity_pacakge = self.load_server_information()
        self.server = GenericServer(self, communication_entity_pacakge)
        self.services = list()
        self.vnfs = list()
        self.vnf_fg_information = []
        self.vnf_fg_update_information = []
        self.logical_clock = dict()
        self.set_up_logical_clocks()
        self.add_service_information()
        self.updates_remaining = 0
        self.inconsistencies = 0
        self.messages_sent = 0
        self.services_to_scale_unique = set()
        self.life_cycle_manager = LifeCycleManagement(self, self.vnfs, self.services)
        self.vector_clock = VectorClock(self.id)
        self.causal_delivery = causal_delivery
        self.pending_lcm_notifications = list()
        log.info(''.join(["Orchestrator: ", self.name, " is running!"]))

    # TODO: This function is too big with a lot of responsabilities...
    def load_server_information(self):
        str_new_file_name = 'experiments/experiment_generator/experiments/' + self.experiment_name
        with open(str_new_file_name) as json_file:
            raw_data = json.load(json_file)
        orchestrator_number = self.name.find('_')
        orchestrator_index = int(self.name[orchestrator_number + 1:])
        print('NAME: ' + str(self.name))
        print('ORCHESTRATOR INDEX: ' + str(orchestrator_index))
        print('IP: ' + str(raw_data['orchestrators'][orchestrator_index]['ip']))
        print('PORT: ' + str(raw_data['orchestrators'][orchestrator_index]['port']))
        print('IDS: ' + str(raw_data['orchestrators'][orchestrator_index]['id']))
        server = CommunicationEntityPackage(raw_data['orchestrators'][orchestrator_index]['ip'],
                                            int(raw_data['orchestrators'][orchestrator_index]['port']))
        self.id = raw_data['orchestrators'][orchestrator_index]['id']
        self.ip = raw_data['orchestrators'][orchestrator_index]['ip']
        self.port = raw_data['orchestrators'][orchestrator_index]['port']
        self.location = raw_data['orchestrators'][orchestrator_index]['location']
        return server

    def set_up_logical_clocks(self):
        self.logical_clock['ANNOTATE'] = 0
        self.logical_clock['BLACK_WHITE'] = 0
        self.logical_clock['COMPOSITE'] = 0
        self.logical_clock['CROP'] = 0
        self.logical_clock['FADE_IN'] = 0
        self.logical_clock['FADE_OUT'] = 0
        self.logical_clock['INVERT_COLORS'] = 0
        self.logical_clock['MIRROR_X'] = 0
        self.logical_clock['MIRROR_Y'] = 0
        self.logical_clock['PAINTING'] = 0
        self.logical_clock['RESIZE'] = 0
        self.logical_clock['ROTATE'] = 0
        self.logical_clock['SPEED_UP'] = 0

    def serve_clients(self):
        self.server.serve_clients()

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

    def send_update_message(self, service_index, vnf_index_to_change, value_to_change, new_value, wait_period):
        print("Changes: ", vnf_index_to_change, ' ', value_to_change, ' ', new_value)
        name_vnf_to_update = self.vnf_fg_information[service_index][vnf_index_to_change]['name']
        self.logical_clock[name_vnf_to_update] += 1
        self.vnf_fg_information[service_index][vnf_index_to_change][value_to_change] = new_value
        s = UpdateVnfInfoAfterInternalOperation(None,
                                                service_index,
                                                vnf_index_to_change,
                                                value_to_change,
                                                new_value,
                                                self.logical_clock[name_vnf_to_update],
                                                wait_period,
                                                name_vnf_to_update)
        for orchestrator in self.list_orchestrator:
            print('orchestrator: ', orchestrator)
            self.messages_sent += 1
            self.server.connect_to_another_server_raw(orchestrator[0], orchestrator[1])
            self.server.send_message(s)

    def update_vnf_info(self, service_index, vnf_index_to_change, value_to_change, new_value, clock, name):
        log.info('Called after trigger ')
        my_clock = self.logical_clock[name] + 1
        if clock < my_clock:
            self.inconsistencies += 1
        self.vnf_fg_information[service_index][vnf_index_to_change][value_to_change] = new_value
        self.updates_remaining -= 1
        self.print_vnf_fg_information()

    def send_lcm_message(self, message, destinatary):
        self.send_message_to_orchestrator(message, destinatary)

    # TODO: Lets try to wait here
    def send_message_to_orchestrator(self, message, destinatary):
        vnf_server = CommunicationEntityPackage(destinatary['ip'], destinatary['port'])
        self.server.connect_to_another_server(vnf_server)
        time.sleep(.5)
        self.server.send_message(message)
        self.server.disconnect_send_channel()

    def request_service_scale(self, service_id):
        log.info('Requested Scaling of service ' + str(service_id))
        self.vector_clock.increment_clock(self.id)
        for service in self.services:
            if service.id == service_id:
                service_as_dictionary = service.format_as_a_dictionary(is_first=True)
                for dependency in service.dependencies:
                    new_dependency_as_dictionary = dict()
                    new_dependency_as_dictionary['id'] = dependency['id']
                    new_dependency_as_dictionary['type'] = dependency['type']
                    new_dependency_as_dictionary['first_operation'] = True
                    service_as_dictionary['pending_operations'].append(new_dependency_as_dictionary)
                self.life_cycle_manager.add_new_service_to_scale(service.id, service_as_dictionary)
                service.scale()

    def get_orchestrator_information_by_id(self, orchestrator_id):
        for orchestrator in self.list_orchestrator:
            if orchestrator['id'] == orchestrator_id:
                return orchestrator
        my_orchestrator = dict()
        my_orchestrator['ip'] = self.ip
        my_orchestrator['port'] = self.port
        my_orchestrator['name'] = self.name
        my_orchestrator['id'] = self.id
        return my_orchestrator

    def entry_as_dictionary(self):
        orchestrator_format = dict()
        orchestrator_format['ip'] = self.ip
        orchestrator_format['port'] = self.port
        orchestrator_format['id'] = self.id
        orchestrator_format['name'] = self.name
        return orchestrator_format

    def get_service_by_id(self, service_id):
        for service in self.services:
            if service.id == service_id:
                return service

    def notification_of_lcm(self, vector_clock, sender_id):
        if sender_id == self.id:
            difference_in_vectors = 0
        else:
            difference_in_vectors = self.vector_clock.compare_clocks(vector_clock, sender_id, self.causal_delivery)
        if difference_in_vectors <= 1:
            self.vector_clock.update_clock(vector_clock, sender_id, self.causal_delivery)
            self.do_pending_lcm_notifications()
        else:
            if self.vector_clock.are_different(vector_clock.clock_list):
                new_pending_operation = PendingLCMScalingOperation('', 'notification', sender_id, vector_clock)
                self.pending_lcm_operations.append(new_pending_operation)

    def do_pending_lcm_notifications(self):
        for pending_operation in self.pending_lcm_operations:
            print('Do Pending operation')

    def grant_lcm_operation(self, vnf_component_to_scale_id, operation, original_service, sender_vector_clock=None):
        if original_service['orchestrator_id'] == self.id:
            difference_in_vectors = 0
        else:
            difference_in_vectors = self.vector_clock.compare_clocks(sender_vector_clock, original_service['orchestrator_id'], self.causal_delivery)
        if difference_in_vectors <= 1:
            if original_service['orchestrator_id'] != self.id:
                self.vector_clock.update_clock(sender_vector_clock,original_service['orchestrator_id'], self.causal_delivery)
            if operation == 'scaling':
                if not self.causal_delivery:
                    self.vector_clock.increment_clock(self.id)
                self.scale_vnfc_operation(vnf_component_to_scale_id, original_service)
            self.do_pending_operations(sender_vector_clock)
        else:
            self.add_pending_operation(vnf_component_to_scale_id, operation, original_service, sender_vector_clock)

    def add_pending_operation(self, vnf_component_to_scale_id, operation, original_service, sender_vector_clock):
        new_operation = PendingLCMScalingOperation(vnf_component_to_scale_id,
                                                   operation,
                                                   original_service,
                                                   sender_vector_clock)
        self.pending_lcm_operations.append(new_operation)

    def scale_vnfc_operation(self, vnf_component_to_scale_id, original_service):
        service_to_scale = self.get_service_by_id(vnf_component_to_scale_id)
        self.life_cycle_manager.add_new_service_to_scale(vnf_component_to_scale_id, original_service)
        is_ok_to_scale, no_dependencies = service_to_scale.validate_scaling()
        if is_ok_to_scale:
            service_to_scale.independent_scale(vnf_component_to_scale_id, original_service['original_service_id'])
        else:
            print('ERROR IN SCALING :(')

    def do_pending_operations(self, sender_vector_clock):
        operations_to_remove = list()
        clock_was_updated = True
        while clock_was_updated:
            at_least_one_clock_changed = False
            for operation in self.pending_lcm_operations:
                if operation.is_not_done and self.vector_clock.compare_stored_clock(operation.sender_vector_clock, self.causal_delivery):
                    self.vector_clock.update_clock(operation.sender_vector_clock, operation.original_service,
                                                   self.causal_delivery)
                    if operation.operation != 'notification':
                        self.scale_vnfc_operation(operation.vnf_component_to_scale_id, operation.original_service)
                    # self.vector_clock.update_clock(operation.sender_vector_clock, operation.original_service, self.causal_delivery)
                    operations_to_remove.append(operation)
                    operation.is_not_done = False
                    at_least_one_clock_changed = True
            clock_was_updated = at_least_one_clock_changed
        for operation in operations_to_remove:
            self.pending_lcm_operations.remove(operation)

    def remove_service_to_scale(self, service):
        self.services_to_scale_unique.remove(service)

    def update_vnf_info_with_clocks(self, service_index, vnf_index_to_change, value_to_change, new_value, clock, name):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.logical_clock[name] += 1
            my_clock = self.logical_clock[name]
            print('Internal clock: ', my_clock, ' External clock: ', clock)
            print('Old value: ', self.vnf_fg_information[service_index][vnf_index_to_change][value_to_change])
            if clock > my_clock:
                log.info('New clock')
                self.vnf_fg_information[service_index][vnf_index_to_change][value_to_change] = new_value
                self.logical_clock[name] = clock

            if self.logical_clock[name] < clock:
                print('Inconsistency- internal: ', self.logical_clock[name], ' external: ', clock)
                self.inconsistencies += 1

            print('New value: ', self.vnf_fg_information[service_index][vnf_index_to_change][value_to_change])
            self.updates_remaining -= 1
            self.print_vnf_fg_information()
        finally:
            lock.release()

    def print_vnf_fg_information(self):
        log.info('Services left to update: ' + str(self.updates_remaining))
        if self.updates_remaining == 0:
            pickle.dump(self.vnf_fg_information, open('vnf_fg_info' + self.name + '.p', 'wb'))
            for clock in self.logical_clock:
                str_log = 'Clock: ' + clock + ' val: ' + str(self.logical_clock[clock])
                log.info(str_log)
            str_incon = 'Inconsistencies: ' + str(self.inconsistencies)
            log.info(str_incon)
            str_message_overhead = 'Messages: ' + str(self.messages_sent)
            log.info(str_message_overhead)

    def update_vnf_info_timer(self, service_index, vnf_index_to_change, value_to_change, new_value, clock, wait_period, name_vnf_to_update):
        wait_period = random.randint(0, 40)
        str_log_wait = 'Waiting period: ' + str(wait_period)
        log.info(str_log_wait)
        other_algorithm = True
        if other_algorithm:
            t = threading.Timer(wait_period, self.update_vnf_info, [service_index,
                                                                    vnf_index_to_change,
                                                                    value_to_change,
                                                                    new_value,
                                                                    clock, name_vnf_to_update])
        else:
            t = threading.Timer(wait_period, self.update_vnf_info_with_clocks, [service_index,
                                                                    vnf_index_to_change,
                                                                    value_to_change,
                                                                    new_value,
                                                                    clock, name_vnf_to_update])
        self.updates_remaining += 1
        t.start()

    # This method should execute in an asynchronous wait to send messages asynchronously
    def send_forwarding_path_updates_to_other_orchestrators(self):
        print('Sending path')
        for service in self.vnf_fg_update_information[0]['updates']:
            vnf_index_to_change = service['vnf_index_to_change']
            value_to_change = service['value_to_change']
            new_value = service['new_value']
            wait_period = service['wait_period']
            self.send_update_message(0, vnf_index_to_change, value_to_change, new_value, wait_period)

        for service in self.vnf_fg_update_information[1]['updates']:
            vnf_index_to_change = service['vnf_index_to_change']
            value_to_change = service['value_to_change']
            new_value = service['new_value']
            wait_period = service['wait_period']
            self.send_update_message(1, vnf_index_to_change, value_to_change, new_value, wait_period)

        for service in self.vnf_fg_update_information[2]['updates']:
            vnf_index_to_change = service['vnf_index_to_change']
            value_to_change = service['value_to_change']
            new_value = service['new_value']
            wait_period = service['wait_period']
            self.send_update_message(2, vnf_index_to_change, value_to_change, new_value, wait_period)
        print('Finish sending messages')

    def load_vnf_components(self):
        str_new_file_name = 'experiments/experiment_generator/experiments/'+ self.experiment_name
        with open(str_new_file_name) as json_file:
            raw_data = json.load(json_file)
        orchestrator_number = self.name.find('_')
        orchestrator_index = int(self.name[orchestrator_number+1:])
        self.instantiate_services(raw_data['orchestrators'][orchestrator_index]['services'])
        self.vnfs = raw_data['orchestrators'][orchestrator_index]['vnfs']

    def instantiate_services(self, services):
        for service in services:
            new_service = GenericService(service['id'], self, service['dependencies'])
            self.services.append(new_service)

    def add_virtual_network_function_forwarding_graph_information(self):
        for service in self.services:
            self.vnf_fg_information.append(service['vnf-fg'])
        self.add_virtual_network_function_updates()

    def add_virtual_network_function_updates(self):
        update_services = []
        index_services = 1
        for service in self.services:
            update_vnfg = dict()
            update_vnfg['name'] = 'service_' + str(index_services)
            update_vnfg['updates'] = []
            for update in service['updates-vnf-fg']:
                index_orchestrator = update['orchestrator']
                if service['orch_names'][index_orchestrator] == self.name:
                    update_vnfg['updates'].append(update)
            update_services.append(update_vnfg)
            index_services += 1
        self.vnf_fg_update_information = update_services

    def print_state_vnf(self):
        log.info(''.join(["VNF name: ", self.name]))

    # TODO: Handle more cases of migration and the orchestrator requires to update his managed vnfs
    def get_local_vnf(self, vnf_name):
        return self.list_vnf.get(vnf_name)

    # Todo: Implement this function to handle dynamic orchestrator
    def add_orchestrator(self, o_host, o_port, o_name='', id=''):
        new_orchestrator = dict()
        new_orchestrator['ip'] = o_host
        new_orchestrator['port'] = o_port
        new_orchestrator['name'] = o_name
        new_orchestrator['id'] = id
        self.list_orchestrator.append(new_orchestrator)
        self.vector_clock.add_clock(id)

    # TODO: Use a dictionary, is more expressive than using indexes
    def add_vnf(self, vnf_information):
        self.list_vnf[vnf_information.name] = vnf_information
        log.info('Add following VNF: ')

    def mark_dependency_for_services(self, dependency_id):
        for service in self.services:
            self.mark_dependency_for_service(service, dependency_id)

    def mark_dependency_for_service(self, service, dependency_id):
        for dependency in service.dependencies:
            if dependency['id'] == dependency_id:
                self.decrease_dependencies_and_check_if_all_dependencies_are_registered(service)

    def decrease_dependencies_and_check_if_all_dependencies_are_registered(self, service):
        service.remaining_acknoledgments -= 1
        if service.remaining_acknoledgments == 0:
            self.acknowledge_other_orchestrators_that_all_dependencies_are_registered(service.id)

    def acknowledge_other_orchestrators_that_all_dependencies_are_registered(self, service_id):
        ack_message = AllDependenciesAreRegistered(service_id)
        self.send_message_to_orchestrators(ack_message)

    def remove_vnf(self, vnf_name):
        self.list_vnf.remove(vnf_name)

    # TODO: Add the other information required for this
    def update_vnf_after_migration(self, vnf_host, new_vnf_host, new_vnf_topolgy):
        for vnf in self.list_vnf:
            if self.list_vnf[vnf][0] == vnf_host:
                self.list_vnf[vnf][0] = new_vnf_host
                self.list_vnf[vnf][2] = new_vnf_topolgy
                old_vnf = dict()
                old_vnf['name'] = vnf
                old_vnf['ip'] = vnf_host
                self.list_old_vnfs.append(old_vnf)
                break

    def update_vnf_after_internal_operation(self, vnf_host, new_connection_points, new_dependencies):
        for vnf in self.list_vnf:
            if self.list_vnf[vnf].name == vnf_host:
                self.list_vnf[vnf].connection_points= new_connection_points
                self.list_vnf[vnf].dependency_list = new_dependencies
                old_vnf = dict()
                old_vnf['name'] = vnf
                old_vnf['ip'] = vnf_host
                self.list_old_vnfs.append(old_vnf)
                for orquestrator in self.list_orchestrator:
                    print('Orchestrator: ', orquestrator)
                break

    def send_message_to_vnf(self, vnf, message):
        vnf_server = CommunicationEntityPackage(vnf['server'], int(vnf['port']))
        self.server.connect_to_another_server(vnf_server)
        self.server.send_message(message)
        self.server.disconnect_send_channel()

    def search_and_remove_vnf(self, vnf):
        for v in self.list_vnf:
            if self.are_vnfs_equal(self.list_vnf[v], vnf):
                self.list_vnf.pop(v)
                break

    # TODO: Implement the new vnf and its parameters for the link using threads
    def send_message_to_orchestrators(self, message):
        message.source_server = self.server
        for o in self.list_orchestrator:
            log.info(''.join(["Log Querying Orchestrator: ", str(o['ip']), " ", str(o['port'])]))
            orchestrator_server = CommunicationEntityPackage(o['ip'], o['port'])
            self.server.connect_to_another_server(orchestrator_server)
            message.source_server = None
            answer_message = self.server.send_message_query_vnf(message)
            self.server.disconnect_send_channel()
            if isinstance(answer_message, VNFFound):
                log.info(''.join(["Querying Orchestrator: ", str(o['ip']), " ", str(o['port']), " has it"]))
                return answer_message
            log.info(''.join(["Querying Orchestrator: ", str(o['ip']), " ", str(o['port']), " does not have it"]))
        return None
