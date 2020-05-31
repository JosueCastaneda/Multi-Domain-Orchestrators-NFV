class PendingLCMScalingOperation:

    def __init__(self, vnf_component_to_scale_id, operation, original_service, sender_vector_clock):
        self.vnf_component_to_scale_id = vnf_component_to_scale_id
        self.operation = operation
        self.original_service = original_service
        self.sender_vector_clock = sender_vector_clock
        self.is_not_done = True
