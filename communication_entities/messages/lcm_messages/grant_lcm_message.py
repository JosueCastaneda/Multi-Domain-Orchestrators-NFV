from communication_entities.messages.abstract_message import AbstractMessage


# TODO: This class requires so much parameters, fix this
from utilities.logger import log


class GrantLCMMessage(AbstractMessage):

    def __init__(self,host, port, data):
        super().__init__(host=host, port=port, data=data, type='grant_service_migration')
        # super().__init__(data=None, vector_clock=vector_clock)
        #
        # self.vnf_component_to_scale_id = vnf_component_to_scale_id
        # self.operation = operation
        # self.vnfs_to_scale = vnfs_to_scale
        # self.services_ids = services_ids
        # self.current_service = current_service
        # self.original_service = original_service

    # def process_by_command_line(self):
    #     log.info('Grant to scale service: ' + str(self.vnf_component_to_scale_id))
    #     log.info('Coming from service: ' + str(self.original_service['original_service_id']))
    #     self.current_server.orchestrator.wait_before_delivery_grant(self.vnf_component_to_scale_id, self.operation, self.original_service, self.vector_clock)

# def __init__(self,
#                  vnf_component_to_scale_id,
#                  operation,
#                  vnfs_to_scale=None,
#                  services_ids=None,
#                  current_service=0,
#                  original_service=None,
#                  vector_clock=None):