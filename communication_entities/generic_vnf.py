import json
import os.path
import pickle
import time

from communication_entities.generic_server import GenericServer
from communication_entities.messages.add_vnf_message import AddVNF
from communication_entities.messages.queue_processing.all_queue_information import AllQueueInformation
from communication_entities.messages.lcm_messages.scale_confirmation_message import ScaleConfirmationMessage
from communication_entities.messages.lcm_messages.migration.migration_ack_message import MigrationAckMessage
from communication_entities.messages.lcm_messages.migration.migration_deactivate_message import MigrationDeactivateMessage
from communication_entities.messages.lcm_messages.migration.migration_deactivate_recusive_message import MigrationDeactivateRecursiveMessage
from communication_entities.messages.raw_text_message import RawTextMessage
from communication_entities.messages.request_update_from_orchestrator_message import \
    RequestUpdateFromOrchestratorMessage
from communication_entities.messages.state_management.send_all_states_message import SendAllStatesMessage
from communication_entities.messages.queue_processing.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.queue_processing.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.queue_processing.send_queue_R_message import SendQueueRMessage
from communication_entities.messages.state_management.switch_message import SwitchMessage
from communication_entities.messages.state_management.terminate_message import TerminateMessage
from communication_entities.messages.state_management.terminate_message_without_recursion import TerminateMessageWithoutRecursion
from communication_entities.messages.vnf_information.update_vnf_info_after_migration import UpdateVnfInfoAfterMigration
from entities.communication_entity_package import CommunicationEntityPackage
from entities.topology import Topology
from utilities.logger import log
from utilities.socket_size import SocketSize


class GenericVNF:

    def __init__(self, experiment_index,  orchestrator_index, vnf_index):
        self.experiment_name = 'experiment_' + str(experiment_index) + '.json'
        self.orchestrator_index = int(orchestrator_index)
        self.vnf_index = int(vnf_index)
        vnf_information, orchestrator_information = self.load_text_data()
        self.id = vnf_information['id']
        self.server = GenericServer(self, CommunicationEntityPackage(vnf_information['server'],
                                                                     int(vnf_information['port'])))
        self.list_affected_vnf = []
        self.orchestrator = CommunicationEntityPackage(orchestrator_information['ip'],
                                                       int(orchestrator_information['port']))
        self.migration_vnf_ip = None
        self.set_up_to_orchestrator(self.orchestrator, orchestrator_information['ip'],
                                    int(orchestrator_information['port']))
        # self.print_state_vnf()

    def load_text_data(self):
        print('VNF INDEX: ' + str(self.vnf_index))
        print('EXPERIMENT INDEX: ' + str(self.experiment_name))
        print('ORCHESTRATOR INDEX: ' + str(self.orchestrator_index))
        str_new_file_name = 'experiments/experiment_generator/experiments/' + self.experiment_name
        with open(str_new_file_name) as json_file:
            raw_data = json.load(json_file)
        vnf_information = raw_data['orchestrators'][self.orchestrator_index]['vnfs'][self.vnf_index]
        orchestrator_information = raw_data['orchestrators'][self.orchestrator_index]
        print('IP: ' + str(vnf_information['server']))
        print('PORT: ' + str(vnf_information['port']))


        return vnf_information, orchestrator_information

    # TODO: Get the topology and possible service working on for migration
    def set_up_to_orchestrator(self, orchestrator, host_orchestrator, port_orchestrator):
        self.server.connect_to_orchestrator(orchestrator)
        add_message = AddVNF(self.id,
                             host_orchestrator,
                             port_orchestrator,
                             self.id,
                             None,
                             None,
                             None,
                             None,
                             None)
        self.server.send_message_to_orchestrator(add_message)

    def send_update_to_orchestrator(self, orchestrator, host, port):
        self.server.connect_to_orchestrator(orchestrator)
        add_message = AddVNF(host, port,
                             self.configuration.name(),
                             self.configuration.get_topology(),
                             self.migration_vnf_ip,
                             self.configuration.topology_migration_vnf(),
                             self.configuration.get_connection_points(),
                             self.configuration.get_dependency_list())
        self.server.send_message_to_orchestrator(add_message)

    def get_configuration(self):
        return self.configuration

    # def print_state_vnf(self):
    #     self.configuration.print_state_vnf()

    # TODO: Change the magic number by saving the port in the generic VNF
    def handle_recursive_migration(self, new_vnf_topology, migrating_vnfs=None):
        if len(self.list_affected_vnf) > 0:
            new_vnf_topology = self.configuration.topology_migration_vnf().split(',')
            new_vnf_ip = self.migration_vnf_ip
            new_vnf = Topology(delay=new_vnf_topology[0],
                               bandwidth=new_vnf_topology[1],
                               loss=new_vnf_topology[2],
                               jitter=new_vnf_topology[3],
                               ip=new_vnf_ip,
                               port=4437)
            self.begin_migration(new_vnf)
            self.handle_migration_affected(new_vnf, migrating_vnfs)
            log.info("Recursive migration is completed")
            return True, new_vnf
        log.info("Recursive migration is completed no Affected VNFs")
        return False, None

    def send_all_data_in_queues(self, all_data):
        self.send_all_data_from_current_vnf_to_new_vnf(all_data)

    # TODO: Handle multi affected cases
    def handle_migration_affected(self, new_vnf, migrating_vnfs=None):
        for v in self.list_affected_vnf:
            print('Affected VNF: ', v)
            is_cycle_found = False
            is_first_migration = False
            if migrating_vnfs is None:
                log.info('First VNF, no migrating VNFS to check')
                self.check_if_previous_vnf_must_migrate(v, new_vnf)
                log.info('No migrating VNFs')
                is_first_migration = True
            else:
                log.info('We already have migrating VNFs')
                if not self.is_affected_vnf_already_migrating(v.host, migrating_vnfs):
                    self.check_if_previous_vnf_must_migrate(v, new_vnf, migrating_vnfs)
                    log.info('No cycle in the migrating list')
                else:
                    log.info('Cycle detected!')
                    is_cycle_found = True
            if not is_cycle_found:
                self.handle_queues_from_previous_vnf_in_chain()
            self.send_data_from_r_queue_to_new_vnf()
            if not is_cycle_found:
                self.migration_switch_message_exchange()
            log.info('Finished with previous VNF now is the NEW VNF')
            all_data = self.configuration.get_state().process_all_data_in_queues(new_vnf)
            self.send_all_data_in_queues(all_data)
            if is_first_migration:
                log.info('Sending terminate without recursion')
                self.terminate_migration_without_recursion()
            else:
                log.info('Sending terminate with recursion')
                self.terminate_migration()
            if is_cycle_found:
                log.info('Cycle migration')
            else:
                log.info('Recursive migration')
            break
        log.info('handle_migration_affected has ended')

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
        print('New VNF: ', new_vnf)
        print('New Delay: ', new_vnf.delay)
        print('New bandwidth: ', new_vnf.bandwidth)
        print('New loss: ', new_vnf.loss)
        print('New jitter: ', new_vnf.jitter)
        # Start time
        start_migration_time = time.time()
        log.info('Begin migration')
        self.begin_migration(new_vnf)
        log.info('Begin handle migration of affected')
        self.handle_migration_affected(new_vnf)
        end_migration_time = time.time()
        total_migration_time = end_migration_time - start_migration_time
        log.info('Saving migration time')
        pickle.dump(total_migration_time, open('migration_time.p', 'wb'))

    def begin_migration(self, new_vnf):
        virtual_link_new_vnf_socket = CommunicationEntityPackage(new_vnf.ip, new_vnf.port, 1)
        log.info(''.join(["New IP: ", new_vnf.ip, " New Port ", str(new_vnf.port)]))
        self.server.connect_to_another_server_virtual(virtual_link_new_vnf_socket)
        raw_text_message = RawTextMessage("Ready to migrate")
        self.server.send_message_virtual(raw_text_message)
        log.info('Waiting for ACK from new VNF')
        x = self.server.send_virtual_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Received answer from new VNF TYPE: ' + str(type(answer_message))
        log.info(str_log)

    def terminate_migration(self):
        m1 = TerminateMessage(None)
        log.info('Send TerminateMessage to new VNF')
        self.server.send_message_virtual(m1)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()
        log.info('Finished disconnecting all the channels')
        self.update_information_after_migration_to_orchestrator()
        # self.print_state_vnf()

    def terminate_migration_without_recursion(self):
        log.info('Send TerminateMessageWithoutRecursion to new VNF')
        m1 = TerminateMessageWithoutRecursion(None)
        self.server.send_message_virtual(m1)
        # Wait for message is power
        log.info('Waiting for Queues answer')
        x = self.server.send_virtual_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Received answer from new VNF TYPE: ' + str(type(answer_message))
        log.info(str_log)

        if isinstance(answer_message, SendAllStatesMessage):
            queue_p = answer_message.queue_p
            queue_q = answer_message.queue_q
            queue_r = answer_message.queue_r
            self.configuration.get_state().exchange_queues(queue_p, queue_q, queue_r)
        m_ack = MigrationAckMessage('OK')
        log.info('Sending ACK message to previous')
        self.server.send_message_virtual(m_ack)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()
        log.info('Finished disconnecting all the channels')
        self.update_information_after_migration_to_orchestrator()
        # self.print_state_vnf()

    def update_information_after_migration_to_orchestrator(self):
        log.info('Sending update to orchestrator')
        self.server.connect_to_orchestrator(self.configuration.get_orchestrator())
        message = UpdateVnfInfoAfterMigration(self.configuration.host(),
                                              self.configuration.host(),
                                              self.migration_vnf_ip,
                                              self.configuration.topology_migration_vnf())
        self.server.send_message_to_orchestrator(message)

    # TODO: Is almost the same, so this can be refactored
    def terminate_virtual_migration(self):
        m1 = TerminateMessage(None)
        log.info('Sending terminate message to new VNF. Migration has ended')
        self.server.send_message_virtual(m1)
        self.server.disconnect_send_virtual_channel()
        # self.print_state_vnf()

    def send_all_data_from_current_vnf_to_new_vnf(self, data):
        m1 = AllQueueInformation(data)
        log.info('Sending all queues to new VNF')
        self.server.send_message_virtual(m1)
        log.info('Waiting for answer from new VNF')
        x = self.server.send_virtual_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Received answer from new VNF TYPE: ' + str(type(answer_message))
        log.info(str_log)

    def send_migration_message_to_previous_vnf(self, previous_vnf, new_vnf, migrating_vnfs=None):
        previous_vnf_in_chain = CommunicationEntityPackage(previous_vnf.host, previous_vnf.port)
        self.server.connect_to_another_server(previous_vnf_in_chain)
        m = MigrationDeactivateMessage(new_vnf)
        migration_vnf = dict()
        migration_vnf['ip'] = self.configuration.host()
        migration_vnf['mig_ip'] = self.migration_vnf_ip
        # TODO: Changes done to
        m.migrating_vnfs.append(migration_vnf)
        if migrating_vnfs is not None:
            for vnf_mig in migrating_vnfs:
                m.migrating_vnfs.append(vnf_mig)
        self.server.send_message(m)
        log.info('Waiting for ACK previous acknowledge message')
        return pickle.loads(self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value))

    def check_if_previous_vnf_must_migrate(self, v, new_vnf, migrating_vnfs=None):
        answer_message = self.send_migration_message_to_previous_vnf(v, new_vnf, migrating_vnfs)
        if isinstance(answer_message.data, Topology):
            m_ack = MigrationAckMessage("Ok for delete")
            log.info('Sending ACK message to previous')
            self.server.send_message(m_ack)
            self.server.disconnect_send_channel()
            # TODO: This connects to the new vnf server
            new_previous_vnf = CommunicationEntityPackage(answer_message.data.ip, answer_message.data.port)
            str_ip = str(answer_message.data.ip)
            log.info('Connecting to new Previous VNF: IP '+ str_ip)
            self.server.connect_to_another_server(new_previous_vnf)
            m_rec_mig = MigrationDeactivateRecursiveMessage("Do it")
            log.info('Send MigrationDeactivateRecursiveMessage to new VNF')
            self.server.send_message(m_rec_mig)
            log.info('Wait for ACK from new NVF')
            # TODO: THis is the correct way to use the constant types
            x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
            answer_message = pickle.loads(x)
            str_log = 'Message received of type: ' + str(type(answer_message))
            log.info(str_log)

    # TODO: Use a more fine approach to prevent deadlocks by blocking operation
    def handle_queues_from_previous_vnf_in_chain(self):
        # FIXME: For now we suppose that there is no transit traffic between coordination
        # FIXME: Since the time is not asynchronous, thus we can take what is stored in previous_VNF.
        m1 = SendQueueQMessage(None)
        log.info('Sending SendQueueQMessage to previous VNF')
        self.server.send_message(m1)
        self.collect_data_to_queue(self.configuration.get_state().get_q())

        m2 = SendQueuePMessage(None)
        log.info('Sending SendQueuePMessage to previous VNF')
        self.server.send_message(m2)
        self.collect_data_to_queue(self.configuration.get_state().get_p())

    def scale(self, vnfc_id, original_sender, service_id):
        print('Scaled: ' + str(self.id))
        acknowledge_message = ScaleConfirmationMessage(self.id, service_id)
        original_orchestrator = CommunicationEntityPackage(original_sender['ip'], int(original_sender['port']))
        self.server.connect_to_orchestrator(original_orchestrator)
        self.server.send_message_to_orchestrator(acknowledge_message)

    # TODO: Use a more fine approach to prevent deadlocks by blocking operation
    def send_data_from_r_queue_to_new_vnf(self):
        data = self.configuration.get_state().get_all_data_from_queue("R")
        log.info('Sending R to new VNF')
        m3 = SendQueueRMessage(data)
        self.server.send_message_virtual(m3)
        log.info('Waiting for reply to R message from new VNF')
        x = self.server.send_virtual_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        log.info(''.join['Message received of type: ', str(type(answer_message))])

    def collect_data_to_queue(self, queue: list):
        log.info('Waiting for answer from previous nfv')
        x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Message received of type: ' + str(type(answer_message))
        log.info(str_log)
        for d in answer_message.data:
            queue.append(d)

    def migration_switch_message_exchange(self):
        m1 = SwitchMessage(None)
        log.info('Sending Switch message to previous VNF')
        self.server.send_message(m1)
        log.info('Waiting for ACK from previous VNF')
        return pickle.loads(self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value))

    def add_affected_vnf(self, vnf_pack):
        self.list_affected_vnf.append(vnf_pack)
        # self.configuration.add_affected_vfn(vnf_pack)

    def request_update_to_orchestrator(self, seed):
        log.info('Sending message to orchestrator')
        start_update_request_time = time.time()
        message = RequestUpdateFromOrchestratorMessage(seed)
        self.server.connect_to_orchestrator(self.orchestrator)
        self.server.send_message_to_orchestrator(message)
        # Wait for the answer from the orchestrator
        x = self.server.send_orchestrator_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        end_update_request_time = time.time()
        total_time = end_update_request_time - start_update_request_time
        file = None
        if not os.path.exists('time_update.txt'):
            file = open('time_update.txt', 'w+')
            file.write(str(total_time))
            file.write('\n')
            file.close()
        else:
            file = open('time_update.txt', 'a')
            file.write(str(total_time))
            file.write('\n')
            file.close()

    def serve_clients(self):
        self.server.serve_clients()
