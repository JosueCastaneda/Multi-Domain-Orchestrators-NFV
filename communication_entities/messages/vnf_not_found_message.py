from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class VNFNotFound(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    def process_by_command_line(self):
        log.info("Not found!")
