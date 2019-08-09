from communication.messages.abstract import AbstractMessage


class VNFNotFound(AbstractMessage):

    def __init__(self):
        print("Hello")

    def process_message(self):
        print("hello")
