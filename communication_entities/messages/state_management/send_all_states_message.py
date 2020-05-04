from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class SendAllStatesMessage(AbstractMessage):

    def __init__(self, data, queue_p, queue_q, queue_r):
        super().__init__(data)
        self.current_server = None
        self.queue_p = queue_p
        self.queue_q = queue_q
        self.queue_r = queue_r

    def process_by_command_line(self):
        log.info("Updating queues with current vnf...")
        self.current_server.orchestrator.configuration_get_state().exchange_queues(self.queue_p,
                                                                                   self.queue_q,
                                                                                   self.queue_r)
        log.info("Finish updating queues with current vnf")