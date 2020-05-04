from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class VNFFound(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    # TODO: Call the server methods to save this
    def process_by_command_line(self):
        log.info("VNF found!")
