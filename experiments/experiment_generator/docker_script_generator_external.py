import json
import os
import random

from utilities.random_integer_generation import generate_random_integer, generate_unique_identifier


class DockerScriptGenerator:

    # def __init__(self, experiment_index, configuration, initial_vnf_port, number_of_vnffg_updates=640):
    def __init__(self, experiment_index, configuration):
        self.experiment_index = experiment_index
        self.configuration = configuration
        self.orchestrator_index = 0
        self.file_commands = None
        self.random_running_index = 0
        self.number_of_vnffg_updates = configuration.number_of_updates
        self.running_experiment = 0
        self.is_external = configuration.is_external
        self.vnf_port = configuration.vnf_port_local
        self.algorithm_index = configuration.algorithm_index

        dir_name_1 = 'experiments/number_of_reconfigurations_' + str(self.number_of_vnffg_updates)
        dir_name_2 = '/experiment_' + str(self.experiment_index) + '/'
        self.dir_name = dir_name_1 + dir_name_2

        self.data = self.load_all_required_data()
        self.all_dependencies = self.get_all_vnf_dependencies()
        self.all_services = self.get_all_services()

    def set_index(self, index):
        self.orchestrator_index = index

    def create_orchestrator_file(self):

        file_directory = self.dir_name + '/docker_files/'
        file_name = 'docker_commands_' + str(self.orchestrator_index) + '.sh'

        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
        self.file_commands = open(file_directory + file_name, 'w+')

    def create_client_file(self):
        # file_directory = 'experiments/experiment_' + self.experiment_index + '/'
        file_name = 'client_commands.sh'
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)
        self.file_commands = open(self.dir_name + file_name, 'w+')

    def generate_orchestrator_commands(self, experiment_index):
        self.create_orchestrator_file()
        self.write_first_line_to_file()
        self.set_up_run_orchestrators()
        self.set_up_chain_orchestrators()
        self.set_up_running_vnf()
        self.close_file()
        return 1

    def generate_client_commands(self):
        self.create_client_file()
        self.write_first_line_to_file()
        self.add_vnf_chains()
        self.add_request_of_updates()
        self.add_request_of_scaling()
        self.close_file()

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

        # dir_name_1 = 'experiments/number_of_reconfigurations_' + str(self.number_of_vnffg_updates)
        # dir_name_2 = '/experiment_' + str(self.experiment_index) + '/'
        # dir_name = 'experiments/experiment_' + str(experiment_number)
        # dir_name = dir_name_1 + dir_name_2
        # print(dir_name)
        # directory_path = 'experiments/experiment_' + self.experiment_index + '/'
        file_name = 'experiment_' + self.experiment_index + '.json'
        with open(self.dir_name + file_name) as json_file:
        # with open(directory_path + file_name) as json_file:
            return json.load(json_file)

    def write_first_line_to_file(self):
        header = '#!/bin/sh' + '\n'
        self.file_commands.write(header + '\n')

    def set_up_run_orchestrators(self):
        self.file_commands.write('# Launch orchestrator' + '\n')
        random_seed = self.configuration.random_seed_list[self.running_experiment]
        current_orchestrator = self.data['orchestrators'][self.orchestrator_index]
        first_string = 'python3 orchestrator_script.py -i ' + str(self.orchestrator_index)
        if self.is_external:
            second_string = ' -e ' + str(self.experiment_index) + ' -h \'0.0.0.0\' -p '
        else:
            second_string = ' -e ' + str(self.experiment_index) + ' -h \'127.0.0.1\' -p '
        five_string = ' -a $3'
        third_string = current_orchestrator['port'] + ' -r ' + str(random_seed) + five_string + ' -x $1 -y $2 -w $4 -u $5 &'
        self.file_commands.write(first_string + second_string + third_string + '\n')
        fourth_string = 'sleep 2'
        self.file_commands.write(fourth_string + '\n')
        self.write_new_line_to_file()

    def set_up_chain_orchestrators(self):
        self.file_commands.write('# Add orchestrator\'s information to my orchestrator' + '\n')
        current_orchestrator = self.data['orchestrators'][self.orchestrator_index]
        for i in range(len(self.data['orchestrators'])):
            if i != self.orchestrator_index:
                other_orchestrator = self.data['orchestrators'][i]
                if self.is_external:
                    first_string = 'python message_factory.py -t add_orchestrator -h 0.0.0.0'
                else:
                    first_string = 'python3 message_factory.py -t add_orchestrator -h 127.0.0.1'
                second_string = ' -p ' + current_orchestrator['port']
                third_string = ' -n none -m none --vnf_host ' + other_orchestrator['ip'] + ' --vnf_port ' + \
                               other_orchestrator[
                                   'port'] + ' -x ' + other_orchestrator['id']
                self.file_commands.write(first_string + second_string + third_string + '\n')
        self.write_new_line_to_file()

    def set_up_running_vnf(self):
        self.file_commands.write('# Instantiate the orchestrator\'s VNFs \n')
        fourth_string = 'sleep 2'
        self.file_commands.write(fourth_string + '\n')
        current_orchestrator = self.data['orchestrators'][self.orchestrator_index]
        vnf_port = 3001
        for vnf_index in range(len(current_orchestrator['vnfs'])):
            first_string = 'python3 vnf_script.py -i ' + str(vnf_index) + ' -o ' + str(self.orchestrator_index) + ' -e '
            if self.is_external:
                third_string = str(self.experiment_index) + ' -h \'0.0.0.0\' -p ' + str(vnf_port) + ' -u $5' + ' &'
            else:
                third_string = str(self.experiment_index) + ' -h \'127.0.0.1\' -p ' + str(self.vnf_port) + ' -u $5' + ' &'
            self.file_commands.write(first_string + third_string + '\n')
            self.vnf_port += 1
            vnf_port += 1
        self.write_new_line_to_file()

    def add_vnf_chains(self):
        self.file_commands.write('#Add chains to services \n')
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
                    if self.is_external:
                        first_str = '# python message_factory.py -t add_chain -h ' + orchestrator['ip'] + ' -p '
                        second_str = orchestrator['port'] + ' -s ' + first_dependency['id'] + ' -d ' + first_dependency[
                            'id']
                    else:
                        first_str = 'docker exec -it mn.source python message_factory.py -t add_chain -h ' + \
                                    first_dependency['server']
                        second_str = ' -p ' + str(first_dependency['port']) + ' -n none -m none -v ' + second_dependency[
                            'server'] + ' --vnf_port ' + str(second_dependency['port'])
                    self.file_commands.write(first_str + second_str + '\n')
                    first_index += 1
                    first_dependency = second_dependency
        self.write_new_line_to_file()

    def get_dependency_connection_point_by_id(self, dependency, is_first=True):
        if dependency['type'] == 'Service':
            return self.find_connection_point_of_service_by_id(dependency['id'], is_first)
        for vnf in self.all_dependencies:
            if vnf['id'] == dependency['id']:
                return vnf

    def find_connection_point_of_service_by_id(self, dependency_id, is_first):
        for orchestrator in self.data['orchestrators']:
            for service in orchestrator['services']:
                if service['id'] == dependency_id:
                    if is_first:
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
        self.file_commands.write('# Request scaling \n')
        for i in range(0, len(self.configuration.random_seed_list)):
            random_seed = self.configuration.random_seed_list[i]
            random_service_to_scalate = self.get_random_service(random_seed)
            first_str = 'docker exec -it mn.source python message_factory.py -t request_scale -h ' + \
                        random_service_to_scalate['orchestrator'][0]
            second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate[
                'service_id']
            third_str = ' --seed ' + str(random_seed)
            self.file_commands.write(first_str + second_str + third_str + '\n')
        self.write_new_line_to_file()

    def add_request_of_updates(self):
        self.file_commands.write('# Request updates (Commented) \n')
        for i in range(0, len(self.configuration.random_seed_list)):
            random_seed = self.configuration.random_seed_list[i]
            random_service_to_scalate = self.get_random_service(random_seed)
            if self.is_external:
                first_str = '# python message_factory.py -t request_update -h ' + \
                            random_service_to_scalate['orchestrator'][0]
                second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate[
                    'service_id']
            else:
                first_str = 'docker exec -it mn.source python message_factory.py -t request_update -h ' + \
                            random_service_to_scalate['orchestrator'][0]
                second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate[
                    'service_id']
            third_str = ' --seed ' + str(random_seed)
            self.file_commands.write(first_str + second_str + third_str + '\n')
        self.write_new_line_to_file()

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
        self.file_commands.write('\n')

    def close_file(self):
        self.file_commands.close()

    def generate_vnf_forwarding_graph_update(self):
        vnf_forwarding_graph_updates = list()
        remaining_updates = int(self.number_of_vnffg_updates)
        # print('Remaining updates ' + str(remaining_updates))
        while remaining_updates:
            random_orchestrator = self.get_random_orchestrator()
            random_vnf_forwarding_graph = self.get_random_vnffg(random_orchestrator)
            type_of_update = self.get_random_vnffg_update()
            new_vnf_forwarding_graph = self.generate_vnffg_update(random_vnf_forwarding_graph,
                                                                  type_of_update,
                                                                  random_orchestrator)
            vnf_forwarding_graph_updates.append(new_vnf_forwarding_graph)
            remaining_updates -= 1
        self.write_vnffg_updates_in_docker_file(vnf_forwarding_graph_updates)

    def write_vnffg_updates_in_docker_file(self, vnf_forwarding_graph_updates:list):
        self.create_vnf_forwarding_graph_update()
        for vnf_forwarding_graph_update in vnf_forwarding_graph_updates:
            if vnf_forwarding_graph_update['type'] == 'rsp':
                self.write_new_rsp_entry(vnf_forwarding_graph_update)
            else:
                self.write_new_classifier_entry(vnf_forwarding_graph_update)
            self.file_vnf_forwarding_graph_update.write('\n')
        self.file_vnf_forwarding_graph_update.flush()
        self.file_vnf_forwarding_graph_update.close()

    # TODO: THE file_directory scrwws over....
    def create_vnf_forwarding_graph_update(self):
        file_name = 'updates_vnf_forwarding_graphs.sh'
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)
        self.file_vnf_forwarding_graph_update = open(self.dir_name + file_name, 'w+')

    def get_random_orchestrator(self):
        number_of_orchestrators = len(self.data['orchestrators'])
        random_index = generate_random_integer(0, number_of_orchestrators - 1)
        return self.data['orchestrators'][random_index]

    def get_random_vnffg(self, orchestrator_as_dictionary:dict):
        number_of_vnf_forwarding_graphs = len(orchestrator_as_dictionary['vnf-forwarding_graphs'])
        random_index = generate_random_integer(0, number_of_vnf_forwarding_graphs - 1)
        return orchestrator_as_dictionary['vnf-forwarding_graphs'][random_index]

    def get_random_vnffg_update(self):
        update_number = generate_random_integer(0, 1)
        if update_number == 0:
            return 'rsp'
        return 'classifier'

    def generate_vnffg_update(self, vnf_forwarding_graph: dict, type_of_update: str, random_orchestrator: dict):
        if type_of_update == 'rsp':
            return self.generate_new_rsp(vnf_forwarding_graph, random_orchestrator)
        return self.generate_new_classifier(vnf_forwarding_graph, random_orchestrator)

    def generate_new_rsp(self, vnf_forwarding_graph:dict, random_orchestrator:dict):
        unique_rsp = vnf_forwarding_graph['rendered_service_paths'][0]
        number_of_vnf_descriptor_points = len(unique_rsp['vnf_descriptor_connection_points'])
        random_connection_point_index = generate_random_integer(0, number_of_vnf_descriptor_points - 1)
        vnf_fg_to_change = unique_rsp['vnf_descriptor_connection_points'][random_connection_point_index]
        new_update = dict()
        new_update['vnf_identifier'] = vnf_fg_to_change['vnf_identifier']
        new_update['order'] = generate_random_integer(0, self.configuration.number_of_vnf_components - 1)
        new_update['ingress_connection_point'] = generate_unique_identifier()
        new_update['egress_connection_point'] = generate_unique_identifier()
        new_update['host'] = random_orchestrator['ip']
        new_update['port'] = random_orchestrator['port']
        new_update['type'] = 'rsp'
        return new_update

    # TODO: This function changes all the entry, it is necessary to change only items instead of the whole thing
    def generate_new_classifier(self, vnf_forwarding_graph:dict, random_orchestrator:dict):
        unique_rule = vnf_forwarding_graph['classification_rules'][0]
        number_of_matching_attributes = len(unique_rule['matching_attributes'])
        random_matching_attribute_index = generate_random_integer(0, number_of_matching_attributes - 1)
        vnf_fg_to_change = unique_rule['matching_attributes'][random_matching_attribute_index]
        new_update = dict()
        new_update['identifier'] = vnf_fg_to_change['identifier']
        # new_update['vnf_identifier'] = vnf_fg_to_change['vnf_identifier']
        # TODO: This line has to create only a couple of valus like tcp, udp, for now a new string
        new_update['ip_proto'] = generate_unique_identifier()
        new_update['source_ip'] = generate_unique_identifier()
        new_update['destination_ip'] = generate_unique_identifier()
        new_update['source_port'] = generate_unique_identifier()
        new_update['destination_port'] = generate_unique_identifier()
        new_update['host'] = random_orchestrator['ip']
        new_update['port'] = random_orchestrator['port']
        new_update['type'] = 'classifier'
        return new_update

    def write_new_rsp_entry(self, vnf_forwarding_graph_update:dict):
        first = 'python3 message_factory.py --type update_vnffg_rsp --host ' + vnf_forwarding_graph_update['host']
        second = ' --port ' + vnf_forwarding_graph_update['port'] + ' --vnf_identifier '
        third = vnf_forwarding_graph_update['vnf_identifier'] + ' --order ' + str(vnf_forwarding_graph_update['order'])
        fourth = ' --ingress_connection_point ' + vnf_forwarding_graph_update['ingress_connection_point']
        fifth = ' --egress_connection_point ' + vnf_forwarding_graph_update['egress_connection_point']
        self.file_vnf_forwarding_graph_update.write(first + second + third + fourth + fifth + ' & \n')

    def write_new_classifier_entry(self, vnf_forwarding_graph_update:dict):
        first = 'python3 message_factory.py --type update_vnffg_classifier --host ' + vnf_forwarding_graph_update['host']
        second = ' --port ' + vnf_forwarding_graph_update['port'] + ' --match_identifier '
        third = vnf_forwarding_graph_update['identifier'] + ' --ip_proto ' + vnf_forwarding_graph_update['ip_proto']
        fourth = ' --source_ip ' + str(vnf_forwarding_graph_update['source_ip'])
        fifth = ' --destination_ip ' + str(vnf_forwarding_graph_update['destination_ip'])
        six = ' --source_port ' + str(vnf_forwarding_graph_update['source_port'])
        seven = ' --destination_port ' + str(vnf_forwarding_graph_update['destination_port'])
        self.file_vnf_forwarding_graph_update.write(first + second + third + fourth + fifth + six + seven + ' & \n')

    def generate_second_experiment_client_commands(self):
        self.add_request_of_scaling_second()
        for experiment_index in range(0, self.configuration.number_of_experiments):
            file_directory = 'experiments/experiment_' + str(experiment_index) + '/'
            file_name = 'client_second_file_commands.sh'
            if not os.path.exists(file_directory):
                os.makedirs(file_directory)
            self.file_commands_causal = open(file_directory + file_name, 'a')
            self.file_commands_causal.write('# Add results \n')
            for orchestrator in self.data['orchestrators']:
                first_str = 'python3 message_factory.py -h ' + str(orchestrator['ip'])
                second_str = ' -p ' + str(orchestrator['port']) + ' -r external'
                self.file_commands_causal.write(first_str + second_str + '\n')

            self.close_file()

    def add_request_of_scaling_second(self):
        self.add_request_of_scaling_external_second_experiment()

    def add_request_of_scaling_external_second_experiment(self):
        list_valid_services = list()
        list_valid_test_experiments = list()
        random_list_per_experiment = list()
        random_list = []
        for i in range(0, self.configuration.max_dependencies):
            list_valid_services.append(self.get_list_of_valid_services_by_total_dependencies(i))
            random_list = self.generate_random_list_from_np_seeds(i, len(list_valid_services[i]))
            random_list_per_experiment.append(random_list)

        for experiment_list in list_valid_services:
            sublist_copia = list()
            for i in random_list:
                if i < len(experiment_list):
                    sublist_copia.append(experiment_list[i])
            list_valid_test_experiments.append(sublist_copia)

        for i in range(0, self.configuration.max_dependencies):
            for service in list_valid_test_experiments[i]:
                self.append_line_to_file_second_experiment(service, i)

    def get_list_of_valid_services_by_total_dependencies(self, required_dependencies):
        list_valid_services = list()
        for experiment_index in range(0, self.configuration.number_of_experiments):
            service_data = self.load_service_data_from_experiment(experiment_index)
            for service in service_data:
                total_dependencies_per_service = self.compute_total_dependencies(service, service_data)
                service['experiment_index'] = experiment_index
                if total_dependencies_per_service == required_dependencies:
                    list_valid_services.append(service)
        return list_valid_services

        # TODO: Make utility function
    def load_service_data_from_experiment(self, experiment_index):
        list_of_services = list()
        # directory_path = 'experiments/experiment_' + str(experiment_index) + '/'
        file_name = 'experiment_' + str(experiment_index) + '.json'

        dir_name_1 = 'experiments/number_of_reconfigurations_' + str(self.number_of_vnffg_updates)
        dir_name_2 = '/experiment_' + str(experiment_index) + '/'
        directory_path = dir_name_1 + dir_name_2
        with open(directory_path + file_name) as json_file:
            all_data = json.load(json_file)
        for orchestrator in all_data['orchestrators']:
            for service in orchestrator['services']:
                list_of_services.append(service)
        return list_of_services

    def append_line_to_file_second_experiment(self, service, dependencies):
        self.create_second_client_file(service['experiment_index'])
        orchestrator = self.get_orchestrator_by_service(service)
        header = '#!/bin/sh' + '\n'
        self.file_commands_causal.write(header + '\n')
        zero_str = '# Dependencies ' + str(dependencies)
        self.file_commands_causal.write(zero_str + '\n')
        first_str = 'python3 message_factory.py -t request_scaling_of_service -h ' + orchestrator['ip']
        second_str = ' -p ' + orchestrator['port'] + ' -i ' + service['id']
        self.file_commands_causal.write(first_str + second_str + '\n')
        fourth_str = 'python3 message_factory.py -r external'
        self.file_commands_causal.write(fourth_str + '\n')
        self.close_file()

    def compute_total_dependencies(self, service, service_data):
        total_dependencies = 0
        if service['are_all_dependencies_vnfs'] or service['type'] != 'Service':
            return 0
        else:
            for dependency in service['dependencies']:
                if dependency['type'] == 'Service':
                    dependency_as_service = self.get_service_by_dependency(dependency, service_data)
                    total_dependencies += (1 + self.compute_total_dependencies(dependency_as_service, service_data))
        return total_dependencies

    # TODO: Make utility function
    def get_service_by_dependency(self, dependency, service_data):
        for service in service_data:
            if dependency['id'] == service['id']:
                return service
        print('Error!!!')

    def generate_random_list_from_np_seeds(self, index, max_numbers):
        random.seed(self.configuration.collect_random[index])
        # print('Max number: ' + str(max_numbers))
        if max_numbers < 5:
            return random.sample(range(0, max_numbers), max_numbers)
        return random.sample(range(0, max_numbers), 5)

    def create_second_client_file(self, experiment_index):
        file_directory = 'experiments/experiment_' + str(experiment_index) + '/'
        file_name = 'client_second_file_commands.sh'
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
        self.file_commands_causal = open(file_directory + file_name, 'a')

    # TODO: Make utility function
    def get_orchestrator_by_service(self, service):
        list_orchestrators = list()
        # directory_path = 'experiments/experiment_' + str(service['experiment_index']) + '/'
        file_name = 'experiment_' + str(service['experiment_index']) + '.json'
        # print(self.dir_name)
        dir_name_1 = 'experiments/number_of_reconfigurations_' + str(self.number_of_vnffg_updates)
        dir_name_2 = '/experiment_' + str(service['experiment_index']) + '/'
        directory_path = dir_name_1 + dir_name_2
        # print(directory_path + file_name)

        with open(directory_path + file_name) as json_file:
            data_orchestrators = json.load(json_file)
            list_orchestrators.append(data_orchestrators)

        for orchestrator_list in list_orchestrators:
            for orchestrator in orchestrator_list['orchestrators']:
                for data_service in orchestrator['services']:
                    if data_service['id'] == service['id']:
                        return orchestrator

    def get_port_based_on_index(self):
        return 5001 + self.orchestrator_index