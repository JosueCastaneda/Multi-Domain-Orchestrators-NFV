from communication_entities.messages.abstract_message import AbstractMessage
import pickle


class RawTextMessage(AbstractMessage):

    def __init__(self, text):
        self.text = text

    def wait_for_R_queue(self):
        # Wait for the sending of queue R
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)

    def wait_for_terminate(self):
        m2 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m2)

    def wait_for_all_queues(self):
        m2 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m2)
        self.current_server.orchestrator.add_affected_vnf(answer_message.data[3])
        # TODO: Update the queues for the state
        # print("Hello")

    def process_message(self):
        print("Hello my friend: ", self.text)
        self.wait_for_R_queue()
        self.wait_for_all_queues()
        self.wait_for_terminate()
        print("Finish processing message")
