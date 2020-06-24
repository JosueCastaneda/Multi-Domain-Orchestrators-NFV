from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import log


class ScaleConfirmationMessage(AbstractMessage):

    def __init__(self, host, port, data):
        super().__init__(host=host, port=port, type='scale_of_service_has_ended', data=data)
        # self.vnf_component_id = vnf_component_id
        # self.original_service_id = original_service_id
        # self.orchestrator_sender_id = orchestrator_sender_id
        # self.original_orchestrator_id = original_orchestrator_id
        # self.vector_clock = vector_clock
        # self.service_sender_id=service_sender_id

    # def process_by_command_line(self):
    #     self.current_server.orchestrator.life_cycle_manager.scale_confirmation(self.vnf_component_id,
    #                                                                            self.original_service_id,
    #                                                                            self.orchestrator_sender_id,
    #                                                                            self.original_orchestrator_id,
    #                                                                            self.vector_clock,
    #                                                                            self.service_sender_id)
 # def __init__(self,
 #                 vnf_component_id,
 #                 original_service_id,
 #                 orchestrator_sender_id,
 #                 original_orchestrator_id,
 #                 vector_clock,
 #                 service_sender_id):