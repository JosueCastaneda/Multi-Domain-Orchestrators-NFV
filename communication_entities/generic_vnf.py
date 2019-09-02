import os
import pickle
import sys

sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.add_vnf_message import AddVNF
from entities.topology import Topology
from communication_entities.messages.raw_text_message import RawTextMessage
from communication_entities.messages.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.send_queue_R_message import SendQueueRMessage
from communication_entities.messages.switch_message import SwitchMessage
from communication_entities.messages.migration_ack_message import MigrationAckMessage
from communication_entities.messages.terminate_message import TerminateMessage
from communication_entities.messages.all_queue_information import AllQueueInformation
from communication_entities.messages.migration_deactivate_message import MigrationDeactivateMessage
from communication_entities.messages.migration_deactivate_recusive_message import MigrationDeactivateRecursiveMessage
from communication_entities.messages.request_new_pop_message import RequestNewPopMessage
from utilities.logger import log
from utilities.socket_size import SocketSize


class GenericVNF:

    def __init__(self, host, port, name, service_package,
                 clients=5, topology=None, orchestrator=None, initial=0):
        self.server_param = CommunicationEntityPackage(host, port, clients)
        self.server = GenericServer(self, self.server_param)
        self.name = name
        self.topology = topology
        log.info(''.join(["VNF: ", self.name, " is running!"]))
        self.server.connect_to_orchestrator(orchestrator)
        add_message = AddVNF(host, port, self.name, self.topology)
        self.server.send_message_to_orchestrator(add_message)
        self.affected_vnfs = []
        self.queue_Q = [initial]
        self.queue_P = [initial + 1]
        self.queue_R = [initial + 2]
        self.service_package = service_package
        self.orchestrator = orchestrator
        self.serve_clients()

    def print_state_vnf(self):
        """
        This function is for debugging purposes, to check the result of
        migration.

        :return:
        """
        print("VNF name: ", self.name)
        print("Orchestrator: ", self.orchestrator.host, " ", self.orchestrator.port)
        print("Affected VNFS: ", self.affected_vnfs[0].host, " ", self.affected_vnfs[0].port)
        print("Queue Q: ")
        for d in self.queue_Q:
            print(d, " ")

    # TODO: Use polymorphism to improve this function. Or better, use the queue to do the operation
    # def get_all_data_from_queue(self, queue):
    def get_all_data_from_queue(self, operation):
        """
        :param operation: The type of queue
        :return: A list of data in the queue
        """
        data = []
        # while queue:
        #     data.append(queue.pop(0))
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

    def check_migration_recursive(self, new_vnf_topology):
        if len(self.affected_vnfs) > 0:
            m = RequestNewPopMessage(new_vnf_topology)
            new_vnf = self.server.send_and_receive_message_to_orchestrator(m)
            self.begin_migration(new_vnf)
            self.handle_migration_affected(new_vnf)
            log.info("Recursive migration is completed")
            return True, new_vnf
        log.info("Recursive migration is completed")
        return False, None

    def send_all_data_in_queues(self, all_data):
        self.send_all_data_from_current_vnf_to_new_vnf(all_data)

    def handle_migration_affected(self, new_vnf):
        for v in self.affected_vnfs:
            self.check_if_previous_vnf_must_migrate(v, new_vnf)
            self.handle_queues_from_previous_vnf_in_chain()
            self.migration_switch_message_exchange()
            all_data = self.process_all_data_in_queues(new_vnf)
            self.send_all_data_in_queues(all_data)
            self.terminate_migration()

    def check_migration_affected(self, message):
        new_vnf = message.data.file_pack
        self.begin_migration(new_vnf)
        self.handle_migration_affected(new_vnf)

    # TODO: Implement this to fit the VNF usage...
    def process_queue(self, my_queue):
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
        self.server.connect_to_another_server_virtual(virtual_link_new_vnf_socket)
        raw_text_message = RawTextMessage("Ready to migrate")
        self.server.send_message_virtual(raw_text_message)

    def terminate_migration(self):
        """
            Send terminate message to previous VNF
            This ends the migration scenario by sending
            a terminate message from the source_VNF to the previous_VNF
        :return:
        """
        m1 = TerminateMessage(None)
        self.server.send_message_virtual(m1)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()
        self.print_state_vnf()

    def process_all_data_in_queues(self, new_vnf):
        """
        Process all the data using the function required for each
        packet in the queues. The messages should contain the required
        process.

        :param new_vnf: The new VNF represented as a Topology entity
        :return: all_data: List of parameters that includes two Queues and a Topology
        """
        x2 = self.process_queue(self.queue_Q)
        x3 = self.process_queue(self.queue_P)
        all_data = [x2, x3, new_vnf]
        return all_data

    def send_all_data_from_current_vnf_to_new_vnf(self, data):
        m1 = AllQueueInformation(data)
        self.server.send_message_virtual(m1)

    def send_migration_message_to_previous_vnf(self, previous_vnf, new_vnf):
        v_server = CommunicationEntityPackage(previous_vnf.host, previous_vnf.port)
        self.server.connect_to_another_server(v_server)
        m = MigrationDeactivateMessage(new_vnf)
        self.server.send_message(m)
        return pickle.loads(self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value))

    def check_if_previous_vnf_must_migrate(self, v, new_vnf):
        """
        Verifies if the previous_VNF must also migrate due to the migration of source_VNF

        :param v: The previous_VNF
        :param new_vnf: The new_VNF
        :return:
        """
        answer_message = self.send_migration_message_to_previous_vnf(v, new_vnf)
        if isinstance(answer_message.data, Topology):
            m_ack = MigrationAckMessage("Ok for delete")
            self.server.send_message(m_ack)
            self.server.disconnect_send_channel()
            v_server = CommunicationEntityPackage(answer_message.data.ip, answer_message.data.port)
            self.server.connect_to_another_server(v_server)
            m_rec_mig = MigrationDeactivateRecursiveMessage("Do it")
            self.server.send_message(m_rec_mig)

    def handle_queues_from_previous_vnf_in_chain(self):
        """
        Send request to coordinate the state exchange in the queues of the VNF ensuring
        the order of messages sent. First ones sent, first ones processed.

        First sends a Q_message to the previous_VNF catching all the messages
        being sent from previous_VNF and source_VNF.

        Then, sends a P_message to the previous_VNF catching all the stored messages
        in previous_VNF that have not been processed.

        Finally, sends a R_message catching all the current messages stored in
        source_VNF and sends it to the new_VNF so they will be the first ones to be processed.

        :return:
        """
        # FIXME: For now we suppose that there is no transit traffic between coordination
        # FIXME: Since the time is not asynchronous, thus we can take what is stored in previous_VNF.
        m1 = SendQueueQMessage(None)
        self.server.send_message(m1)
        self.collect_data_to_queue(self.queue_Q)

        m2 = SendQueuePMessage(None)
        self.server.send_message(m2)
        self.collect_data_to_queue(self.queue_P)

        data = self.get_all_data_from_queue("R")
        m3 = SendQueueRMessage(data)
        self.server.send_message_virtual(m3)

    def collect_data_to_queue(self, queue: list):
        """
        Saves all the data sent by a message from previous_VNF

        :param queue: Current queue to append data to
        :return:
        """
        x = self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        for d in answer_message.data:
            queue.append(d)

    def migration_switch_message_exchange(self):
        """
        Exchanges messages to be sure the switch phase is done correctly.
        First, sends a switch message and then waits for a confirmation message
        :return:
        """
        m1 = SwitchMessage(None)
        self.server.send_message(m1)
        return pickle.loads(self.server.send_channel.recv(SocketSize.RECEIVE_BUFFER.value))

    def add_affected_vnf(self, vnf_pack):
        self.affected_vnfs.append(vnf_pack)

    def serve_clients(self):
        self.server.serve_clients()

    def remove_videos(self, name_original: str, name_processed: str):
        os.remove(name_original)
        os.remove(name_processed)
