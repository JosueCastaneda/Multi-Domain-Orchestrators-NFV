from communication.generic_server import GenericServer
from communication.messages.vnf_found import VNFFound


class Orchestrator:

    def __init__(self, server, topology=None):
        self.vnfs = []
        self.orchestrators = []
        self.topology = topology
        self.server = GenericServer(self, server)
        self.serve_clients()

    def serve_clients(self):
        self.server.serve_clients()

    # TODO: This linear search could be done more efficiently
    def get_local_vnf(self, vnf_name):
        for vnf in self.vnfs:
            if vnf.name == vnf_name:
                return vnf
        return None

    # TODO: Implement this function
    def handle_add_orchestrator(self, parameters):
        self.add_orchestrator(parameters.orchestrator)

    # TODO:Implement this function
    def handle_add_vnf(self, parameters):
        self.vnfs.append(parameters.vnf)

    def add_orchestrator(self, orchestrator):
        self.orchestrators.append(orchestrator)

    # TODO: Implement this correctly, handle the answer from the client
    def send_message_to_vnf(self, vnf, message):
        self.server.connect_to_another_server(vnf)
        self.server.send_message(message)
        print("Server response: ", self.server.get_ack())
        self.server.disconnect_send_channel()

    # TODO: Implement the new vnf and its parameters for the link using threads
    def send_message_to_orchestrators(self, message):
        message.source_server = self.server
        for o in self.orchestrators:
            self.server.connect_to_another_server(o.server)
            answer_message = self.server.send_message_query_vnf(message)
            self.server.disconnect_send_channel()
            if isinstance(answer_message, VNFFound):
                return answer_message
        return None
