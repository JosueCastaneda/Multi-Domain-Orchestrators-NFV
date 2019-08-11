class AbstractMessage:

    def __init__(self, data, client=None, source_server=None):
        self.data = data
        self.client = client
        self.source_server = source_server
        self.current_server = None
        self.client_socket = None

    def process_message(self):
        pass

    def terminate_connections(self):
        self.client_socket.close()
        self.current_server.disconnect_send_channel()
