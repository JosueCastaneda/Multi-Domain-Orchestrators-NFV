import getopt
import sys

from communication_entities.generic_vnf import GenericVNF
from entities.communication_entity_package import CommunicationEntityPackage
from entities.service_package import ServicePackage
from entities.topology import Topology

help_message = "vnf_script.py -v <port> -n <vnf_name> -o <orchestrator_ip> -q <orchestrator_port>"


# TODO: Check this, for the moment accept given input
def valid_input(vnf_host, vnf_port, vnf_name, orchestrator_port, orchestrator_host):
    all_parameters_given = vnf_host != "" and \
                           vnf_port != "" and \
                           orchestrator_port != "" and \
                           orchestrator_host != "" and \
                           vnf_name != ""
    # TODO: Write function to check the ports are in correct format
    all_parameters_format = True
    return all_parameters_given and all_parameters_format


def parse_parameters(host, port, name):
    if type(host) != str:
        host = str(host)
    if type(port) != int:
        port = int(port)
    if type(name) != str:
        name = str(name)
    return host, port, name


def main(argv):
    vnf_host = "127.0.0.1"
    debug = False
    vnf_port = ""
    orchestrator_host = ""
    orchestrator_port = ""
    vnf_name = ""
    initial_seed = ""
    services = []
    topology = []
    migration_vnf = ""
    topology_migration_vnf = []
    list_of_services = []

    if debug:
        vnf_port = "4433"
        orchestrator_host = "127.0.0.1"
        orchestrator_port = "5463"
        vnf_name = "other"
        services = [50, 23, 12, 53]
        topology = [22, 20, 3.5, 13]
        initial_seed = 4
        migration_vnf = "500.0.0.1"
        topology_migration_vnf = [13, 32, 325, 313]

    try:
        opts, args = getopt.getopt(argv, "h:v:o:q:n:s:t:x:k:i",
                                   ["vnf_host=",
                                    "vnf_port=",
                                    "orq_host=",
                                    "orq_port=",
                                    "vnf_name=",
                                    "services=",
                                    "topology=",
                                    "migration_ip=",
                                    "migration_topology=",
                                    "initial="])
    except getopt.GetoptError:
        print(help_message)
        sys.exit(2)
    for opt, arg in opts:
        print(opt, ' ', arg)
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
        elif opt in("-s", "--services"):
            services = arg
        elif opt in("-x", "--migration_topology"):
            topology_migration_vnf = arg
        elif opt in ("-k", "--migration_ip"):
            migration_vnf = arg
        elif opt in("-t", "--topology"):
            topology = arg
        elif opt in("-i", "--initial"):
            initial_seed = arg

    # print("Initial seed: ", initial_seed)

    if isinstance(topology, str):
        topology = topology.split(",")

    if isinstance(services, str):
        services = services.split(",")
    # if isinstance(limits, str):
    #     limits = limits.split(",")
    if valid_input(vnf_host, vnf_port, vnf_name, orchestrator_host, orchestrator_port):
        if len(topology_migration_vnf) == 0 or migration_vnf == '' or len(services) == 0:
            print("Invalid input")
            print(help_message)
            exit()
        orchestrator_port = int(orchestrator_port)
        topology_vnf = Topology(topology[0], topology[1], topology[2], topology[3])
        topology_vnf.ip = vnf_host
        topology_vnf.port = vnf_port
        number_of_services = int(len(services)/4)
        running_index = 0
        for i in range(number_of_services):
            print('Service: ', str(i))
            print('Running_index: ', running_index)
            service = ServicePackage(services[running_index],
                                     services[running_index + 1],
                                     services[running_index + 2],
                                     services[running_index + 3])
            running_index += 4
            list_of_services.append(service)
        # service_vnf = ServicePackage(service[0], service[1], service[2], service[3])

        orchestrator = CommunicationEntityPackage(orchestrator_host, orchestrator_port)
        vnf_host, vnf_port, vnf_name = parse_parameters(vnf_host, vnf_port, vnf_name)
        annotate_vnf = GenericVNF(vnf_host,
                                  vnf_port,
                                  vnf_name,
                                  orchestrator=orchestrator,
                                  initial=int(initial_seed),
                                  service_package= list_of_services,
                                  topology=topology_vnf,
                                  migration_vnf=migration_vnf,
                                  topology_migration_vnf=topology_migration_vnf)
        annotate_vnf.serve_clients()
    else:
        print("Invalid input")
        print(help_message)


if __name__ == "__main__":
    main(sys.argv[1:])
