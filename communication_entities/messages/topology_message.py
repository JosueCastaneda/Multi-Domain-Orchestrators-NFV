import sys

from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class TopologyMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_by_command_line(self):
        log.info("Topology message received...")
        self.current_server.orchestrator.check_migration_affected(self)
        log.info("Finish processing message")
        # TODO: Include this in the recursive migration scenario to elinminate the VNF once is finish
        # sys.exit()
