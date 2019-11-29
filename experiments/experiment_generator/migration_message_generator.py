import json
from utilities.json_parser import JsonParser


class MigrationMessageGenerator:

    def __init__(self, path, name_of_experiment):
        self.path = path
        self.name_experiment = name_of_experiment
        self.file_commands = open(self.path + 'migration_messages_' + self.name_experiment + '.sh', 'w+')
        self.migration_vnfs = []
        self.list_of_detailed_vnfs = []
        self.all_migration_vnfs_for_experiment = []
        self.list_datacenters_of_vnfs = []
        print('python message_factory.py -t migration -h 10.0.0.32 -p 5463 -n speed_up -m new -v none --vnf_port none')

    def generate(self):
        self.write_first_line_to_file()
        self.load_all_required_data()
        self.set_up_containers()
        self.write_new_line_to_file()
        self.set_up_migration_vnfs_docker()
        self.write_new_line_to_file()
        self.set_up_migration_messages()
        self.close_file()

    def set_up_containers(self):
        new_line = '\n'
        for mig_vnf in self.migration_vnfs:
            vnf = self.get_vnf_by_migration(mig_vnf)
            new_vnf = self.get_data_center(vnf)
            data_center = new_vnf['datacenter']
            vnf_name = vnf['name'] + '_new'
            new_ip = vnf['migration_vnf_ip']
            first_str = 'vim-emu compute start -d ' + data_center + ' -n ' + vnf_name + ' --image vnf_experiment'
            second_str = '--net \'(id=input,ip=' + new_ip + '/24)\''
            self.file_commands.write(first_str + second_str + new_line)

    def get_data_center(self, vnf):
        for data_center_vnf in self.list_datacenters_of_vnfs:
            if data_center_vnf['ip'] == vnf['ip']:
                return data_center_vnf
        return None

    def get_vnf_by_migration(self, mig_vnf):
        for vnf in self.list_of_detailed_vnfs:
            if vnf['ip'] == mig_vnf:
                return vnf
        return None

    def set_up_migration_vnfs_docker(self):
        new_line = '\n'
        for mig_vnf in self.migration_vnfs:
            vnf = self.get_vnf_by_migration(mig_vnf)
            name = vnf['name'] + '_new'
            ip = vnf['migration_vnf_ip']
            new_vnf = self.get_new_vnf_details(ip)
            orch_ip = vnf['orch_ip']
            orch_port = vnf['orch_port']
            topology = self.create_topology_from_vnf(new_vnf)
            services = vnf['services']
            initial = str(new_vnf['queue_p'][0])
            first_str = 'docker exec -it mn.' + name + ' python vnf_script.py -h ' + ip + ' -v 4437 -o ' + orch_ip
            second_str = ' -q ' + orch_port + ' -n ' + name + ' --topology ' + topology
            third_str = ' --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services ' + services
            fourth_str = ' --initial ' + initial + ' &'
            self.file_commands.write(first_str + second_str + third_str + fourth_str + new_line)

    def create_topology_from_vnf(self, vnf):
        str_test = str(vnf['delay']) \
                   + ',' \
                   + str(vnf['bandwidth']) \
                   + ',' \
                   + str(vnf['loss']) \
                   + ',' \
                   + str(vnf['jitter'])
        return str_test

    def get_new_vnf_details(self, ip):
        for new_vnf in self.all_migration_vnfs_for_experiment:
            if new_vnf['server'] == ip:
                return new_vnf
        return None

    def set_up_migration_messages(self):
        new_line = '\n'
        for vnf_migration in self.migration_vnfs:
            for vnf in self.list_of_detailed_vnfs:
                if vnf['ip'] == vnf_migration:
                    first_str = 'python message_factory.py -t migration -h ' + vnf['orch_ip'] + ' -p '+ vnf['orch_port']
                    second_str = ' -n ' + vnf['name'] + ' -m new -v none --vnf_port none'
                    self.file_commands.write(first_str + second_str + new_line)
                    break
            # self.write_new_line_to_file()
        print('Writing done!')

    def load_all_required_data(self):
        self.load_migration_vnfs()
        self.load_detailed_information_vnfs()
        self.load_data_centers()
        self.load_list_of_all_migration_vnfs()

    def load_data_centers(self):
        file_container = open(self.path + 'containers_vnfs.sh', 'r+')
        for line in file_container:
            if 'vim-emu' in line:
                vnf = dict()
                vnf['datacenter'] = JsonParser.parse_for_datacenter(line)
                vnf['name'] = JsonParser.parse_for_name_vnf_data_center(line)
                vnf['ip'] = JsonParser.parse_for_ip_vnf_data_center(line)
                self.list_datacenters_of_vnfs.append(vnf)
        file_container.close()

    def load_list_of_all_migration_vnfs(self):
        with open(self.path + 'migration_vnfs.json') as json_file:
            self.all_migration_vnfs_for_experiment = json.load(json_file)

    def load_migration_vnfs(self):
        with open(self.path + self.name_experiment + '.json') as json_file:
            raw_data = json.load(json_file)
            self.migration_vnfs = raw_data['migrating_vnfs']

    def load_detailed_information_vnfs(self):
        vnf_mig_list = self.get_vnf_info_migration()
        file_container = open(self.path + 'docker_commands_' + self.name_experiment+'.sh', 'r+')
        for line in file_container:
            if 'mn.vnf' in line:
                vnf = dict()
                vnf['name'] = JsonParser.parse_for_name_vnf(line)
                vnf['orch_ip'] = JsonParser.parse_for_ip_orchestrator(line)
                vnf['orch_port'] = JsonParser.parse_for_port_orchestrator(line)
                vnf['ip'] = JsonParser.parse_for_ip_vnf(line)
                vnf['port'] = JsonParser.parse_for_port_vnf(line)
                vnf['services'] = JsonParser.parse_for_services(line)
                vnf['migration_vnf_ip'] = self.get_migration_ip(vnf['ip'], vnf_mig_list)
                self.list_of_detailed_vnfs.append(vnf)
        file_container.close()

    def get_migration_ip(self, vnf_ip, vnf_mig_list):
        for mig_vnf in vnf_mig_list:
            if mig_vnf['server'] == vnf_ip:
                return mig_vnf['migration_vnf_ip']
        return None

    def get_vnf_info_migration(self):
        with open(self.path + 'vnf_info_migration.json') as json_file:
            raw_data = json.load(json_file)
            return raw_data['vnf']

    def write_new_line_to_file(self):
        new_line = '\n'
        self.file_commands.write(new_line)

    def write_first_line_to_file(self):
        header = '#!/bin/sh'
        new_line = '\n'
        self.file_commands.write(header + new_line)

    def close_file(self):
        self.file_commands.close()


# def main():
#     print('Begin')
#     length_of_vnfs = 4
#     video_definition = 480
#     name_of_experiment = 'experiment_0'
#     experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
#     exp = MigrationMessageGenerator(path=experiment_path, name_of_experiment=name_of_experiment)
#     exp.generate()
#
#
# if __name__ == '__main__':
#     main()
