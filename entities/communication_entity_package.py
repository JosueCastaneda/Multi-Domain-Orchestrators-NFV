class CommunicationEntityPackage:

    def __init__(self, host, port, clients=1):
        self.host = host
        self.port = port
        self.max_clients = clients