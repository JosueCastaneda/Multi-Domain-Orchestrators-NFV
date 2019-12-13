from moviepy.editor import VideoFileClip, vfx

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameter_package import ParameterPackage
from utilities.logger import log


class ResizeVideo(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source, param):
        log.info(''.join(["SOURCE: ", source]))
        resized_clip = (VideoFileClip(source).fx(vfx.resize, width=param.width, height=param.height))
        log.info(''.join(["Video processed correctly: "]))
        return resized_clip

    def process_by_message(self, parameter: ParameterPackage):
        resize_parameter = parameter.resize_parameter
        source = parameter.file_pack.get_vnf_name
        video = self.process_package(source, resize_parameter)
        source_no_format = source[:-4]
        operation_name = "_resize"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format