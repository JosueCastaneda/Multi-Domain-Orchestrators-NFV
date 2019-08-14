import os

import sys

sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.add_vnf_message import AddVNF
from utilities.logger import *


class GenericVNF:

    def __init__(self, host, port, name, clients=5, topology=None, orchestrator=None):
        self.server_param = CommunicationEntityPackage(host, port, clients)
        self.server = GenericServer(self, self.server_param)
        self.name = name
        self.topology = topology
        log.info(''.join(["VNF: ", self.name, " is running!"]))
        self.server.connect_to_another_server(orchestrator)
        add_message = AddVNF(host, port, self.name, self.topology)
        self.server.send_message(add_message)
        self.server.disconnect_send_channel()
        self.serve_clients()

    def serve_clients(self):
        self.server.serve_clients()

    def remove_videos(name_original: str, name_processed: str):
        os.remove(name_original)
        os.remove(name_processed)
