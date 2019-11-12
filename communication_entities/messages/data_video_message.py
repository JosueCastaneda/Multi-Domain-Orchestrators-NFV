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
            events = self.current_server.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    self.current_server.accept_wrapper(key.fileobj)
                else:
                    self.current_server.service_connection_two_channel(key, mask, self.video_name)
                    break

            # conn, address = self.current_server.receive_two_communication_channel.accept()
            # with open(self.video_name, 'wb') as f:
            #     log.info('receiving data...')
            #     while True:
            #         data = conn.recv(1024)
            #         if not data:
            #             break
            #         f.write(data)
            #
            # f.close()
            # log.info('Successfully got the file')
            # conn.close()
            # log.info('Connection closed')
            # break
