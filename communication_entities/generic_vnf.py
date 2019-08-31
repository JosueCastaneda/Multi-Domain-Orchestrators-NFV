import os
import pickle
import sys

sys.path.append('../')

from communication_entities.generic_server import GenericServer
from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.messages.add_vnf_message import AddVNF
from communication_entities.messages.raw_text_message import RawTextMessage
from communication_entities.messages.send_queue_Q_message import SendQueueQMessage
from communication_entities.messages.send_queue_P_message import SendQueuePMessage
from communication_entities.messages.send_queue_R_message import SendQueueRMessage
from communication_entities.messages.switch_message import SwitchMessage
from communication_entities.messages.remove_vnf_from_orchestrator import RemoveVnfFromOrchestrator
from communication_entities.messages.terminate_message import TerminateMessage
from communication_entities.messages.all_queue_information import AllQueueInformation
from communication_entities.messages.migration_deactivate_message import MigrationDeactivateMessage
from communication_entities.messages.request_new_pop_message import RequestNewPopMessage
from utilities.logger import *


class GenericVNF:

    def __init__(self, host, port, name, service_package, clients=5, topology=None, orchestrator=None):
        self.server_param = CommunicationEntityPackage(host, port, clients)
        self.server = GenericServer(self, self.server_param)
        self.name = name
        self.topology = topology
        log.info(''.join(["VNF: ", self.name, " is running!"]))
        self.server.connect_to_orchestrator(orchestrator)
        add_message = AddVNF(host, port, self.name, self.topology)
        self.server.send_message_to_orchestrator(add_message)
        self.affected_vnfs = []
        self.queue_Q = []
        self.queue_P = []
        self.queue_R = []
        self.service_package = service_package
        self.orchestrator = orchestrator
        self.serve_clients()

    # TODO: Use polymorphism to improve this function
    def get_all_data_from_queue(self, operation):
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

    # TODO: Check if channels are correct
    def check_migration_recursive(self, new_vnf_topology):

        if len(self.affected_vnfs) > 0:
            m = RequestNewPopMessage(new_vnf_topology)
            new_vnf = self.server.send_message_to_orchestrator(m)

            for v in self.affected_vnfs:
                self.check_if_previous_vnf_must_migrate(v, new_vnf)
                self.handle_queues_from_previous_vnf_in_chain()
                self.migration_switch_message_exchange()
                self.process_all_data_in_queues()
                self.terminate_migration()
        log.info("Migration is completed")

    def check_migration_affected(self, message):
        new_vnf = message.data.file_pack
        self.begin_migration(new_vnf)

        for v in self.affected_vnfs:
            self.check_if_previous_vnf_must_migrate(v, new_vnf)
            self.handle_queues_from_previous_vnf_in_chain()
            self.migration_switch_message_exchange()
            self.process_all_data_in_queues(v)
            self.terminate_migration()
        # log.info("Send delete to orchestrator")
        # m = RemoveVnfFromOrchestrator("Helicopter")
        # self.server.send_message_to_orchestrator(m)
        # log.info("Migration is completed")

    def process_queue(self, my_queue):
        log.info("Processing queue.....")
        return 0

    def begin_migration(self, new_vnf):
        # Establish a link, or channel between source_VNF and new_VNF
        virtual_link_new_vnf_socket = CommunicationEntityPackage(new_vnf.ip, new_vnf.port, 1)
        self.server.connect_to_another_server_virtual(virtual_link_new_vnf_socket)
        raw_text_message = RawTextMessage("Ready to migrate")
        self.server.send_message_virtual(raw_text_message)

    def terminate_migration(self):
        # Send terminate message to previous VNF
        m1 = TerminateMessage(None)
        self.server.send_message_virtual(m1)
        self.server.disconnect_send_virtual_channel()
        self.server.disconnect_send_channel()

    def process_all_data_in_queues(self, new_vnf):
        x1 = self.process_queue(self.queue_R)
        x2 = self.process_queue(self.queue_Q)
        x3 = self.process_queue(self.queue_P)
        all_data = [x1, x2, x3, new_vnf]
        self.send_all_data_from_current_vnf_to_new_vnf(all_data)

    def send_all_data_from_current_vnf_to_new_vnf(self, data):
        m1 = AllQueueInformation(data)
        self.server.send_message_virtual(m1)

    def check_if_previous_vnf_must_migrate(self, v, new_vnf):
        # Generate the object to connect to the server
        v_server = CommunicationEntityPackage(v.host, v.port)
        self.server.connect_to_another_server(v_server)

        # Generated validationMigrationMessage
        m = MigrationDeactivateMessage(new_vnf)

        # send the migration to server
        self.server.send_message(m)
        # Wait for answer
        # TODO: Change the constant to the class definition of Buffersize
        x = self.server.send_channel.recv(4096)
        answer_message = pickle.loads(x)

    def handle_queues_from_previous_vnf_in_chain(self):
        # Q are the requests in transit between previous_VNF and old_VNF
        # FIXME: For now we suppose that there is no transit traffic between coordination
        # FIXME: Since the time is not asynchronous, thus we can take what is stored in previous_VNF.
        m1 = SendQueueQMessage(None)
        self.server.send_message(m1)
        self.collect_data_to_queue()

        # P are the requests stored in the previous_VNF
        m2 = SendQueuePMessage(None)
        self.server.send_message(m2)
        self.collect_data_to_queue()

        # R is the request currently stored in the old_VNF
        data = self.get_all_data_from_queue("R")
        m3 = SendQueueRMessage(data)
        self.server.send_message_virtual(m3)

    def collect_data_to_queue(self):
        x = self.server.send_channel.recv(4096)
        answer_message = pickle.loads(x)
        print('Stub Q')

    def migration_switch_message_exchange(self):
        # Send switch message
        m1 = SwitchMessage(None)
        self.server.send_message(m1)
        # Switch done ready
        x = self.server.send_channel.recv(4096)
        answer_message = pickle.loads(x)

    def add_affected_vnf(self, vnf_pack):
        self.affected_vnfs.append(vnf_pack)

    def serve_clients(self):
        self.server.serve_clients()

    def remove_videos(self, name_original: str, name_processed: str):
        os.remove(name_original)
        os.remove(name_processed)
