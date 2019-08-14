from communication.messages.abstract_message import AbstractMessage
from utilities.logger import *


class VNFFound(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    # TODO: Call the server methods to save this
    def process_message(self):
        log.info("VNF found!")
