import os
import pickle
import socket
import time
import sys

sys.path.append('../')
from entities.communication_entity_package import CommunicationEntityPackage


def send_video(file_name: str, server_s: socket):
    print("Sending video..")
    os.chdir("../communication")
    file_path = os.getcwd() + "/" + file_name
    with open(file_path, "rb") as video:
        buffer = video.read()
        server_s.sendall(buffer)


def read_video_package(client_socket: socket, parameters):
    source_file_complete = str(parameters.current_vnf_index) + "_" + parameters.file_pack.full_name_processed()
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


def connect_to_server(host_server, port_server):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_server, port_server))
    return s


def acknowledge_message(client: socket, message: str):
    message_encoded = message.encode("UTF-8")
    client.send(message_encoded)


# TODO: Update this function to reflect changes in the generic VNF
def get_request_parameters(client: socket):
    parameters = client.recv(4096)
    acknowledge_message(client, "Ok")
    return pickle.loads(parameters)

def serve_clients(server_connection: socket):
    print("Listening for connections...")
    client_socket, address = server_connection.accept()
    print("Connection from: " + str(address))

    try:
        parameters = get_request_parameters(client_socket)
        print("Starting to read bytes..")
        file_name = read_video_package(client_socket, parameters)
        total_time = (time.time() - parameters.latest_time) + parameters.processed_time
        print("Time taken: ", total_time)
        pickle.dump(total_time, open("time_" + file_name+".pk", "wb"))
        x = pickle.load(open("time_" + file_name+".pk", "rb"))
        print("Time taken retrieved: ", x)
        client_socket.close()
    except KeyboardInterrupt:
        if client_socket:
            client_socket.close()
    client_socket.close()

def init_parameters() -> CommunicationEntityPackage:
    host_server = "127.0.0.1"
    port_server = 65435
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
