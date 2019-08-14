from communication.messages.abstract_message import AbstractMessage
from communication.messages.search_vnf_message import SearchVNFMessage
from entities.parameter_package import ParameterPackage
from utilities.logger import *

class MigrationMessage(AbstractMessage):
    """
        The migration messaged sent to the orchestrator
    """

    def __init__(self, source_vnf_name, next_in_chain_vnf_name):
        """
        Set up the message
        :param source_vnf_name: The VNF to be migrated
        :param next_in_chain_vnf_name: The VNF that appears in the SFC after the source
        :param data: Data to check if migration is possible
        """
        self.current_server = None
        self.source_vnf_name = source_vnf_name
        self.next_in_chain_vnf_name = next_in_chain_vnf_name

    def process_message(self):
        local_vnf = self.current_server.orchestrator.get_local_vnf(self.source_vnf_name)
        new_vnf = self.current_server.orchestrator.get_local_vnf(self.next_in_chain_vnf_name)
        if new_vnf is None:
            log.info("Not found, sending to orchestrators...")
            data = ParameterPackage(vnf_name=self.next_in_chain_vnf_name)
            message_request = SearchVNFMessage(data)
            message_request.test_server = self.current_server.orchestrator.server_orch
            found_message = self.current_server.orchestrator.send_message_to_orchestrators(message_request)
            new_vnf_message = self.current_server.generate_new_message_parameters(found_message.data.topology)
        else:
            new_vnf_message = self.current_server.generate_new_message_parameters(new_vnf.topology)
        self.current_server.orchestrator.send_message_to_vnf(local_vnf, new_vnf_message)
