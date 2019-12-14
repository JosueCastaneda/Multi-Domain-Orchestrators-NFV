import random
import time

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from utilities.logger import log


class RequestUpdateFromOrchestratorMessage(AbstractMessage):

    def __init__(self, seed):
        super().__init__(None)
        self.current_server = None
        self.save_client_socket = None
        log.info('SEED IS: ')
        log.info(str(seed))
        self.seed = seed

    def answer_back(self):
        m = MigrationAckMessage(None)
        log.info('Sending ACK to previous VNF so he can connect to the new vnf')
        self.current_server.send_message_to_socket(self.client_socket, m)

    def process_by_command_line(self):
        random.seed(self.seed)
        wait_period = random.uniform(0, 1)
        time.sleep(wait_period)
        self.answer_back()