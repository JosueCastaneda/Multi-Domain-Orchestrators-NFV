from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class SwitchDoneMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_message(self):
        # Here we need to wait to handle the migration....
        log.info("Switch done...")
        print("Hey poderoso")

