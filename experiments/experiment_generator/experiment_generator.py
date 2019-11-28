import json
import os
import random

import numpy as np

from experiments.experiment_generator.docker_commands_generator import DockerCommandsGenerator
from experiments.experiment_generator.update_service_with_migration_generator import UpdateServiceWithMigrationGenerator
from experiments.experiment_generator.validator_generator import ValidatorGenerator
from experiments.experiment_generator.update_vnf_information_with_migration_generator import UpdateVnfInformationWithMigrationGenerator
from utilities.random_integer_generation import generate_random_integer


class ExperimentGenerator():

    def __init__(self, number_experiments, number_services, length_vnf, experiment_path, delay, bandwidth, loss, jitter):
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
        random.seed(5)

        with open(self.path + 'vnf_info.json') as json_file:
            raw_data = json.load(json_file)
            self.vnf_data = raw_data['vnf']

    def generate_experiment(self):
        for experiment in range(self.number_of_experiments):
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

    def generate_migration_parameter(self, migration_indexes, experiment):
        migration = []
        vnf_index = 0
        number_of_migrations = 0
        for index in migration_indexes:
            if self.valid_migration_index(index):
                host_migrating = self.vnf_data[vnf_index]
                migration.append(host_migrating['server'])
                number_of_migrations += 1
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
        random.seed(5)
        np.random.seed(10)
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
        return parameters

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
        return service


def main():
    number_of_experiments = 3
    number_of_services = 3
    length_of_vnfs = 4
    video_definition = 480
    delay = [0, 20]
    bandwidth = [0, 70]
    loss = [0, 10]
    jitter = [0, 10]
    experiment_path = '../first/' + str(video_definition) +'/exp_1_' + str(length_of_vnfs) + '/experiments/'
    experiment_file = 'experiment_0'

    print('Begin experiment generator')
    exp_gen = ExperimentGenerator(number_of_experiments,
                                  number_of_services,
                                  length_of_vnfs,
                                  experiment_path,
                                  delay,
                                  bandwidth,
                                  loss,
                                  jitter)
    list_name_experiments = exp_gen.generate_experiment()
    print('End experiment generation')

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

    with open(experiment_path + 'experiment_0.json') as jsonfile:
        parsed = json.load(jsonfile)
    print(json.dumps(parsed, indent=2, sort_keys=True))

    print('------------------------------------------------------------------')
    print('                      VALIDATION                                  ')
    print('------------------------------------------------------------------')

    with open(experiment_path + experiment_file + '_validate.json') as jsonfile:
        parsed = json.load(jsonfile)
    print(json.dumps(parsed, indent=2, sort_keys=True))

    print('Finish setting up experiment!')


if __name__ == "__main__":
    main()