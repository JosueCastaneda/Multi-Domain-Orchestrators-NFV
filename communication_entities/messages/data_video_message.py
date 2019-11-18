from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class DataVideoMessage(AbstractMessage):

    def __init__(self, video_name, data_q):
        super().__init__(None)
        self.current_server = None
        self.video_name = video_name
        self.queue_p = data_q[0]
        self.queue_q = data_q[1]
        self.queue_r = data_q[2]

    def process_by_command_line(self):
        log.info("Extending the current queues based with the previous one to new VNF")
        self.current_server.orchestrator.extend_queue("P", self.queue_p)
        self.current_server.orchestrator.extend_queue("Q", self.queue_q)
        self.current_server.orchestrator.extend_queue("R", self.queue_r)

        log.info("Waiting for video from client")
        while True:
            conn, address = self.current_server.receive_two_communication_channel.accept()
            with open(self.video_name, 'wb') as f:
                log.info('receiving data...')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)

            f.close()
            log.info('Successfully got the file')
            conn.close()
            log.info('Connection closed')
            break
