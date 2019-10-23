from entities.parameters.resize import ResizeParameters
from entities.parameters.annotation import AnnotationParameters
from entities.parameters.crop import CropParameters
from entities.parameters.file_name import FileNameParameters
from entities.parameters.fade_out import FadeOutParameters
from entities.parameters.fade_in import FadeInParameters


class ParameterGenerator:

    def __init__(self, annotation=None, crop=None, fade_in=None, fade_out=None, file=None, resize=None):
        self.annotation = annotation
        self.crop = crop
        self.fade_in = fade_in
        self.fade_out = fade_out
        self.file = file
        self.resize = resize

    def generate_parameters(self):
        self.annotation = self.generate_annotate_parameter()
        self.crop = self.generate_crop_parameter()
        self.file = self.generate_file_parameter()

    def generate_annotate_parameter(self):
        if self.annotation:
            return AnnotationParameters(text=self.annotation['text'],
                                        font_size=int(self.annotation['font_size']),
                                        color=self.annotation['color'])

    def generate_crop_parameter(self):
        if self.crop:
            return CropParameters(initial_time=self.crop['initial_time'], end_time=self.crop['end_time'])

    def generate_fade_in_parameter(self):
        if self.fade_in:
            return FadeInParameters(duration=self.crop['duration'])

    def generate_fade_out_parameter(self):
        if self.fade_out:
            return FadeOutParameters(duration=self.crop['duration'])

    def generate_file_parameter(self):
        if self.file:
            filename_processed = self.file['filename_processed']
            return FileNameParameters(self.file['file_name'], self.file['format_file'], filename_processed)

    def generate_resize_parameter(self):
        if self.resize:
            return ResizeParameters(width=self.resize['width'], height=self.resize['height'])
