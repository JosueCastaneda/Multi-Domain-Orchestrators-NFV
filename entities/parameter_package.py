import time


# TODO: Refactor this class, it has many responsibilities and bloated construction
class ParameterPackage:

    def __init__(self, file_pack=None,
                 operations=None,
                 speed_factor=0,
                 second="",
                 audio_file="",
                 vnf_servers=None,
                 annotation=None,
                 crop=None,
                 resize=None,
                 vnf_name="",
                 topology=None,
                 fade_in=None,
                 fade_out=None):
        self.file_pack = file_pack
        self.operations = operations
        self.vnf_servers = vnf_servers
        self.current_vnf_index = 0
        self.speed_factor = speed_factor
        self.second = second
        self.audio_file = audio_file
        self.annotation_parameter = annotation
        self.crop_parameter = crop
        self.resize_parameter = resize
        # Current time when this package was generated
        self.latest_time = time.time()
        self.processed_time = 0
        self.vnf_name = vnf_name
        self.topology = topology
        self.fade_in_parameter = fade_in
        self.fade_out_parameter = fade_out

    def increase_time(self):
        new_latest_time = time.time()
        self.processed_time += new_latest_time - self.latest_time
        self.latest_time = new_latest_time

    def increase_current_vnf(self):
        if len(self.vnf_servers) > self.current_vnf_index + 1:
            self.current_vnf_index += 1

    def get_current_vnf_server(self):
        return self.vnf_servers[self.current_vnf_index]

    def get_current_operation(self):
        return self.operations[self.current_vnf_index]

    def set_annotation_parameter(self, annotation_pack):
        self.annotation_parameter = annotation_pack

    def set_crop_parameter(self, crop_pack):
        self.crop_parameter = crop_pack

    def set_resize_parameter(self, resize_pack):
        self.resize_parameter = resize_pack

    def set_fade_in_parameter(self, fade_in_pack):
        self.fade_in_parameter = fade_in_pack

    def set_fade_out_parameter(self, fade_out_pack):
        self.fade_out_parameter = fade_out_pack
