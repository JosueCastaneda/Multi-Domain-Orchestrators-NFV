import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class RawTextMessage(AbstractMessage):

    def __init__(self, text):
        super().__init__(None)
        self.text = text

    def wait_for_r_queue(self):
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        for d in answer_message.data:
            self.current_server.orchestrator.add_states_to_queue(d, "R")

    def wait_for_terminate(self):
        m2 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m2)
        log.info(answer_message)

    def wait_for_all_queues(self):
        m2 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m2)
        for d in answer_message.data[0]:
            self.current_server.orchestrator.add_states_to_queue(d, "Q")
        for d in answer_message.data[1]:
            self.current_server.orchestrator.add_states_to_queue(d, "P")
        self.current_server.orchestrator.add_affected_vnf(answer_message.data[2])

    def process_message(self):
        self.wait_for_r_queue()
        self.wait_for_all_queues()
        self.wait_for_terminate()
