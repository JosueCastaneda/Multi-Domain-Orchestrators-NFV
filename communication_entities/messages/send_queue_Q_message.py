from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class SendQueueQMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_message(self):
        log.info("Sending Q message to Q...")
