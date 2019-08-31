import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.switch_done_message import SwitchDoneMessage
from entities.service_package import ServicePackage
from utilities.logger import *


class MigrationDeactivateMessage(AbstractMessage):

    def __init__(self, data, server=None):
        super().__init__(data)
        self.current_server = None


    def handle_switch_exchange(self):
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        m2 = SwitchDoneMessage(None)
        self.current_server.send_message_to_socket(self.client_socket, m2)

    # TODO: Improve the class by using polymorphism and dont require three ifs
    def handle_queue_migration(self, operation):
        # Receive message to send from queue
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        if operation == "P":
            data_queue_tmp = self.current_server.orchestrator.get_all_data_from_queue("P")
        elif operation == "Q":
            data_queue_tmp = self.current_server.orchestrator.get_all_data_from_queue("Q")
        else:
            data_queue_tmp = self.current_server.orchestrator.get_all_data_from_queue("R")
        return data_queue_tmp

    def check_if_migration_is_needed(self):
        new_requirements = ServicePackage()
        new_requirements.create_from_topology(self.data)
        is_valid = self.current_server.orchestrator.service_package.is_new_vnf_valid_for_service(new_requirements)
        if not is_valid:
            # self.data is a TopologyMessage
            self.current_server.orchestrator.check_migration_recursive(self.data)
            log.info("Migration chain")
        else:
            log.info("No migration is required")

    def process_message(self):
        # Here we need to wait to handle the migration....
        log.info("Checking if I need to migrate...")
        # x = CommunicationEntityPackage(self.data.ip, self.data.port)
        # self.current_server.connect_to_another_server(x)
        log.info("For the moment say ok")
        self.check_if_migration_is_needed()
        m = MigrationAckMessage("Ok")
        self.current_server.send_message_to_socket(self.client_socket, m)

        data_q = self.handle_queue_migration("Q")
        m1 = SendQueueQMessage(data_q)
        self.current_server.send_message_to_socket(self.client_socket, m1)

        data_p = self.handle_queue_migration("P")
        m2 = SendQueuePMessage(data_p)
        self.current_server.send_message_to_socket(self.client_socket, m2)
        self.handle_switch_exchange()
        print("Finish processing message")

