import socket
import os
import time
from vnfs.annotate import annotate
from vnfs.transcoder_mp4 import transcoder_mp4
import pickle

def send_video(file_name, server):
    print("Sending video..")
    os.chdir("../communication")
    file_path = os.getcwd() + "/" + file_name
    # Load video as bytes and send it to the server
    with open(file_path, "rb") as video:
        buffer = video.read()
        server.sendall(buffer)

def process_package(data):
    start = time.time()
    video = annotate(data, 'Test', 3)
    end = time.time()
    return video, (end - start)

def read_video_package(buffer, n, client_socket, client_host, client_port):
    source_file = 'video_' + str(n)
    file_format = '.mp4'
    source_file_complete = source_file + file_format

    with open(source_file_complete, "wb") as video:
        n += 1
        i = 0
        while buffer:
            video.write(buffer)
            i += 1
            buffer = client_socket.recv(1024)

    print("Now is process time")
    source_file_processed = source_file + "_annotated" + file_format
    video, time_processing = process_package(source_file_complete)
    pickle.dump(time_processing, open(source_file_complete + "_time", "wb"))
    print(time_processing)
    transcoder_mp4(video, source_file_processed)

    # send process video back to client
    s_client = connect_to_server(client_host, client_port)
    send_video(source_file_processed, s_client)
    s_client.close()

    # Delete the video both video files
    os.remove(source_file_complete)
    os.remove(source_file_processed)
    return n

def set_up_server(host_server, port_server, max_clients):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host_server, port_server))
    s.listen(max_clients)
    return s

def connect_to_server(host_server, port_server):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_server, port_server))
    return s

def serve_clients(server_connection, n, host_client, port_client):
    while True:
        print("Listening for connections...")
        # now our endpoint knows about the OTHER endpoint.
        clientsocket, address = server_connection.accept()
        print("Connection from: " + str(address))
        try:
            print("Starting to read bytes..")
            buffer = clientsocket.recv(1024)
            n = read_video_package(buffer, n, clientsocket, host_client, port_client)
            clientsocket.close()

        except KeyboardInterrupt:
            if clientsocket:
                clientsocket.close()
            break
    clientsocket.close()

if __name__ == '__main__':
    host_server = '127.0.0.1'
    port_server = 65432
    host_client = '127.0.0.1'
    port_client = port_server + 1
    max_clients = 5
    n = 0
    s = set_up_server(host_server, port_server, max_clients)
    serve_clients(s, n, host_client, port_client)

