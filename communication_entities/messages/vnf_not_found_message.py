from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class VNFNotFound(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    def process_message(self):
        log.info("Not found!")
