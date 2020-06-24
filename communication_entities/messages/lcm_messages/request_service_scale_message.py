from communication_entities.messages.abstract_message import AbstractMessage


class RequestServiceScaleMessage(AbstractMessage):

    def __init__(self, service_id, seed):
        super().__init__(None)
        self.service_id = service_id
        self.data = dict()
        self.data['service_id'] = service_id
        # TODO: REMOVE THIS SEED
        self.seed = seed

    def process_by_command_line(self):
        self.current_server.orchestrator.request_service_scale(self.service_id)
