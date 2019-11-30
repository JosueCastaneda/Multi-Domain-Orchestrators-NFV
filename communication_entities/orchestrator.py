import sys


sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.vnf_found_message import VNFFound
from utilities.logger import *


class Orchestrator:

    def __init__(self, server, orchestrator_list=None, topology=None, name=""):
        self.list_vnf = dict()
        self.list_old_vnfs = []
        self.list_orchestrator = orchestrator_list
        if self.list_orchestrator == None:
            self.list_orchestrator = []
        self.topology = topology
        self.server = GenericServer(self, server)
        self.name = name
        self.server_orchestrator = server
        log.info(''.join(["Orchestrator: ", self.name, " is running!"]))

    def serve_clients(self):
        self.server.serve_clients()

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
    def add_vnf(self, vnf_host, vnf_port, vnf_name, topology, migration_ip, topology_migration_vnf):
        self.list_vnf[vnf_name] = [vnf_host, vnf_port, topology, migration_ip, topology_migration_vnf]
        log.info('Add following VNF: ')
        print(self.list_vnf[vnf_name])

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
