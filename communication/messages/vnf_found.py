from communication.messages.abstract import AbstractMessage

class VNFFound(AbstractMessage):

    def __init__(self, topology):
        self.topology = topology

    def process_message(self):
        print("HELLO")
