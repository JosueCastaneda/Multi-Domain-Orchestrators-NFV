from communication_entities.messages.abstract_message import AbstractMessage


class ReplyProposedVNFForwardingGraphUpdateMessage(AbstractMessage):

    def __init__(self, host, port, data):
        super().__init__(None)
        self.current_server = None
        self.type = 'reply_to_notify_proposal_vnf_forwarding_graph'
        self.host = host
        self.port = port
        self.data = data


    def process_by_command_line(self):
        pass
