from communication_entities.messages.abstract_message import AbstractMessage


class RequestUpdateAllVNFFGSequentialMessage(AbstractMessage):

    def __init__(self):
        super().__init__(None)
        self.current_server = None

    def process_by_command_line(self):
        pass