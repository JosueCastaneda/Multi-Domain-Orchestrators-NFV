import os
import pickle
import socket
import sys


sys.path.append('../')

from entities.message_type import MessageType
# from entities import *
# from vnfs import *
from entities.communication_entity_package import CommunicationEntityPackage
from entities.parameter_annotation_package import ParameterAnnotationPackage
from entities.parameter_crop_package import ParameterCropPackage
from entities.parameter_file_package import ParameterFilePackage
from entities.parameter_package import ParameterPackage
from entities.parameter_resize_package import ParameterResizePackage
from vnfs.annotate import Annotate
from vnfs.speed_up import SpeedUp
from vnfs.invert_colors import InvertColors
from vnfs.crop import Crop
from vnfs.resize_video import ResizeVideo


def send_video(file_name: str, server: socket):
    os.chdir("../videos")
    file_path = os.getcwd() + "/" + file_name
    print("Sending video.. ", file_path)
    with open(file_path, "rb") as video:
        buffer = video.read()
        server.sendall(buffer)
    print("Video sent..")


# TODO: Document function with python docstrings
def send_parameters(server_socket: socket, parameters: ParameterPackage):
    print('Sending parameters..')
    data_string = pickle.dumps(parameters)
    server_socket.send(data_string)
    print("Server response: ", server_socket.recv(1024).decode("UTF-8"))


def read_video_package(buffer, client: socket, name_processed_video: str):
    source_file_complete = name_processed_video

    with open(source_file_complete, "wb") as video:
        while buffer:
            video.write(buffer)
            buffer = client.recv(1024)


def serve_clients(server_connection: socket, name_processed_video: str):
    print("Listening for connections...")
    client_socket, address = server_connection.accept()
    print("Connection from: " + str(address))
    try:
        print("Starting to read bytes..")
        buffer = client_socket.recv(1024)
        read_video_package(buffer, client_socket, name_processed_video)
        client_socket.close()

    except KeyboardInterrupt:
        if client_socket:
            client_socket.close()
    client_socket.close()


def connect_to_server(server):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server.host, server.port))
    return s


def set_up_server(client: CommunicationEntityPackage) -> socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((client.host, client.port))
    s.listen(client.max_clients)
    return s


def init_parameters():
    filename = "small"
    format_file = ".mp4"
    # TODO: Implement serving multiple clients at once
    max_clients = 1
    speed_factor = 2
    text = "Test"
    width = 200
    height = 200
    second = "grb_2"
    servers = list()
    # operations = ["annotate", "invert_colors", "speed_up"]
    operations = [MessageType.ANNOTATE, MessageType.INVERT_COLORS, MessageType.SPEED_UP]
    filename_processed = "small_processed_" + str(operations[0])
    number_servers = 4
    # TODO: This can be done with a cycle
    host_server = '127.0.0.1'
    port_server = 65432

    for i in range(number_servers):
        servers.append(CommunicationEntityPackage(host_server, port_server))
        port_server += 1

    # Packages
    file_pack = ParameterFilePackage(filename, format_file, filename_processed)
    parameter_crop = ParameterCropPackage(2, 4)
    annotation_pack = ParameterAnnotationPackage(text)
    resize_pack = ParameterResizePackage(width, height)

    parameters = ParameterPackage(file_pack, operations, speed_factor=speed_factor, second=second,
                                  vnf_servers=servers, crop=parameter_crop,
                                  annotation=annotation_pack, resize=resize_pack)

    anotate_parameters = Annotate(parameters)
    return anotate_parameters


if __name__ == '__main__':
    param = init_parameters()
    client_connection_server = connect_to_server(param.data.get_current_vnf_server())
    send_parameters(client_connection_server, param)
    send_video(param.data.file_pack.full_name_original(), client_connection_server)
    client_connection_server.close()
