from communication_entities.messages.abstract_message import AbstractMessage


class GetOrchestratorInformation(AbstractMessage):

    def __init__(self, host, port, data):
        super().__init__(host=host, port=port, data=data)
        self.type = 'info'
