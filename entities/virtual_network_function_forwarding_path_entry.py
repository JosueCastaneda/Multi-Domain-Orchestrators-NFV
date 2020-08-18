class VirtualNetworkFunctionForwardingPathEntry:

    def __init__(self, name, first_connection_point, second_connection_point):
        self.vnf_name = name
        self.first_connection_point = first_connection_point
        self.second_connection_point = second_connection_point

    def get_name(self):
        return self.vnf_name

    def set_name(self, value):
        self.vnf_name = value

    def get_first_connection_point(self):
        return self.first_connection_point

    def set_first_connection_point(self, value):
        self.first_connection_point = value

    def get_second_connection_point(self):
        return self.first_connection_point

    def set_second_connection_point(self, value):
        self.first_connection_point = value
