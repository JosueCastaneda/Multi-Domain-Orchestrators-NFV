from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class OrderingMessage(AbstractMessage):

    def __init__(self, text):
        super().__init__(None)
        self.text = text

    def process_by_command_line(self):
        str_log = 'Received message from: ' + str(self.client_socket) + ' address: ' + str(self.client_address)
        log.info(self.text)
        log.info(str_log)
