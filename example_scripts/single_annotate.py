import sys

sys.path.append('../')

from communication.generic_vnf import GenericVNF

# TODO: Create scripts and use threads and non-blocking sockets to run the example in a single machine
if __name__ == '__main__':
    # Unidirectional Client
    # client_host = "127.0.0.1"
    # client_port = 65431
    # client_name = "client"
    # client = GenericVNF(client_host, client_port, client_name)

    # VNF
    vnf_host = "127.0.0.1"
    vnf_port = 65434
    vnf_name = "annotate"
    annotate_vnf = GenericVNF(vnf_host, vnf_port, vnf_name)

    # Unidirectional Server
    # server_host = "127.0.0.1"
    # server_port = 65433
    # server_name = "server"
    # server = GenericVNF(server_host, server_port, server_name)