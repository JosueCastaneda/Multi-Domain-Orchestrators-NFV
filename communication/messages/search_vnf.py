import pickle

from communication.messages.abstract import AbstractMessage
from communication.messages.vnf_not_found import VNFNotFound
from communication.messages.vnf_found import VNFFound


class SearchVNFMessage(AbstractMessage):

    def __init__(self, server=None):
        self.current_server = server
        print('Hello')

    def process_message(self):
        vnf_local = self.current_server.orchestrator.get_local_vnf(self.parameters.source_vnf)
        if vnf_local is None:
            answer = VNFNotFound(self.data)
        else:
            answer = VNFFound(self.data, topology=vnf_local.topology)
        data_string = pickle.dumps(answer)
        self.client.send(data_string)
        print("Server response: ", self.client.recv(1024).decode("UTF-8"))