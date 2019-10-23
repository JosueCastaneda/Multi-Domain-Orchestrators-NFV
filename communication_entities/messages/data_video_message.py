from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class DataVideoMessage(AbstractMessage):

    def __init__(self, video_name):
        super().__init__(None)
        self.current_server = None
        self.video_name = video_name

    def process_by_command_line(self):
        log.info("Waiting for video from client")

        while True:
            conn, address = self.current_server.receive_two_communication_channel.accept()
            # TODO: Check this address variable because triggers a bug since it contains an integer
            # log.info('Got connection from', address)

            # with open("test_video.mp4", 'wb') as f:
            with open(self.video_name, 'wb') as f:
                # log.info('file opened')
                log.info('receiving data...')
                while True:
                    # log.info('receiving data...')
                    data = conn.recv(1024)
                    # log.info('data=%s', data)
                    if not data:
                        break
                    f.write(data)

            f.close()
            log.info('Successfully got the file')
            conn.close()
            log.info('connection closed')
            break
