import os

from moviepy.editor import VideoFileClip, vfx

from communication_entities.messages.abstract_message import AbstractMessage


class ResizeVideo(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source, param):
        resized_clip = (VideoFileClip(source).fx(vfx.resize, width=param.width, height=param.height))
        return resized_clip

    # def process_by_command_line(self):
    #     self.current_server.acknowledge_message(self.client_socket, "OK")
    #
    #     video_file_name = self.current_server.read_video_package(self.data.file_pack, self.client_socket)
    #     video = self.process_package(os.getcwd() + "/" + video_file_name, self.data.resize_parameter)
    #
    #     self.current_server.save_processed_video(video, self.data.file_pack.process_name, self.data.file_pack.format)
    #
    #     self.current_server.send_video_to_client(self.data)
    #
    #     self.terminate_connections()
