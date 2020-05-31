from communication_entities.messages.lcm_messages.grant_lcm_message import GrantLCMMessage
from communication_entities.messages.lcm_messages.notification_lcm_operation import NotificationLCMOperation
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
        exclude_list_of_orchestrators = list()
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
                                                  original_service=service_definition,
                                                  vector_clock=self.orchestrator.vector_clock)
                orchestrator = self.orchestrator.get_orchestrator_information_by_id(dependency['orchestrator_id'])
                exclude_list_of_orchestrators.append(orchestrator)
                self.orchestrator.send_lcm_message(scaling_message, orchestrator)

            exclude_list_of_orchestrators.append(self.orchestrator.entry_as_dictionary())
            new_message = NotificationLCMOperation(self.orchestrator.vector_clock, self.orchestrator.id)
            for orchestrator in self.orchestrator.list_orchestrator:
                if self.is_orchestrator_included_for_notification(orchestrator['id'], exclude_list_of_orchestrators):
                    self.orchestrator.send_message_to_orchestrator(new_message, orchestrator)

    def is_orchestrator_included_for_notification(self, id_orch, excluding_list):
        for orchestrator in excluding_list:
            if isinstance(orchestrator, str):
                if id_orch == orchestrator:
                    return False
            elif id_orch == orchestrator['id']:
                return False
        return True

    def independent_scale(self, service_id='', original_service_id=''):
        if service_id == '':
            self.orchestrator.life_cycle_manager.scale_vnfs(self.dependencies, service_id)
        else:
            exclude_list_of_orchestrators = list()
            self.orchestrator.vector_clock.increment_clock(self.orchestrator.id)
            for dependency in self.dependencies:
                external_orchestrator = self.orchestrator.life_cycle_manager.scale_vnf_component(dependency,service_id, original_service_id)
                if external_orchestrator != '':
                    exclude_list_of_orchestrators.append(external_orchestrator)
            exclude_list_of_orchestrators.append(self.orchestrator.entry_as_dictionary())
            new_message = NotificationLCMOperation(self.orchestrator.vector_clock, self.orchestrator.id)
            for orchestrator in self.orchestrator.list_orchestrator:
                if self.is_orchestrator_included_for_notification(orchestrator['id'], exclude_list_of_orchestrators):
                    self.orchestrator.send_message_to_orchestrator(new_message, orchestrator)

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
