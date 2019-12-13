import os

from moviepy.editor import VideoFileClip

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameter_package import ParameterPackage
from entities.parameters.crop import CropParameters
from utilities.logger import log


class Crop(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source: str, parameters: CropParameters):
        log.info(''.join(["SOURCE: ", source]))
        clip = VideoFileClip(source)
        clip_cropped = clip.subclip(parameters.initial_time, parameters.end_time)
        return clip_cropped

    def process_by_message(self, parameter: ParameterPackage):
        crop_parameter = parameter.crop_parameter
        source = parameter.file_pack.get_vnf_name
        video = self.process_package(source, crop_parameter)
        source_no_format = source[:-4]
        operation_name = "_crop"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format