import json
import random


class DockerScriptGenerator:

    def __init__(self, experiment_index, configuration):
        self.experiment_index = experiment_index
        self.configuration = configuration
        self.data = self.load_all_required_data()
        self.file_commands = open('experiments/docker_commands_' + self.experiment_index + '.sh', 'w+')
        self.all_dependencies = self.get_all_vnf_dependencies()
        self.all_services = self.get_all_services()

    def generate_commands(self):
        self.write_first_line_to_file()
        self.set_up_run_orchestrators()
        self.set_up_chain_orchestrators()
        self.set_up_running_vnf()
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
        file_name = 'experiments/experiment_' + self.experiment_index + '.json'
        with open(file_name) as json_file:
            return json.load(json_file)

    def write_first_line_to_file(self):
        header = '#!/bin/sh'
        self.file_commands.write(header + '\n')

    def set_up_run_orchestrators(self):
        for index in range(len(self.data['orchestrators'])):
            first_string = 'docker exec -it mn.orch_' + str(index) + ' python orchestrator_script.py -i ' + str(index)
            second_string = ' -e ' + str(self.experiment_index) + ' &'
            self.file_commands.write(first_string + second_string + '\n')
        self.write_new_line_to_file()

    def set_up_chain_orchestrators(self):
        for index in range(len((self.data['orchestrators']))):
            current_orchestrator = self.data['orchestrators'][index]
            for i in range(len(self.data['orchestrators'])):
                if i != index:
                    other_orch = self.data['orchestrators'][i]
                    first_string = 'docker exec -it mn.source python message_factory.py -t add_orchestrator -h '
                    second_string = current_orchestrator['ip'] + ' -p ' + current_orchestrator['port']
                    third_string = ' -n none -m none --vnf_host ' + other_orch['ip']+ ' --vnf_port ' + other_orch['port'] + ' -x ' + other_orch['id']
                    self.file_commands.write(first_string + second_string + third_string + '\n')
        self.write_new_line_to_file()

    def set_up_running_vnf(self):
        for orchestrator_index in range(len((self.data['orchestrators']))):
            current_orchestrator = self.data['orchestrators'][orchestrator_index]
            for vnf_index in range(len(current_orchestrator['vnfs'])):
                vnf = current_orchestrator['vnfs'][vnf_index]
                first_string = 'docker exec -it mn.' + vnf['id'] + ' python vnf_script.py'
                second_string = ' -i ' + str(vnf_index) + ' -o ' + str(orchestrator_index) + ' -e '
                third_string = str(self.experiment_index) + ' &'
                self.file_commands.write(first_string + second_string + third_string + '\n')
        self.write_new_line_to_file()

    def add_vnf_chains(self):
        for orchestrator in self.data['orchestrators']:
            for service in orchestrator['services']:
                first_index = 0
                first_dependency = None
                while first_index < len(service['dependencies']) - 1:
                    if first_dependency == None:
                        first_dependency = self.get_dependency_connection_point_by_id(service['dependencies'][first_index])
                    second_dependecy = self.get_dependency_connection_point_by_id(service['dependencies'][first_index + 1],
                                                                                  False)
                    first_str = 'docker exec -it mn.source python message_factory.py -t add_chain -h ' + first_dependency['server']
                    second_str = ' -p ' + str(first_dependency['port']) +' -n none -m none -v ' + second_dependecy['server'] + ' --vnf_port ' + str(second_dependecy['port'])
                    self.file_commands.write(first_str + second_str + '\n')
                    first_index += 1
                    first_dependency = second_dependecy
        self.write_new_line_to_file()

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
        for i in range(0, len(self.configuration.random_seed_list)):
            random_seed = self.configuration.random_seed_list[i]
            random_service_to_scalate = self.get_random_service(random_seed)
            first_str = 'docker exec -it mn.source python message_factory.py -t request_scale -h ' + random_service_to_scalate['orchestrator'][0]
            second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate['service_id']
            third_str = ' --seed ' + str(random_seed)
            self.file_commands.write(first_str + second_str + third_str +'\n')
        self.write_new_line_to_file()


    def add_request_of_updates(self):
        for i in range(0, len(self.configuration.random_seed_list)):
            random_seed = self.configuration.random_seed_list[i]
            random_service_to_scalate = self.get_random_service(random_seed)
            first_str = 'docker exec -it mn.source python message_factory.py -t request_update -h ' + random_service_to_scalate['orchestrator'][0]
            second_str = ' -p ' + random_service_to_scalate['orchestrator'][1] + ' -i ' + random_service_to_scalate['service_id']
            third_str = ' --seed ' + str(random_seed)
            self.file_commands.write(first_str + second_str + third_str +'\n')
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