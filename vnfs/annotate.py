import os

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

from communication.messages.abstract import AbstractMessage
from entities.parameter_annotation_package import ParameterAnnotationPackage


class Annotate(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    def process_package(self, source: str, parameters: ParameterAnnotationPackage):
        main_clip = VideoFileClip(source)
        txt_clip = TextClip(parameters.text, fontsize=parameters.font_size, color=parameters.color)
        txt_clip = txt_clip.set_pos('center').set_duration(parameters.duration)
        video = CompositeVideoClip([main_clip, txt_clip])
        return video

    def process_message(self):
        self.current_server.acknowledge_message(self.client_socket, "OK")

        video_file_name = self.current_server.read_video_package(self.data.file_pack, self.client_socket)
        video = self.process_package(os.getcwd() + "/" + video_file_name, self.data.annotation_parameter)

        self.current_server.save_processed_video(video, self.data.file_pack.process_name, self.data.file_pack.format)

        self.current_server.send_video_to_client(self.data)

        self.terminate_connections()
