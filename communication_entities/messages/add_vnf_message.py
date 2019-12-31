from communication_entities.messages.abstract_message import AbstractMessage
from entities.vnf_information import VnfInformation


class AddVNF(AbstractMessage):

    def __init__(self, configuration):
        super().__init__(None)
        self.current_server = None
        self.vnf_host = configuration.host()
        self.vnf_port = configuration.port()
        self.vnf_name = configuration.name()
        self.vnf_topology = configuration.get_topology()
        self.migration_vnf_ip = configuration.migration_vnf()
        self.topology_migration_vnf = configuration.topology_migration_vnf()
        self.connection_points = configuration.get_connection_points()
        self.dependency_list = configuration.get_dependency_list()

    def process_by_command_line(self):
        vnf_information = VnfInformation(self.vnf_host,
                                         self.vnf_port,
                                         self.vnf_name,
                                         self.vnf_topology,
                                         self.migration_vnf_ip,
                                         self.topology_migration_vnf,
                                         self.connection_points,
                                         self.dependency_list)
        self.current_server.orchestrator.add_vnf(vnf_information)
