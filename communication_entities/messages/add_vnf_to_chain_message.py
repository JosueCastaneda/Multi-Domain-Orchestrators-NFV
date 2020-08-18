from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class AddVNFToChainMessage(AbstractMessage):

    def __init__(self, host, port):
        super().__init__(None)
        self.current_server = None
        self.data = dict()
        self.data['ip'] = host
        self.data['port'] = port

    def process_by_command_line(self):
        log.info("Adding VNF to the chain...")
        self.current_server.orchestrator.add_affected_vnf(self.data)
