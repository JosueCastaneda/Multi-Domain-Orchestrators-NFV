import asyncio
import datetime
import json

from communication_entities.messages.lcm_messages.grant_lcm_message import GrantLCMMessage
from communication_entities.messages.lcm_messages.scale_confirmation_message import ScaleConfirmationMessage
from communication_entities.messages.lcm_messages.scale_vnf_message import ScaleVNFMessage
from communication_entities.orchestrator_classes.pending_lcm_scaling_operation import PendingLCMScalingOperation
from communication_entities.vector_clock import VectorClock
from utilities.json_loader import my_date_converter
from utilities.life_cycle_management_update import send_message, return_success
from utilities.logger import log


class LifeCycleManagement:

    def __init__(self, orchestrator, vnfs, services):
        self.vnfs = vnfs
        self.services = services
        self.orchestrator = orchestrator
        self.pending_operations = list()
        self.are_VNFs_scaled = False
        self.has_finished = False

    @staticmethod
    def create_new_operation(vnf_component_dict, original_service_id=''):
        new_operation = dict()
        new_operation['id'] = vnf_component_dict['id']
        new_operation['pending_dependencies'] = list()
        new_operation['type'] = vnf_component_dict['type']
        new_operation['original_service_id'] = original_service_id
        return new_operation

    async def scale_vnf_component(self, vnf_dict, service_id='', original_service_id='',
                                  original_service_orchestrator_id=''):
        self.add_pending_operations_to_service(vnf_dict, service_id, original_service_id)
        if vnf_dict['type'] == 'VNF':
            await self.scale_vnf(vnf_dict['id'], service_id, original_service_id, original_service_orchestrator_id)
        else:
            await self.scale_service(vnf_dict['id'], vnf_dict['orchestrator_id'], service_id)

    def add_pending_operations_to_service(self, vnf_dict, service_id, original_service_id):
        for pending_operation in self.pending_operations:
            if pending_operation['id'] == service_id and pending_operation[
                'original_service_id'] == original_service_id:
                new_dependency_as_dictionary = dict()
                new_dependency_as_dictionary['id'] = vnf_dict['id']
                new_dependency_as_dictionary['type'] = vnf_dict['type']
                new_dependency_as_dictionary['pending_operations'] = list()
                pending_operation['pending_operations'].append(new_dependency_as_dictionary)
                break

    async def scale_vnf(self, vnf_component_id, service_id, original_service_id, original_service_orchestrator_id=''):
        log.info('Scaling VNF: ' + vnf_component_id)
        for vnf in self.orchestrator.vnfs:
            if vnf['id'] == vnf_component_id:
                data = dict()
                data['vnf_component_id'] = vnf['id']
                data['original_service_id'] = original_service_id
                data['orchestrator_sender_id'] = self.orchestrator.id
                data['original_orchestrator_id'] = original_service_orchestrator_id
                data['vector_clock'] = self.orchestrator.vector_clock.to_json()
                data['service_sender_id'] = service_id
                message = ScaleVNFMessage(vnf['server'], vnf['port'], data)
                await send_message(message)

    async def scale_service(self, vnf_component_id, external_orchestrator_id, original_service_id):
        log.info('Scaling Service: ' + vnf_component_id)
        external_orchestrator_info = self.orchestrator.find_orchestrator_by_id(external_orchestrator_id)
        original_service = self.service_as_a_dictionary(vnf_component_id, original_service_id)
        data = dict()
        data['vnf_component_to_scale_id'] = vnf_component_id
        data['operation'] = 'scaling'
        data['vnfs_to_scale'] = None
        data['services_ids'] = None
        data['current_service'] = None
        data['original_service'] = original_service
        data['sender_vector_clock'] = self.orchestrator.vector_clock.to_json()
        message = GrantLCMMessage(host=external_orchestrator_info['ip'], port=external_orchestrator_info['port'],
                                  data=data)
        await send_message(message)

    async def scale_vnfs(self, vnfs_to_scale, service_id, original_service_id):
        list_of_tasks = list()
        for vnf_to_scale in vnfs_to_scale:
            list_of_tasks.append(self.scale_vnf(vnf_to_scale['id'], service_id, original_service_id))
        await asyncio.gather(*list_of_tasks)

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

    def no_more_dependencies_to_scale(self, operation, type):
        log.info('Checking if no more dependencies to scale')
        no_services = self.no_more_service_dependencies_to_scale(operation)
        if self.is_simple_scaling(type, no_services, operation['is_first_operation'], operation['pending_operations']):
            log.info('Is simple scaling')
            return True
        at_least_one_vnf = self.are_there_still_vnfs_to_scale(operation)
        if no_services and not at_least_one_vnf:
            return True
        log.info('There are still dependencies to scale')
        return False

    def is_simple_scaling(self, dependency_type, no_services, is_first_operation, list_of_operations):
        first = not list_of_operations
        second = self.is_base_case(dependency_type, no_services, is_first_operation)
        return first or second

    def is_base_case(self, dependency_type, no_services, is_first_operation):
        return dependency_type == 'Service' and no_services and is_first_operation

    @staticmethod
    def remove_dependency_from_service(operation, vnf_component_id):
        vnf_index_to_remove = 0
        for index in range(len(operation['pending_operations'])):
            dependency = operation['pending_operations'][index]
            if dependency['id'] == vnf_component_id:
                vnf_index_to_remove = index
                break
        return operation['pending_operations'].pop(vnf_index_to_remove)

    @staticmethod
    def is_single_scale_operation(operation, service_original_id, service_id, sender_service_id):
        if operation['id'] == '' and operation[
            'original_service_id'] == service_original_id and service_original_id == sender_service_id:
            for pending_operation in operation['pending_operations']:
                if service_id == pending_operation['id']:
                    return True
        return False

    def is_received_service_a_original_dependency_from_the_scale_request(self, operation, service_original_id,
                                                                         service_id, sender_service_id):
        if operation['id'] == '' and operation[
            'original_service_id'] == service_original_id and service_id == sender_service_id:
            for pending_operation in operation['pending_operations']:
                if service_id == pending_operation['id'] and pending_operation['type'] == 'Service' or \
                        pending_operation['type'] == '':
                    return True
        return False

    @staticmethod
    def is_operation_original_service_and_service_received_is_a_pending_operation(operation, service_original_id,
                                                                                  service_id):
        if operation['id'] == service_original_id:
            for pending_operation in operation['pending_operations']:
                if pending_operation['id'] == service_id:
                    return True
        return False

    def is_received_service_a_dependency_of_operation_with_same_original_service_id_comes_from_same_sender(self,
                                                                                                           operation,
                                                                                                           service_original_id,
                                                                                                           service_id,
                                                                                                           sender_service_id):
        if operation['id'] == sender_service_id and operation['original_service_id'] == service_original_id:
            for pending_operation in operation['pending_operations']:
                if pending_operation['id'] == service_id:
                    return True
        return False

    def get_operation_by_id_and_original_service_id(self, service_id, service_original_id, sender_service_id):
        for operation in self.pending_operations:
            # log.info('Pending operation: ' + str(operation))
            if self.is_single_scale_operation(operation, service_original_id, service_id, sender_service_id):
                return operation
            elif self.is_operation_original_service_and_service_received_is_a_pending_operation(operation,
                                                                                                service_original_id,
                                                                                                service_id):
                log.info('Operation is original service and service received is a pending operation')
                # log.info('Removing from Pending operation: ' + str(operation))
                return operation
            elif self.is_received_service_a_dependency_of_operation_with_same_original_service_id_comes_from_same_sender(
                    operation, service_original_id, service_id, sender_service_id):
                log.info('Service is a dependency with the same original service and sender')
                # log.info('Removing from Pending operation: ' + str(operation))
                return operation

            elif self.is_received_service_a_original_dependency_from_the_scale_request(operation, service_original_id,
                                                                                       service_id, sender_service_id):
                return operation

        if len(self.pending_operations) == 0:
            empty_operation = dict()
            empty_operation['id'] = ''
            empty_operation['type'] = ''
            empty_operation['first_operation'] = True
            empty_operation['pending_operations'] = list()
            str_log = 'Operation of ' + service_id[0:8] + ' originally from ' + service_original_id[0:8] + ' not found!'
            log.info(str_log)
            return empty_operation

        if self.vnfc_is_not_a_dependency_from_operation(operation, service_original_id, service_id, sender_service_id):
            empty_operation = dict()
            empty_operation['id'] = ''
            empty_operation['type'] = ''
            empty_operation['first_operation'] = True
            empty_operation['pending_operations'] = list()
            str_log = 'Operation of ' + service_id[0:8] + ' originally from ' + service_original_id[0:8] + ' not found!'
            log.info(str_log)
            return empty_operation
        log.info('None, serious error why!?')
        return None

    def vnfc_is_not_a_dependency_from_operation(self, operation, service_original_id, service_id, sender_service_id):
        if operation['id'] == '' and operation[
            'original_service_id'] == service_original_id and service_id == sender_service_id:
            for pending_operation in operation['pending_operations']:
                if service_id == pending_operation['id']:
                    return False
        return True

    async def scale_confirmation(self,
                                 vnf_component_id,
                                 original_service_id,
                                 orchestrator_sender_id,
                                 original_orchestrator_id,
                                 sender_vector_clock_string,
                                 service_sender_id,
                                 was_called_by_pending_operations=False):
        if not isinstance(sender_vector_clock_string, VectorClock):
            sender_vector_clock = VectorClock()
            sender_vector_clock.create_from_list(sender_vector_clock_string)
        else:
            sender_vector_clock = sender_vector_clock_string
        log.info('Confirmation for: ' + str(vnf_component_id[0:8]) + ' from service ' + str(
            service_sender_id[0:8]) + ' originally by: ' + str(original_service_id[0:8]) + ' sent by: ' + str(
            orchestrator_sender_id[0:8]))
        log.info(
            'Received ' + sender_vector_clock.as_string() + ' My clock ' + self.orchestrator.vector_clock.as_string())
        my_clock_is_bigger = True
        if original_service_id == self.orchestrator.id:
            difference_in_vectors = 0
        else:
            difference_in_vectors = self.orchestrator.vector_clock.compare_clocks(sender_vector_clock,
                                                                                  orchestrator_sender_id,
                                                                                  self.orchestrator.causal_delivery)
            my_clock_is_bigger = self.orchestrator.vector_clock.is_greater_than_other(sender_vector_clock)
            if difference_in_vectors == 2:
                difference_in_clocks, real_orchestrator_sender_id = self.orchestrator.vector_clock.check_single_difference(
                    sender_vector_clock)
                if difference_in_clocks == 1:
                    orchestrator_sender_id = real_orchestrator_sender_id

        if not self.orchestrator.causal_delivery:
            if difference_in_vectors > 1:
                str_log = 'A new inconsistency because Sender VT' + sender_vector_clock.as_string() + ' > '
                str_log_2 = str_log + self.orchestrator.vector_clock.as_string()
                log.info(str_log_2)
                self.orchestrator.inconsistencies += 1
            await self.check_if_clocks_are_valid_and_do_operation(vnf_component_id=vnf_component_id,
                                                                  original_service_id=original_service_id,
                                                                  orchestrator_sender_id=orchestrator_sender_id,
                                                                  service_sender_id=service_sender_id,
                                                                  was_called_by_pending_operations=was_called_by_pending_operations,
                                                                  my_clock_is_bigger=my_clock_is_bigger,
                                                                  sender_vector_clock=sender_vector_clock)
        else:
            if difference_in_vectors <= 1 or my_clock_is_bigger:
                await self.check_if_clocks_are_valid_and_do_operation(vnf_component_id=vnf_component_id,
                                                                      original_service_id=original_service_id,
                                                                      orchestrator_sender_id=orchestrator_sender_id,
                                                                      service_sender_id=service_sender_id,
                                                                      was_called_by_pending_operations=was_called_by_pending_operations,
                                                                      my_clock_is_bigger=my_clock_is_bigger,
                                                                      sender_vector_clock=sender_vector_clock)
            else:
                log.info(
                    'Added to pending operations because ' + self.orchestrator.vector_clock.as_string() + ' < ' + sender_vector_clock.as_string())
                original_service = dict()
                original_service['id'] = vnf_component_id
                original_service['original_service_id'] = original_service_id
                original_service['ip'] = ''
                original_service['port'] = ''
                original_service['orchestrator_id'] = orchestrator_sender_id
                original_service['pending_operations'] = list()
                original_service['type'] = 'XXX'
                original_service['is_first_operation'] = False
                self.orchestrator.pending_operations_repetitions += 1
                new_operation = PendingLCMScalingOperation(vnf_component_to_scale_id=vnf_component_id,
                                                           operation='scale',
                                                           original_service_id=original_service_id,
                                                           orchestrator_sender_id=orchestrator_sender_id,
                                                           original_orchestrator_id=original_orchestrator_id,
                                                           sender_vector_clock=sender_vector_clock,
                                                           service_sender_id=service_sender_id,
                                                           original_service=original_service)
                self.orchestrator.add_pending_operation(new_operation)
        return return_success()

    async def check_if_clocks_are_valid_and_do_operation(self,
                                                         vnf_component_id,
                                                         original_service_id,
                                                         orchestrator_sender_id,
                                                         service_sender_id,
                                                         was_called_by_pending_operations,
                                                         my_clock_is_bigger,
                                                         sender_vector_clock):
        if not my_clock_is_bigger:
            self.orchestrator.vector_clock.update_clock(sender_vector_clock, orchestrator_sender_id,
                                                        self.orchestrator.causal_delivery)
        if vnf_component_id == '':
            log.info('Scaling operation of VNF has finished')
        else:
            operation = self.get_operation_by_id_and_original_service_id(vnf_component_id, original_service_id,
                                                                         service_sender_id)
            if operation['pending_operations']:
                dependency = self.remove_dependency_from_service(operation, vnf_component_id)
                if self.no_more_dependencies_to_scale(operation, dependency['type']):
                    log.info('No more dependencies to scale')
                    await self.end_scaling(operation)
                    empty_pending_operations = list()
                    for op in self.pending_operations:
                        if len(op['pending_operations']) == 0:
                            empty_pending_operations.append(op)

                    for op in empty_pending_operations:
                        self.pending_operations.remove(op)
            else:
                log.info('Scaling of operation ' + vnf_component_id[0:8] + ' from ' + original_service_id[0:8] + ' has finished')
        if not was_called_by_pending_operations:
            log.info('Scaling - Do Pending Operations - ')
            if self.are_there_pending_operations():
                await self.orchestrator.do_pending_operations()
            self.orchestrator.pending_operations_repetitions = 0

    def are_there_pending_operations(self):
        return len(self.pending_operations) > 0 or len(self.orchestrator.pending_lcm_operations) > 0

    def remove_operation_by_service_id_and_original_service_id(self, service_id, service_original_id):
        index_to_remove = -1
        for i in range(len(self.pending_operations)):
            operation = self.pending_operations[i]
            if operation['id'] == service_id and operation['original_service_id'] == service_original_id:
                index_to_remove = i
                break
        if index_to_remove >= 0:
            return self.pending_operations.pop(index_to_remove)
        else:
            return -1

    async def send_confirmation_to_end_scaling(self, service):
        data = dict()
        data['vnf_component_id'] = service['id']
        data['original_service_id'] = service['original_service_id']
        data['orchestrator_sender_id'] = self.orchestrator.id
        data['original_orchestrator_id'] = service['orchestrator_id']
        data['vector_clock'] = self.orchestrator.vector_clock.to_json()
        data['service_sender_id'] = service['id']
        acknowledge_message = ScaleConfirmationMessage(host=service['ip'], port=int(service['port']), data=data)
        await send_message(acknowledge_message)
        log_str = 'End external scaling of service:' + service['id'][0:8] + ' requested from service: ' + service[
            'original_service_id'][0:8] + ' Inconsistencies: ' + str(self.orchestrator.inconsistencies)
        log.info(log_str)

    async def end_scaling(self, service):
        log.info('End Scaling')
        if self.is_external_vnf_component(service['original_service_id']):
            log.info('Is external VNF Component')
            await self.send_confirmation_to_end_scaling(service)
        else:
            if self.is_internal_pending_operation(service):
                log.info('Is internal pending operation')
                await self.send_confirmation_to_end_scaling(service)
            else:
                if service['id'] == '' and self.only_pending_vnfs() and not self.are_VNFs_scaled and len(
                        service['pending_operations']) > 0:
                    log.info('Only pending VNFs, not scaled and there are pending operations')
                    await self.scale_vnfs(service['pending_operations'], service['original_service_id'],
                                          service['original_service_id'])
                    # self.are_VNFs_scaled = True
                else:
                    if len(service['pending_operations']) == 0:
                        self.are_VNFs_scaled = False
                        elapsed = datetime.datetime.now() - service['start_time']
                        str_log_1 = 'End of Scaling of service ' + service['original_service_id'][0:8] + ' time elapsed: '
                        str_log_2 = str(elapsed.total_seconds()) + ' seconds '
                        str_log_3 = ' with ' + str(self.orchestrator.inconsistencies) + ' inconsistencies'
                        log.info(str_log_1 + str_log_2 + str_log_3)
                        log.info('Are VNFs SCALED? ' + str(self.are_VNFs_scaled))
                        self.orchestrator.time_elapsed_in_reconfiguration = elapsed.total_seconds()
                        self.has_finished = True
                        # log.info(' End Scaling: VT- ' + self.orchestrator.vector_clock.as_string())

    def only_pending_vnfs(self):
        last_operation = self.pending_operations[0]
        for pending_operation in last_operation['pending_operations']:
            if pending_operation['type'] != 'VNF':
                return False
        return True

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
        service_format['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps(service_format, default=my_date_converter)

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
        service_format['start_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return json.dumps(service_format, default=my_date_converter)
