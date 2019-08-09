import os
import socket
import sys

sys.path.append('../')

from vnfs.annotate import annotate
from vnfs.crop import crop
from vnfs.invert_colors import invert_colors
from vnfs.resize_video import resize_video
from vnfs.speed_up import speed_up_raw


class PackageProcessor:

    def __init__(self, data):
        self.data = data

    def process_video(self, parameters):
        pass

    def process_package(self, data: str, parameters):
        # Todo: Handle the selection of processing function with a pattern
        virtual_function = parameters.get_current_operation()
        full_name = os.getcwd() + "/" + self.data
        video = None

        if virtual_function == MessageType.ANNOTATE:
            video = annotate(full_name, parameters.annotation_parameter.text)
        elif virtual_function == MessageType.CROP:
            initial_time = parameters.crop_parameter.initial_time
            end_time = parameters.crop_parameter.end_time
            video = crop(full_name, initial_time, end_time)
        elif virtual_function == MessageType.INVERT_COLORS:
            video = invert_colors(full_name)
        elif virtual_function == MessageType.RESIZE:
            width = parameters.resize_parameter.width
            height = parameters.resize_parameter.height
            video = resize_video(full_name, width, height)
        elif virtual_function == MessageType.SPEED_UP:
            video = speed_up_raw(full_name, parameters.speed_factor)
        return video

        # TODO: The name of the package should be updated

    def read_video_package(client_socket: socket, file_pack):
        source_file_complete = file_pack.name + "_server" + file_pack.format
        # I need to ack the server
        buffer = client_socket.recv(1024)

        with open(source_file_complete, "wb") as video:
            while buffer:
                video.write(buffer)
                buffer = client_socket.recv(1024)

        return source_file_complete