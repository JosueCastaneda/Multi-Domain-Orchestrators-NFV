import os
import pickle
import socket

import sys


sys.path.append('../')
print(sys.path)

from communication.messages.abstract import AbstractMessage
from communication.messages.migration import MigrationMessage
from entities.communication_entity_package import CommunicationEntityPackage
from entities.message_type import MessageType
from entities.topology import Topology
from vnfs.annotate import Annotate
from vnfs.speed_up import SpeedUp
from vnfs.invert_colors import InvertColors
from vnfs.crop import Crop
from vnfs.resize_video import ResizeVideo


class GenericServer:

    def __init__(self, orchestrator, socket_pkg: CommunicationEntityPackage):
        self.send_channel = None
        self.receive_channel = None
        self.set_up_receive_channel(socket_pkg)
        self.orchestrator = orchestrator

    def serve_clients(self):
        while True:
            print("Listening for connections...")
            client_socket, address = self.receive_channel.accept()
            print("Connection from: " + str(address))
            try:
                message = self.get_message(client_socket)
                message.current_server = self
                message.client_socket = client_socket
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

    def get_ack(self, client: socket):
        ans = client.recv(1024).decode("UTF-8")
        return ans

    def get_message(self, client: socket) -> AbstractMessage:
        # TODO: This gets errors
        parameters = client.recv(4096)
        # self.acknowledge_message(client, str(MessageType.MSG_RECIVED))
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
        answer_message = pickle.loads(self.send_channel.recv(4096))
        self.acknowledge_message(self.send_channel, str(MessageType.MSG_RECIVED))
        return answer_message

    def read_video_package(self, file_pack, client_socket):
        source_file_complete = file_pack.name + "_server" + file_pack.format
        buffer = client_socket.recv(1024)
        with open(source_file_complete, "wb") as video:
            while buffer:
                video.write(buffer)
                buffer = client_socket.recv(1024)
        return source_file_complete

    # TODO: Update function definition to include the new name
    def send_video_to_client(self, parameters):
        print('Sending video to client:')
        parameters.increase_time()
        parameters.increase_current_vnf()
        parameters.file_pack.name = parameters.file_pack.full_name_processed()
        self.connect_to_another_server(parameters.get_current_vnf_server())

        # TODO: Use polimorphism
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
        print("Sending video..")
        # os.chdir("../communication")
        file_path = os.getcwd() + "/" + file_name
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
