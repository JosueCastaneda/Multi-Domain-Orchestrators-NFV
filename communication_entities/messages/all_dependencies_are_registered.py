from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class AllDependenciesAreRegistered(AbstractMessage):

    def __init__(self, service_id):
        super().__init__(None)
        self.current_server = None
        self.service_id = service_id

    def process_by_command_line(self):
        log.info('Received new Service (ID):' + str(self.service_id))
        # self.current_server.orchestrator.mark_dependency_for_services(self.service_id)

