from communication_entities.messages.abstract_message import AbstractMessage


class InitiateVNFFGUpdatesMessage(AbstractMessage):

    def __init__(self):
        super().__init__(None)
        self.current_server = None

    def process_by_command_line(self):
        self.current_server.orchestrator.send_forwarding_path_updates_to_other_orchestrators()