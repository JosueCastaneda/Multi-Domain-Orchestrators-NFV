import getopt
import sys

from communication_entities.generic_vnf import GenericVNF
from entities.communication_entity_package import CommunicationEntityPackage

help_message = "vnf_script.py -v <port> -n <vnf_name> -o <orchestrator_ip> -q <orchestrator_port>"


def valid_input(vnf_host, vnf_port, vnf_name, orchestrator_port, orchestrator_host):
    all_paremeters_given = vnf_host != "" and \
                           vnf_port != "" and \
                           orchestrator_port != "" and \
                           orchestrator_host != "" and \
                           vnf_name != ""
    # TODO: Write function to check the ports are in correct format
    all_parameters_format = True
    return all_paremeters_given and all_parameters_format


def main(argv):
    vnf_host = "127.0.0.1"
    debug = False
    vnf_port = ""
    orchestrator_host = ""
    orchestrator_port = ""
    vnf_name = ""

    if debug:
        vnf_port = "4431"
        orchestrator_host = "127.0.0.1"
        orchestrator_port = "5461"
        vnf_name = "annotation"

    else:
        try:
            opts, args = getopt.getopt(argv, "h:v:o:q:n:",
                                       ["help=", "vnf_port=", "orq_host=", "orq_port=", "vnf_name="])
        except getopt.GetoptError:
            print(help_message)
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print(help_message)
                sys.exit()
            elif opt in ("-v", "--vnf_port"):
                vnf_port = arg
            elif opt in ("-o", "--orq_host"):
                orchestrator_host = arg
            elif opt in ("-q", "--orq_port"):
                orchestrator_port = arg
            elif opt in("-n", "--vnf_name"):
                vnf_name = arg

    if valid_input(vnf_host, vnf_port, vnf_name, orchestrator_host, orchestrator_port):
        orchestrator_port = int(orchestrator_port)
        orchestrator = CommunicationEntityPackage(orchestrator_host, orchestrator_port)
        annotate_vnf = GenericVNF(vnf_host, vnf_port, vnf_name, orchestrator=orchestrator, initial=1)
        annotate_vnf.serve_clients()
    else:
        print("Invalid input")
        print(help_message)


if __name__ == "__main__":
    main(sys.argv[1:])
