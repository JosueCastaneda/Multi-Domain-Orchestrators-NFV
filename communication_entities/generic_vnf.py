import pickle
import random
import time

from communication_entities.generic_server import GenericServer
from communication_entities.messages.add_vnf_message import AddVNF
from communication_entities.messages.all_queue_information import AllQueueInformation
from communication_entities.messages.inform_of_vnf_update import InformOfVnfUpdate
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from communication_entities.messages.migration_deactivate_recusive_message import MigrationDeactivateRecursiveMessage
from communication_entities.messages.raw_text_message import RawTextMessage
from communication_entities.messages.request_update_from_orchestrator_message import \
    RequestUpdateFromOrchestratorMessage
from communication_entities.messages.send_all_states_message import SendAllStatesMessage
from communication_entities.messages.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.send_queue_R_message import SendQueueRMessage
from communication_entities.messages.switch_message import SwitchMessage
from communication_entities.messages.terminate_message import TerminateMessage
from communication_entities.messages.terminate_message_without_recursion import TerminateMessageWithoutRecursion
from communication_entities.messages.update_vnf_info_after_migration import UpdateVnfInfoAfterMigration
from entities.communication_entity_package import CommunicationEntityPackage
from entities.topology import Topology
from utilities.logger import log
from utilities.socket_size import SocketSize
from utilities.string_constants import StringConstants
from utilities.vnf_factory import crete_new_vnf_from_topology, create_migration_deactivate_message
from utilities.vnf_fg_update import save_update_time, save_migration_time


class GenericVNF:

    def __init__(self, configuration):
        self.configuration = configuration
        self.server = GenericServer(self, CommunicationEntityPackage(configuration.host(),
                                                                     configuration.port()))
        self.list_affected_vnf = []
        self.orchestrator = configuration.get_orchestrator()
        self.migration_vnf_ip = configuration.migration_vnf()
        self.set_up_to_orchestrator()
        self.print_state_vnf()

    def set_up_to_orchestrator(self):
        add_message = AddVNF(self.configuration)
        self.connect_and_send_message_to_orchestrator(add_message)

    def get_configuration(self):
        return self.configuration

    def print_state_vnf(self):
        self.configuration.print_state_vnf()

    def handle_recursive_migration(self, new_vnf_topology, migrating_vnfs=None):
        if len(self.list_affected_vnf) > 0:
            new_vnf_topology = self.configuration.topology_migration_vnf().split(',')
            new_vnf = crete_new_vnf_from_topology(new_vnf_topology, self.migration_vnf_ip)
            self.begin_migration(new_vnf)
            self.handle_migration_affected(new_vnf, migrating_vnfs)
            log.info("Recursive migration is completed")
            return True, new_vnf
        log.info("Recursive migration is completed no affected VNFs")
        return False, None

    def send_all_data_in_queues(self, all_data):
        self.send_all_data_from_current_vnf_to_new_vnf(all_data)

    def handle_migration_affected(self, new_vnf, migrating_vnfs=None):
        for v in self.list_affected_vnf:
            is_cycle_found = False
            is_first_migration = False
            if migrating_vnfs is None:
                is_first_migration = self.handle_first_migration(v, new_vnf)
            else:
                is_cycle_found = self.handle_recursive_migration()
            if not is_cycle_found:
                self.handle_queues_from_previous_vnf_in_chain()
            self.send_data_from_r_queue_to_new_vnf()
            if not is_cycle_found:
                self.migration_switch_message_exchange()
            self.handle_queues_during_migration(new_vnf)
            self.terminate_migration_affected(is_first_migration)
            break

    def terminate_migration_affected(self, is_first_migration):
        if is_first_migration:
            self.terminate_migration_without_recursion()
        else:
            self.terminate_migration()

    def handle_queues_during_migration(self, new_vnf):
        log.info('Finished with previous VNF now is the NEW VNF')
        all_data = self.configuration.get_state().process_all_data_in_queues(new_vnf)
        self.send_all_data_in_queues(all_data)

    def handle_first_migration(self, v, new_vnf):
        log.info('First VNF, no migrating VNFS to check')
        self.check_if_previous_vnf_must_migrate(v, new_vnf)
        log.info('No migrating VNFs')
        return True

    def handle_recursive_migration(self, v, new_vnf, migrating_vnfs):
        log.info('We already have migrating VNFs')
        if not self.is_affected_vnf_already_migrating(v.host, migrating_vnfs):
            self.check_if_previous_vnf_must_migrate(v, new_vnf, migrating_vnfs)
            log.info('No cycle in the migrating list')
            return False
        log.info('Cycle detected!')
        return True

    def is_affected_vnf_already_migrating(self, vnf, migrating_vnfs):
        for mig_vnf in migrating_vnfs:
            if vnf == mig_vnf['ip']:
                log.info('VNF found, cycle detected!')
                self.update_affected_vnf(vnf, mig_vnf['mig_ip'])
                return True
        return False

    def update_affected_vnf(self, vnf, new_vnf_ip):
        for affected_vnf in self.list_affected_vnf:
            if affected_vnf.host == vnf:
                affected_vnf.host = new_vnf_ip
                break

    def check_migration_affected(self, message):
        new_vnf = message.data.file_pack
        str_log = 'New VNF: ' + new_vnf + ' New delay: ' + new_vnf.delay + ' new bandwidth: ' + new_vnf.delay
        str_log_extended = str_log + ' new loss: ' + new_vnf.loss + ' new jitter: ' + new_vnf.jitter
        log.info(str_log_extended)
        log.info('Begin migration')
        start_migration_time = time.time()
        self.begin_migration(new_vnf)
        log.info('Begin handle migration of affected')
        self.handle_migration_affected(new_vnf)
        end_migration_time = time.time()
        total_migration_time = end_migration_time - start_migration_time
        save_migration_time(total_migration_time)

    def begin_migration(self, new_vnf):
        virtual_link_new_vnf_socket = CommunicationEntityPackage(new_vnf.ip, new_vnf.port, 1)
        log.info(''.join(["New IP: ", new_vnf.ip, " New Port ", str(new_vnf.port)]))
        self.server.connect_to_another_server_virtual(virtual_link_new_vnf_socket)
        raw_text_message = RawTextMessage("Ready to migrate")
        self.send_message_using_virtual_channel(StringConstants.SEND_NEW_VNF_BEGIN_MIGRATION, raw_text_message)
        self.get_answer_from_new_vnf()

    def terminate_migration(self):
        log.info('Sending terminate with recursion')
        m1 = TerminateMessage(None)
        self.send_message_using_virtual_channel(StringConstants.SEND_NEW_VNF_TERMINATE_MESSAGE, m1)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()
        log.info('Finished disconnecting all the channels')
        self.update_information_after_migration_to_orchestrator()
        self.print_state_vnf()

    def terminate_migration_without_recursion(self):
        log.info('Sending terminate without recursion')
        m1 = TerminateMessageWithoutRecursion(None)
        self.send_message_using_virtual_channel(StringConstants.SEND_NEW_VNF_TERMINATE_MIGRATION_NO_RECURSION, m1)
        answer_message = self.get_answer_from_new_vnf()
        self.exchange_queues_if_necessary(answer_message)
        self.terminate_connections_and_update_information()

    def exchange_queues_if_necessary(self, answer_message):
        if isinstance(answer_message, SendAllStatesMessage):
            queue_p = answer_message.queue_p
            queue_q = answer_message.queue_q
            queue_r = answer_message.queue_r
            self.configuration.get_state().exchange_queues(queue_p, queue_q, queue_r)

    def terminate_connections_and_update_information(self):
        m_ack = MigrationAckMessage('OK')
        self.send_message_using_virtual_channel(StringConstants.SEND_NEW_VNF_ACK, m_ack)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()
        log.info('Finished disconnecting all the channels')
        self.update_information_after_migration_to_orchestrator()
        self.print_state_vnf()

    def update_information_after_migration_to_orchestrator(self):
        log.info('Sending update to orchestrator')
        message = UpdateVnfInfoAfterMigration(self.configuration)
        self.connect_and_send_message_to_orchestrator(message)

    def terminate_virtual_migration(self):
        m1 = TerminateMessage(None)
        self.send_message_using_virtual_channel(StringConstants.SEND_NEW_VNF_MIGRATION_HAS_ENDED, m1)
        self.server.disconnect_send_virtual_channel()
        self.print_state_vnf()

    def send_all_data_from_current_vnf_to_new_vnf(self, data):
        m1 = AllQueueInformation(data)
        self.send_message_using_virtual_channel(StringConstants.SEND_NEW_VNF_QUEUES, m1)
        self.get_answer_from_previous_vnf()

    def send_migration_message_to_previous_vnf(self, previous_vnf, new_vnf, migrating_vnfs=None):
        previous_vnf_in_chain = CommunicationEntityPackage(previous_vnf.host, previous_vnf.port)
        self.server.connect_to_another_server(previous_vnf_in_chain)
        migration_deactivate_message = create_migration_deactivate_message(new_vnf,
                                                                           migrating_vnfs,
                                                                           self.configuration.host(),
                                                                           self.migration_vnf_ip)
        self.send_message(StringConstants.SEND_PREVIOUS_VNF_MIGRATION_DEACTIVATE, migration_deactivate_message)
        return self.get_answer_from_previous_vnf()

    def check_if_previous_vnf_must_migrate(self, v, new_vnf, migrating_vnfs=None):
        answer_message = self.send_migration_message_to_previous_vnf(v, new_vnf, migrating_vnfs)
        if isinstance(answer_message.data, Topology):
            self.create_and_send_migration_acknowledgement_message()
            self.create_and_send_migration_deactivate_recursive_message_wait_for_answer(answer_message)

    def create_and_send_migration_acknowledgement_message(self):
        m_ack = MigrationAckMessage("Ok for delete")
        self.send_message(StringConstants.SEND_PREVIOUS_VNF_ACK, m_ack)
        self.server.disconnect_send_channel()

    def create_and_send_migration_deactivate_recursive_message_wait_for_answer(self, answer_message):
        new_previous_vnf = CommunicationEntityPackage(answer_message.data.ip, answer_message.data.port)
        log.info('Connecting to new Previous VNF: IP ' + str(answer_message.data.ip))
        self.server.connect_to_another_server(new_previous_vnf)
        m_rec_mig = MigrationDeactivateRecursiveMessage("Do it")
        self.send_message(StringConstants.SEND_NEW_VNF_DEACTIVATE_RECURSIVE, m_rec_mig)
        self.get_answer_from_previous_vnf()

    def handle_queues_from_previous_vnf_in_chain(self):
        self.handle_q_queue()
        self.handle_p_queue()

    def handle_q_queue(self):
        m1 = SendQueueQMessage(None)
        self.send_message(StringConstants.SEND_PREVIOUS_VNF_Q, m1)
        self.collect_data_to_queue(self.configuration.get_state().get_q())

    def handle_p_queue(self):
        m2 = SendQueuePMessage(None)
        self.send_message(StringConstants.SEND_PREVIOUS_VNF_P, m2)
        self.collect_data_to_queue(self.configuration.get_state().get_p())

    def send_data_from_r_queue_to_new_vnf(self):
        data = self.configuration.get_state().get_all_data_from_queue("R")
        m3 = SendQueueRMessage(data)
        self.send_message(StringConstants.SEND_NEW_VNF_R, m3)
        self.get_answer_from_new_vnf()

    def collect_data_to_queue(self, queue: list):
        answer_message = self.get_answer_from_previous_vnf()
        for d in answer_message.data:
            queue.append(d)

    def send_message(self, message_log, message):
        log.info(message_log)
        self.server.send_message(message)

    def send_message_using_virtual_channel(self, message_log, message):
        log.info(message_log)
        self.server.send_message_virtual(message)

    def migration_switch_message_exchange(self):
        m1 = SwitchMessage(None)
        self.send_message(StringConstants.SEND_PREVIOUS_VNF_SWITCH, m1)
        self.get_answer_from_previous_vnf()

    def get_answer_from_previous_vnf(self):
        log.info('Waiting for ACK from previous VNF')
        x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        self.log_answer_message_type(answer_message)
        return answer_message

    def get_answer_from_new_vnf(self):
        log.info('Waiting for ACK from new VNF')
        x = self.server.send_virtual_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        self.log_answer_message_type(answer_message)
        return answer_message

    @staticmethod
    def log_answer_message_type(answer_message):
        str_log = 'Received answer from new VNF TYPE: ' + str(type(answer_message))
        log.info(str_log)

    def add_affected_vnf(self, vnf_pack):
        self.list_affected_vnf.append(vnf_pack)
        self.configuration.add_affected_vfn(vnf_pack)

    def request_update_to_orchestrator_and_save_time(self, seed, end_time):
        log.info('Sending message to orchestrator')
        start_update_request_time = time.time()
        message = RequestUpdateFromOrchestratorMessage(seed, end_time)
        self.connect_and_send_message_to_orchestrator(message)
        self.wait_for_orchestrator_answer()
        end_update_request_time = time.time()
        total_time = end_update_request_time - start_update_request_time
        save_update_time(total_time)

    def connect_and_send_message_to_orchestrator(self, message):
        self.connect_to_orchestrator()
        self.send_message_to_orchestrator(message)

    def send_message_to_orchestrator(self, message):
        self.server.send_message_to_orchestrator(message)

    def connect_to_orchestrator(self):
        self.server.connect_to_orchestrator(self.orchestrator)

    def wait_for_orchestrator_answer(self):
        x = self.server.send_orchestrator_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        return answer_message

    def serve_clients(self):
        self.server.serve_clients()

    def update_vnf_by_operation_simple(self, operation, first_operation):
        self.apply_operation(operation)
        for affected in self.list_affected_vnf:
            if first_operation:
                self.handle_first_operation(affected, operation)
            else:
                self.handle_recursive_operation(affected, operation)

    # TODO: Stub operation
    def apply_operation(self, operation):
        print('Operation: ', operation)

    def handle_first_operation(self, affected, operation):
        new_message = InformOfVnfUpdate(affected, operation, first=False, local_search=True)
        self.connect_and_send_message_to_orchestrator(new_message)

    def handle_recursive_operation(self, affected, operation):
        if self.is_dependent_change():
            self.handle_first_operation(affected, operation)

    def is_dependent_change(self):
        if random.randint(1, 100) >= self.configuration.dependent_changes_threshold:
            return True
        return False
