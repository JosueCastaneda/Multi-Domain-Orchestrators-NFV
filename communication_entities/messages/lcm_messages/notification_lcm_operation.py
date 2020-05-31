from communication_entities.messages.abstract_message import AbstractMessage


class NotificationLCMOperation(AbstractMessage):

    def __init__(self, vector_clock, service_id):
        super().__init__(None)
        self.vector_clock = vector_clock
        self.service_id = service_id

    def process_by_command_line(self):
        self.current_server.orchestrator.notification_of_lcm(self.vector_clock, self.service_id)

