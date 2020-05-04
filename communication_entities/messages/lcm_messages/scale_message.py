from communication_entities.messages.abstract_message import AbstractMessage


class ScaleMessage(AbstractMessage):

    def __init__(self, vnfc_id, sender, service_id):
        super().__init__(None)
        self.vnfc_id = vnfc_id
        self.sender = sender
        self.service_id = service_id

    def process_by_command_line(self):
        self.current_server.orchestrator.scale(self.vnfc_id, self.sender, self.service_id)
