import getopt
import sys

from communication_entities.generic_vnf import GenericVNF
from entities.topology import Topology
from entities.service_package import ServicePackage
from entities.communication_entity_package import CommunicationEntityPackage

help_message = "vnf_script.py -v <port> -n <vnf_name> -o <orchestrator_ip> -q <orchestrator_port>"


def valid_input(vnf_host, vnf_port, vnf_name, orchestrator_port, orchestrator_host):
    all_parameters_given = vnf_host != "" and \
                           vnf_port != "" and \
                           orchestrator_port != "" and \
                           orchestrator_host != "" and \
                           vnf_name != ""
    # TODO: Write function to check the ports are in correct format
    all_parameters_format = True
    return all_parameters_given and all_parameters_format


def main(argv):
    vnf_host = "127.0.0.1"
    debug = True
    vnf_port = ""
    orchestrator_host = ""
    orchestrator_port = ""
    vnf_name = ""
    initial_seed = ""
    service = []
    topology = []

    if debug:
        vnf_port = "4433"
        orchestrator_host = "127.0.0.1"
        orchestrator_port = "5465"
        vnf_name = "other"
        service = [50, 23, 12, 53]
        topology = [22, 20, 3.5, 13]
        initial_seed = 4

    try:
        opts, args = getopt.getopt(argv, "h:v:o:q:n:s:t:i",
                                   ["vnf_host=",
                                    "vnf_port=",
                                    "orq_host=",
                                    "orq_port=",
                                    "vnf_name=",
                                    "service=",
                                    "topology=",
                                    "initial="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--vnf_host"):
            vnf_host = arg
        elif opt in ("-v", "--vnf_port"):
            vnf_port = arg
        elif opt in ("-o", "--orq_host"):
            orchestrator_host = arg
        elif opt in ("-q", "--orq_port"):
            orchestrator_port = arg
        elif opt in("-n", "--vnf_name"):
            vnf_name = arg
        elif opt in("-s", "--service"):
            service = arg
        elif opt in("-t", "--topology"):
            topology = arg
        elif opt in("-i", "--initial"):
            initial_seed = arg

    # print("Initial seed: ", initial_seed)

    if isinstance(topology, str):
        topology = topology.split(",")

    if isinstance(service, str):
        service = service.split(",")
    if valid_input(vnf_host, vnf_port, vnf_name, orchestrator_host, orchestrator_port):
        orchestrator_port = int(orchestrator_port)
        topology_vnf = Topology(topology[0], topology[1], topology[2], topology[3])
        topology_vnf.ip = vnf_host
        topology_vnf.port = vnf_port
        service_vnf = ServicePackage(service[0], service[1], service[2], service[3])
        orchestrator = CommunicationEntityPackage(orchestrator_host, orchestrator_port)
        annotate_vnf = GenericVNF(vnf_host,
                                  vnf_port,
                                  vnf_name,
                                  orchestrator=orchestrator,
                                  initial=int(initial_seed),
                                  service_package= service_vnf,
                                  topology=topology_vnf)
        annotate_vnf.serve_clients()
    else:
        print("Invalid input")
        print(help_message)


if __name__ == "__main__":
    main(sys.argv[1:])
