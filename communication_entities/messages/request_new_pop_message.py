from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.topology_message import TopologyMessage
from entities.parameter_package import ParameterPackage
from entities.topology import Topology


class RequestNewPopMessage(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)
        self.current_server = None

    # TODO: Program the new pop request to the orchestrator
    # FIXME: For now it will send a hardcoded vnf
    def process_by_command_line(self):
        # vnf_new_host = "127.0.0.1"
        # vnf_new_port = 4441
        vnf_new_host = "10.0.0.15"
        vnf_new_port = 4441

        top = Topology(1, 10, 1, 3)
        top.ip = vnf_new_host
        top.port = vnf_new_port
        param_pkg = ParameterPackage(topology=top)
        m = TopologyMessage(data=param_pkg)
        self.current_server.send_message_to_socket(self.client_socket, m)
