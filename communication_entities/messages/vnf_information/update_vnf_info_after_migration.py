from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class UpdateVnfInfoAfterMigration(AbstractMessage):

    def __init__(self, data, previous_vnf, new_vnf, new_vnf_topology):
        super().__init__(data)
        self.current_server = None
        self.previous_vnf = previous_vnf
        self.new_vnf = new_vnf
        self.new_vnf_topology = new_vnf_topology

    def process_by_command_line(self):
        log.info("UpdateVnfInfoAfterMigration...")
        # self.current_server.orchestrator.update_vnf_after_migration(self.previous_vnf,
        #                                                             self.new_vnf,
        #                                                             self.new_vnf_topology)
        # log.info("Finish processing message")
