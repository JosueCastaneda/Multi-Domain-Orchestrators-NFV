from entities.parameter_package import ParameterPackage
from utilities.logger import log


class AbstractMessage:
    """
        This class represents a generic message, all messages
        have the process_message function and override it with
        their own implementation
    """
    def __init__(self, data, client=None, source_server=None):
        self.data = data
        self.client = client
        self.source_server = source_server
        self.current_server = None
        self.client_socket = None
        self.client_address = None
        self.test_server = None

    def process_message(self):
        pass

    def process_with_parameters(self, parameter: ParameterPackage):
        pass

    def parse_name(self, name: str):
        is_format = name[-4:]
        if is_format == ".mp4" or is_format == ".webm":
            return name[:-4]
        return name

    def save_video(self, video, name: str, format_file="", operation=""):
        name = self.parse_name(name)
        if format_file == ".mp4":
            self.transcoder_mp4(video, name + operation)
        elif format_file == ".webm":
            self.transcoder_web(video, name + operation)

    def transcoder_mp4(self, source_clip, name):
        source_clip.write_videofile(name + ".mp4")
        log.info(''.join(["File ", name, " saved!"]))

    def transcoder_web(self, source_clip, name):
        source_clip.write_videofile(name + ".webm")
        log.info(''.join(["File ", name, " saved!"]))

    def terminate_connections(self):
        self.client_socket.close()
        self.current_server.disconnect_send_channel()
