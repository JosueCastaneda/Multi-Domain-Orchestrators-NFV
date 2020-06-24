import pickle
import random
import selectors
import socket
import time
import types

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.topology_message import TopologyMessage
from entities.parameters.parameter_package import ParameterPackage
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
        self.sel = selectors.DefaultSelector()

        if socket_pkg is not None:
            self.set_up_channel(socket_pkg, self.receive_channel)
        self.orchestrator = orchestrator
        self.current_topology = None
        socket_pkg.port = socket_pkg.port + 1
        self.set_up_channel(socket_pkg, self.receive_two_communication_channel)

    def serve_clients(self):
        # log.info("Listening for connections...")
        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                if key.data is None:
                    self.accept_wrapper(key.fileobj)
                else:
                    self.service_connection(key, mask)

            # client_socket, address = self.receive_channel.accept()
            # try:
            #     message = self.get_message(client_socket)
            #     message.current_server = self
            #     message.client_address = address
            #     message.client_socket = client_socket
            #     message.process_by_command_line()
            # except KeyboardInterrupt:
            #     log.exception("Keyboard interruption")
            #     if client_socket:
            #         client_socket.close()
            #     break
        # client_socket.close()

    # TODO: Use this function in all connect to server
    def connect_channel_to_server(self, server, channel):
        # log.info(''.join(["Channel connects to Server: Host: ", server.host, " Port: ", str(server.port)]))
        channel.connect((server.host, int(server.port)))

    def connect_to_another_server(self, server):
        # self.connect_channel_to_server(server, self.send_channel)
        self.send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.info(''.join(["Send Channel Host: ", server.host, " Port: ", str(server.port)]))
        val = self.send_channel.connect_ex((server.host, int(server.port)))
        counter = 0
        # TODO: IMPMENTE THIS COD
        # while val != 0 and counter < 15:
        #     wait_time = random.uniform(0, 1)
        #     time.sleep(wait_time)
        #     print(wait_time)
        #     counter +=1
        #     if counter >= 10:
        #         print('Wait me')
        #     log.info(''.join(["Send Channel Host: ", server.host, " Port: ", str(server.port)]))
        #     val = self.send_channel.connect_ex((server.host, int(server.port)))

        # if (val != 0):
        #     print('Something bad happened')
        #     log.info('Something go WRONG!!!')

    def connect_to_another_server_raw(self, host, port):
        self.send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # log.info(''.join(["Send Channel Host: ", host, " Port: ", port]))
        self.send_channel.connect((host, int(port)))

    def connect_to_orchestrator(self, server):
        self.send_orchestrator_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.info(''.join(["Orchestrator Host: ", server.host, " Port: ", str(server.port)]))
        val = self.send_orchestrator_channel.connect_ex((server.host, server.port))
        if (val != 0):
            print('Something bad happened')

    def connect_to_another_server_virtual(self, server):
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
        # log.info(''.join(["Self Host: ", socket_pkg.host, " Port: ", str(socket_pkg.port)]))
        try:
            channel.bind((socket_pkg.host, socket_pkg.port))
            channel.listen(socket_pkg.max_clients)
            # log.info('listening on ' + str(socket_pkg.host) + ' ' + str(socket_pkg.port))
            channel.setblocking(False)
            self.sel.register(channel, selectors.EVENT_READ, data=None)

        except OSError as err:
            log.critical("OS error: {0}".format(err))

    @staticmethod
    def acknowledge_message(client: socket, message: str):
        message_encoded = message.encode("UTF-8")
        client.sendall(message_encoded)

    @staticmethod
    def send_message_to_socket(client: socket, message):
        # log.info("Sending Message using socket: ")
        data_string = pickle.dumps(message)
        # log.info('Socket: ' + str(client))
        client.sendall(data_string)

    def get_ack_channel(self):
        return self.send_channel.recv(SocketSize.ACK_BUFFER.value).decode("UTF-8")

    @staticmethod
    def get_message(client: socket) -> AbstractMessage:
        str_log = str(client)
        # log.info(str_log)
        parameters = client.recv(SocketSize.RECEIVE_BUFFER.value)
        return pickle.loads(parameters)

    @staticmethod
    def generate_new_message_parameters(vnf_topology: Topology):
        print('Topology: Delay ', str(vnf_topology.delay), ' bandwidth: ', str(vnf_topology.bandwidth))
        print('Topology: Loss ', str(vnf_topology.loss), ' jitter: ', str(vnf_topology.jitter))
        param = ParameterPackage(vnf_topology)
        new_message = TopologyMessage(data=param)
        return new_message

    def send_message(self, message):
        str_log = 'Sending Message using send_channel of type:' + str(type(message))
        # log.info(str_log)

        data_string = pickle.dumps(message)
        self.send_channel.sendall(data_string)

    def send_and_receive_message_to_orchestrator(self, message):
        # log.info("Sending Message using send_channel_orchestrator")
        self.connect_to_another_server(self.orchestrator.orchestrator)
        self.send_message(message)
        x = self.send_channel.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(x)
        return answer_message.data.topology

    def send_message_to_orchestrator(self, message):
        log.info("Sending Message using send_channel_orchestrator")
        data_string = pickle.dumps(message)
        self.send_orchestrator_channel.sendall(data_string)

    def send_message_virtual(self, message):
        str_log = 'Sending Message using send_virtual_channel of type: ' + str(type(message))
        # log.info(str_log)
        data_string = pickle.dumps(message)
        self.send_virtual_channel.sendall(data_string)

    def send_message_query_vnf(self, message):
        str_log = 'Sending Message using send_channel of type: ' + str(type(message))
        # log.info(str_log)
        data_string = pickle.dumps(message)
        self.send_channel.send(data_string)
        answer_message = self.wait_for_reply_two_communication_channel()
        return answer_message

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        str_log = "accepted connection from" + str(addr)
        log.info(str_log)
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            client_socket = sock
            address = data.addr
            try:
                message = self.get_message(client_socket)
                message.current_server = self
                message.client_address = address
                message.client_socket = client_socket
                message.process_by_command_line()
                str_log_connection = "closing connection to" + str(data.addr)
                # log.info(str_log_connection)
                self.sel.unregister(sock)
                sock.close()

            except KeyboardInterrupt:
                log.exception("Keyboard interruption")
                if client_socket:
                    client_socket.close()
            client_socket.close()

            # recv_data = sock.recv(1024)  # Should be ready to read
            # if recv_data:
            #     data.outb += recv_data
            # else:
            #     print("closing connection to", data.addr)
            #     self.sel.unregister(sock)
            #     sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print("echoing", repr(data.outb), "to", data.addr)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]
