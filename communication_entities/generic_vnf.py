import pickle

from communication_entities.generic_server import GenericServer
from communication_entities.messages.add_vnf_message import AddVNF
from communication_entities.messages.all_queue_information import AllQueueInformation
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from communication_entities.messages.migration_deactivate_message import MigrationDeactivateMessage
from communication_entities.messages.migration_deactivate_recusive_message import MigrationDeactivateRecursiveMessage
from communication_entities.messages.raw_text_message import RawTextMessage
from communication_entities.messages.request_new_pop_message import RequestNewPopMessage
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


class GenericVNF:

    def __init__(self, host, port, name, service_package=None,
                 clients=5, topology=None, orchestrator=None, initial=0, migration_vnf=None, topology_migration_vnf=None):

        self.server_param = CommunicationEntityPackage(host, port, clients)
        self.server = GenericServer(self, self.server_param)
        self.name = name
        self.topology = topology
        self.list_affected_vnf = []
        self.queue_P = [initial]
        self.queue_Q = [initial + 1]
        self.queue_R = [initial + 2]
        self.service_package = service_package
        self.orchestrator = orchestrator
        self.migration_vnf_ip = migration_vnf
        self.topology_migration_vnf = topology_migration_vnf
        self.set_up_to_orchestrator(orchestrator, host, port)
        log.info(''.join(["VNF: ", self.name, " is running!"]))
        log.info(''.join(["Delay: ", str(self.topology.delay)]))
        log.info(''.join(["Bandwidth: ", str(self.topology.bandwidth)]))
        log.info(''.join(["Loss: ", str(self.topology.loss)]))
        log.info(''.join(["Jitter: ", str(self.topology.jitter)]))
        self.print_state_vnf()

    # TODO: Get the topology and possible service working on for migration
    def set_up_to_orchestrator(self, orchestrator, host, port):
        self.server.connect_to_orchestrator(orchestrator)
        add_message = AddVNF(host, port, self.name, self.topology, self.migration_vnf_ip, self.topology_migration_vnf)
        self.server.send_message_to_orchestrator(add_message)

    def print_state_vnf(self):
        log.info(''.join(["VNF name: ", self.name]))
        log.info(''.join(["Orchestrator: ", self.orchestrator.host, " ", str(self.orchestrator.port)]))
        for vnf in self.list_affected_vnf:
            print(vnf)
        #     log.info(''.join(["Affected VNF Host: ", vnf.host, " Port: ", vnf.port]))

        log.info("Queue Q: ")
        for d in self.queue_Q:
            log.info(''.join([str(d), " "]))

    # TODO: Use polymorphism to improve this function. Or better, use the queue to do the operation
    # def get_all_data_from_queue(self, queue):
    def get_all_data_from_queue(self, operation):
        str_log = 'Collecting data from queue:' + str(operation)
        log.info(str_log)
        data = []
        if operation == "P":
            while self.queue_P:
                data.append(self.queue_P.pop(0))
        elif operation == "Q":
            while self.queue_Q:
                data.append(self.queue_Q.pop(0))
        elif operation == "R":
            while self.queue_R:
                data.append(self.queue_R.pop(0))
        return data

    # TODO: Use polymorphism to improve this function. Better, use the queue in parameters
    def add_states_to_queue(self, state, operation):
        if operation == "P":
            self.queue_P.append(state)
        elif operation == "Q":
            self.queue_Q.append(state)
        elif operation == "R":
            self.queue_R.append(state)

    def extend_queue(self, queue, extension):
        if queue == "P":
            self.queue_P.extend(extension)
        elif queue == "Q":
            self.queue_Q.extend(extension)
        elif queue == "R":
            self.queue_R.extend(extension)

    # TODO: Change the magic number by saving the port in the generic VNF
    def handle_recursive_migration(self, new_vnf_topology, migrating_vnfs=None):
        if len(self.list_affected_vnf) > 0:
            # m = RequestNewPopMessage(new_vnf_topology)
            # new_vnf = self.server.send_and_receive_message_to_orchestrator(m)
            new_vnf_topology = self.topology_migration_vnf.split(',')
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

    # TODO: Work on this function, a lot of repeated code
    def handle_migration_affected(self, new_vnf, migrating_vnfs=None):
        for v in self.list_affected_vnf:
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
            all_data = self.process_all_data_in_queues(new_vnf)
            self.send_all_data_in_queues(all_data)
            if is_first_migration:
                self.terminate_migration_without_recursion()
            else:
                self.terminate_migration()
            if is_cycle_found:
                log.info('Cycle migration')
            else:
                log.info('Recursive migration')
        log.info('handle_migration_affected has ended')

    def is_affected_vnf_already_migrating(self, vnf, migrating_vnfs):
        # print('Affected VNF: ', vnf, ' type: ', type(vnf))
        for mig_vnf in migrating_vnfs:
            # print('Mig: ', mig_vnf['ip'], ' type: ', type(mig_vnf))
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
        self.begin_migration(new_vnf)
        self.handle_migration_affected(new_vnf)

    # TODO: Implement this to fit the VNF usage...
    @staticmethod
    def process_queue(my_queue):
        log.info("Processing queue.....")

        return my_queue

    def begin_migration(self, new_vnf):
        """
        Establish a link, or channel between source_VNF and new_VNF and send a
        migration message to the new_VNF to get it ready to receive data

        :param new_vnf: New VNF in a Topology message containing the connection information
        :return:
        """
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
        self.print_state_vnf()

    def terminate_migration_without_recursion(self):
        log.info('Send TerminateMessageWithoutRecursion to new VNF')
        m1 = TerminateMessageWithoutRecursion(None)
        self.server.send_message_virtual(m1)
        # Wait for message is power
        log.info('Waiting for Queues answer')
        x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Received answer from new VNF TYPE: ' + str(type(answer_message))
        log.info(str_log)
        if isinstance(answer_message, SendAllStatesMessage):
            queue_p = answer_message.queue_p
            queue_q = answer_message.queue_q
            queue_r = answer_message.queue_r
            self.exchange_queues(queue_p, queue_q, queue_r)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()
        log.info('Finished disconnecting all the channels')
        self.update_information_after_migration_to_orchestrator()
        self.print_state_vnf()

    def update_information_after_migration_to_orchestrator(self):
        log.info('Sending update to orchestrator')
        self.server.connect_to_orchestrator(self.orchestrator)
        message = UpdateVnfInfoAfterMigration(self.server_param.host,
                                              self.server_param.host,
                                              self.migration_vnf_ip,
                                              self.topology_migration_vnf)
        self.server.send_message_to_orchestrator(message)

    # TODO: Is almost the same, so this can be refactored
    def terminate_virtual_migration(self):
        m1 = TerminateMessage(None)
        log.info('Sending terminate message to new VNF. Migration has ended')
        self.server.send_message_virtual(m1)
        self.server.disconnect_send_virtual_channel()
        self.print_state_vnf()

    def process_all_data_in_queues(self, new_vnf):
        x2 = self.process_queue(self.queue_Q)
        x3 = self.process_queue(self.queue_P)
        all_data = [x2, x3, new_vnf]
        return all_data

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
        migration_vnf['ip'] = self.server_param.host
        migration_vnf['mig_ip'] = self.migration_vnf_ip
        # TODO: Changes done to
        m.migrating_vnfs.append(migration_vnf)
        if migrating_vnfs is not None:
            for vnf_mig in migrating_vnfs:
                m.migrating_vnfs.append(vnf_mig)
        self.server.send_message(m)
        log.info('Waiting for ACK previous acknowledge message')
        return pickle.loads(self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value))

    def exchange_queues(self, new_queue_p, new_queue_q, new_queue_r):
        self.queue_P = new_queue_p
        self.queue_Q = new_queue_q
        self.queue_R = new_queue_r

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
        self.collect_data_to_queue(self.queue_Q)

        m2 = SendQueuePMessage(None)
        log.info('Sending SendQueuePMessage to previous VNF')
        self.server.send_message(m2)
        self.collect_data_to_queue(self.queue_P)

    # TODO: Use a more fine approach to prevent deadlocks by blocking operation
    def send_data_from_r_queue_to_new_vnf(self):
        data = self.get_all_data_from_queue("R")
        log.info('Sending R to new VNF')
        m3 = SendQueueRMessage(data)
        self.server.send_message_virtual(m3)
        log.info('Waiting for reply to R message from new VNF')
        x = self.server.send_virtual_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Message received of type: ' + str(type(answer_message))
        log.info(str_log)
    #     WAIT FOR ANSWER

    def collect_data_to_queue(self, queue: list):
        """
        Saves all the data sent by a message from previous_VNF

        :param queue: Current queue to append data to
        :return:
        """
        log.info('Waiting for answer from previous nfv')
        x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        str_log = 'Message received of type: ' + str(type(answer_message))
        log.info(str_log)
        for d in answer_message.data:
            queue.append(d)

    def migration_switch_message_exchange(self):
        """
        Exchanges messages to be sure the switch phase is done correctly.
        First, sends a switch message and then waits for a confirmation message
        :return:
        """
        m1 = SwitchMessage(None)
        log.info('Sending Switch message to previous VNF')
        self.server.send_message(m1)
        log.info('Waiting for ACK from previous VNF')
        return pickle.loads(self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value))

    def add_affected_vnf(self, vnf_pack):
        self.list_affected_vnf.append(vnf_pack)

    def serve_clients(self):
        self.server.serve_clients()

    def get_all_queue_data(self):
        data = list()
        data.append(self.queue_P)
        data.append(self.queue_Q)
        data.append(self.queue_R)
        return data
