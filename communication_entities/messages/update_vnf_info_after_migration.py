from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class UpdateVnfInfoAfterMigration(AbstractMessage):

    def __init__(self, configuration):
        super().__init__(configuration.host())
        self.previous_vnf = configuration.host()
        self.new_vnf = configuration.migration_vnf()
        self.new_vnf_topology = configuration.topology_migration_vnf()
        self.current_server = None

    def process_by_command_line(self):
        log.info("UpdateVnfInfoAfterMigration...")
        self.current_server.orchestrator.update_vnf_after_migration(self.previous_vnf,
                                                                    self.new_vnf,
                                                                    self.new_vnf_topology)
        log.info("Finish processing message")
