import os

from communication.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage


class GenericVNF:

    def __init__(self, host, port, name, clients=5, topology=None):
        self.server_param = CommunicationEntityPackage(host, port, clients)
        self.server = GenericServer(self, self.server_param)
        self.name = name
        self.topology = topology
        print("VNF: ", self.name, " is running!")
        self.serve_clients()

    def serve_clients(self):
        self.server.serve_clients()

    def remove_videos(name_original: str, name_processed: str):
        os.remove(name_original)
        os.remove(name_processed)
