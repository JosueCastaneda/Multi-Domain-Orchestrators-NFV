from communication_entities.messages.abstract_message import AbstractMessage


class ScaleVNFMessage(AbstractMessage):

    def __init__(self, host, port, data):
        super().__init__(host=host, port=port, type='scale_vnf', data=data)

    # def process_by_command_line(self):
    #     self.current_server.orchestrator.scale(self.vnf_component_id,
    #                                            self.original_service_id,
    #                                            self.orchestrator_sender_id,
    #                                            self.original_orchestrator_id,
    #                                            self.vector_clock,
    #                                            self.service_sender_id)
#
# def __init__(self,
#                  vnf_component_id,
#                  original_service_id,
#                  orchestrator_sender_id,
#                  original_orchestrator_id,
#                  vector_clock,
#                  service_sender_id,
#                  host,
#                  port,
#                  data):