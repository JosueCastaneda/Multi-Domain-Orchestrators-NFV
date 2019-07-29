class ParameterPackage:

    def __init__(self, file_pack, operation,
                 speed_factor=0, second="", audio_file="",
                 new_client=None, new_server=None, annotation=None, crop=None, resize=None):
        self.file_pack = file_pack
        self.operation = operation
        self.new_client = new_client
        self.new_server = new_server
        self.speed_factor = speed_factor
        self.second = second
        self.audio_file = audio_file
        self.annotation_parameter = annotation
        self.crop_parameter = crop
        self.resize_parameter = resize

    def set_annotation_parameter(self, annotation_pack):
        self.annotation_parameter = annotation_pack

    def set_crop_parameter(self, crop_pack):
        self.crop_parameter = crop_pack

    def set_resize_parameter(self, resize_pack):
        self.resize_parameter = resize_pack

