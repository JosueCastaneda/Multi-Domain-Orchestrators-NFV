class PendingLCMScalingOperation:

    def __init__(self,
                 vnf_component_to_scale_id,
                 operation,
                 original_service_id='',
                 orchestrator_sender_id='',
                 original_orchestrator_id='',
                 sender_vector_clock=None,
                 service_sender_id='',
                 original_service=None):
        self.vnf_component_to_scale_id = vnf_component_to_scale_id
        self.operation = operation
        self.original_service_id = original_service_id
        self.orchestrator_sender_id = orchestrator_sender_id
        self.original_orchestrator_id = original_orchestrator_id
        self.sender_vector_clock = sender_vector_clock
        self.service_sender_id = service_sender_id
        self.original_service = original_service
        self.is_not_done = True

