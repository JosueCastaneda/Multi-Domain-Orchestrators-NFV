import getopt
import pickle
import socket
import sys

from communication_entities.messages.add_vnf_message import AddVNF
from communication_entities.messages.add_vnf_to_chain_message import AddVNFToChainMessage
from communication_entities.messages.migration_message import MigrationMessage
from communication_entities.messages.process_data_message import ProcessDataMessage
from entities.communication_entity_package import CommunicationEntityPackage
from entities.parameter_annotation_package import ParameterAnnotationPackage
from entities.parameter_crop_package import ParameterCropPackage
from entities.parameter_file_package import ParameterFilePackage
from entities.parameter_package import ParameterPackage
from entities.vnf_package import VnfPackage
from utilities.message_type import MessageType

help_message = "message_factory.py -t <message_type> -h <host> -p <port> " \
               "-n <name> -m <new_name> -v <vnf_host> -w <vnf_port>"
debug = False


def valid_input(host, port, message_type, vnf_host, vnf_port):
    all_parameters_given = host != "" and port != "" and \
                           message_type != "" and vnf_host != "" and vnf_port != ""
    # TODO: Write function to check the ports are in correct format
    all_parameters_format = True
    if debug:
        print("Host is valid? ", host != "", " ", host)
        print("Port is valid? ", port != "", " ", port)
        print("Message type is valid? ", message_type != "", " ", message_type)
        print("VNF host is valid? ", vnf_host != "", " ", vnf_host)
        print("VNF port is valid? ", vnf_port != "", " ", vnf_port)

    return all_parameters_given and all_parameters_format


def main(argv):
    host = ""
    port = ""
    name = ""
    new_name = ""
    message_type = ""
    vnf_host = ""
    vnf_port = ""

    try:
        opts, args = getopt.getopt(argv, "t:h:p:n:m:v:w",
                                   ["type=", "host=", "port=", "name=", "new_name=", "vnf_host=", "vnf_port="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        if debug:
            print("Option: ", opt, " Argument: ", arg)
        if opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in("-n", "--name"):
            name = arg
        elif opt in("-m", "--new_name"):
            new_name = arg
        elif opt in("-t", "--type"):
            message_type = arg
        elif opt in("-v", "--vnf_host"):
            vnf_host = arg
        elif opt in("-w", "--vnf_port"):
            vnf_port = arg

    # TODO: Use enum
    if valid_input(host, port, message_type, vnf_host, vnf_port):
        port = int(port)
        m = None
        if message_type == "add_vnf":
            m = AddVNF(vnf_host, vnf_port, name)
        elif message_type == "add_chain":
            m = AddVNFToChainMessage(VnfPackage(vnf_host, vnf_port))
        elif message_type == "migration":
            m = MigrationMessage(name, new_name)
        elif message_type == "new_pop":
            print("Request new pop")
        elif message_type == "process":
            number_servers = 2
            operations = [MessageType.ANNOTATE, MessageType.SPEED_UP, MessageType.INVERT_COLORS]
            file_name = "videos/small.mp4"
            format_file = ".mp4"
            filename_processed = "small_processed_" + str(operations[0])
            file_pack = ParameterFilePackage(file_name, format_file, filename_processed)
            p = ParameterAnnotationPackage(text="Test", font_size=30, color="white")
            crop_p = ParameterCropPackage(initial_time=1, end_time=2)

            # hosts_server_num = ["10.0.0.13", "10.0.0.14"]
            hosts_server_num = ["127.0.0.1", "127.0.0.1"]
            port_server = 4435
            speed_factor = 1.5
            servers = list()

            for i in range(number_servers):
                servers.append(CommunicationEntityPackage(hosts_server_num[i], port_server))
                port_server += 2

            parameters = ParameterPackage(annotation=p,
                                          file_pack=file_pack,
                                          vnf_servers=servers,
                                          operations=operations,
                                          speed_factor=speed_factor,
                                          crop=crop_p)
            m = ProcessDataMessage(parameters)

        # Send VNF port
        send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Host: ", host, " Port: ", port)
        send_channel.connect((host, port))
        data_string = pickle.dumps(m)
        send_channel.send(data_string)
        send_channel.close()
    else:
        print("Invalid input")
        print(help_message)


if __name__ == "__main__":
    main(sys.argv[1:])
