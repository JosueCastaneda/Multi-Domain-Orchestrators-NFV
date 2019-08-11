from communication.messages.abstract import AbstractMessage
from communication.messages.search_vnf import SearchVNFMessage


class MigrationMessage(AbstractMessage):

    def __init__(self):
        self.current_server = None

    def process_message(self):
        local_vnf = self.current_server.orchestrator.get_local_vnf(self.parameters.source_vnf)
        new_vnf = self.current_server.orchestrator.get_local_vnf(self.parameters.migration_vnf)
        if new_vnf is None:
            message_request = SearchVNFMessage(self.data)
            new_vnf_message = self.current_server.orchestrator.send_message_to_orchestrators(message_request)
        else:
            new_vnf_message = self.current_server.generate_new_message_parameters(new_vnf.topology)
        self.current_server.orchestrator.send_message_to_vnf(local_vnf, new_vnf_message)
