from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class RequestNewPopMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    # TODO: Program the new pop request to the orchestrator
    def process_message(self):
        log.info("New request")
