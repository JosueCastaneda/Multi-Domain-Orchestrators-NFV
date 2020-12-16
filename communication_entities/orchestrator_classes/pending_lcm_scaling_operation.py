from utilities.logger import log


class PendingLCMScalingOperation:

    def __init__(self,
                 vnf_component_to_scale_id,
                 operation,
                 original_service_id='',
                 orchestrator_sender_id='',
                 original_orchestrator_id='',
                 sender_vector_clock=None,
                 service_sender_id='',
                 original_service=None,
                 data=None):
        self.vnf_component_to_scale_id = vnf_component_to_scale_id
        self.operation = operation
        self.original_service_id = original_service_id
        self.orchestrator_sender_id = orchestrator_sender_id
        self.original_orchestrator_id = original_orchestrator_id
        self.sender_vector_clock = sender_vector_clock
        self.service_sender_id = service_sender_id
        self.original_service = original_service
        self.is_not_done = True
        self.data = data

    def set_vector_clock(self, new_vector_clock):
        log.info(self.sender_vector_clock.to_json())
        log.info(new_vector_clock)
        log.info(new_vector_clock.to_json())
        self.sender_vector_clock = new_vector_clock
        log.info('After setting vector clock ')
        log.info(self.sender_vector_clock.to_json())

    def as_dictionary(self):
        dictionary_definition = dict()
        dictionary_definition['vnf_component_to_scale_id'] = self.vnf_component_to_scale_id
        dictionary_definition['operation'] = self.operation
        dictionary_definition['original_service_id'] = self.original_service_id
        dictionary_definition['orchestrator_sender_id'] = self.orchestrator_sender_id
        dictionary_definition['original_orchestrator_id'] = self.original_orchestrator_id
        if type(self.sender_vector_clock) == 'str':
            dictionary_definition['sender_vector_clock'] = self.sender_vector_clock
        else:
            dictionary_definition['sender_vector_clock'] = self.sender_vector_clock.to_json()
        dictionary_definition['service_sender_id'] = self.service_sender_id
        dictionary_definition['original_service'] = self.original_service
        dictionary_definition['is_not_done'] = self.is_not_done
        dictionary_definition['data'] = self.data
        return dictionary_definition
