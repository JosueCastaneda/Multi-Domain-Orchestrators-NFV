from communication_entities.messages.abstract_message import AbstractMessage


class UpdateVnfFgRenderedServicePathMessage(AbstractMessage):

    def __init__(self, vnf_identifier, order, ingress_connection_point, egress_connection_point):
        super().__init__(None)
        self.current_server = None
        self.vnf_identifier = vnf_identifier
        self.order = order
        self.ingress_connection_point = ingress_connection_point
        self.egress_connection_point = egress_connection_point
        self.data = dict()
        self.data['vnf_identifier'] = self.vnf_identifier
        self.data['order'] = self.order
        self.data['ingress_connection_point'] = self.ingress_connection_point
        self.data['egress_connection_point'] = self.egress_connection_point

    def process_by_command_line(self):
        self.current_server.orchestrator.send_forwarding_path_updates_to_other_orchestrators()
