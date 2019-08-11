import os

from moviepy.editor import VideoFileClip, vfx

from communication.messages.abstract import AbstractMessage


class InvertColors(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    def process_package(self, source):
        inverted_clip = (VideoFileClip(source).fx(vfx.invert_colors))
        return inverted_clip

    def process_message(self):
        self.current_server.acknowledge_message(self.client_socket, "OK")

        video_file_name = self.current_server.read_video_package(self.data.file_pack, self.client_socket)
        video = self.process_package(os.getcwd() + "/" + video_file_name)

        self.current_server.save_processed_video(video, self.data.file_pack.process_name, self.data.file_pack.format)

        self.current_server.send_video_to_client(self.data)

        self.terminate_connections()
