from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class SendQueueRMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_message(self):
        # Here we need to wait to handle the migration....
        log.info("Sending R message to R...")
        # Here we need to call our VNF and save the data from the message to our R queue
        print("Hey poderoso")

