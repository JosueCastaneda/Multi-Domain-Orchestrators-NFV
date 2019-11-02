import os

from moviepy.editor import VideoFileClip, vfx

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameter_package import ParameterPackage
from entities.parameters.fade_in import FadeInParameters
from utilities.logger import log


class FadeIn(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source: str, parameters: FadeInParameters):
        log.info(''.join(["SOURCE: ", source]))
        main_clip = VideoFileClip(source)
        video = main_clip.fx(vfx.fadein, parameters.duration)
        return video

    def process_by_message(self, parameter: ParameterPackage):
        annotation_parameter = parameter.fade_in_parameter
        source = parameter.file_pack.name
        video = self.process_package(source, annotation_parameter)
        source_no_format = source[:-4]
        operation_name = "_fadeIn"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format

    # def process_by_command_line(self):
    #     self.current_server.acknowledge_message(self.client_socket, "OK")
    #     video_file_name = self.current_server.read_video_package(self.data.file_pack, self.client_socket)
    #     video = self.process_package(os.getcwd() + "/" + video_file_name, self.data.fade_in_parameter)
    #     self.current_server.save_processed_video(video, self.data.file_pack.process_name, self.data.file_pack.format)
    #     self.current_server.send_video_to_client(self.data)
    #     self.terminate_connections()
