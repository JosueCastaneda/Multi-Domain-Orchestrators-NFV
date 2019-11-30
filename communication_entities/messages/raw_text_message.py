import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from communication_entities.messages.send_all_states_message import SendAllStatesMessage
from communication_entities.messages.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.terminate_message_without_recursion import TerminateMessageWithoutRecursion
from utilities.logger import log


class RawTextMessage(AbstractMessage):

    def __init__(self, text):
        super().__init__(None)
        self.text = text

    def wait_for_r_queue(self):
        log.info('Waiting for R data from source VNF')
        m1 = self.client_socket.recv(8192)
        answer_message = pickle.loads(m1)
        for d in answer_message.data:
            self.current_server.orchestrator.add_states_to_queue(d, "R")

    def wait_for_terminate(self):
        log.info('Waiting for terminate message from current VNF')
        m2 = self.client_socket.recv(8192)
        answer_message = pickle.loads(m2)
        log.info('Received answer: ')
        if isinstance(answer_message, TerminateMessageWithoutRecursion):
            log.info('Sending my queues to current VNF')
            queue_p = self.current_server.orchestrator.queue_P
            queue_q = self.current_server.orchestrator.queue_Q
            queue_r = self.current_server.orchestrator.queue_R
            exchange_queue_message = SendAllStatesMessage(queue_p,
                                                          queue_q,
                                                          queue_r)
            log.info('Sending exchange queues to my current VNF')
            self.current_server.send_message_to_socket(self.client_socket, exchange_queue_message)
        log.info('Finish migration procedure from new vnf')

    def wait_for_all_queues(self):
        log.info('Waiting for Queues data from source VNF')
        m2 = self.client_socket.recv(8192)
        answer_message = pickle.loads(m2)
        # while not isinstance(answer_message, SendQueueQMessage) or isinstance(answer_message, SendQueuePMessage) :
        #     print('Answer message of type: ', type(answer_message))
        #     m2 = self.client_socket.recv(4096)
        #     answer_message = pickle.loads(m2)

        for d in answer_message.data[0]:
            self.current_server.orchestrator.add_states_to_queue(d, "Q")
        for d in answer_message.data[1]:
            self.current_server.orchestrator.add_states_to_queue(d, "P")
        self.current_server.orchestrator.add_affected_vnf(answer_message.data[2])
        m = MigrationAckMessage(None)
        log.info('Sending ACK to current VNF so he can terminate the connection')
        self.current_server.send_message_to_socket(self.client_socket, m)

    def process_by_command_line(self):
        self.wait_for_r_queue()
        self.wait_for_all_queues()
        self.wait_for_terminate()
