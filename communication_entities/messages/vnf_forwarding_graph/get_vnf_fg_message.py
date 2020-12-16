from communication_entities.messages.abstract_message import AbstractMessage


class GetVNFFGMessage(AbstractMessage):

    def __init__(self, host, port, data):
        super().__init__(host=host, port=port, data=data)
        self.type = 'get_vnf_forwarding_graphs'
