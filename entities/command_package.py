class CommandPackage:

    def __init__(self):
        # self.host = "10.0.0.13"
        # self.port = 4433
        # self.name = ""
        # self.new_name = ""
        # self.message_type = "process"
        # self.vnf_host = None
        # self.vnf_port = None
        self.host = "127.0.0.1"
        # self.host = "10.0.0.32"
        self.port = 5463
        self.name = "other"
        self.new_name = ''
        self.message_type = "migration"
        self.vnf_host = None
        self.vnf_port = None
        self.experiment = ''
        self.seed = None
        self.help_message = "message_factory.py -t <message_type> -h <host> -p <port>" \
                            " -n <name> -m <new_name> -v <vnf_host> -w <vnf_port>"

    def is_valid(self):
        all_parameters_given = self.host != "" and self.port != "" and \
                               self.message_type != "" and self.vnf_host != "" and self.vnf_port != ""
        all_parameters_format = True
        return all_parameters_given and all_parameters_format
