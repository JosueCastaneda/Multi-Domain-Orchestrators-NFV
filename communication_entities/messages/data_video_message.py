from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class DataVideoMessage(AbstractMessage):

    def __init__(self, video_name):
        super().__init__(None)
        self.current_server = None
        self.video_name = video_name

    def process_message(self):
        log.info("Waiting for video from client")

        while True:
            conn, address = self.current_server.receive_two_communication_channel.accept()
            log.info('Got connection from', address)

            # with open("test_video.mp4", 'wb') as f:
            with open(self.video_name, 'wb') as f:
                log.info('file opened')
                while True:
                    log.info('receiving data...')
                    data = conn.recv(1024)
                    log.info('data=%s', data)
                    if not data:
                        break
                    f.write(data)

            f.close()
            log.info('Successfully get the file')
            conn.close()
            log.info('connection closed')
            break
