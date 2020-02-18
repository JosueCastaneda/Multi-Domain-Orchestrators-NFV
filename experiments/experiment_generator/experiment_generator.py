import json
import os
import random

import numpy as np

from experiments.experiment_generator.docker_commands_generator import DockerCommandsGenerator
from experiments.experiment_generator.migration_message_generator import MigrationMessageGenerator
from experiments.experiment_generator.update_service_with_migration_generator import UpdateServiceWithMigrationGenerator
from experiments.experiment_generator.validator_generator import ValidatorGenerator
from utilities.random_integer_generation import generate_random_integer
from utilities.vnf_fg_update import generate_number_of_updates, generate_waiting_period, generate_index_to_change, \
    generate_random_string_value, generate_index_to_change_by_value, generate_random_orchestrator_index


class ExperimentGenerator():

    def __init__(self, number_experiments,
                 number_services,
                 length_vnf,
                 experiment_path,
                 delay,
                 bandwidth,
                 loss,
                 jitter,
                 random_seed_list,
                 random_np_seed_list,
                 max_number_of_changes):
        self.number_of_experiments = number_experiments
        self.number_of_services = number_services
        self.length_of_vnfs = length_vnf
        self.number_of_vnf = 13
        self.path = experiment_path
        self.list_name_of_experiments = []
        self.delay_low = delay[0]
        self.delay_high = delay[1]
        self.bandwidth_low = bandwidth[0]
        self.bandwidth_high = bandwidth[1]
        self.loss_low = loss[0]
        self.loss_high = loss[1]
        self.jitter_low = jitter[0]
        self.jitter_high = jitter[1]
        self.random_seed_list = random_seed_list
        self.random_np_seed_list = random_np_seed_list
        self.max_number_of_changes = max_number_of_changes

        with open(self.path + 'vnf_info.json') as json_file:
            raw_data = json.load(json_file)
            self.vnf_data = raw_data['vnf']

    def generate_experiment(self):

        for experiment in range(self.number_of_experiments):
            random.seed(self.random_seed_list[experiment])
            np.random.seed(self.random_np_seed_list[experiment])

            if not os.path.exists(self.path):
                os.makedirs(self.path)

            self.list_name_of_experiments.append('experiment_' + str(experiment))
            with open(self.path + 'experiment_' + str(experiment) + '.json', 'w') as json_file:
                experiment = dict()
                experiment['services'] = []
                for service in range(self.number_of_services):
                    list_random_index = self.generate_random_indexes()
                    vnf_list = []
                    for index in list_random_index:
                        vnf_list.append(self.vnf_data[index])
                    service = self.create_entry_service(vnf_list)
                    experiment['services'].append(service)

                # Select the VNFs to migrate
                migration_indexes = self.generate_random_vector()
                self.generate_migration_parameter(migration_indexes, experiment)
                json.dump(experiment, json_file)
        return self.list_name_of_experiments

    def generate_constraints(self):
        topology_constraints = dict()
        topology_constraints['delay'] = self.length_of_vnfs * generate_random_integer(self.delay_low, self.delay_high)
        topology_constraints['bandwidth'] = self.length_of_vnfs * generate_random_integer(self.bandwidth_low, self.bandwidth_high)
        topology_constraints['loss'] = self.length_of_vnfs * generate_random_integer(self.loss_low, self.loss_high)
        topology_constraints['jitter'] = self.length_of_vnfs * generate_random_integer(self.jitter_low, self.jitter_high)
        return topology_constraints

    # TODO: Handle multiple migrations, for the moment just one
    def generate_migration_parameter(self, migration_indexes, experiment):
        migration = []
        vnf_index = 0
        number_of_migrations = 0
        for index in migration_indexes:
            if self.valid_migration_index(index):
                host_migrating = self.vnf_data[vnf_index]
                migration.append(host_migrating['server'])
                number_of_migrations += 1
                break
            vnf_index += 1
        experiment['migrating_vnfs'] = migration
        experiment['number_of_migrations'] = number_of_migrations
        return experiment

    @staticmethod
    def valid_migration_index(index):
        return index > 1.0 or index < -1.0

    def generate_random_vector(self):
        standard_deviation = 0
        variance = 1
        # TODO: CHANGE FOR CLASS PARAMETER
        x = np.random.normal(standard_deviation, variance, self.number_of_vnf)
        return x

    def generate_random_indexes(self):
        return random.sample(range(self.number_of_vnf), self.length_of_vnfs)

    def handle_parameters(self, operation, parameters):
        generic_parameter = dict()
        if operation == 'ANNOTATE':
            generic_parameter['text'] = 'Test'
            generic_parameter['font_size'] = 30
            generic_parameter['color'] = 'white'
            parameters['annotation'] = generic_parameter

        if operation == 'CROP':
            generic_parameter['initial_time'] = 0
            generic_parameter['end_time'] = 10
            parameters['crop'] = generic_parameter

        if operation == 'FADE_IN':
            generic_parameter['duration'] = 10
            parameters['fade_in'] = generic_parameter

        if operation == 'FADE_OUT':
            generic_parameter['duration'] = 10
            parameters['fade_out'] = generic_parameter

        if operation == 'RESIZE':
            generic_parameter['width'] = 300
            generic_parameter['height'] = 300
            parameters['resize'] = generic_parameter

        if operation == 'SPEED_UP':
            parameters['speed_up'] = 2
        return parameters

    def generate_virtual_network_function_forwarding_graph(self, operations):
        vnf_fg_list = []
        previous_vnf = None
        for operation in operations:
            vnf_fg_entry = dict()
            vnf = self.get_vnf_by_operation(operation)
            vnf_fg_entry['name'] = vnf['operation']
            if previous_vnf:
                vnf_fg_entry['first_connection_point'] = previous_vnf['exit_connection_point']
            else:
                vnf_fg_entry['first_connection_point'] = None
            vnf_fg_entry['second_connection_point'] = vnf['entry_connection_point']
            previous_vnf = vnf
            vnf_fg_list.append(vnf_fg_entry)
        return vnf_fg_list

    def get_vnf_by_operation(self, operation):
        for vnf in self.vnf_data:
            if vnf['operation'] == operation:
                return vnf
        return None

    def create_file_parameter(self, parameters):
        file = dict()
        file['file_name'] = "videos/small_480.mp4"
        file['format_file'] = '.mp4'
        file['filename_processed'] = 'small_processed_'
        parameters['file'] = file
        return parameters

    def create_entry_service(self, vnf_list):
        operations = []
        servers = []
        ports = []
        parameters = dict()
        parameters = self.initialize_parameters(parameters)

        for vnf in vnf_list:
            operation = vnf['operation']
            operations.append(operation)
            servers.append(vnf['server'])
            ports.append(vnf['port'])
            parameters = self.handle_parameters(operation, parameters)

        parameters = self.create_file_parameter(parameters)
        service = dict()
        service['operations'] = operations
        service['host_servers'] = servers
        service['port_servers'] = ports
        service['parameters'] = parameters
        service['queue_q'] = []
        service['queue_p'] = []
        service['queue_r'] = []
        service['constraints'] = self.generate_constraints()
        service['vnf-fg'] = self.generate_virtual_network_function_forwarding_graph(operations)
        service['updates-vnf-fg'] = self.generate_updates_for_vnf_fg(service['vnf-fg'])
        #TODO: This needs to change to add more orchestrators
        service['orch_names'] = ['orch_1', 'orch_2', 'orch_3', 'orch_4']
        # TODO: Move this to the parameter
        if 'SPEED_UP' in operations:
            service['speed_factor'] = 2
        else:
            service['speed_factor'] = None
        return service

    def generate_updates_for_vnf_fg(self, vnf_fg):
        vnf_fg_list_updates = []
        number_of_changes = generate_number_of_updates(self.max_number_of_changes)
        for i in range(0, number_of_changes):
            wait_period = generate_waiting_period()
            vnf_index_to_change = generate_index_to_change_by_value(len(vnf_fg) - 1)
            index_to_change = generate_index_to_change()
            value_to_change = ''
            if index_to_change == 0:
                value_to_change = 'name'
            elif index_to_change == 1:
                value_to_change = 'first_connection_point'
            elif index_to_change == 2:
                value_to_change = 'second_connection_point'

            new_value = generate_random_string_value()
            orchestrator = generate_random_orchestrator_index()
            vnf_fg_update_entry = dict()
            vnf_fg_update_entry['wait_period'] = wait_period
            vnf_fg_update_entry['vnf_index_to_change'] = vnf_index_to_change
            vnf_fg_update_entry['value_to_change'] = value_to_change
            vnf_fg_update_entry['new_value'] = new_value
            vnf_fg_update_entry['orchestrator'] = orchestrator
            vnf_fg_list_updates.append(vnf_fg_update_entry)
        return vnf_fg_list_updates

    def initialize_parameters(self, parameters):
        parameters['annotation'] = None
        parameters['crop'] = None
        parameters['fade_in'] = None
        parameters['fade_out'] = None
        parameters['resize'] = None
        parameters['speed_up'] = None
        return parameters


def main():
    number_of_experiments = 10
    number_of_services = 3
    length_of_vnfs = 5
    video_definition = 480
    delay = [0, 20]
    bandwidth = [0, 70]
    loss = [0, 10]
    jitter = [0, 10]
    # FOR the 4th SIZE
    # random_seed_list = [5, 1234, 12424, 282812, 239423]
    # random_np_seed_list = [10, 2939, 104739, 14, 297573]

    # FOR THE 8 Size
    random_seed_list = [2940627, 3717510, 4651201, 5211310, 8760564]
    random_np_seed_list = [3060307, 3953270, 5291516, 7353312, 8607401]

    # For the 10 Size
    random_seed_list = [42191, 41898, 41358, 91689, 36924, 89787, 52971, 88074, 12951, 79798]
    random_np_seed_list = [72023, 75939, 31797, 34039, 41622, 16211, 31596, 84615, 31047, 59125]

    experiment_path = '../first/' + str(video_definition) +'/exp_1_' + str(length_of_vnfs) + '/experiments/'
    max_number_of_changes = 20

    print('Begin experiment generator')
    exp_gen = ExperimentGenerator(number_of_experiments,
                                  number_of_services,
                                  length_of_vnfs,
                                  experiment_path,
                                  delay,
                                  bandwidth,
                                  loss,
                                  jitter,
                                  random_seed_list,
                                  random_np_seed_list,
                                  max_number_of_changes)
    list_name_experiments = exp_gen.generate_experiment()
    print('End experiment generation')

    for experiment_file in list_name_experiments:
        print('Begin docker commands')
        dock_gen = DockerCommandsGenerator(experiment_path,
                                           delay,
                                           bandwidth,
                                           loss,
                                           jitter,
                                           experiment_file,
                                           length_of_vnfs)
        dock_gen.generate_commands()
        print('End docker commands')

    for experiment_file in list_name_experiments:
        print('Begin applying migration information ....')
        up_service = UpdateServiceWithMigrationGenerator(experiment_path, experiment_file)
        up_service.add_migration_information_to_services()
        print('Finish applying migration information ....')

    for experiment_file in list_name_experiments:
        print('Begin valid generation')
        val_gen = ValidatorGenerator(experiment_file, experiment_path)
        val_gen.validate_experiment()
        print('End valid generation')

    # for experiment_file in list_name_experiments:
    #     print('Begin docker commands')
    #     dock_gen = DockerCommandsGenerator(experiment_path,
    #                                        delay,
    #                                        bandwidth,
    #                                        loss,
    #                                        jitter,
    #                                        experiment_file,
    #                                        length_of_vnfs)
    #     dock_gen.generate_commands()
    #     print('End docker commands')

    for experiment_file in list_name_experiments:
        print('Begin migration message generator')
        message_gen = MigrationMessageGenerator(path=experiment_path,
                                                name_of_experiment=experiment_file)
        message_gen.generate()
        print('End migration message generator')

    # with open(experiment_path + 'experiment_0.json') as jsonfile:
    #     parsed = json.load(jsonfile)
    # print(json.dumps(parsed, indent=2, sort_keys=True))

    with open(experiment_path + 'vnf_info.json') as jsonfile:
        parsed = json.load(jsonfile)
    print(json.dumps(parsed, indent=2, sort_keys=True))

    # print('------------------------------------------------------------------')
    # print('                      VALIDATION                                  ')
    # print('------------------------------------------------------------------')
    #
    # with open(experiment_path + experiment_file + '_validate.json') as jsonfile:
    #     parsed = json.load(jsonfile)
    # print(json.dumps(parsed, indent=2, sort_keys=True))

    print('Finish setting up experiment!')


if __name__ == "__main__":
    main()