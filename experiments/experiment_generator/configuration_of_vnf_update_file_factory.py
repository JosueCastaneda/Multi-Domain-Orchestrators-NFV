import json


class ConfigurationOfVnfUpdateFileFactory:

    def __init__(self, configuration, path):
        self.configuration = configuration
        self.path = path

    def create_file_for_internal_update(self):
        entry = dict()
        entry['service_index'] = self.configuration.service_index
        entry['vnf_index_to_change'] = self.configuration.vnf_index_to_change
        entry['value_to_change'] = self.configuration.value_to_change
        entry['new_value'] = self.configuration.new_value
        entry['name_vnf_to_update'] = self.configuration.name_vnf_to_update
        entry['hosts'] = self.add_hosts_to_internal_update()

    def add_hosts_to_internal_update(self):
        hosts = []
        for i in range(self.configuration.number_of_hosts):
            entry_host = dict()
            entry_host['host'] = self.configuration.list_hosts[i]
            entry_host['port'] = self.configuration.list_ports[i]
            entry_host['seed'] = self.configuration.list_seeds[i]
            hosts.append(entry_host)
        return hosts

    def save_message_for_internal_update(self, data):
        with open(self.path, 'w') as write_file:
            json.dump(data, write_file)
