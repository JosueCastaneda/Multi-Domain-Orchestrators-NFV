import os
import socket
import sys

sys.path.append('../')
from entities.communication_entity_package import CommunicationEntityPackage
from vnfs.transcoder_mp4 import transcoder_mp4
from communication.generic_server import GenericServer

class GenericVNF:

    def __init__(self, host="127.0.0.1", port=65432, clients=5, name="", topology=None):
        self.server_param = CommunicationEntityPackage(host, port, clients)
        self.server = GenericServer(self, self.server_param)
        self.name = name
        self.topology = topology
        self.serve_clients()

    def serve_clients(self):
        self.server.serve_clients()

    def send_video(file_name: str, server_s: socket):
        print("Sending video..")
        os.chdir("../communication")
        file_path = os.getcwd() + "/" + file_name
        with open(file_path, "rb") as video:
            buffer = video.read()
            server_s.sendall(buffer)

    # TODO: Update function definition to include the new name
    # def send_video_to_client(parameters, new_name_file: str):
    def send_video_to_client(parameters):
        print('Sending video to client:')
        parameters.increase_time()
        parameters.increase_current_vnf()
        parameters.file_pack.name = parameters.file_pack.full_name_processed()
        s_client = connect_to_server(parameters.get_current_vnf_server())
        send_parameters(s_client, parameters)
        send_video(parameters.file_pack.full_name_processed(), s_client)
        s_client.close()

    def save_processed_video(video, name: str):
        transcoder_mp4(video, name)

    def process_video(client_socket: socket, parameters):
        video_file_name = read_video_package(client_socket, parameters.file_pack)
        print("The filename is: ", video_file_name)
        video = process_package(video_file_name, parameters)
        save_processed_video(video, parameters.file_pack.process_name)
        return video_file_name

    def remove_videos(name_original: str, name_processed: str):
        os.remove(name_original)
        os.remove(name_processed)

