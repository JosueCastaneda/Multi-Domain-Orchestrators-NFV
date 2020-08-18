class VnfStaticConfiguration:

    def __init__(self, host, port, name, initial):
        self.host = host
        self.port = port
        self.name = name
        self.initial = initial

    def get_initial(self):
        return self.initial

    def get_vnf_name(self):
        return self.name

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port
