import os

from moviepy.editor import VideoFileClip

from communication.messages.abstract_message import AbstractMessage
from entities.parameter_crop_package import ParameterCropPackage


class Crop(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    def process_package(self, source: str, parameters: ParameterCropPackage):
        clip = VideoFileClip(source)
        clip_cropped = clip.subclip(parameters.initial_time, parameters.end_time)
        return clip_cropped

    def process_message(self):
        self.current_server.acknowledge_message(self.client_socket, "OK")

        video_file_name = self.current_server.read_video_package(self.data.file_pack, self.client_socket)
        video = self.process_package(os.getcwd() + "/" + video_file_name, self.data.crop_parameter)

        self.current_server.save_processed_video(video, self.data.file_pack.process_name, self.data.file_pack.format)

        self.current_server.send_video_to_client(self.data)

        self.terminate_connections()
