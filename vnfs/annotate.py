from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, vfx

from communication_entities.messages.abstract_message import AbstractMessage
from entities.parameters.parameter_package import ParameterPackage
from entities.parameters.annotation import AnnotationParameters
from utilities.logger import log


class Annotate(AbstractMessage):

    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def process_package(source: str, parameters: AnnotationParameters):
        log.info(''.join(["SOURCE: ", source]))
        main_clip = VideoFileClip(source)
        log.info(''.join(["Parameters: Font size: ",
                          str(parameters.font_size),
                          " Text: ",
                          parameters.text,
                          " duration: ",
                          str(parameters.duration),
                          " color:",
                          parameters.color]))
        txt_clip = TextClip(parameters.text, fontsize=parameters.font_size, color=parameters.color)
        txt_clip = txt_clip.set_pos('center').set_duration(parameters.duration)
        video = CompositeVideoClip([main_clip, txt_clip])
        log.info(''.join(["Video processed correctly: "]))
        return video

    @staticmethod
    def process_by_script(main_clip):
        video = main_clip.fx(vfx.blackwhite).fx(vfx.painting).subclip(0, 10)
        txt_clip = TextClip("Test", fontsize=16, color='white')
        txt_clip = txt_clip.set_pos('center').set_duration(10)
        final_clip = CompositeVideoClip([video, txt_clip])
        return final_clip

    def process_by_message(self, parameter: ParameterPackage):
        annotation_parameter = parameter.annotation_parameter
        source = parameter.file_pack.get_vnf_name
        video = self.process_package(source, annotation_parameter)
        source_no_format = source[:-4]
        operation_name = "_annotate"
        self.save_video(video, source_no_format, parameter.file_pack.format, operation_name)
        return source_no_format + operation_name + parameter.file_pack.format
