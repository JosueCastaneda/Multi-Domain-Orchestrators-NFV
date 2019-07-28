import socket
from moviepy.editor import *

def send_video(file_name, server):
    print("Sending video..")
    os.chdir("../videos")
    file_path = os.getcwd() + "/" + file_name
    # Load video as bytes and send it to the server
    with open(file_path, "rb") as video:
        buffer = video.read()
        server.sendall(buffer)

def read_video_package(buffer, n, client_socket):
    source_file = 'video_recieved_' + str(n)
    file_format = '.mp4'
    source_file_complete = source_file + file_format

    with open(source_file_complete, "wb") as video:
        while buffer:
            video.write(buffer)
            buffer = client_socket.recv(1024)

def serve_clients(server_connection):
    # while True:
    print("Listening for connections...")
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = server_connection.accept()
    print("Connection from: " + str(address))
    try:
        print("Starting to read bytes..")
        buffer = clientsocket.recv(1024)
        read_video_package(buffer, 0, clientsocket)
        clientsocket.close()

    except KeyboardInterrupt:
        if clientsocket:
            clientsocket.close()
    clientsocket.close()

def connect_to_server(host_server, port_server):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_server, port_server))
    return s

def set_up_server(host_server, port_server, max_clients):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host_server, port_server))
    s.listen(max_clients)
    return s

if __name__ == '__main__':
    host_server = '127.0.0.1'
    port_server = 65432
    host_client = '127.0.0.1'
    port_client = port_server + 1
    filename = "small.mp4"
    max_clients = 1

    s = connect_to_server(host_server, port_server)
    send_video(filename, s)
    s.close()
    s = set_up_server(host_client, port_client, max_clients)
    serve_clients(s)
