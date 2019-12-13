from moviepy.editor import VideoFileClip, vfx

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameter_package import ParameterPackage
from utilities.logger import log


class SpeedUp(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source: str, factor: int):
        log.info(''.join(["SOURCE: ", source]))
        speed_clip = (VideoFileClip(source).fx(vfx.speedx, factor=factor))
        return speed_clip

    def process_by_message(self, parameter: ParameterPackage):
        source = parameter.file_pack.get_vnf_name
        factor = parameter.speed_factor
        video = self.process_package(source, factor)
        source_no_format = source[:-4]
        operation_name = "_speed_up"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format
