from communication_entities.messages.abstract_message import AbstractMessage


class UpdateVnfFgClassifierMessage(AbstractMessage):

    def __init__(self, identifier, ip_proto, source_ip, destination_ip, source_port, destination_port):
        super().__init__(None)
        self.current_server = None
        self.identifier = identifier
        self.ip_proto = ip_proto
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.data = dict()
        self.data['identifier'] = self.identifier
        self.data['ip_proto'] = self.ip_proto
        self.data['source_ip'] = self.source_ip
        self.data['destination_ip'] = self.destination_ip
        self.data['source_port'] = self.source_port
        self.data['destination_port'] = self.destination_port

    def process_by_command_line(self):
        pass
