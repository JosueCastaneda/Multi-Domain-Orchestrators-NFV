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


class VNFGenerator:

    def __init__(self, operation, parameters):
        print('Hello')
        self.operation = operation
        self.parameters = parameters

    def create_message_type_by_operation(self):
        if self.operation == MessageType.ANNOTATE:
            m1 = Annotate(self.parameters)
        elif self.operation == MessageType.BLACK_WHITE:
            m1 = BlackWhite(self.parameters)
        elif self.operation == MessageType.COMPOSITE:
            m1 = CompositeFour(self.parameters)
        elif self.operation == MessageType.CROP:
            m1 = Crop(self.parameters)
        elif self.operation == MessageType.FADE_IN:
            m1 = FadeIn(self.parameters)
        elif self.operation == MessageType.FADE_OUT:
            m1 = FadeOut(self.parameters)
        elif self.operation == MessageType.INVERT_COLORS:
            m1 = InvertColors(self.parameters)
        elif self.operation == MessageType.MIRROR_X:
            m1 = MirrorX(self.parameters)
        elif self.operation == MessageType.MIRROR_Y:
            m1 = MirrorY(self.parameters)
        elif self.operation == MessageType.PAINTING:
            m1 = Painting(self.parameters)
        elif self.operation == MessageType.RESIZE:
            m1 = ResizeVideo(self.parameters)
        elif self.operation == MessageType.ROTATE:
            m1 = Rotate(self.parameters)
        elif self.operation == MessageType.SPEED_UP:
            m1 = SpeedUp(self.parameters)
        else:
            raise Exception('Type not supported. The value of operation was:{}'.format(self.operation))
        return m1
