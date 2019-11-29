from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.search_vnf_message import SearchVNFMessage
from entities.parameter_package import ParameterPackage
from entities.topology import Topology


class MigrationMessage(AbstractMessage):
    """
        The migration message sent to the orchestrator
    """

    def __init__(self, source_vnf_name, new_in_chain_vnf_name):
        """
        Set up the message
        :param source_vnf_name: The VNF to be migrated
        :param new_in_chain_vnf_name: The VNF that appears in the SFC after the source
        """
        super().__init__(None)
        self.current_server = None
        self.source_vnf_name = source_vnf_name
        self.new_in_chain_vnf_name = new_in_chain_vnf_name

    # TODO: Change the magic number to another better representation
    def process_by_command_line(self):
        local_vnf = self.current_server.orchestrator.get_local_vnf(self.source_vnf_name)
        print('Local VNF')
        print(local_vnf)
        new_vnf_constraints = local_vnf[4].split(',')
        # new_vnf = self.current_server.orchestrator.get_local_vnf(self.new_in_chain_vnf_name)
        new_topology = Topology(new_vnf_constraints[0],
                                new_vnf_constraints[1],
                                new_vnf_constraints[2],
                                new_vnf_constraints[3],
                                ip=local_vnf[3],
                                port=4437)
        new_vnf_message = self.current_server.generate_new_message_parameters(new_topology)
        # if new_vnf is None:
        #     data = ParameterPackage(vnf_name=self.new_in_chain_vnf_name)
        #     message_request = SearchVNFMessage(data)
        #     message_request.test_server = self.current_server.orchestrator.server_orchestrator
        #     found_message = self.current_server.orchestrator.send_message_to_orchestrators(message_request)
        #     new_vnf_message = self.current_server.generate_new_message_parameters(found_message.data.topology)
        # else:
        #     new_vnf_message = self.current_server.generate_new_message_parameters(new_vnf.topology)
        print("Message type: ", type(new_vnf_message))
        print('Data: ', new_vnf_message.data.file_pack)
        print('Data delay: ', new_vnf_message.data.file_pack.delay)
        print('Data bandwidth: ', new_vnf_message.data.file_pack.bandwidth)
        print('Data loss: ', new_vnf_message.data.file_pack.loss)
        print('Data jitter: ', new_vnf_message.data.file_pack.jitter)

        self.current_server.orchestrator.send_message_to_vnf(local_vnf, new_vnf_message)
        # This next line can be commented when debugging since it will remove the vnf and further testing cannot be done
        # self.current_server.orchestrator.search_and_remove_vnf(local_vnf)

