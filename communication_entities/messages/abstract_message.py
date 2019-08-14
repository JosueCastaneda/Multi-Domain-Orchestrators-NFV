class AbstractMessage:
    """
        This class represents a generic message, all messages
        have the process_message function and override it with
        their own implementation
    """
    def __init__(self, data, client=None, source_server=None):
        self.data = data
        self.client = client
        self.source_server = source_server
        self.current_server = None
        self.client_socket = None
        self.client_addres = None
        self.test_server = None

    def process_message(self):
        pass

    def terminate_connections(self):
        self.client_socket.close()
        self.current_server.disconnect_send_channel()
