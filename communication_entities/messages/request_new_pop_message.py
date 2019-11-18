from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.topology_message import TopologyMessage
from entities.parameter_package import ParameterPackage
from entities.topology import Topology
from utilities.random_integer_generation import generate_random_integer


class RequestNewPopMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    @staticmethod
    def generate_new_topology():
        new_vnf_delay = generate_random_integer(0, 20)
        new_vnf_bw = generate_random_integer(0,70)
        new_vnf_loss = generate_random_integer(0, 10)
        new_vnf_jitter = generate_random_integer(0, 10)
        top = Topology(new_vnf_delay,
                       new_vnf_bw,
                       new_vnf_loss,
                       new_vnf_jitter)
        last_ip = 200 + generate_random_integer(0,55)
        vnf_new_host = "10 .0.0." + str(last_ip)
        vnf_new_port = 4437
        top.ip = vnf_new_host
        top.port = vnf_new_port
        return top

    # TODO: Program the new pop request to the orchestrator
    # FIXME: For now it will send a hardcoded vnf
    def process_by_command_line(self):
        # vnf_new_host = "10.0.0.15"
        # vnf_new_port = 4441
        # top = Topology(1, 10, 1, 3)
        # top.ip = vnf_new_host
        # top.port = vnf_new_port
        top = self.generate_new_topology()
        param_pkg = ParameterPackage(topology=top)
        m = TopologyMessage(data=param_pkg)
        self.current_server.send_message_to_socket(self.client_socket, m)
