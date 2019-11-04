import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.data_video_message import DataVideoMessage
from entities.communication_entity_package import CommunicationEntityPackage
from entities.vnf_generator import VNFGenerator
from utilities.logger import log


class ProcessDataMessage(AbstractMessage):

    def __init__(self, parameters):
        super().__init__(None)
        self.current_server = None
        self.current_op_index = 0
        self.parameters = parameters
        self.vnf_server = None
        self.new_message = None

    def process_by_command_line(self):
        log.info(''.join(["Current index: ", str(self.current_op_index)]))
        if self.is_index_valid():
            operation = self.parameters.operations[self.current_op_index]
            # TODO: Deleteme Debugg operation
            self.debug_operation_ip()
            log.info(''.join(["Current operation of type: ", str(operation)]))
            m1 = self.create_message_type_by_operation(operation)
            new_file = m1.process_by_message(self.parameters)
            self.update_and_save_processing_time()
            self.send_video_to_next_vnf_in_chain(new_file)

    def debug_operation_ip(self):
        # Debug for the operation
        ip_index = 0
        for op in self.parameters.operations:
            log.info(''.join(["Operation : ", str(op), " IP: ", str(self.parameters.vnf_servers[ip_index])]))
            ip_index += 1

    def update_and_save_processing_time(self):
        self.parameters.increase_time()
        pickle.dump(self.parameters.processed_time, open('time_spent.p', 'wb'))

    def create_message_type_by_operation(self, operation):
        message_generator = VNFGenerator(operation, self.parameters)
        return message_generator.create_message_type_by_operation()

    def send_video_to_next_vnf_in_chain(self, new_file):
        log.info(''.join(["LEN SEND: ", str(len(self.parameters.vnf_servers)), " IDX: ", str(self.current_op_index)]))
        if self.still_need_to_process():
            vnf_server = self.get_new_vnf_in_chain()
            self.process_by_current_index(new_file, vnf_server)
            self.send_video_to_new_vnf(new_file)
            self.connect_to_virtual_channel_from_vnf(vnf_server)
            self.send_message_to_server(new_file)
            self.disconnect_current_channel()
            self.connect_to_new_channel(vnf_server, self.new_message)

    def is_index_valid(self):
        return len(self.parameters.operations) > self.current_op_index

    def still_need_to_process(self):
        return len(self.parameters.vnf_servers) > self.current_op_index

    def get_new_vnf_in_chain(self):
        return self.parameters.vnf_servers[self.current_op_index]

    def process_by_current_index(self, new_file, vnf_server):
        self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))
        self.increase_operation_index()
        self.new_message = ProcessDataMessage(self.parameters)
        self.new_message.current_op_index = self.current_op_index
        self.new_message.parameters.file_pack.name = new_file

    def increase_operation_index(self):
        operation = self.parameters.operations[self.current_op_index]
        log.info(''.join(['Increasing current operation index', 'Operation: ', str(operation)]))
        self.current_op_index += 1
        log.info(''.join(['New operation index', 'Operation: ', str(operation)]))

    def send_video_to_new_vnf(self, new_file):
        message_prepare_data_transfer = DataVideoMessage(new_file)
        self.current_server.send_message(message_prepare_data_transfer)

    def connect_to_virtual_channel_from_vnf(self, vnf_server):
        self.current_server.connect_to_another_server_virtual(CommunicationEntityPackage(vnf_server.host,
                                                                                         vnf_server.port + 1))

    # TODO: Check why the enumeration does not work and change the magic number
    def send_message_to_server(self, new_file):
        filename = new_file
        f = open(filename, 'rb')
        l_buffer = f.read(1024)
        while l_buffer:
            self.current_server.send_virtual_channel.send(l_buffer)
            l_buffer = f.read(1024)
        f.close()
        log.info('Done sending')

    def disconnect_current_channel(self):
        self.current_server.send_virtual_channel.send('Thank you for connecting'.encode())
        self.current_server.send_virtual_channel.close()
        log.info('Disconnecting old send channel')
        self.current_server.disconnect_send_channel()

    def connect_to_new_channel(self, vnf_server, new_message):
        log.info('Connecting to new channel')
        self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))
        self.current_server.send_message(new_message)
        self.current_server.disconnect_send_channel()