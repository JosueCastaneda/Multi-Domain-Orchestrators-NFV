from moviepy.editor import VideoFileClip, vfx

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameters.parameter_package import ParameterPackage
from utilities.logger import log


class Painting(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source: str):
        log.info(''.join(["SOURCE: ", source]))
        main_clip = VideoFileClip(source)
        video = main_clip.fx(vfx.painting)
        return video

    def process_by_message(self, parameter: ParameterPackage):
        source = parameter.file_pack.get_vnf_name
        video = self.process_package(source)
        source_no_format = source[:-4]
        operation_name = "_painting"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format
