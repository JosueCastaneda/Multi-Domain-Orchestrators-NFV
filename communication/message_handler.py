import sys

sys.path.append('../')
from communication.messages.migration import MigrationMessage
from communication.messages.abstract import AbstractMessage
from vnfs.package_processor import PackageProcessor


class MessageHandler:

    def __init__(self, server):
        self.server = server

    def handle_message(self, message: AbstractMessage):
        message.process_message()


    # def handle_message(self, parameters: MigrationMessage, client: socket):
    #
    #
    #     if parameters.message_type == MessageType.MIGRATION:
    #         self.handle_migration(parameters)
    #     elif parameters.message_type == MessageType.SEARCH_VNF:
    #         self.handle_search_for_vnf(parameters, client)
    #     # elif parameters.message_type == MessageType.ADD_VNF:
    #     #     self.handle_add_vnf(parameters)
    #     # elif parameters.message_type == MessageType.ADD_ORCH:
    #     #     self.handle_add_orchestrator(parameters)

    def handle_message_vnf(self, parameters: MigrationMessage):
        pkg_processor = PackageProcessor(parameters)
        answer = pkg_processor.process_package()
        return answer

    # TODO:LATER WE TEST
    # def handle_add_orchestrator(self, parameters):
    #     self.add_orchestrator(parameters.orchestrator)

    # TODO:LATER WE TEST
    # def handle_add_vnf(self, parameters):
    #     self.vnfs.append(parameters.vnf)

    # def handle_search_for_vnf(self, parameters: MigrationMessage, client: socket):
    #     vnf_local = self.server.orchestrator.get_local_vnf(parameters.source_vnf)
    #     if vnf_local is None:
    #         answer = MigrationMessage(MessageType.VNF_NOT_FOUND)
    #     else:
    #         answer = MigrationMessage(MessageType.VNF_FOUND, topology_pack=vnf_local.topology)
    #     data_string = pickle.dumps(answer)
    #     client.send(data_string)
    #     print("Server response: ", client.recv(1024).decode("UTF-8"))

    # def handle_migration(self, parameters: MigrationMessage):
    #     local_vnf = self.server.orchestrator.get_local_vnf(parameters.source_vnf)
    #     new_vnf = self.server.orchestrator.get_local_vnf(parameters.migration_vnf)
    #     if new_vnf is None:
    #         message_request = MigrationMessage(str(MessageType.SEARCH_VNF), parameters.migration_vnf)
    #         new_vnf_message = self.server.orchestrator.send_message_to_orchestrators(message_request)
    #     else:
    #         new_vnf_message = self.server.generate_new_message_parameters(new_vnf.topology)
    #     self.server.orchestrator.send_message_to_vnf(local_vnf, new_vnf_message)