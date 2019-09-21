class CommunicationEntityPackage:

    def __init__(self, host, port, clients=5):
        self.host = host
        self.port = port
        self.max_clients = clients
