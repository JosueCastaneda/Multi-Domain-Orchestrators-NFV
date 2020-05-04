import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.lcm_messages.migration.migration_ack_message import MigrationAckMessage
from communication_entities.messages.queue_processing.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.queue_processing.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.state_management.switch_done_message import SwitchDoneMessage
from entities.service_entities.service_package import ServicePackage
from utilities.logger import log


class MigrationDeactivateRecursiveMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    # TODO: Use the type RECEIVE_BUFFER = 4096
    def handle_switch_exchange(self):
        log.info('Waiting for SWITCH MESSAGE?')
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        log.info(answer_message)
        m2 = SwitchDoneMessage(None)
        log.info('Sending SwitchDoneMessage to previous client')
        self.current_server.send_message_to_socket(self.client_socket, m2)

    # TODO: Improve the class by using polymorphism and do not require three ifs
    # TODO use the type RECEIVE_BUFFER = 4096
    def handle_queue_migration(self, operation):
        str_log = 'Waiting for ' + operation + ' message'
        log.info(str_log)
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        str_log = 'Received message of type: ' + str(type(answer_message))
        log.info(str_log)
        log.info(answer_message)
        return self.current_server.orchestrator.get_configuration().get_state().get_all_data_from_queue(operation)

    def check_if_migration_is_needed(self):
        new_requirements = ServicePackage()
        new_requirements.create_from_topology(self.data)
        old_requirements = self.current_server.orchestrator.topology()
        current_service = self.current_server.orchestrator.service_package
        is_valid = current_service.is_new_vnf_valid_for_service(new_requirements, old_requirements)
        recursive_took_place = False
        new_vnf = None
        if not is_valid:
            recursive_took_place, new_vnf = self.current_server.orchestrator.handle_recursive_migration(self.data)
            log.info('check_if_migration_is_needed recursive - Migration Deactivate Recursive Message')
        return recursive_took_place, new_vnf

    def process_by_command_line(self):
        str_log = 'Received message from: ' + str(self.client_socket) + ' address: ' + str(self.client_address)
        log.info(str_log)
        log.info('Send ACK message to current VNF')
        ack_msg = MigrationAckMessage(None)
        self.current_server.send_message_to_socket(self.client_socket, ack_msg)
        data_q = self.handle_queue_migration("Q")
        m1 = SendQueueQMessage(data_q)
        log.info('Send SendQueueQMessage to previous VNF')
        self.current_server.send_message_to_socket(self.client_socket, m1)

        data_p = self.handle_queue_migration("P")
        m2 = SendQueuePMessage(data_p)
        log.info('Send SendQueuePMessage to previous VNF')
        self.current_server.send_message_to_socket(self.client_socket, m2)
        self.handle_switch_exchange()
