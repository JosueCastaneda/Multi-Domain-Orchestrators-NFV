import sys


sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.vnf_found_message import VNFFound
from utilities.logger import *


class Orchestrator:

    def __init__(self, server, orchestrators=None, topology=None, name=""):
        self.vnfs = {}
        self.orchestrators = orchestrators
        self.topology = topology
        self.server = GenericServer(self, server)
        self.name = name
        self.server_orch = server
        log.info(''.join(["Orchestrator: ", self.name, " is running!"]))

    def serve_clients(self):
        self.server.serve_clients()

    def get_local_vnf(self, vnf_name):
        return self.vnfs.get(vnf_name)

    # Todo: Implement this function to handle dynamic orchestrators
    def add_orchestrator(self, o_host, o_port, o_name):
        self.orchestrators.append((o_host, o_port, o_name))

    def add_vnf(self, vnf_host, vnf_port, vnf_name, topology):
        self.vnfs[vnf_name] = [vnf_host, vnf_port, topology]

    def remove_vnf(self, vnf_name):
        self.vnfs.remove(vnf_name)

    def send_message_to_vnf(self, vnf, message):
        vnf_server = CommunicationEntityPackage(vnf[0], vnf[1])
        self.server.connect_to_another_server(vnf_server)
        self.server.send_message(message)
        self.server.disconnect_send_channel()

    def search_and_remove_vnf(self, vnf):
        for v in self.vnfs:
            if self.are_vnfs_equal(self.vnfs[v], vnf):
                self.vnfs.pop(v)
                break

    # TODO: Implement the new vnf and its parameters for the link using threads
    def send_message_to_orchestrators(self, message):
        message.source_server = self.server
        for o in self.orchestrators:
            log.info(''.join(["Log Querying Orch: ", str(o[0]), " ", str(o[1])]))
            orch_server = CommunicationEntityPackage(o[0], o[1])
            self.server.connect_to_another_server(orch_server)
            message.source_server = None
            answer_message = self.server.send_message_query_vnf(message)
            self.server.disconnect_send_channel()
            if isinstance(answer_message, VNFFound):
                log.info(''.join(["Querying Orch: ", str(o[0]), " ", str(o[1]), " has it"]))
                return answer_message
            log.info(''.join(["Querying Orch: ", str(o[0]), " ", str(o[1]), " does not have it"]))
        return None
