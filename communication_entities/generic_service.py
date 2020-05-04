from communication_entities.messages.lcm_messages.grant_lcm_message import GrantLCMMessage
from utilities.logger import log


class GenericService:

    def __init__(self, unique_id, orchestrator, dependencies):
        self.id = unique_id
        self.orchestrator = orchestrator
        self.max_delay = 0
        self.max_jitter = 0
        self.max_throughput = 0
        self.loss_ratio = 0
        self.dependencies = dependencies
        self.type = 'Service'

    # TODO: Implement the validation code
    def validate_scaling(self):
        no_dependencies = True
        is_valid = True
        for dependency in self.dependencies:
            if dependency['type'] == 'Service':
                no_dependencies = False
                break

        return is_valid, no_dependencies

    # TODO: RENAME TO first_scale or something like that
    def scale(self):
        log.info('Beginning to scale service: ' + str(self.id))
        no_service_dependencies = True
        vnfs_to_scale = dict()
        vnfs_to_scale[self.id] = list()
        services_ids = list()
        services_ids.append(self.id)
        services_to_scale = list()
        for dependency in self.dependencies:
            if dependency['type'] == 'VNF':
                vnfs_to_scale[self.id].append(dependency)
            else:
                services_to_scale.append(dependency)
                no_service_dependencies = False
        if no_service_dependencies:
            self.independent_scale()
        else:
            for dependency in services_to_scale:
                service_definition = self.format_as_a_dictionary(dependency['id'], dependency['type'])
                scaling_message = GrantLCMMessage(dependency['id'],
                                                  'scaling',
                                                  vnfs_to_scale,
                                                  services_ids,
                                                  current_service=0,
                                                  original_service=service_definition)
                orchestrator = self.orchestrator.get_orchestrator_information_by_id(dependency['orchestrator_id'])
                self.orchestrator.send_lcm_message(scaling_message, orchestrator)

    def independent_scale(self, service_id=''):
        if service_id == '':
            self.orchestrator.life_cycle_manager.scale_vnfs(self.dependencies, service_id)
        else:
            # vnfs_to_scale = list()
            for dependency in self.dependencies:
                self.orchestrator.life_cycle_manager.scale_vnf_component(dependency,service_id)

    def scale_with_grant(self, original_sender, original_service_id):
        new_operation = self.orchestrator.life_cycle_manager.create_new_operation(self.id, original_service_id)
        self.orchestrator.life_cycle_manager.pending_operations.append(new_operation)
        for dependency in self.dependencies:
            new_operation['pending_dependencies'].append(dependency.id)
            if dependency.type == 'vnf':
                dependency.scale(self.orchestrator, self.id)
            else:
                dependency.scale_with_grant(self.orchestrator, self.id)

    def format_as_a_dictionary(self, vnf_component_id='', vnf_component_type='', is_first=False):
        service_format = dict()
        service_format['id'] = vnf_component_id
        service_format['original_service_id'] = self.id
        service_format['ip'] = self.orchestrator.ip
        service_format['port'] = self.orchestrator.port
        service_format['orchestrator_id'] = self.orchestrator.id
        service_format['pending_operations'] = list()
        service_format['type'] = vnf_component_type
        service_format['is_first_operation'] = is_first
        return service_format
