from communication_entities.messages.abstract_message import AbstractMessage


# TODO: This class requires so much parameters, fix this
class GrantLCMMessage(AbstractMessage):

    def __init__(self,
                 vnf_component_to_scale_id,
                 operation,
                 vnfs_to_scale=None,
                 services_ids=None,
                 current_service=0,
                 original_service=None,
                 vector_clock=None):
        super().__init__(data=None, vector_clock=vector_clock)
        self.vnf_component_to_scale_id = vnf_component_to_scale_id
        self.operation = operation
        self.vnfs_to_scale = vnfs_to_scale
        self.services_ids = services_ids
        self.current_service = current_service
        self.original_service = original_service

    def process_by_command_line(self):
        print('Grant to scale service: ' + str(self.vnf_component_to_scale_id))
        print('Coming from service: ' + str(self.original_service['original_service_id']))
        self.current_server.orchestrator.grant_lcm_operation(self.vnf_component_to_scale_id,
                                                             self.operation,
                                                             self.original_service,
                                                             self.vector_clock)
