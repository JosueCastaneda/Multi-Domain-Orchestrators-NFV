from communication_entities.messages.lcm_messages.grant_lcm_message import GrantLCMMessage
from communication_entities.messages.lcm_messages.scale_confirmation_message import ScaleConfirmationMessage
from communication_entities.messages.lcm_messages.scale_message import ScaleMessage
from entities import CommunicationEntityPackage
from utilities.logger import log


class LifeCycleManagement:

    def __init__(self, orchestrator, vnfs, services):
        self.vnfs = vnfs
        self.services = services
        self.orchestrator = orchestrator
        self.pending_operations = list()

    @staticmethod
    def create_new_operation(vnf_component_dict, original_service_id=''):
        new_operation = dict()
        new_operation['id'] = vnf_component_dict['id']
        new_operation['pending_dependencies'] = list()
        new_operation['type'] = vnf_component_dict['type']
        new_operation['original_service_id'] = original_service_id
        return new_operation

    def scale_vnf_component(self, vnf_dict, service_id='', original_service_id=''):
        external_orchestrator_id = ''
        self.add_pending_operations_to_service(vnf_dict, service_id, original_service_id)
        if vnf_dict['type'] == 'VNF':
            print('Scaling VNF: ' + vnf_dict['id'])
            self.scale_vnf(vnf_dict['id'], service_id, original_service_id)
        else:
            external_orchestrator_id = vnf_dict['orchestrator_id']
            original_service_id = service_id
            self.scale_service(vnf_dict['id'], external_orchestrator_id, original_service_id)
        return external_orchestrator_id

    def add_pending_operations_to_service(self, vnf_dict, service_id, original_service_id):
        for pending_operation in self.pending_operations:
            if pending_operation['id'] == service_id and pending_operation['original_service_id'] == original_service_id:
                new_dependency_as_dictionary = dict()
                new_dependency_as_dictionary['id'] = vnf_dict['id']
                new_dependency_as_dictionary['type'] = vnf_dict['type']
                new_dependency_as_dictionary['pending_operations'] = list()
                pending_operation['pending_operations'].append(new_dependency_as_dictionary)
                break

    def scale_vnf(self, vnf_component_id, service_id, original_service_id):
        for vnf in self.orchestrator.vnfs:
            if vnf['id'] == vnf_component_id:
                orchestrator_information = self.orchestrator.entry_as_dictionary()
                message = ScaleMessage(vnf['id'], orchestrator_information, service_id, original_service_id)
                self.orchestrator.send_message_to_vnf(vnf, message)

    def scale_service(self, vnf_component_id, external_orchestrator_id, original_service_id):
        external_orchestrator_info = self.orchestrator.find_orchestrator_by_id(external_orchestrator_id)
        original_service = self.service_as_a_dictionary(vnf_component_id, original_service_id)
        message = GrantLCMMessage(vnf_component_id,
                                  'scaling',
                                  original_service=original_service,
                                  vector_clock=self.orchestrator.vector_clock)
        self.orchestrator.send_message_to_orchestrator(message, external_orchestrator_info)

    def scale_vnfs(self, vnfs_to_scale, service_id, original_service_id):
        for vnf_to_scale in vnfs_to_scale:
            self.scale_vnf(vnf_to_scale['id'], service_id, original_service_id)

    @staticmethod
    def no_more_service_dependencies_to_scale(operation):
        for dependency in operation['pending_operations']:
            if dependency['type'] == 'Service':
                return False
        return True

    @staticmethod
    def are_there_still_vnfs_to_scale(operation):
        are_there_still_vnfs_to_scale = False
        for dependency in operation['pending_operations']:
            if dependency['type'] == 'VNF':
                are_there_still_vnfs_to_scale = True
                break
        if are_there_still_vnfs_to_scale and operation['is_first_operation'] == True:
            return False
        return are_there_still_vnfs_to_scale

    def no_more_dependencies_to_scale(self, service_id, original_service_id, type):
        operation = self.get_operation_by_id_and_original_service_id(service_id, original_service_id)
        no_services = self.no_more_service_dependencies_to_scale(operation)
        if self.is_simple_scaling(type, no_services, operation['is_first_operation'], operation['pending_operations']):
            return True
        at_least_one_vnf = self.are_there_still_vnfs_to_scale(operation)
        if no_services and not at_least_one_vnf:
            return True
        return False

    def is_simple_scaling(self, dependency_type, no_services, is_first_operation, list_of_operations):
        first = not list_of_operations
        second = self.is_base_case(dependency_type, no_services, is_first_operation)
        return first or second

    def is_base_case(self, dependency_type, no_services, is_first_operation):
        return dependency_type == 'Service' and no_services and is_first_operation

    def remove_dependency_from_service(self, service_id, original_service_id, vnf_component_id):
        vnf_index_to_remove = 0
        operation = self.get_operation_by_id_and_original_service_id(service_id, original_service_id)
        for index in range(len(operation['pending_operations'])):
            dependency = operation['pending_operations'][index]
            if dependency['id'] == vnf_component_id:
                vnf_index_to_remove = index
                break
        return operation['pending_operations'].pop(vnf_index_to_remove)

    def get_operation_by_id_and_original_service_id(self, service_id, service_original_id):
        for operation in self.pending_operations:
            if operation['id'] == service_id and operation['original_service_id'] == service_original_id:
                return operation
            elif operation['id'] == '' and operation['original_service_id'] == service_id:
                return operation
            elif operation['id'] == service_id:
                return operation

        # if len(self.pending_operations) == 0 and service_id == service_original_id:
        if len(self.pending_operations) == 0:
            empty_operation = dict()
            empty_operation['id'] = ''
            empty_operation['type'] = ''
            empty_operation['first_operation'] = True
            empty_operation['pending_operations'] = list()
            str_log = 'Operation of ' + service_id + ' originally from ' + service_original_id + ' not found!'
            print(str_log)
            log.info(str_log)
            return empty_operation

    def scale_confirmation(self, vnf_component_id, service_id, original_service_id):
        if service_id == '':
            log.info('Scaling operation of VNF has finished')
        else:
            operation = self.get_operation_by_id_and_original_service_id(service_id, original_service_id)
            if operation['pending_operations']:
                dependency = self.remove_dependency_from_service(service_id, original_service_id, vnf_component_id)
                if self.no_more_dependencies_to_scale(service_id, original_service_id, dependency['type']):
                    operation = self.remove_operation_by_service_id_and_original_service_id(service_id, original_service_id)
                    self.end_scaling(operation)
                    empty_pending_operations = list()
                    for i in range(len(self.pending_operations)):
                        if len(self.pending_operations[i]['pending_operations']) == 0:
                            empty_pending_operations.append(i)
                    for index in empty_pending_operations:
                        self.pending_operations.pop(index)
            else:
                str_log = 'Scaling of operation ' + service_id + ' from ' + original_service_id + ' has finished'
                log.info(str_log)

    def remove_operation_by_service_id_and_original_service_id(self, service_id, service_original_id):
        index_to_remove = 0
        for i in range(len(self.pending_operations)):
            operation = self.pending_operations[i]
            if operation['id'] == service_id and operation['original_service_id'] == service_original_id:
                index_to_remove = i
                break
        return self.pending_operations.pop(index_to_remove)

    def send_confirmation_to_end_scaling(self, service):
        acknowledge_message = ScaleConfirmationMessage(service['id'], service['original_service_id'], service['orchestrator_id'])
        communication_package = CommunicationEntityPackage(service['ip'], int(service['port']))
        self.orchestrator.server.connect_to_orchestrator(communication_package)
        self.orchestrator.server.send_message_to_orchestrator(acknowledge_message)
        log_str = 'End external scaling of service:' + service['id'] + ' requested from service: ' + service['original_service_id']
        log.info(log_str)
        print(log_str)

    def end_scaling(self, service):
        if self.is_external_vnf_component(service['original_service_id']):
            self.send_confirmation_to_end_scaling(service)
        else:
            if self.is_internal_pending_operation(service):
                self.send_confirmation_to_end_scaling(service)
            else:
                if self.no_more_pending_operations():
                    self.scale_vnfs(service['pending_operations'], service['original_service_id'], service['original_service_id'])
                else:
                    print('END SCALING')

    def no_more_pending_operations(self):
        return not self.pending_operations

    def is_internal_pending_operation(self, service):
        x = service['id']
        for operation in self.pending_operations:
            for waiting_operation in operation['pending_operations']:
                if waiting_operation['id'] == x:
                    return True
        return False

    def is_external_vnf_component(self, vnf_component_id):
        if vnf_component_id == '':
            return False
        for vnf in self.vnfs:
            if vnf['id'] == vnf_component_id:
                return False
        for service in self.services:
            if service.id == vnf_component_id:
                return False
        return True

    def add_new_service_to_scale(self, service_id, original_service):
        self.pending_operations.append(original_service)

    def format_as_a_dictionary(self, vnf_component_id='', vnf_component_type='', service_caller_id=''):
        service_format = dict()
        service_format['id'] = vnf_component_id
        service_format['original_service_id'] = service_caller_id
        service_format['ip'] = self.orchestrator.ip
        service_format['port'] = self.orchestrator.port
        service_format['orchestrator_id'] = self.orchestrator.id
        service_format['pending_operations'] = list()
        service_format['is_first_operation'] = False
        service_format['type'] = vnf_component_type
        return service_format

    def service_as_a_dictionary(self, vnf_component_id='', service_caller_id=''):
        service_format = dict()
        service_format['id'] = vnf_component_id
        service_format['original_service_id'] = service_caller_id
        service_format['ip'] = self.orchestrator.ip
        service_format['port'] = self.orchestrator.port
        service_format['orchestrator_id'] = self.orchestrator.id
        service_format['pending_operations'] = list()
        service_format['type'] = 'Service'
        service_format['is_first_operation'] = False
        return service_format
