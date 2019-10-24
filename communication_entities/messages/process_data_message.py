import sys
sys.path.append('../')

from communication_entities.messages.abstract_message import AbstractMessage
from communication_entities.messages.data_video_message import DataVideoMessage
from entities.communication_entity_package import CommunicationEntityPackage
from utilities.logger import log
from utilities.message_type import MessageType
from vnfs.annotate import Annotate
from vnfs.black_white import BlackWhite
from vnfs.composite_four import CompositeFour
from vnfs.crop import Crop
from vnfs.fade_in import FadeIn
from vnfs.fade_out import FadeOut
from vnfs.invert_colors import InvertColors
from vnfs.mirror_X import MirrorX
from vnfs.mirror_Y import MirrorY
from vnfs.painting import Painting
from vnfs.resize_video import ResizeVideo
from vnfs.rotate import Rotate
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
        self.current_op_index = 0
        self.parameters = parameters

    def increase_operation_index(self):
        self.current_op_index += 1

    # TODO: Create a special class that handles this, so adding new types only changes a single file
    def create_message_type_by_operation(self, operation):
        # TODO: Change to polymorphism
        m1 = AbstractMessage(self.parameters)

        if operation == MessageType.ANNOTATE:
            m1 = Annotate(self.parameters)
        elif operation == MessageType.BLACK_WHITE:
            m1 = BlackWhite(self.parameters)
        elif operation == MessageType.COMPOSITE:
            m1 = CompositeFour(self.parameters)
        elif operation == MessageType.CROP:
            m1 = Crop(self.parameters)
        elif operation == MessageType.FADE_IN:
            m1 = FadeIn(self.parameters)
        elif operation == MessageType.FADE_OUT:
            m1 = FadeOut(self.parameters)
        elif operation == MessageType.INVERT_COLORS:
            m1 = InvertColors(self.parameters)
        elif operation == MessageType.MIRROR_X:
            m1 = MirrorX(self.parameters)
        elif operation == MessageType.MIRROR_Y:
            m1 = MirrorY(self.parameters)
        elif operation == MessageType.PAINTING:
            m1 = Painting(self.parameters)
        elif operation == MessageType.RESIZE:
            m1 = ResizeVideo(self.parameters)
        elif operation == MessageType.ROTATE:
            m1 = Rotate(self.parameters)
        elif operation == MessageType.SPEED_UP:
            m1 = SpeedUp(self.parameters)
        else:
            raise Exception('Type not supported. The value of operation was:{}'.format(operation))
        return m1

    def send_video_to_next_vnf_in_chain(self, new_file):
        log.info(''.join(["LEN SEND: ", str(len(self.parameters.vnf_servers)), " IDX: ", str(self.current_op_index)]))
        if len(self.parameters.vnf_servers) > self.current_op_index:
            vnf_server = self.parameters.vnf_servers[self.current_op_index]
            self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))
            self.increase_operation_index()
            new_message = ProcessDataMessage(self.parameters)
            new_message.current_op_index = self.current_op_index
            new_message.parameters.file_pack.name = new_file

            # First send the video with a channel
            message_prepare_data_transfer = DataVideoMessage(new_file)
            self.current_server.send_message(message_prepare_data_transfer)

            self.current_server.connect_to_another_server_virtual(CommunicationEntityPackage(vnf_server.host,
                                                                                             vnf_server.port + 1))

            filename = new_file
            f = open(filename, 'rb')
            l_buffer = f.read(1024)
            while l_buffer:
                self.current_server.send_virtual_channel.send(l_buffer)
                # log.info(''.join(['Sent ', repr(l_buffer)]))
                l_buffer = f.read(1024)
            f.close()

            log.info('Done sending')
            self.current_server.send_virtual_channel.send('Thank you for connecting'.encode())
            self.current_server.send_virtual_channel.close()

            log.info('Disconnecting old send channel')
            self.current_server.disconnect_send_channel()
            log.info('Connecting to new channel')
            self.current_server.connect_to_another_server(CommunicationEntityPackage(vnf_server.host, vnf_server.port))
            self.current_server.send_message(new_message)
            self.current_server.disconnect_send_channel()

    def process_by_command_line(self):
        log.info(''.join(["Current index: ", str(self.current_op_index)]))
        if len(self.parameters.operations) > self.current_op_index:
            operation = self.parameters.operations[self.current_op_index]
            log.info(''.join(["Operation of type: ", str(operation)]))
            m1 = self.create_message_type_by_operation(operation)
            new_file = m1.process_by_message(self.parameters)
            self.send_video_to_next_vnf_in_chain(new_file)
