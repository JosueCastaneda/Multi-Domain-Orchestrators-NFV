from communication_entities.messages.abstract_message import AbstractMessage
from entities.vnf_entities.vnf_information import VnfInformation


class AddVNF(AbstractMessage):

    def __init__(self,
                 id,
                 vnf_host,
                 vnf_port,
                 vnf_name,
                 topology=None,
                 migration_vnf_ip=None,
                 topology_migration_vnf=None,
                 connection_points=None,
                 dependency_list=None):
        super().__init__(None)
        self.id = id
        self.current_server = None
        self.vnf_host = vnf_host
        self.vnf_port = vnf_port
        self.vnf_name = vnf_name
        self.vnf_topology = topology
        self.migration_vnf_ip = migration_vnf_ip
        self.topology_migration_vnf = topology_migration_vnf
        self.connection_points = connection_points
        self.dependency_list = dependency_list
        self.message_type = 'add_vnf'
        self.data = dict()
        self.data['ip'] = self.vnf_host
        self.data['port'] = self.vnf_port
        self.data['name'] = self.vnf_name
        self.data['topology'] = self.vnf_topology
        self.data['migration_vnf_ip'] = self.migration_vnf_ip
        self.data['topology_migration_vnf'] = self.topology_migration_vnf
        self.data['connection_points'] = self.connection_points
        self.data['dependency_list'] = self.dependency_list
        self.data['id'] = self.id

    def process_by_command_line(self):
        vnf_information = VnfInformation(self.vnf_host,
                                         self.vnf_port,
                                         self.vnf_name,
                                         self.vnf_topology,
                                         self.migration_vnf_ip,
                                         self.topology_migration_vnf,
                                         self.connection_points,
                                         self.dependency_list,
                                         self.id)
        self.current_server.orchestrator.add_vnf(vnf_information)
