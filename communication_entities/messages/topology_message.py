from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *
import sys


class TopologyMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    def process_message(self):
        log.info("Topology message received...")
        self.current_server.orchestrator.check_migration_affected(self)
        print("Finish processing message")
        sys.exit()
