import time

class ParameterPackage:

    def __init__(self, file_pack, operations,
                 speed_factor=0, second="", audio_file="",
                 vnf_servers=None, annotation=None, crop=None, resize=None):
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
        # TODO: Update this time, it will be sent by the server to multiple clients
        self.processed_time = 0

    def increase_time(self):
        new_latest_time = time.time()
        self.processed_time += new_latest_time - self.latest_time
        self.latest_time = new_latest_time

    def increase_current_vnf(self):
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

