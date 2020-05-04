class JsonParser:

    def __init__(self):
        print('JsonParse')

    @staticmethod
    def parse_for_vnf_topology(line):
        index = line.find('--topology')
        index_image = line.find('--initial')
        sub_line = line[index + 11:index_image - 1]
        topology_array = sub_line.split(',')
        return topology_array

    @staticmethod
    def parse_for_ip_vnf(line):
        index = line.find('-h')
        index_image = line.find('-v')
        sub_line = line[index + 3:index_image - 1]
        return sub_line

    @staticmethod
    def parse_for_name_vnf(line):
        index = line.find('vnf_')
        index_image = line.find('python')
        sub_line = line[index:index_image - 2]
        return sub_line

    @staticmethod
    def parse_for_ip_orchestrator(line):
        index = line.find('-o')
        index_image = line.find('-q')
        sub_line = line[index + 3:index_image - 1]
        return sub_line

    @staticmethod
    def parse_for_port_orchestrator(line):
        index = line.find('-q')
        index_image = line.find('-n')
        sub_line = line[index + 3:index_image - 1]
        return sub_line

    @staticmethod
    def parse_for_port_vnf(line):
        index = line.find('-v')
        index_image = line.find('-o')
        sub_line = line[index + 3:index_image - 1]
        return sub_line

    @staticmethod
    def parse_for_data_center(line):
        index = line.find('-d')
        index_image = line.find('-n')
        sub_line = line[index + 3:index_image - 1]
        return sub_line

    @staticmethod
    def parse_for_name_vnf_data_center(line):
        index = line.find('-n')
        index_image = line.find('--image')
        sub_line = line[index + 3:index_image - 1]
        return sub_line

    @staticmethod
    def parse_for_ip_vnf_data_center(line):
        index = line.find('ip=')
        index_image = line.find('/24')
        sub_line = line[index + 3:index_image]
        return sub_line

    # TODO: Use a similar approach for all the other methods, to eliminate magic numbers
    @staticmethod
    def parse_for_services(line):
        index = line.find('--services')
        index_image = line.find('--initial')
        initial_index = len('--services') + 1
        sub_line = line[index + initial_index:index_image - 1]
        return sub_line
