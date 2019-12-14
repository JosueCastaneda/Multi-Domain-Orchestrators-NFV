from communication_entities.messages.abstract_message import AbstractMessage
from utilities.logger import *


class UpdateVnfInfoAfterInternalOperation(AbstractMessage):

    def __init__(self, data,
                 service_index,
                 vnf_index_to_change,
                 value_to_change,
                 new_value,
                 logical_clock,
                 wait_period,
                 name_vnf_to_update):
        super().__init__(data)
        self.current_server = None
        self.service_index = service_index
        self.vnf_index_to_change = vnf_index_to_change
        self.value_to_change = value_to_change
        self.new_value = new_value
        self.logical_clock = logical_clock
        self.wait_period = wait_period
        self.name_vnf_to_update = name_vnf_to_update

    def process_by_command_line(self):
        log.info("UpdateVnfInfoAfterInternalOperation...")
        self.current_server.orchestrator.update_vnf_info_timer(self.service_index,
                                                               self.vnf_index_to_change,
                                                               self.value_to_change,
                                                               self.new_value,
                                                               self.logical_clock,
                                                               self.wait_period,
                                                               self.name_vnf_to_update)
        # ack_msg = MigrationAckMessage(None)
        # self.current_server.send_message_to_socket(self.client_socket, ack_msg)