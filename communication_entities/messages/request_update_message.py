from communication_entities.messages.abstract_message import AbstractMessage


class RequestUpdateMessage(AbstractMessage):

    def __init__(self, seed, end_time):
        super().__init__(None)
        self.current_server = None
        self.seed = seed
        self.end_time = end_time

    def process_by_command_line(self):
        self.current_server.orchestrator.request_update_to_orchestrator_and_save_time(self.seed)