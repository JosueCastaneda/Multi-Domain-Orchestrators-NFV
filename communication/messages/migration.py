from communication.messages.abstract import AbstractMessage


class MigrationMessage(AbstractMessage):

    # def __init__(self, operation, migration_vnf_name="", source_vnf_name="",
    #              topology_pack=None, migration_vnf=None, source_vnf=None):
    #     self.message_type = operation
    #     self.topology = topology_pack
    #     self.source_vnf_name = source_vnf_name
    #     self.migration_vnf_name = migration_vnf_name
    #     self.migration_vnf = migration_vnf
    #     self.source_vnf = source_vnf

    def __init__(self, server):
        self.server = server

    def process_message(self):
        local_vnf = self.server.orchestrator.get_local_vnf(self.parameters.source_vnf)
        new_vnf = self.server.orchestrator.get_local_vnf(self.parameters.migration_vnf)
        if new_vnf is None:
            message_request = MigrationMessage(self.data)
            new_vnf_message = self.server.orchestrator.send_message_to_orchestrators(message_request)
        else:
            new_vnf_message = self.server.generate_new_message_parameters(new_vnf.topology)
        self.server.orchestrator.send_message_to_vnf(local_vnf, new_vnf_message)
