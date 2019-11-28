from communication_entities.messages.abstract_message import AbstractMessage


class AddVNF(AbstractMessage):

    def __init__(self, vnf_host, vnf_port, vnf_name, topology=None, migration_vnf_ip=None, topology_migration_vnf=None):
        super().__init__(None)
        self.current_server = None
        self.vnf_host = vnf_host
        self.vnf_port = vnf_port
        self.vnf_name = vnf_name
        self.vnf_topology = topology
        self.migration_vnf_ip = migration_vnf_ip
        self.topology_migration_vnf = topology_migration_vnf

    def process_by_command_line(self):
        self.current_server.orchestrator.add_vnf(self.vnf_host,
                                                 self.vnf_port,
                                                 self.vnf_name,
                                                 self.vnf_topology,
                                                 self.migration_vnf_ip,
                                                 self.topology_migration_vnf)
