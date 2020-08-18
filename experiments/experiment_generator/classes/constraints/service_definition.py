from utilities.random_integer_generation import generate_unique_identifier


class ServiceDefinition:

    def __init__(self, orchestrator):
        self.id = generate_unique_identifier()
        self.type = 'Service'
        self.orchestrator_id = orchestrator.id
        self.list_of_vnf_components = list()
        self.are_all_dependencies_vnfs = True

    def add_vnf_component(self, vnf_component):
        if vnf_component.type == 'Service':
            self.are_all_dependencies_vnfs = False
        self.list_of_vnf_components.append(vnf_component)

    def is_new_vnf_component_unique(self, new_vnfc):
        for vnfc in self.list_of_vnf_components:
            if new_vnfc.id == vnfc.id:
                return False
        return True

    def is_new_vnf_component_in_a_loop(self, new_vnfc):
        if self.are_all_dependencies_vnfs:
            for vnfc in self.list_of_vnf_components:
                if vnfc.type == 'VNF' and vnfc.id == new_vnfc.id:
                    return True
            return False
        return self.handle_service_dependencies(new_vnfc)

    def handle_service_dependencies(self, new_vnfc):
        for vnfc in self.list_of_vnf_components:
            if vnfc.type == 'VNF' and vnfc.id == new_vnfc.id:
                return True

            if vnfc.type == 'Service':
                is_loop = vnfc.is_new_vnf_component_in_a_loop(new_vnfc)
                if is_loop:
                    return True
        return False

    def create_dictionary_specification(self):
        new_service = dict()
        new_service['id'] = self.id
        new_service['orchestrator_id'] = self.orchestrator_id
        new_service['are_all_dependencies_vnfs'] = self.are_all_dependencies_vnfs
        new_service['type'] = self.type
        new_service['dependencies'] = list()
        for dependency in self.list_of_vnf_components:
            new_dependency = dict()
            new_dependency['id'] = dependency.id
            new_dependency['orchestrator_id'] = dependency.orchestrator_id
            new_dependency['type'] = dependency.type
            new_service['dependencies'].append(new_dependency)
        return new_service

    def get_vnf_components(self):
        return self.list_of_vnf_components
