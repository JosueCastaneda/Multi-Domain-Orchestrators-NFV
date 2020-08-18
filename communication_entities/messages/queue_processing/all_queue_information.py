from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class AllQueueInformation(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.queue_p = data[0]
        self.queue_q = data[1]
        self.queue_r = data[2]
        self.current_server = None

    def process_by_command_line(self):
        log.info("Extending the current queues based with the previous one to new VNF")
        self.current_server.orchestrator.configuration.get_state().extend_queue("P", self.queue_p)
        self.current_server.orchestrator.configuration.get_state().extend_queue("Q", self.queue_q)
        self.current_server.orchestrator.configuration.get_state().extend_queue("R", self.queue_r)
        # Send an ack to synchronize servers
        ack_message = 'Queue received'
        self.client_socket.send(ack_message.encode("UTF-8"))
