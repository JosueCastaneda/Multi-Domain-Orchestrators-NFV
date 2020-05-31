from communication_entities.messages.abstract_message import AbstractMessage


class ScaleConfirmationMessage(AbstractMessage):

    def __init__(self, vnf_component_id, service_id, original_orchestrator_id):
        super().__init__(None)
        self.vnf_component_id = vnf_component_id
        self.service_id = service_id
        self.original_orchestrator_id = original_orchestrator_id

    def process_by_command_line(self):
        print('Confirmation for: ' + str(self.vnf_component_id))
        self.current_server.orchestrator.life_cycle_manager.scale_confirmation(self.vnf_component_id, self.service_id, self.original_orchestrator_id)

