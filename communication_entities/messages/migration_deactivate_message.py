import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from communication_entities.messages.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.switch_done_message import SwitchDoneMessage
from entities.service_package import ServicePackage
from utilities.logger import log
from utilities.socket_size import SocketSize


class MigrationDeactivateMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None
        self.migrating_vnfs = []

    # TODO: Use this instead of magic number: RECEIVE_BUFFER = 4096
    def handle_switch_exchange(self):
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        log.info(answer_message)
        m2 = SwitchDoneMessage(None)
        # TODO: This could only be a talk with self.client instead of server.send_socket
        self.current_server.send_message_to_socket(self.client_socket, m2)

    # TODO: Improve the class by using polymorphism and do not require three ifs
    # TODO: Duplicated code
    # TODO: Use this instead of magic number: RECEIVE_BUFFER = 4096
    def handle_queue_migration(self, operation):
        m1 = self.client_socket.recv(4096)
        answer_message = pickle.loads(m1)
        log.info(answer_message)
        return self.current_server.orchestrator.get_configuration().get_state().get_all_data_from_queue(operation)

    def check_if_migration_is_needed(self):
        print('Migration Deactivate Message: ', self.data)
        new_requirements = ServicePackage()
        new_requirements.create_from_topology(self.data)
        # print('New requirements type: ', type(new_requirements))
        # print('New requirements: ', new_requirements)
        old_requirements = self.current_server.orchestrator.topology
        current_services = self.current_server.orchestrator.service_package
        is_new_vnf_valid = True
        index_service = 1
        for service in current_services:
            log.info('Checking for Service #' + str(index_service))
            is_new_vnf_valid = service.is_new_vnf_valid_for_service(new_requirements, old_requirements)
            if not is_new_vnf_valid:
                log.info('Recursive migration is necessary')
                break
            index_service += 1
        recursive_took_place = False
        new_vnf = None
        if not is_new_vnf_valid:
            recursive_took_place, new_vnf = self.current_server.orchestrator.handle_recursive_migration(self.data, self.migrating_vnfs)
            log.info('New VNF was not valid - Migration deactivate message')
        return recursive_took_place, new_vnf

    # TODO: Check why the magnc numbers are necessary use RECEIVE_BUFFER = 4096

    def process_by_command_line(self):
        # for vnf in self.migrating_vnfs:
        #     print('Migrating IP vnf: ', vnf['ip'], ' mig_ip: ', vnf['mig_ip'])
        str_log = 'Received message from: ' + str(self.client_socket) + ' address: ' + str(self.client_address)
        log.info(str_log)
        recursive_migration_took_place, new_vnf = self.check_if_migration_is_needed()
        if recursive_migration_took_place:
            log.info('Recursive migration took place')
            m = MigrationAckMessage(new_vnf)
            log.info('Sending ACK to previous VNF so he can connect to the new vnf')
            self.current_server.send_message_to_socket(self.client_socket, m)
            log.info('Waiting for answer')
            x = self.client_socket.recv(4096)
            log.info('Answer:')
            log.info(x)
            return
            # sys.exit()
        log.info('No recursive migration took place')
        m = MigrationAckMessage("Ok")
        log.info('Sending ACK to previous VNF')
        self.current_server.send_message_to_socket(self.client_socket, m)

        data_q = self.handle_queue_migration("Q")
        m1 = SendQueueQMessage(data_q)
        log.info('Send Q message to previous VNF')
        self.current_server.send_message_to_socket(self.client_socket, m1)

        data_p = self.handle_queue_migration("P")
        m2 = SendQueuePMessage(data_p)
        log.info('Send P message to previous VNF')
        self.current_server.send_message_to_socket(self.client_socket, m2)
        self.handle_switch_exchange()
