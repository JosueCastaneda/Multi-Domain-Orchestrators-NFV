from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class AllQueueInformation(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_message(self):
        # Here we need to wait to handle the migration....
        log.info("Saving the queue to new VNF")
