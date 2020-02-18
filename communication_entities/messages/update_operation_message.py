from communication_entities.messages.abstract_message import AbstractMessage


class UpdateVnfViaOperationMessage(AbstractMessage):

    # TODO: Change to the configuration to save space
    def __init__(self, configuration):
        super().__init__(None)
        self.current_server = None
        self.operation = configuration.operation
        self.first = configuration.first
        self.local_search = configuration.local_search
        self.wait_period = configuration.wait_period
        self.clock = configuration.clock
        self.time_elapsed = configuration.time_elapsed

    # TODO: Update
    def process_by_command_line(self):
        print('Update operation')
        self.current_server.orchestrator.update_vnf_by_operation_simple(self.operation,
                                                                        self.first,
                                                                        self.wait_period,
                                                                        self.clock,
                                                                        self.time_elapsed)
