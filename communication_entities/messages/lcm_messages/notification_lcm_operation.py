from communication_entities.messages.abstract_message import AbstractMessage


class NotificationLCMOperation(AbstractMessage):

    def __init__(self, host, port, data):
        super().__init__(host=host, port=port, data=data, type='notify_update_of_vector_clock')
        # self.vector_clock = vector_clock
        # self.orchestrator_sender_id = orchestrator_sender_id

    # def process_by_command_line(self):
    #     self.current_server.orchestrator.wait_before_notification(self.vector_clock, self.orchestrator_sender_id)

