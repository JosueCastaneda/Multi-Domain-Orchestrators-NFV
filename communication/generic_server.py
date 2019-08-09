import pickle
import socket
import sys

sys.path.append('../')
from entities.communication_entity_package import CommunicationEntityPackage
from communication.message_handler import MessageHandler
from entities.message_type import MessageType
from communication.messages.migration import MigrationMessage
from communication.messages.abstract import AbstractMessage
from entities.topology import Topology


class GenericServer:

    def __init__(self, orchestrator, socket_pkg: CommunicationEntityPackage):
        self.send_channel = None
        self.receive_channel = None
        self.set_up_receive_channel(socket_pkg)
        self.message_handler = MessageHandler(self)
        self.orchestrator = orchestrator

    def serve_clients(self):
        while True:
            print("Listening for connections...")
            client_socket, address = self.receive_channel.accept()
            print("Connection from: " + str(address))
            try:
                message = self.get_message(client_socket)
                message.process_message()
            except KeyboardInterrupt:
                if client_socket:
                    client_socket.close()
                break
        client_socket.close()

    def connect_to_another_server(self, server):
        self.send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_channel.connect((server.host, server.port))

    def disconnect_send_channel(self):
        self.send_channel.close()

    def set_up_receive_channel(self, socket_pkg):
        self.receive_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_channel.bind((socket_pkg.host, socket_pkg.port))
        self.receive_channel.listen(socket_pkg.max_clients)

    def acknowledge_message(self, client: socket, message: str):
        message_encoded = message.encode("UTF-8")
        client.send(message_encoded)

    # TODO: Eliminate ans, just for debugging purposes
    def get_ack(self):
        ans = self.request_channel.recv(1024).decode("UTF-8")
        return ans

    def get_message(self, client: socket):
        parameters = client.recv(4096)
        self.acknowledge_message(client, "Ok")
        return pickle.loads(parameters)

    def generate_new_message_parameters(self, vnf_topology: Topology):
        new_message = MigrationMessage(MessageType.MIGRATION_TOPOLOGY, topology_pack=vnf_topology)
        return new_message

    def send_message(self, message):
        print('Sending Message..')
        data_string = pickle.dumps(message)
        self.send_channel.send(data_string)

    def send_message_query_vnf(self, message):
        print('Sending Message..')
        data_string = pickle.dumps(message)
        self.send_channel.send(data_string)
        # Answer from the client
        answer_message = pickle.loads(self.send_channel.recv(4096))
        self.acknowledge_message(self.send_channel, str(MessageType.MSG_RECIVED))
        message_type = answer_message.operation
        new_message = self.generate_new_message_parameters(answer_message.topology)
        return message_type, new_message




