from communication.messages.abstract_message import AbstractMessage


class AddVNF(AbstractMessage):

    def __init__(self, vnf_host, vnf_port, vnf_name, topology):
        self.current_server = None
        self.vnf_host = vnf_host
        self.vnf_port = vnf_port
        self.vnf_name = vnf_name
        self.vnf_topology = topology

    def process_message(self):
        self.current_server.orchestrator.add_vnf(self.vnf_host, self.vnf_port,
                                                 self.vnf_name, self.vnf_topology)
