from utilities.logger import log


class VnfState:

    def __init__(self, initial_value=0):
        self.queue_P = [initial_value]
        self.queue_Q = [initial_value + 1]
        self.queue_R = [initial_value + 2]

    def get_all_queue_data(self):
        data = list()
        data.append(self.queue_P)
        data.append(self.queue_Q)
        data.append(self.queue_R)
        return data

    def add_states_to_queue(self, state, operation):
        if operation == "P":
            self.queue_P.append(state)
        elif operation == "Q":
            self.queue_Q.append(state)
        elif operation == "R":
            self.queue_R.append(state)

    def extend_queue(self, queue, extension):
        if queue == "P":
            self.queue_P.extend(extension)
        elif queue == "Q":
            self.queue_Q.extend(extension)
        elif queue == "R":
            self.queue_R.extend(extension)

    def process_all_data_in_queues(self, new_vnf):
        x2 = self.process_queue(self.queue_Q)
        x3 = self.process_queue(self.queue_P)
        all_data = [x2, x3, new_vnf]
        return all_data

    def exchange_queues(self, new_queue_p, new_queue_q, new_queue_r):
        self.queue_P = new_queue_p
        self.queue_Q = new_queue_q
        self.queue_R = new_queue_r

    def process_queue(self, my_queue):
        log.info("Processing queue.....")
        return my_queue

    def get_and_remove_first_element_in_p(self):
        return self.queue_P.pop(0)

    def get_and_remove_first_element_in_q(self):
        return self.queue_Q.pop(0)

    def get_and_remove_first_element_in_r(self):
        return self.queue_R.pop(0)

    # TODO: Use polymorphism to improve this function. Or better, use the queue to do the operation
    def get_all_data_from_queue(self, queue):
        str_log = 'Collecting data from queue:' + str(queue)
        log.info(str_log)
        data = []
        if queue == "P":
            while self.queue_P:
                data.append(self.get_and_remove_first_element_in_p())
        elif queue == "Q":
            while self.queue_Q:
                data.append(self.get_and_remove_first_element_in_q())
        elif queue == "R":
            while self.queue_R:
                data.append(self.get_and_remove_first_element_in_r())
        return data

    # TODO: Continue working with this class
    # def collect_data_to_queue(self, queue: list):
    #     log.info('Waiting for answer from previous nfv')
    #     x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
    #     answer_message = pickle.loads(x)
    #     str_log = 'Message received of type: ' + str(type(answer_message))
    #     log.info(str_log)
    #     for d in answer_message.data:
    #         queue.append(d)

    # def collect_data_to_p_queue(self):

    def get_p(self):
        return self.queue_P

    def get_q(self):
        return self.queue_Q

    def get_r(self):
        return self.queue_R