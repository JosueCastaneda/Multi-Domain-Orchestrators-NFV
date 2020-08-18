import datetime
import json

from utilities.json_parser import JsonParser


class JsonLoader:

    def __init__(self, experiment_path, experiment_name):
        self.experiment_path = experiment_path
        self.experiment_name = experiment_name

    def load_service_information(self):
        with open(self.experiment_path + self.experiment_name + '.json') as json_file:
            raw_data = json.load(json_file)
            service_list = raw_data['services']
            migrating_vnf_list = raw_data['migrating_vnfs']
            return service_list, migrating_vnf_list

    def load_detailed_vnf_information(self):
        with open(self.experiment_path + 'vnf_info_migration' + '.json') as json_file:
            raw_data = json.load(json_file)
            return raw_data['vnf']

    def load_list_of_migration_vnfs(self):
        with open(self.experiment_path + 'migration_vnfs' + '.json') as json_file:
            return json.load(json_file)

    def load_list_of_vnf_topology(self):
        str_name = ''.join([self.experiment_path, 'docker_commands_', self.experiment_name, '.sh'])
        file_docker = open(str_name, 'r')
        list_of_vnf_topology = []
        for line in file_docker:
            if 'mn.vnf_' in line:
                vnf = dict()
                vnf['ip'] = JsonParser.parse_for_ip_vnf(line)
                vnf['topology'] = JsonParser.parse_for_vnf_topology(line)
                list_of_vnf_topology.append(vnf)
        return list_of_vnf_topology


def my_date_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
