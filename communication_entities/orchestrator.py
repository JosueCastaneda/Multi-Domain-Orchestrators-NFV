import json
import pickle
import random
import sys
import threading

from communication_entities.messages.update_vnf_info_after_internal_operation import UpdateVnfInfoAfterInternalOperation

sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.vnf_found_message import VNFFound
from utilities.logger import *


class Orchestrator:

    def __init__(self, server, path, experiment_name, orchestrator_list=None, topology=None, name=""):
        self.list_vnf = dict()
        self.list_old_vnfs = []
        self.list_orchestrator = orchestrator_list
        if self.list_orchestrator is None:
            self.list_orchestrator = []
        self.topology = topology
        self.server = GenericServer(self, server)
        self.name = name
        self.server_orchestrator = server
        self.experiment_path = path
        self.experiment_name = experiment_name
        self.services = None
        self.vnf_fg_information = []
        self.vnf_fg_update_information = []
        self.logical_clock = dict()
        self.set_up_logical_clocks()
        self.add_service_information()
        log.info(''.join(["Orchestrator: ", self.name, " is running!"]))
        self.updates_remaining = 0
        self.inconsistencies = 0
        self.messages_sent = 0

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

    def add_service_information(self):
        self.load_services_information()
        self.add_virtual_network_function_forwarding_graph_information()

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

            # x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
            # answer_message = pickle.loads(x)
            # str_log = 'Received answer from new VNF TYPE: ' + str(type(answer_message))
            # self.server.disconnect_send_channel()

    def update_vnf_info(self, service_index, vnf_index_to_change, value_to_change, new_value, clock, name):
        log.info('Called after trigger ')
        my_clock = self.logical_clock[name] + 1
        if clock < my_clock:
            self.inconsistencies += 1
        self.vnf_fg_information[service_index][vnf_index_to_change][value_to_change] = new_value
        self.updates_remaining -= 1
        self.print_vnf_fg_information()

    def update_vnf_info_with_clocks(self, service_index, vnf_index_to_change, value_to_change, new_value, clock, name):
        # name_vnf_to_update = self.vnf_fg_information[service_index][vnf_index_to_change]['name']
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
        #wait_period += random.randint(0, 5)
        wait_period = random.randint(0, 2)
        str_log_wait = 'Waiting period: ' + str(wait_period)
        log.info(str_log_wait)

        t = threading.Timer(wait_period, self.update_vnf_info, [service_index,
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
        # t = threading.Timer(3.0, self.hello, [0, 1, 2, 'SAS'])

    def load_services_information(self):
        with open('experiments/' + self.experiment_path + self.experiment_name) as json_file:
            raw_data = json.load(json_file)
            self.services = raw_data['services']

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
        # # First check if the name is present in old ones to update
        # for old_vnfs in self.list_old_vnfs:
        #     if old_vnfs['name'] == vnf_name:
        # # If not then use the normal list

        return self.list_vnf.get(vnf_name)

    # Todo: Implement this function to handle dynamic orchestrator
    def add_orchestrator(self, o_host, o_port, o_name=""):
        self.list_orchestrator.append((o_host, o_port, o_name))

    # TODO: Use a dictionary, is more expressive than using indexes
    def add_vnf(self, vnf_information):
        self.list_vnf[vnf_information.name] = vnf_information
        log.info('Add following VNF: ')
        self.list_vnf[vnf_information.name].print_information()

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
                # SEND TO ALL ORCHESTRATORS MESSAGES
                for orquestrator in self.list_orchestrator:
                    print('Orchestrator: ', orquestrator)
                break

    def send_message_to_vnf(self, vnf, message):
        vnf_server = CommunicationEntityPackage(vnf[0], vnf[1])
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
            log.info(''.join(["Log Querying Orchestrator: ", str(o[0]), " ", str(o[1])]))
            orchestrator_server = CommunicationEntityPackage(o[0], o[1])
            self.server.connect_to_another_server(orchestrator_server)
            message.source_server = None
            answer_message = self.server.send_message_query_vnf(message)
            self.server.disconnect_send_channel()
            if isinstance(answer_message, VNFFound):
                log.info(''.join(["Querying Orchestrator: ", str(o[0]), " ", str(o[1]), " has it"]))
                return answer_message
            log.info(''.join(["Querying Orchestrator: ", str(o[0]), " ", str(o[1]), " does not have it"]))
        return None
