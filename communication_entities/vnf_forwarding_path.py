class VnfForwardingPath:

    def __init__(self):
        self.identifier = 0
        self.name = ''
        self.virtual_network_functions = []
        self.current_operation_index = 0

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, value):
        self.identifier = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_virtual_network_functions(self):
        return self.virtual_network_functions

    def add_virtual_network_function(self, vnf):
        self.virtual_network_functions.append(vnf)

    def get_virtual_network_function_by_index(self, index):
        return self.virtual_network_functions[index]

    def get_virtual_network_function_by_current_index(self):
        return self.virtual_network_functions[self.current_operation_index]

    def get_virtual_network_function_by_name(self, name):
        for vnf in self.virtual_network_functions:
            if vnf['name'] == name:
                return vnf
        raise Exception('VNF with name {} was not found'.format(name))

    def update_virtual_network_function_by_name(self, name, value):
        for vnf in self.virtual_network_functions:
            if vnf['name'] == name:
                vnf = value
                return vnf
        raise Exception('VNF with name {} was not found'.format(name))

    def update_virtual_network_function_by_index(self, index, value):
        self.virtual_network_functions[index] = value
        return self.virtual_network_functions[index]

    def get_index(self):
        return self.current_operation_index

    def set_index(self, value):
        self.current_operation_index = value

    def increase_index(self):
        self.current_operation_index += 1

    def decrease_index(self):
        self.current_operation_index -= 1
        self.validate_and_set_index()

    def validate_and_set_index(self):
        if self.current_operation_index < 0:
            self.current_operation_index = 0

    def increase_index_by_value(self, value):
        self.current_operation_index += value

    def decrease_index_by_value(self, value):
        self.current_operation_index -= value
        self.validate_and_set_index()
