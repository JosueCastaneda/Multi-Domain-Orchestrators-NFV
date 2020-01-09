from communication_entities.messages.abstract_message import AbstractMessage


class InformOfVnfUpdate(AbstractMessage):

    def __init__(self, name_of_vnf_to_change, operation, delay, first=True, local_search=True):
        super().__init__(None)
        self.current_server = None
        self.name_of_vnf_to_change = name_of_vnf_to_change
        self.operation = operation
        self.first_operation = first
        self.delay = delay
        self.local_search = local_search

    def process_by_command_line(self):
        self.current_server.orchestrator.send_update_to_vnf_by_oss(self.name_of_vnf_to_change,
                                                                   self.operation,
                                                                   self.first_operation,
                                                                   self.delay,
                                                                   self.local_search)
