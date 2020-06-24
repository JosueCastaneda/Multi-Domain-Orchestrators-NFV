from communication_entities.messages.abstract_message import AbstractMessage


class AddOrchestratorMessage(AbstractMessage):

    def __init__(self, vnf_host, vnf_port, vnf_name='', topology=None, orchestrator_id=''):
        super().__init__(None)
        self.current_server = None
        self.vnf_host = vnf_host
        self.vnf_port = vnf_port
        self.vnf_name = vnf_name
        self.vnf_topology = topology
        self.orchestrator_id = orchestrator_id
        self.data = dict()
        self.data['id'] = self.orchestrator_id
        self.data['ip'] = self.vnf_host
        self.data['port'] = self.vnf_port
        self.data['name'] = self.vnf_name

    def process_by_command_line(self):
        self.current_server.orchestrator.add_orchestrator(self.vnf_host,
                                                          self.vnf_port,
                                                          self.vnf_name,
                                                          self.orchestrator_id)
