import asyncio
import datetime

from communication_entities.messages.lcm_messages.grant_lcm_message import GrantLCMMessage
from communication_entities.messages.lcm_messages.notification_lcm_operation import NotificationLCMOperation
from utilities.life_cycle_management_update import send_message
from utilities.logger import log
from utilities.json_loader import my_date_converter
import json


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

    def as_string(self):
        dictionary_string = dict()
        dictionary_string['id'] = self.id
        return dictionary_string

    # TODO: Implement the validation code
    def validate_scaling(self):
        no_dependencies = True
        is_valid = True
        for dependency in self.dependencies:
            if dependency['type'] == 'Service':
                no_dependencies = False
                break
        return is_valid, no_dependencies

    async def scale(self):
        log.info('Beginning to scale service: ' + str(self.id))
        vnfs_to_scale = dict()
        vnfs_to_scale[self.id] = list()
        services_ids = list()
        services_ids.append(self.id)
        services_to_scale, vnfs_to_scale = self.gather_dependencies(vnfs_to_scale)
        if not services_to_scale:
            await self.scale_withouth_dependencies(list())
        else:
            await self.scale_with_dependencies(services_to_scale, vnfs_to_scale, services_ids, list())

    def gather_dependencies(self, vnfs_to_scale):
        services_to_scale = list()
        for dependency in self.dependencies:
            if dependency['type'] == 'VNF':
                vnfs_to_scale[self.id].append(dependency)
            else:
                services_to_scale.append(dependency)
        return services_to_scale, vnfs_to_scale

    async def scale_withouth_dependencies(self, exclude_list_of_orchestrators):
        current_vector_clock = self.orchestrator.vector_clock
        await asyncio.gather(self.independent_scale_causal(),
                             self.orchestrator.notify_all_orchestrators_of_change(exclude_list_of_orchestrators,
                                                                                  current_vector_clock))

    async def send_grant_messages_to_dependencies(self, data_list):
        asynchronous_tasks = list()
        for data in data_list:
            log.info('Sending grant to ' + data['vnf_component_to_scale_id'])
            scaling_message = GrantLCMMessage(host=data['host_dependency'], port=data['port_dependency'], data=data)
            asynchronous_tasks.append(send_message(scaling_message))
        await asyncio.gather(*asynchronous_tasks)

    async def scale_with_dependencies(self, services_to_scale, vnfs_to_scale, services_ids,
                                      exclude_list_of_orchestrators):
        data_list, exclude_list_of_orchestrators = self.gather_service_dependencies(services_to_scale, vnfs_to_scale,
                                                                                    services_ids,
                                                                                    exclude_list_of_orchestrators)
        current_vector_clock = self.orchestrator.vector_clock
        await asyncio.gather(self.send_grant_messages_to_dependencies(data_list),
                             self.orchestrator.notify_all_orchestrators_of_change(exclude_list_of_orchestrators,
                                                                                  current_vector_clock))

    def gather_service_dependencies(self, services_to_scale, vnfs_to_scale, services_ids,
                                    exclude_list_of_orchestrators):
        data_list = list()
        for dependency in services_to_scale:
            service_definition = self.format_as_a_dictionary_json(dependency['id'], dependency['type'])
            orchestrator = self.orchestrator.get_orchestrator_information_by_id(dependency['orchestrator_id'])
            data = dict()
            data['vnf_component_to_scale_id'] = dependency['id']
            data['operation'] = 'scale'
            data['vnfs_to_scale'] = vnfs_to_scale
            data['services_ids'] = services_ids
            data['current_service'] = 0
            data['original_service'] = service_definition
            data['sender_vector_clock'] = self.orchestrator.vector_clock.to_json()
            data['host_dependency'] = orchestrator['ip']
            data['port_dependency'] = orchestrator['port']
            data_list.append(data)
            exclude_list_of_orchestrators.append(orchestrator)
        return data_list, exclude_list_of_orchestrators

    def is_orchestrator_included_for_notification(self, id_orch, excluding_list):
        for orchestrator in excluding_list:
            if isinstance(orchestrator, str):
                if id_orch == orchestrator:
                    return False
            elif id_orch == orchestrator['id']:
                return False
        return True

    async def scale_dependencies(self, service_id, original_service_id, original_service_orchestrator_id):
        for dependency in self.dependencies:
            await asyncio.create_task(self.orchestrator.life_cycle_manager.scale_vnf_component(dependency,
                                                                                               service_id,
                                                                                               original_service_id,
                                                                                               original_service_orchestrator_id))

    def gather_external_dependencies(self):
        exclude_list_of_orchestrators = list()
        for dependency in self.dependencies:
            if dependency['type'] != 'VNF':
                exclude_list_of_orchestrators.append(dependency['orchestrator_id'])
        return exclude_list_of_orchestrators

    async def scale_from_external_orchestrator(self, service_id, original_service_id, original_service_orchestrator_id):
        old_value = self.orchestrator.vector_clock
        self.orchestrator.vector_clock.increment_clock(self.orchestrator.id)
        current_vector_clock = self.orchestrator.vector_clock
        log.info('Old Value VT: ' + old_value.as_string() + ' New Value VT: ' + current_vector_clock.as_string())
        exclude_list_of_orchestrators = self.gather_external_dependencies()
        await asyncio.gather(self.scale_dependencies(service_id, original_service_id, original_service_orchestrator_id),
                             self.orchestrator.notify_all_orchestrators_of_change(exclude_list_of_orchestrators,
                                                                                  current_vector_clock))

    async def independent_scale_causal(self, service_id='', original_service_id='',
                                       original_service_orchestrator_id=''):
        if service_id == '':
            self.orchestrator.life_cycle_manager.are_VNFs_scaled = True
            await self.orchestrator.life_cycle_manager.scale_vnfs(self.dependencies, service_id, self.id)
        else:
            await self.scale_from_external_orchestrator(service_id,
                                                        original_service_id,
                                                        original_service_orchestrator_id)

    # def independent_scale_normal(self, service_id='', original_service_id='', original_service_orchestrator_id=''):
    #     log.info('Old Value VT: ' + self.orchestrator.vector_clock.as_string())
    #     self.orchestrator.vector_clock.increment_clock(self.orchestrator.id)
    #     log.info('New Value VT: ' + self.orchestrator.vector_clock.as_string())
    #     if service_id == '':
    #         self.orchestrator.life_cycle_manager.scale_vnfs(self.dependencies, service_id)
    #     else:
    #         for dependency in self.dependencies:
    #             self.orchestrator.life_cycle_manager.scale_vnf_component(dependency,
    #                                                                      service_id,
    #                                                                      original_service_id,
    #                                                                      original_service_orchestrator_id)

    def format_as_a_dictionary_json(self, vnf_component_id='', vnf_component_type='', is_first=False):
        service_format = dict()
        service_format['id'] = vnf_component_id
        service_format['original_service_id'] = self.id
        service_format['ip'] = self.orchestrator.ip
        service_format['port'] = self.orchestrator.port
        service_format['orchestrator_id'] = self.orchestrator.id
        service_format['pending_operations'] = list()
        service_format['type'] = vnf_component_type
        service_format['is_first_operation'] = is_first
        service_format['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps(service_format, default=my_date_converter)

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
        service_format['start_time'] = datetime.datetime.now()
        return service_format

    def create_service_as_dictionary_and_add_pending_operations_to_service(self):
        service_as_dictionary = self.format_as_a_dictionary(is_first=True)
        for dependency in self.dependencies:
            new_dependency_as_dictionary = dict()
            new_dependency_as_dictionary['id'] = dependency['id']
            new_dependency_as_dictionary['type'] = dependency['type']
            new_dependency_as_dictionary['first_operation'] = True
            service_as_dictionary['pending_operations'].append(new_dependency_as_dictionary)
        return service_as_dictionary
