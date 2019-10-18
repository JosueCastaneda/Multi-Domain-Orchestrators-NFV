import os

from moviepy.editor import VideoFileClip

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameter_crop_package import ParameterCropPackage
from entities.parameter_package import ParameterPackage
from utilities.logger import log


class Crop(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source: str, parameters: ParameterCropPackage):
        log.info(''.join(["SOURCE: ", source]))
        clip = VideoFileClip(source)
        clip_cropped = clip.subclip(parameters.initial_time, parameters.end_time)
        return clip_cropped

    def process_by_message(self, parameter: ParameterPackage):
        crop_parameter = parameter.crop_parameter
        source = parameter.file_pack.name
        video = self.process_package(source, crop_parameter)
        source_no_format = source[:-4]
        operation_name = "_crop"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format

    def process_by_command_line(self):
        self.current_server.acknowledge_message(self.client_socket, "OK")
        video_file_name = self.current_server.read_video_package(self.data.file_pack, self.client_socket)
        video = self.process_package(os.getcwd() + "/" + video_file_name, self.data.crop_parameter)
        self.current_server.save_processed_video(video, self.data.file_pack.process_name, self.data.file_pack.format)
        self.current_server.send_video_to_client(self.data)
        self.terminate_connections()
