from communication_entities.messages.abstract_message import AbstractMessage


class RequestUpdateMessage(AbstractMessage):

    def __init__(self, seed):
        super().__init__(None)
        self.current_server = None
        self.seed = seed

    def process_by_command_line(self):
        self.current_server.orchestrator.request_update_to_orchestrator(self.seed)