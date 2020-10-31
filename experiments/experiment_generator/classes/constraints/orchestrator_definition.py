from utilities.random_integer_generation import generate_unique_identifier


class OrchestratorDefinition:

    def __init__(self, ip, port, location, constraints):
        self.id = generate_unique_identifier()
        self.type = 'orchestrator'
        self.ip = ip
        self.port = port
        self.vnfs = list()
        self.services = list()
        self.location = location
        self.current_ip = 1
        self.constraints = constraints
        self.vnf_forwarding_graphs = list()

    def add_vnf_forwarding_graph(self, vnf_forwarding_graph):
        self.vnf_forwarding_graphs.append(vnf_forwarding_graph)

    def add_vnf(self, vnf):
        self.vnfs.append(vnf)

    def add_service(self, service):
        self.services.append(service)

    def clear_all(self):
        self.vnfs.clear()
        self.services.clear()

    def create_dictionary_specification(self):
        new_orchestrator = dict()
        new_orchestrator['id'] = self.id
        new_orchestrator['ip'] = self.ip
        new_orchestrator['location'] = self.location
        new_orchestrator['port'] = self.port
        new_orchestrator['type'] = self.type
        new_orchestrator['vnfs'] = list()
        new_orchestrator['services'] = list()
        new_orchestrator['vnf-forwarding_graphs'] = list()
        for vnf in self.vnfs:
            new_vnf = vnf.create_dictionary_specification()
            new_orchestrator['vnfs'].append(new_vnf)
        for service in self.services:
            new_service = service.create_dictionary_specification()
            new_orchestrator['services'].append(new_service)

        for vnf_forwarding_graph in self.vnf_forwarding_graphs:
            new_orchestrator['vnf-forwarding_graphs'].append(vnf_forwarding_graph)

        return new_orchestrator

    def get_vnfs(self):
        return self.vnfs

    def get_services(self):
        return self.services

    def get_new_ip(self):
        return '0.0.0.0'

    def increase_current_ip(self):
        self.current_ip += 1
