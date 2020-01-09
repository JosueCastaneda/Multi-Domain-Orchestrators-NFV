from communication_entities.messages.abstract_message import AbstractMessage


class UpdateOperationMessage(AbstractMessage):

    def __init__(self, operation, first=False, local_search=True):
        super().__init__(None)
        self.current_server = None
        self.operation = operation
        self.first = first
        self.local_search = local_search

    # TODO: Update
    def process_by_command_line(self):
        print('Update operation')
        self.current_server.orchestrator.update_vnf_by_operation_simple(self.operation,
                                                                        self.first)
