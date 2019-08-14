from communication.messages.abstract_message import AbstractMessage
from communication.messages.vnf_not_found_message import VNFNotFound
from communication.messages.vnf_found_message import VNFFound
from utilities.logger import *


class SearchVNFMessage(AbstractMessage):

    def __init__(self, data, server=None):
        super().__init__(data)
        self.current_server = server

    def process_message(self):
        vnf_local = self.current_server.orchestrator.get_local_vnf(self.data.vnf_name)
        if vnf_local is None:
            log.info("VNF not Found!")
            answer = VNFNotFound(self.data)
        else:
            log.info("Found!")
            self.data.topology = vnf_local[2]
            answer = VNFFound(self.data)
        log.info(''.join(["Sending message to", str(self.client_addres)]))
        self.current_server.connect_to_another_server(self.test_server)
        self.current_server.send_message(answer)
        self.current_server.get_ack_channel()
        self.current_server.disconnect_send_channel()
        self.terminate_connections()
