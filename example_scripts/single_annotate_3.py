import sys

sys.path.append('../')


from entities.communication_entity_package import CommunicationEntityPackage
from communication_entities.generic_vnf import GenericVNF
from entities.topology import Topology
from entities.service_package import ServicePackage


# TODO: Create scripts and use threads and non-blocking sockets to run the example in a single machine
if __name__ == '__main__':

    # Orchestrator
    orchestrator_host = "127.0.0.1"
    orchestrator_port = 65435
    number = 1
    orchestrator = CommunicationEntityPackage(orchestrator_host, orchestrator_port)

    # VNF
    vnf_host = "127.0.0.1"
    service = ServicePackage(50, 23, 12, 53)
    vnf_port = 0
    vnf_name = ""
    top = None

    if orchestrator_port == 65431:
        vnf_port = 65437
        vnf_name = "annotate"
        top = Topology(10, 2, 1.5, 2)
    elif orchestrator_port == 65433:
        vnf_port = 65439
        vnf_name = "speed_up"
        top = Topology(22, 22, 13.5, 42)
    elif orchestrator_port == 65435:
        if number == 1:
            vnf_port = 65441
            vnf_name = "invert_color"
            top = Topology(100, 25, 8.5, 32)
        elif number == 2:
            vnf_port = 65443
            vnf_name = "do_stuff"
            top = Topology(40, 25, 8.5, 32)

    annotate_vnf = GenericVNF(vnf_host, vnf_port, vnf_name,
                              service_package=service, topology=top, orchestrator=orchestrator,
                              initial=7)
