import os
import pickle
import socket
import sys


sys.path.append('../')

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.topology_message import TopologyMessage
from utilities.message_type import MessageType
from entities.parameter_package import ParameterPackage
from entities.topology import Topology
from vnfs.annotate import Annotate
from vnfs.speed_up import SpeedUp
from vnfs.invert_colors import InvertColors
from vnfs.crop import Crop
from vnfs.resize_video import ResizeVideo
from utilities.socket_size import SocketSize
from utilities.logger import *


class GenericServer:

    def __init__(self, orchestrator, socket_pkg=None):
        self.send_channel = None
        self.receive_channel = None
        self.receive_two_communication_channel = None
        self.send_virtual_channel = None
        self.send_orchestrator_channel = None
        # FIXME: Temporary solution because a virtual link needs to be established
        self.sockt_pkg = socket_pkg
        if socket_pkg is not None:
            self.set_up_receive_channel(socket_pkg)
        self.orchestrator = orchestrator
        self.current_topology = None
        socket_pkg.port = socket_pkg.port + 1
        self.set_up_two_communication_channel(socket_pkg)

    def serve_clients(self):
        while True:
            log.info("Listening for connections...")
            client_socket, address = self.receive_channel.accept()
            log.info(''.join(["Connection from: ", str(address)]))
            try:
                message = self.get_message(client_socket)
                print(type(message))
                message.current_server = self
                message.client_addres = address
                message.client_socket = client_socket
                message.process_message()
                print("CONNECTIONS ENDED")
            except KeyboardInterrupt:
                log.exception("Keyboard interruption")
                if client_socket:
                    client_socket.close()
                break
        client_socket.close()

    def connect_to_another_server(self, server):
        self.send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_channel.connect((server.host, server.port))

    def connect_to_orchestrator(self, server):
        self.send_orchestrator_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_orchestrator_channel.connect((server.host, server.port))

    def connect_to_another_server_virtual(self, server):
        self.send_virtual_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.send_virtual_channel.connect((server.host, server.port))

    def wait_for_reply_two_communication_channel(self):
        conn, addr = self.receive_two_communication_channel.accept()
        answer_two_channel = conn.recv(SocketSize.RECEIVE_BUFFER.value)
        answer_message = pickle.loads(answer_two_channel)
        self.acknowledge_message(self.send_channel, str(MessageType.MSG_RECIVED))
        return answer_message

    def disconnect_send_channel(self):
        self.send_channel.close()

    def disconnect_send_virtual_channel(self):
        self.send_virtual_channel.close()

    def set_up_two_communication_channel(self, socket_pkg):
        self.receive_two_communication_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_two_communication_channel.bind((socket_pkg.host, socket_pkg.port))
        self.receive_two_communication_channel.listen(socket_pkg.max_clients)

    def set_up_receive_channel(self, socket_pkg):
        self.receive_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.receive_channel.bind((socket_pkg.host, socket_pkg.port))
        self.receive_channel.listen(socket_pkg.max_clients)

    def acknowledge_message(self, client: socket, message: str):
        message_encoded = message.encode("UTF-8")
        client.send(message_encoded)

    def send_message_to_socket(self, client: socket, message):
        log.info("Sending Message using socket: ")
        data_string = pickle.dumps(message)
        client.send(data_string)

    def get_ack_channel(self):
        return self.send_channel.recv(SocketSize.ACK_BUFFER.value).decode("UTF-8")

    def get_ack(self, client: socket):
        ans = client.recv(SocketSize.ACK_BUFFER.value).decode("UTF-8")
        return ans

    def get_message(self, client: socket) -> AbstractMessage:
        parameters = client.recv(SocketSize.RECEIVE_BUFFER.value)
        return pickle.loads(parameters)

    def generate_new_message_parameters(self, vnf_topology: Topology):
        param = ParameterPackage(vnf_topology)
        new_message = TopologyMessage(data=param)
        return new_message

    def send_message(self, message):
        log.info("Sending Message using send_channel")
        data_string = pickle.dumps(message)
        self.send_channel.send(data_string)

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

    def read_video_package(self, file_pack, client_socket):
        source_file_complete = ''.join([file_pack.name, "_server", file_pack.format])
        buffer = client_socket.recv(SocketSize.ACK_BUFFER.value)
        with open(source_file_complete, "wb") as video:
            while buffer:
                video.write(buffer)
                buffer = client_socket.recv(SocketSize.ACK_BUFFER.value)
        return source_file_complete

    def send_video_to_client(self, parameters):
        log.info("Sending video to client..")
        parameters.increase_time()
        parameters.increase_current_vnf()
        parameters.file_pack.name = parameters.file_pack.full_name_processed()
        self.connect_to_another_server(parameters.get_current_vnf_server())

        # FIXME: Use polymorphism
        if len(parameters.operations) > parameters.current_vnf_index:
            new_operation = parameters.operations[parameters.current_vnf_index]
            if new_operation == MessageType.ANNOTATE:
                new_parameters = Annotate(parameters)
            elif new_operation == MessageType.SPEED_UP:
                new_parameters = SpeedUp(parameters)
            elif new_operation == MessageType.INVERT_COLORS:
                new_parameters = InvertColors(parameters)
            elif new_operation == MessageType.CROP:
                new_parameters = Crop(parameters)
            elif new_operation == MessageType.RESIZE:
                new_parameters = ResizeVideo(parameters)
        else:
            new_parameters = parameters

        self.send_message(new_parameters)
        self.get_ack(self.send_channel)
        self.send_video(parameters.file_pack.full_name_processed())

    def send_video(self, file_name: str):
        log.info("Sending video..")
        file_path = ''.join([os.getcwd(), "/", file_name])
        with open(file_path, "rb") as video:
            buffer = video.read()
            self.send_channel.sendall(buffer)

    # TODO: Change constants by using polymorphism
    def save_processed_video(self, video, name: str, format=""):
        if format == ".mp4":
            self.transcoder_mp4(video, name)
        elif format == ".webm":
            self.transcoder_web(video, name)

    def transcoder_mp4(self, source_clip, name):
        source_clip.write_videofile(name + ".mp4")

    def transcoder_web(self, source_clip, name):
        source_clip.write_videofile(name + ".webm")
