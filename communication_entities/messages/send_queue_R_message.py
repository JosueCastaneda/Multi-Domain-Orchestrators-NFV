from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class SendQueueRMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_message(self):
        log.info("Sending R message to R...")
