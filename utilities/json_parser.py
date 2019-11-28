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