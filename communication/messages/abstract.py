class AbstractMessage:

    def __init__(self, data, client=None):
        self.data = data
        self.client = client

    def process_message(self):
        pass
