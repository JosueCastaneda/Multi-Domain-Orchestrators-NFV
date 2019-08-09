import os
import pickle
import socket
import sys

sys.path.append('../')
from entities.communication_entity_package import CommunicationEntityPackage
from vnfs.annotate import annotate
from vnfs.crop import crop
from vnfs.invert_colors import invert_colors
from vnfs.resize_video import resize_video
from vnfs.speed_up import speed_up_raw
from vnfs.transcoder_mp4 import transcoder_mp4
from entities.parameter_package import ParameterPackage


def send_video(file_name: str, server_s: socket):
    print("Sending video..")
    os.chdir("../communication")
    file_path = os.getcwd() + "/" + file_name
    with open(file_path, "rb") as video:
        buffer = video.read()
        server_s.sendall(buffer)


def process_package(data: str, parameters):
    # Todo: Handle the selection of processing function with a pattern
    virtual_function = parameters.get_current_operation()
    full_name = os.getcwd() + "/" + data

    if virtual_function == 'annotate':
        video = annotate(full_name, parameters.annotation_parameter.text)
    elif virtual_function == 'crop':
        initial_time = parameters.crop_parameter.initial_time
        end_time = parameters.crop_parameter.end_time
        video = crop(full_name, initial_time, end_time)
    elif virtual_function == 'invert_colors':
        video = invert_colors(full_name)
    elif virtual_function == 'resize':
        width = parameters.resize_parameter.width
        height = parameters.resize_parameter.height
        video = resize_video(full_name, width, height)
    elif virtual_function == 'speed_up':
        video = speed_up_raw(full_name, parameters.speed_factor)
    return video

# TODO: The name of the package should be updated
def read_video_package(client_socket: socket, file_pack):
    source_file_complete = file_pack.name + "_server" + file_pack.format
    # I need to ack the server
    buffer = client_socket.recv(1024)

    with open(source_file_complete, "wb") as video:
        while buffer:
            video.write(buffer)
            buffer = client_socket.recv(1024)

    return source_file_complete


def remove_videos(name_original: str, name_processed: str):
    os.remove(name_original)
    os.remove(name_processed)


def set_up_server(server_s: socket):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((server_s.host, server_s.port))
    s.listen(server_s.max_clients)
    return s


def connect_to_server(server):
    print("Attempting to connect.... ", str(server.host) + " " + str(server.port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server.host, server.port))
    print('Connection with host: ', str(server.host) + " " + str(server.port))
    return s


def save_processed_video(video, name: str):
    transcoder_mp4(video, name)


def acknowledge_message(client: socket, message: str):
    message_encoded = message.encode("UTF-8")
    client.send(message_encoded)


def get_request_parameters(client: socket):
    acknowledge_message(client, "Ok")
    parameters = client.recv(4096)
    acknowledge_message(client, "Ok")
    return pickle.loads(parameters)

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


# TODO: Document function with python docstrings
def send_parameters(server_socket: socket, parameters: ParameterPackage):
    print('Sending parameters..')
    initial_message = "begin"
    server_socket.send(initial_message.encode("UTF-8"))
    print("Server response: ", server_socket.recv(1024).decode("UTF-8"))
    data_string = pickle.dumps(parameters)
    server_socket.send(data_string)
    print("Server response: ", server_socket.recv(1024).decode("UTF-8"))


def process_video(client_socket: socket, parameters):
    video_file_name = read_video_package(client_socket, parameters.file_pack)
    print("The filename is: ", video_file_name)
    video = process_package(video_file_name, parameters)
    save_processed_video(video, parameters.file_pack.process_name)
    return video_file_name


def serve_clients(server_connection: socket):
    while True:
        print("Listening for connections.")
        client_socket, address = server_connection.accept()
        print("Connection from: " + str(address))
        operation_request = client_socket.recv(1024).decode("UTF-8")
        print('Requested operation:', operation_request)
        if operation_request == "begin":
            try:
                parameters = get_request_parameters(client_socket)
                original_video_name = process_video(client_socket, parameters)
                send_video_to_client(parameters)
                # remove_videos(original_video_name, parameters.file_pack.full_name_processed())
                client_socket.close()
            except KeyboardInterrupt:
                if client_socket:
                    client_socket.close()
                break
    client_socket.close()


def init_parameters() -> CommunicationEntityPackage:
    host_server = "127.0.0.1"
    port_server = 65432
    max_clients = 5
    server_param = CommunicationEntityPackage(host_server, port_server, max_clients)
    return server_param


if __name__ == '__main__':
    server_parameters = init_parameters()
    server = CommunicationEntityPackage(server_parameters.host,
                                        server_parameters.port,
                                        server_parameters.max_clients)
    s = set_up_server(server)
    serve_clients(s)
