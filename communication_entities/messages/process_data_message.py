from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.data_video_message import DataVideoMessage
from entities.communication_entity_package import CommunicationEntityPackage
from utilities.logger import log
from utilities.message_type import MessageType
from vnfs.annotate import Annotate
from vnfs.crop import Crop
from vnfs.invert_colors import InvertColors
from vnfs.resize_video import ResizeVideo
from vnfs.speed_up import SpeedUp


class ProcessDataMessage(AbstractMessage):
    """
        The message sent to the a VNF to process the data specified in the operation
    """

    def __init__(self, parameters):
        """
        Set up the message
        :param parameters: An object that contains all the required parameters to process the video
        """
        super().__init__(None)
        self.current_server = None
        self.current_operation_index = 0
        self.parameters = parameters

    def increase_operation_index(self):
        self.current_operation_index += 1

    def create_message_type_by_operation(self, operation):
        # TODO: Change to polymorphism
        m1 = AbstractMessage(self.parameters)

        if operation == MessageType.ANNOTATE:
            m1 = Annotate(self.parameters)
        elif operation == MessageType.RESIZE:
            m1 = ResizeVideo(self.parameters)
        elif operation == MessageType.CROP:
            m1 = Crop(self.parameters)
        elif operation == MessageType.INVERT_COLORS:
            m1 = InvertColors(self.parameters)
        elif operation == MessageType.SPEED_UP:
            m1 = SpeedUp(self.parameters)

        return m1

    # TODO: Working on this
    def send_video_to_next_vnf_in_chain(self, new_file):
        log.info("LEN SEND: ", len(self.parameters.vnf_servers), " IDX: ", self.current_operation_index)
        if len(self.parameters.vnf_servers) > self.current_operation_index:
            vnf_server = self.parameters.vnf_servers[self.current_operation_index]
            self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))
            self.increase_operation_index()
            new_message = ProcessDataMessage(self.parameters)
            new_message.current_operation_index = self.current_operation_index
            new_message.parameters.file_pack.name = new_file

            # First send the video with a channel
            message_prepare_data_transfer = DataVideoMessage(new_file)
            self.current_server.send_message(message_prepare_data_transfer)

            self.current_server.connect_to_another_server_virtual(CommunicationEntityPackage(vnf_server.host,
                                                                                             vnf_server.port + 1))

            self.current_server.send_virtual_channel.send("Hello server!".encode())
            filename = new_file
            f = open(filename, 'rb')
            l_buffer = f.read(1024)
            while l_buffer:
                self.current_server.send_virtual_channel.send(l_buffer)
                log.info('Sent ', repr(l_buffer))
                l_buffer = f.read(1024)
            f.close()

            log.info('Done sending')
            self.current_server.send_virtual_channel.send('Thank you for connecting'.encode())
            self.current_server.send_virtual_channel.close()

            self.current_server.disconnect_send_channel()
            self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))
            self.current_server.send_message(new_message)
            self.current_server.disconnect_send_channel()

    def process_message(self):
        log.info("Current index: ", self.current_operation_index)
        if len(self.parameters.operations) > self.current_operation_index:
            operation = self.parameters.operations[self.current_operation_index]
            m1 = self.create_message_type_by_operation(operation)
            new_file = m1.process_with_parameters(self.parameters)
            self.send_video_to_next_vnf_in_chain(new_file)
