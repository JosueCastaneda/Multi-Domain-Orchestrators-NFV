from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class SwitchDoneMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_by_command_line(self):
        log.info("Switch done...")
