import getopt
import sys

from communication_entities.orchestrator import Orchestrator
from entities.communication_entity_package import CommunicationEntityPackage

help_message = "orchestrator_script.py -p <port> -n <orch_name>"


def valid_input(host, port, name):
    all_parameters_given = host != "" and port != "" and name != ""
    # TODO: Write function to check the ports are in correct format
    all_parameters_format = True
    return all_parameters_given and all_parameters_format


def main(argv):
    host = "127.0.0.1"
    port = ""
    name = ""

    try:
        opts, args = getopt.getopt(argv, "h:p:n:", ["host=", "port=", "name="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in("-n", "--name"):
            name = arg

    if valid_input(host, port, name):
        port = int(port)
        server = CommunicationEntityPackage(host, port)
        orchestrator = Orchestrator(server, name=name)
        orchestrator.serve_clients()
    else:
        print("Invalid input")
        print(help_message)


if __name__ == "__main__":
    main(sys.argv[1:])
