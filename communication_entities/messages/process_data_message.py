import pickle

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.data_video_message import DataVideoMessage
from communication_entities.messages.queue_processing.all_queue_information import AllQueueInformation
from entities.communication_entity_package import CommunicationEntityPackage
from entities.vnf_entities.vnf_generator import VNFGenerator
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
            # TODO: Delete debugging operation
            self.debug_operation_ip()
            log.info(''.join(["Current operation of type: ", str(operation)]))
            m1 = self.create_message_type_by_operation(operation)
            new_file = m1.process_by_message(self.parameters)
            self.update_time_and_save_all_queues_and_processing_time()
            self.increase_operation_index()
            if self.still_need_to_process():
                next_vnf_in_chain = self.get_new_vnf_in_chain()
                self.connect_to_new_server(next_vnf_in_chain)
                self.connect_to_virtual_channel_from_vnf(next_vnf_in_chain)
                self.send_information_to_next_vnf_in_chain(new_file)
                self.disconnect_current_channel()
                self.connect_to_new_channel(next_vnf_in_chain, self.new_message)

    def update_time_and_save_all_queues_and_processing_time(self):
        self.parameters.increase_time()
        self.save_processing_time()
        self.save_queue_to_file()

    def save_processing_time(self):
        name_no_format = self.parameters.file_pack.get_vnf_name[:-4]
        pickle.dump(self.parameters.processed_time, open(name_no_format + '_time_spent.p', 'wb'))

    def save_queue_to_file(self):
        name_no_format = self.parameters.file_pack.get_vnf_name[:-4]
        data_queue = self.current_server.orchestrator.configuration.state.get_all_queue_data()
        # data_queue = self.current_server.orchestrator.get_all_queue_data()
        pickle.dump(data_queue, open(name_no_format + '_queue.p', 'wb'))

    def create_message_type_by_operation(self, operation):
        message_generator = VNFGenerator(operation, self.parameters)
        return message_generator.create_message_type_by_operation()

    def send_information_to_next_vnf_in_chain(self, new_file):
        log.info(''.join(["LEN SEND: ", str(len(self.parameters.vnf_servers)), " IDX: ", str(self.current_op_index)]))
        self.generate_new_message(new_file)
        # self.send_all_queues_to_new_vnf()
        self.send_data_message_video_to_new_vnf(new_file)
        self.send_video_to_next_vnf_in_chain(new_file)

    def send_all_queues_to_new_vnf(self):
        log.info('Sending all the queue information to the next VNF in the chain')
        data_queue = self.current_server.orchestrator.configuration.state.get_all_queue_data()
        message_all_queue = AllQueueInformation(data_queue)
        self.current_server.send_message(message_all_queue)
        self.current_server.get_ack_channel()
        log.info('Finish sending all the queue information!')

    def is_index_valid(self):
        return len(self.parameters.operations) >= self.current_op_index

    def still_need_to_process(self):
        return len(self.parameters.vnf_servers) > self.current_op_index

    def get_new_vnf_in_chain(self):
        return self.parameters.vnf_servers[self.current_op_index]

    def connect_to_new_server(self, vnf_server):
        self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))

    def generate_new_message(self, new_file):
        self.new_message = ProcessDataMessage(self.parameters)
        self.new_message.current_op_index = self.current_op_index
        self.new_message.parameters.file_pack.get_vnf_name = new_file

    def increase_operation_index(self):
        # TODO: Remove, only for debugging purposes
        operation = self.parameters.operations[self.current_op_index]
        log.info(''.join(['Increasing current operation index', 'Operation: ', str(operation)]))
        self.current_op_index += 1
        # TODO: Remove, only for debugging purposes
        if len(self.parameters.operations) > self.current_op_index:
            operation = self.parameters.operations[self.current_op_index]
            log.info(''.join(['New operation index', 'Operation: ', str(operation)]))

    def send_data_message_video_to_new_vnf(self, new_file):
        log.info('Sending DataVideoMessage to next VNF in chain')
        data_queue = self.current_server.orchestrator.configuration.state.get_all_queue_data()
        message_prepare_data_transfer = DataVideoMessage(new_file, data_queue)
        self.current_server.send_message(message_prepare_data_transfer)
        log.info('Finish sending DataVideoMessage to next VNF in chain')

    def connect_to_virtual_channel_from_vnf(self, vnf_server):
        self.current_server.connect_to_another_server_virtual(CommunicationEntityPackage(vnf_server.host,
                                                                                         vnf_server.port + 1))

    # TODO: Check why the enumeration does not work and change the magic number
    def send_video_to_next_vnf_in_chain(self, new_file):
        log.info('Sending serialized video as bytes...')
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

    def debug_operation_ip(self):
        # Debug for the operation
        log.info(''.join(["# Operations : ", str(len(self.parameters.operations))]))
        for op in self.parameters.operations:
            log.info(''.join(["Operation : ", str(op)]))

        log.info(''.join(["# Servers : ", str(len(self.parameters.vnf_servers))]))
        for vnf in self.parameters.vnf_servers:
            log.info(''.join(['IP: ', str(vnf.host)]))
