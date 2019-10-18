from communication_entities.messages.abstract_message import AbstractMessage


class AddOrchestratorMessage(AbstractMessage):

    def __init__(self, vnf_host, vnf_port, vnf_name="", topology=None):
        super().__init__(None)
        self.current_server = None
        self.vnf_host = vnf_host
        self.vnf_port = vnf_port
        self.vnf_name = vnf_name
        self.vnf_topology = topology

    def process_by_command_line(self):
        self.current_server.orchestrator.add_orchestrator(self.vnf_host, self.vnf_port)
