import pickle
import socket

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.topology_message import TopologyMessage
from entities.parameter_package import ParameterPackage
from entities.topology import Topology
from utilities.logger import log
from utilities.message_type import MessageType
from utilities.socket_size import SocketSize


class GenericServer:

    def __init__(self, orchestrator, socket_pkg=None):
        self.send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_two_communication_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_virtual_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_orchestrator_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_pkg = socket_pkg
        if socket_pkg is not None:
            self.set_up_channel(socket_pkg, self.receive_channel)
        self.orchestrator = orchestrator
        self.current_topology = None
        socket_pkg.port = socket_pkg.port + 1
        self.set_up_channel(socket_pkg, self.receive_two_communication_channel)

    def serve_clients(self):
        while True:
            log.info("Listening for connections...")
            client_socket, address = self.receive_channel.accept()
            try:
                message = self.get_message(client_socket)
                log.info(type(message))
                message.current_server = self
                message.client_address = address
                message.client_socket = client_socket
                message.process_by_command_line()
                log.info("CONNECTIONS ENDED")
                self.orchestrator.print_state_vnf()
            except KeyboardInterrupt:
                log.exception("Keyboard interruption")
                if client_socket:
                    client_socket.close()
                break
        client_socket.close()

    # TODO: Use this function in all connect to server
    def connect_channel_to_server(self, server, channel):
        log.info(''.join(["Channel connects to Server: Host: ", server.host, " Port: ", str(server.port)]))
        channel.connect((server.host, int(server.port)))

    def connect_to_another_server(self, server):
        # self.connect_channel_to_server(server, self.send_channel)
        self.send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.info(''.join(["Send Channel Host: ", server.host, " Port: ", str(server.port)]))
        self.send_channel.connect((server.host, int(server.port)))

    def connect_to_orchestrator(self, server):
        # self.connect_channel_to_server(server, self.send_orchestrator_channel)
        self.send_orchestrator_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.info(''.join(["Orchestrator Host: ", server.host, " Port: ", str(server.port)]))
        self.send_orchestrator_channel.connect((server.host, server.port))

    def connect_to_another_server_virtual(self, server):
        # self.connect_channel_to_server(server, self.send_virtual_channel)
        self.send_virtual_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_virtual_channel.connect((server.host, server.port))

    def wait_for_reply_two_communication_channel(self):
        conn, address = self.receive_two_communication_channel.accept()
        answer_two_channel = conn.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(answer_two_channel)
        self.acknowledge_message(self.send_channel, str(MessageType.MSG_RECEIVED))
        return answer_message

    def disconnect_send_channel(self):
        self.send_channel.close()

    def disconnect_send_virtual_channel(self):
        self.send_virtual_channel.close()

    def set_up_channel(self, socket_pkg, channel):
        log.info(''.join(["Self Host: ", socket_pkg.host, " Port: ", str(socket_pkg.port)]))
        try:
            channel.bind((socket_pkg.host, socket_pkg.port))
            channel.listen(socket_pkg.max_clients)
        except OSError as err:
            log.critical("OS error: {0}".format(err))

    @staticmethod
    def acknowledge_message(client: socket, message: str):
        message_encoded = message.encode("UTF-8")
        client.send(message_encoded)

    @staticmethod
    def send_message_to_socket(client: socket, message):
        log.info("Sending Message using socket: ")
        data_string = pickle.dumps(message)
        client.send(data_string)

    def get_ack_channel(self):
        return self.send_channel.recv(SocketSize.ACK_BUFFER.value).decode("UTF-8")

    @staticmethod
    def get_message(client: socket) -> AbstractMessage:
        parameters = client.recv(SocketSize.RECEIVE_BUFFER.value)
        return pickle.loads(parameters)

    @staticmethod
    def generate_new_message_parameters(vnf_topology: Topology):
        param = ParameterPackage(vnf_topology)
        new_message = TopologyMessage(data=param)
        return new_message

    def send_message(self, message: AbstractMessage):
        log.info("Sending Message using send_channel")
        data_string = pickle.dumps(message)
        self.send_channel.send(data_string)

    def send_and_receive_message_to_orchestrator(self, message):
        log.info("Sending Message using send_channel_orchestrator")
        self.connect_to_another_server(self.orchestrator.orchestrator)
        self.send_message(message)
        x = self.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        return answer_message.data.topology

    def send_message_to_orchestrator(self, message):
        log.info("Sending Message using send_channel_orchestrator")
        data_string = pickle.dumps(message)
        self.send_orchestrator_channel.send(data_string)

    def send_message_virtual(self, message):
        log.info("Sending Message using send_virtual_channel")
        data_string = pickle.dumps(message)
        self.send_virtual_channel.send(data_string)

    def send_message_query_vnf(self, message):
        log.info("Sending Message using send_channel")
        data_string = pickle.dumps(message)
        self.send_channel.send(data_string)
        answer_message = self.wait_for_reply_two_communication_channel()
        return answer_message