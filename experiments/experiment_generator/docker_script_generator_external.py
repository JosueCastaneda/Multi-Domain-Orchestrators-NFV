import json
import os
import random


class DockerScriptGeneratorExternal:
    def __init__(self, experiment_index, configuration, random_running_index):
        self.experiment_index = experiment_index
        self.configuration = configuration
        self.data = self.load_all_required_data()
        self.all_dependencies = self.get_all_vnf_dependencies()
        self.all_services = self.get_all_services()
        self.orchestrator_index = 0
        self.file_commands_causal = None
        self.file_commands_normal = None
        self.running_experiment = 0
        self.random_running_index = random_running_index

    def set_index(self, index):
        self.orchestrator_index = index

    def create_orchestrator_file(self):
        file_directory = 'experiments/experiment_' + self.experiment_index + '/docker_files/'
        file_name = 'docker_commands_' + str(self.orchestrator_index) + '.sh'
        file_name_normal = 'docker_commands_normal_' + str(self.orchestrator_index) + '.sh'
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
        self.file_commands_causal = open(file_directory + file_name, 'w+')
        self.file_commands_normal = open(file_directory + file_name_normal, 'w+')

    def create_client_file(self):
        file_directory = 'experiments/experiment_' + self.experiment_index + '/'
        file_name = 'client_commands.sh'
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
        self.file_commands_causal = open(file_directory + file_name, 'w+')

    def generate_orchestrator_commands(self, running_experiment):
        self.running_experiment = running_experiment
        self.create_orchestrator_file()
        self.write_first_line_to_file()
        self.set_up_run_orchestrators()
        self.set_up_chain_orchestrators()
        self.set_up_running_vnf()
        self.close_file()
        return self.random_running_index

    def generate_client_commands(self):
        self.create_client_file()
        self.write_first_line_to_file()
        self.add_vnf_chains()
        self.add_request_of_updates()
        self.add_request_of_scaling()
        self.add_results()
        self.close_file()

    def add_results(self):
        self.file_commands_causal.write('# Add results \n')
        self.file_commands_normal.write('# Add results \n')
        self.add_results_external()
        self.write_new_line_to_file()

    def add_results_external(self):
        for orchestrator in self.data['orchestrators']:
            first_str = 'python3 message_factory.py -h ' + str(orchestrator['ip'])
            second_str = ' -p ' + str(orchestrator['port']) + ' -r external'
            self.file_commands_causal.write(first_str + second_str + '\n')
            self.file_commands_normal.write(first_str + second_str + '\n')

    def get_all_vnf_dependencies(self):
        list_dependencies = list()
        for orchestrator in self.data['orchestrators']:
            for vnf in orchestrator['vnfs']:
                list_dependencies.append(vnf)
        return list_dependencies

    def get_all_services(self):
        services = list()
        for orchestrator in self.data['orchestrators']:
            for service in orchestrator['services']:
                new_service = dict()
                new_service['orchestrator'] = [orchestrator['ip'], orchestrator['port']]
                new_service['service_id'] = service['id']
                services.append(new_service)
        return services

    def load_all_required_data(self):
        directory_path = 'experiments/experiment_' + self.experiment_index + '/'
        file_name = 'experiment_' + self.experiment_index + '.json'
        with open(directory_path + file_name) as json_file:
            return json.load(json_file)

    def write_first_line_to_file(self):
        header = '#!/bin/sh' + '\n'
        self.file_commands_causal.write(header + '\n')
        self.file_commands_normal.write(header + '\n')

    def get_port_based_on_index(self):
        return 5001 + self.orchestrator_index

    def set_up_run_orchestrators_external(self):
        random_seed = self.configuration.random_seed_list[self.running_experiment]
        first_string = 'python orchestrator_script.py -i ' + str(self.orchestrator_index)
        first_string_normal = 'python orchestrator_script_normal.py -i ' + str(self.orchestrator_index)
        second_string = ' -e ' + str(self.experiment_index) + ' -h \'0.0.0.0\' -p '
        third_string = str(self.get_port_based_on_index()) + ' -r ' + str(random_seed) + ' &'
        self.file_commands_causal.write(first_string + second_string + third_string + '\n')
        self.file_commands_normal.write(first_string_normal + second_string + third_string + '\n')
        print('Seed list: ' + str(len(self.configuration.random_seed_list)) + ' Running experiment: ' + str(self.running_experiment))

    def set_up_run_orchestrators(self):
        self.file_commands_causal.write('# Launch orchestrator' + '\n')
        self.file_commands_normal.write('# Launch orchestrator' + '\n')
        self.set_up_run_orchestrators_external()
        self.write_new_line_to_file()

    def set_up_chain_orchestrators_external(self):
        current_orchestrator = self.data['orchestrators'][self.orchestrator_index]
        for i in range(len(self.data['orchestrators'])):
            if i != self.orchestrator_index:
                other_orch = self.data['orchestrators'][i]
                first_string = 'python message_factory.py -t add_orchestrator -h 0.0.0.0'
                second_string = ' -p ' + current_orchestrator['port']
                third_string = ' -n none -m none --vnf_host ' + other_orch['ip'] + ' --vnf_port ' + other_orch[
                    'port'] + ' -x ' + other_orch['id']
                self.file_commands_causal.write(first_string + second_string + third_string + '\n')
                self.file_commands_normal.write(first_string + second_string + third_string + '\n')

    def set_up_chain_orchestrators(self):
        self.file_commands_causal.write('# Add orchestrator\'s informaton to my orchestrator' + '\n')
        self.file_commands_normal.write('# Add orchestrator\'s informaton to my orchestrator' + '\n')
        self.set_up_chain_orchestrators_external()
        self.write_new_line_to_file()

    def set_up_running_vnf_external(self):
        current_orchestrator = self.data['orchestrators'][self.orchestrator_index]
        vnf_port = 3001
        for vnf_index in range(len(current_orchestrator['vnfs'])):
            vnf = current_orchestrator['vnfs'][vnf_index]
            first_string = 'python vnf_script.py -i ' + str(vnf_index) + ' -o ' + str(self.orchestrator_index) + ' -e '
            third_string = str(self.experiment_index) + ' -h \'0.0.0.0\' -p ' + str(vnf_port) + ' &'
            self.file_commands_causal.write(first_string + third_string + '\n')
            self.file_commands_normal.write(first_string + third_string + '\n')
            vnf_port += 1

    def set_up_running_vnf(self):
        self.file_commands_causal.write('# Instantiate the orchestrator\'s VNFs \n')
        self.file_commands_normal.write('# Instantiate the orchestrator\'s VNFs \n')
        self.set_up_running_vnf_external()
        self.write_new_line_to_file()

    def add_vnf_chains(self):
        self.file_commands_causal.write('#Add chains to services \n')
        self.file_commands_normal.write('#Add chains to services \n')
        self.add_vnf_chains_external()
        self.write_new_line_to_file()

    def add_vnf_chains_external(self):
        for orchestrator in self.data['orchestrators']:
            for service in orchestrator['services']:
                first_index = 0
                first_dependency = None
                while first_index < len(service['dependencies']) - 1:
                    if first_dependency is None:
                        first_dependency = self.get_dependency_connection_point_by_id(
                            service['dependencies'][first_index])
                    second_dependency = self.get_dependency_connection_point_by_id(
                        service['dependencies'][first_index + 1],
                        False)
                    first_str = '# python message_factory.py -t add_chain -h ' + orchestrator['ip'] + ' -p '
                    second_str = orchestrator['port'] + ' -s ' + first_dependency['id'] + ' -d ' + first_dependency[
                        'id']
                    self.file_commands_causal.write(first_str + second_str + '\n')
                    self.file_commands_normal.write(first_str + second_str + '\n')
                    first_index += 1
                    first_dependency = second_dependency

    def get_dependency_connection_point_by_id(self, dependency, isFirst=True):
        if dependency['type'] == 'Service':
            return self.find_connection_point_of_service_by_id(dependency['id'], isFirst)
        for vnf in self.all_dependencies:
            if vnf['id'] == dependency['id']:
                return vnf

    def find_connection_point_of_service_by_id(self, dependency_id, isFirst):
        for orchestrator in self.data['orchestrators']:
            for service in orchestrator['services']:
                if service['id'] == dependency_id:
                    if isFirst:
                        new_connection_point = service['dependencies'][0]
                    else:
                        new_connection_point = service['dependencies'][len(service['dependencies']) - 1]
                    if new_connection_point['type'] == 'VNF':
                        for vnf in self.all_dependencies:
                            if vnf['id'] == new_connection_point['id']:
                                return vnf
                    else:
                        new_connection_point = self.get_vnf_from_service(new_connection_point)
                        for vnf in self.all_dependencies:
                            if vnf['id'] == new_connection_point['id']:
                                return vnf

    def get_vnf_from_service(self, new_connection_point):
        new_service = dict()
        new_service['type'] = new_connection_point['type']
        new_service['id'] = new_connection_point['id']
        while new_service['type'] != 'VNF':
            new_service = self.find_connection_point_recursive(new_service['id'])
        return new_service

    def add_request_of_scaling(self):
        self.file_commands_causal.write('# Request scaling \n')
        self.file_commands_normal.write('# Request scaling \n')
        self.add_request_of_scaling_external()
        self.write_new_line_to_file()

    def add_request_of_scaling_external(self):
        for i in range(0, self.configuration.number_of_scalings):
            random_seed = self.configuration.random_np_seed_list[self.random_running_index + self.running_experiment]
            random_service_to_scalate = self.get_random_service(random_seed)
            first_str = 'python message_factory.py -t request_scaling_of_service -h ' + \
                        random_service_to_scalate['orchestrator'][0]
            second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate[
                'service_id']
            third_str = ' --seed ' + str(random_seed)
            self.file_commands_causal.write(first_str + second_str + third_str + '\n')
            self.file_commands_normal.write(first_str + second_str + third_str + '\n')
            self.random_running_index += 1

    def add_request_of_updates(self):
        self.file_commands_causal.write('# Request updates (Commented) \n')
        self.file_commands_normal.write('# Request updates (Commented) \n')
        self.add_request_of_updates_external()
        self.write_new_line_to_file()

    def add_request_of_updates_external(self):
        for i in range(0, len(self.configuration.random_seed_list)):
            random_seed = self.configuration.random_seed_list[i]
            random_service_to_scalate = self.get_random_service(random_seed)
            first_str = '# python message_factory.py -t request_update -h ' + \
                        random_service_to_scalate['orchestrator'][0]
            second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate[
                'service_id']
            third_str = ' --seed ' + str(random_seed)
            self.file_commands_causal.write(first_str + second_str + third_str + '\n')
            self.file_commands_normal.write(first_str + second_str + third_str + '\n')

    def get_random_service(self, seed):
        random.seed(seed)
        random_index = random.randint(0, len(self.all_services) - 1)
        return self.all_services[random_index]

    def find_connection_point_recursive(self, dependency_id):
        for orchestrator in self.data['orchestrators']:
            for service in orchestrator['services']:
                if service['id'] == dependency_id:
                    return service['dependencies'][0]

    def write_new_line_to_file(self):
        self.file_commands_causal.write('\n')
        self.file_commands_normal.write('\n')

    def close_file(self):
        self.file_commands_causal.close()
        # self.file_commands_normal.close()
