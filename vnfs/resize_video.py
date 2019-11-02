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
