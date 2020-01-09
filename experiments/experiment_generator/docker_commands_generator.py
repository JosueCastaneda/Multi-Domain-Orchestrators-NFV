import random
import json
from utilities.random_integer_generation import generate_random_integer


class DockerCommandsGenerator:

    # TODO: Update the constructor to use a single object instead of multiple variables
    def __init__(self, path, delay, bandwidth, loss, jitter, name_of_experiment, length_of_vnfs):
        self.path = path
        self.list_orchestrator = list()
        self.vnf_list_detailed = []
        self.vnf_container_list = []
        self.detailed_services = []
        self.vnf_list_detailed_migration = []
        self.list_of_migrating_vnfs_detail = []
        self.delay_low = delay[0]
        self.delay_high = delay[1]
        self.bandwidth_low = bandwidth[0]
        self.bandwidth_high = bandwidth[1]
        self.loss_low = loss[0]
        self.loss_high = loss[1]
        self.jitter_low = jitter[0]
        self.jitter_high = jitter[1]
        self.name_experiment = name_of_experiment
        self.length_of_vnfs = length_of_vnfs
        self.file_orchestrator = open(self.path + 'containers_orchestrator.sh', 'r+')
        self.file_commands = open(self.path + 'docker_commands_' + self.name_experiment + '.sh', 'w+')
        self.seeds = None
        random.seed(5)

    def generate_commands(self):
        self.write_first_line_to_file()
        self.load_all_required_data()
        self.set_up_run_orchestrators()
        self.write_new_line_to_file()
        self.set_up_chain_orchestrators()
        self.write_new_line_to_file()
        self.set_up_running_vnf()
        self.write_new_line_to_file()
        self.add_vnf_chains()
        self.write_new_line_to_file()
        self.set_up_running_vnf_unique()
        self.write_new_line_to_file()
        self.add_request_of_updates()
        self.close_file()

    def load_all_required_data(self):
        self.load_list_vnf()
        self.load_container_information()
        self.load_services()
        self.load_list_vnf_migration()
        self.load_list_of_migrating_vnfs_detail()
        self.load_seeds()

    def set_up_run_orchestrators(self):
        new_line = '\n'
        for line in self.file_orchestrator:
            if line:
                name_orchestrator = self.parse_for_name_orchestrator(line)
                orch_ip = self.parse_for_ip_orchestrator(line)
                self.list_orchestrator.append([name_orchestrator, orch_ip])
                first_string = 'docker exec -it mn.' + name_orchestrator + 'python orchestrator_script.py -h ' + orch_ip
                second_string = ' -p 5461 -n ' + name_orchestrator + ' --path ' + self.path[2:]
                third_string = ' --experiment_name ' + self.name_experiment+'.json ' + ' &'
                self.file_commands.write(first_string + second_string + third_string + new_line)
        print('Finish set up run orchestrator')

    # TODO: Need to get all other orchestrators and send
    def set_up_chain_orchestrators(self):
        print('Chaining')
        new_line = '\n'
        for index in range(len(self.list_orchestrator)):
            current_orchestrator = self.list_orchestrator[index]
            for i in range(len(self.list_orchestrator)):
                if i != index:
                    other_orch = self.list_orchestrator[i]
                    first_string = 'docker exec -it mn.source python message_factory.py -t add_orchestrator -h '
                    second_string = current_orchestrator[1] + ' -p 5461 -n none -m none --vnf_host ' + other_orch[1]
                    third_string = ' --vnf_port 5461'
                    self.file_commands.write(first_string + second_string + third_string + new_line)

    def write_new_line_to_file(self):
        new_line = '\n'
        self.file_commands.write(new_line)

    def set_up_running_vnf(self):
        print('Running VNF')
        new_line = '\n'
        for vnf in self.vnf_container_list:
            index = self.generate_random_indexes() - 1
            orch_ip = self.list_orchestrator[index][1]
            operation = vnf['name'][4:]
            detailed_vnf = self.get_vnf_detailed_information(operation)
            vnf_topology = self.generate_topology()
            migration_ip = self.generate_migration_ip(detailed_vnf['server'])
            migration_ip_topology = self.generate_migration_ip_topology(migration_ip)
            services = self.generate_services()
            vnf_initial = str(detailed_vnf['queue_p'][0])
            first_str = 'docker exec -it mn.' + vnf['name'] + ' python vnf_script.py -h ' + vnf['ip'] + ' -v 4437 -o ' + orch_ip
            second_str = ' -q 5461 -n ' + vnf['name'] + ' --topology ' + vnf_topology + ' --migration_ip ' + migration_ip
            third_str = ' --migration_topology ' + migration_ip_topology + ' --services ' + services
            fourth_str = ' --initial ' + vnf_initial + ' &'
            self.file_commands.write(first_str + second_str + third_str + fourth_str + new_line)

    def set_up_running_vnf_unique(self):
        print('Running VNF')
        new_line = '\n'
        index = self.generate_random_indexes() - 1
        orch_ip = self.list_orchestrator[index][1]
        for vnf in self.vnf_container_list:
            operation = vnf['name'][4:]
            detailed_vnf = self.get_vnf_detailed_information(operation)
            vnf_topology = self.generate_topology()
            migration_ip = self.generate_migration_ip(detailed_vnf['server'])
            migration_ip_topology = self.generate_migration_ip_topology(migration_ip)
            services = self.generate_services()
            vnf_initial = str(detailed_vnf['queue_p'][0])
            first_str = 'docker exec -it mn.' + vnf['name'] + ' python vnf_script.py -h ' + vnf['ip'] + ' -v 4437 -o ' + orch_ip
            second_str = ' -q 5461 -n ' + vnf['name'] + ' --topology ' + vnf_topology + ' --migration_ip ' + migration_ip
            third_str = ' --migration_topology ' + migration_ip_topology + ' --services ' + services
            fourth_str = ' --initial ' + vnf_initial + ' &'
            self.file_commands.write(first_str + second_str + third_str + fourth_str + new_line)


    def generate_random_indexes(self):
        return random.randint(1, len(self.list_orchestrator))

    def generate_migration_ip(self, vnf_ip):
        for vnf in self.vnf_list_detailed_migration:
            if vnf['server'] == vnf_ip:
                return vnf['migration_vnf_ip']
        return None

    def generate_services(self):
        constraints_of_services = []
        for service in self.detailed_services:
            constraints_of_services.append(str(service['constraints']['delay']))
            constraints_of_services.append(str(service['constraints']['bandwidth']))
            constraints_of_services.append(str(service['constraints']['loss']))
            constraints_of_services.append(str(service['constraints']['jitter']))
        x = ','.join(constraints_of_services)
        return x

    def generate_migration_ip_topology(self, vnf_ip):
        vnf_topology = dict()
        for vnf in self.list_of_migrating_vnfs_detail:
            if vnf['server'] == vnf_ip:
                vnf_topology['delay'] = vnf['delay']
                vnf_topology['loss'] = vnf['loss']
                vnf_topology['jitter'] = vnf['jitter']
                vnf_topology['bandwidth'] = vnf['bandwidth']
                str_topology = str(vnf_topology['delay']) \
                               + ',' \
                               + str(vnf_topology['bandwidth']) \
                               + ',' \
                               + str(vnf_topology['loss']) \
                               + ',' \
                               + str(vnf_topology['jitter'])
                return str_topology
        return ''

    def add_vnf_chains(self):
        print('Setting chains VNF')
        new_line = '\n'
        for service in self.detailed_services:
            for i in range(0, self.length_of_vnfs - 1):
                first_ip, second_ip = self.get_pair_of_ip(service, i)
                first_str = 'docker exec -it mn.source python message_factory.py -t add_chain -h ' + first_ip
                second_str = ' -p 4437 -n none -m none -v ' + second_ip + ' --vnf_port 4437'
                self.file_commands.write(first_str + second_str + new_line)
            self.write_new_line_to_file()
        print('Chaining Done!')

    def add_request_of_updates(self):
        print('Setting up updates')
        new_line = '\n'
        for i in range(0, len(self.seeds)):
            random_seed = self.seeds[i]
            random_vnf_ip = self.get_random_vnf_ip(random_seed)
            first_str = 'docker exec -it mn.source python message_factory.py -t request_update -h ' + random_vnf_ip
            second_str = ' -p 4437 -n none -m none --vnf_host none --vnf_port none --seed ' + str(random_seed)
            self.file_commands.write(first_str + second_str + new_line)
        self.write_new_line_to_file()
        print('Setting done!')

    # TODO: Complete this function
    def add_internal_updates_information(self):
        pass

    def get_random_vnf_ip(self, seed):
        random.seed(seed)
        random_index = random.randint(0, len(self.vnf_container_list) - 1)
        return self.vnf_container_list[random_index]['ip']

    def get_pair_of_ip(self, service, index):
        first_ip = service['host_servers'][self.length_of_vnfs - index - 1]
        second_ip = service['host_servers'][self.length_of_vnfs - index - 2]
        return first_ip, second_ip

    def generate_topology(self):
        topology = dict()
        topology['delay'] = generate_random_integer(self.delay_low, self.delay_high)
        topology['bandwidth'] = generate_random_integer(self.bandwidth_low, self.bandwidth_high)
        topology['loss'] = generate_random_integer(self.loss_low, self.loss_high)
        topology['jitter'] = generate_random_integer(self.jitter_low, self.jitter_high)
        str_topology = str(topology['delay']) \
                       + ',' \
                       + str(topology['bandwidth']) \
                       + ',' \
                       + str(topology['loss']) \
                       + ',' \
                       + str(topology['jitter'])
        return str_topology

    def get_vnf_detailed_information(self, operation):
        for vnf in self.vnf_list_detailed:
            if vnf['operation'] + ' ' == operation:
                return vnf
        return None

    def write_first_line_to_file(self):
        header = '#!/bin/sh'
        new_line = '\n'
        self.file_commands.write(header + new_line)
        self.file_orchestrator.readline()

    # TODO: Create an utility class that handles all of the searches
    def parse_for_name_orchestrator(self, line):
        index = line.find('orch_')
        index_image = line.find('--image')
        sub_line = line[index:index_image]
        return sub_line

    # TODO: Create an utility class that handles all of the searches
    def parse_for_ip_orchestrator(self, line):
        index = line.find('ip=')
        index_image = line.find('/24')
        sub_line = line[index + 3:index_image]
        return sub_line

    def close_file(self):
        self.file_orchestrator.close()
        self.file_commands.close()

    def load_container_information(self):
        file_container = open(self.path + "containers_vnfs.sh", "r+")
        file_container.readline()
        file_container.readline()
        for line in file_container:
            vnf = dict()
            vnf['name'] = self.parse_for_name_vnf(line)
            vnf['ip'] = self.parse_for_ip_vnf(line)
            self.vnf_container_list.append(vnf)
        file_container.close()

    # TODO: Create an utility class that handles all of the searches. Already class, update code
    def parse_for_name_vnf(self, line):
        index = line.find('vnf_')
        index_image = line.find('--image')
        sub_line = line[index:index_image]
        return sub_line

    # TODO: Create an utility class that handles all of the searches. Already a class, update code
    def parse_for_ip_vnf(self, line):
        index = line.find('ip=')
        index_image = line.find('/24')
        sub_line = line[index + 3:index_image]
        return sub_line

    def load_list_vnf(self):
        with open('vnf_info.json') as json_file:
            raw_data = json.load(json_file)
            self.vnf_list_detailed = raw_data['vnf']

    def load_seeds(self):
        with open('random_seeds.txt', 'r') as f:
            self.seeds = [line.strip() for line in f]

    # TODO: Use join to add two strings togehter
    def load_list_vnf_migration(self):
        with open(self.path + 'vnf_info_migration.json') as json_file:
            raw_data = json.load(json_file)
            self.vnf_list_detailed_migration = raw_data['vnf']

    def load_list_of_migrating_vnfs_detail(self):
        with open(self.path + 'migration_vnfs.json') as json_file:
            self.list_of_migrating_vnfs_detail = json.load(json_file)


    def load_services(self):
        with open(self.path + self.name_experiment + '.json') as json_file:
            raw_data = json.load(json_file)
            self.detailed_services = raw_data['services']


# # TODO: Put constants instead of magic numbers
# def main():
#     print('Begin')
#     length_of_vnfs = 4
#     video_definition = 480
#     delay = [0, 20]
#     bandwidth = [0, 70]
#     loss = [0, 10]
#     jitter = [0, 10]
#     name_of_experiment = 'experiment_0'
#
#     experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
#     exp_gen = DockerCommandsGenerator(experiment_path, delay, bandwidth, loss, jitter, name_of_experiment, length_of_vnfs)
#     exp_gen.generate_commands()
#

# if __name__ == main():
#     main()