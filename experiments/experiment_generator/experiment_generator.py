import json
import os
import random

import numpy as np

from experiments.experiment_generator.classes.constraints.service_definition import ServiceDefinition
from experiments.experiment_generator.classes.constraints.vnf_definition import VNFDefinition
from experiments.experiment_generator.classes.constraints.vnf_definition_configuration import VNFDefinitionConfiguration
from utilities.experiment_file_loader import load_orchestrators, create_empty_experiment_entry, load_vnf_raw_data
from utilities.random_integer_generation import generate_random_integer, generate_unique_identifier, \
    generate_random_index_from_vnf_components


class ExperimentGenerator():

    def __init__(self, configuration, local_deployment=False):
        self.number_of_experiments = configuration.number_of_experiments
        self.number_of_services = configuration.number_of_services
        self.length_of_vnfs = configuration.number_of_vnf_components
        self.number_of_vnf = configuration.number_of_vnfs
        self.path = configuration.path
        self.random_seed_list = configuration.random_seed_list
        self.random_np_seed_list = configuration.random_np_seed_list
        self.number_of_vnfs_per_orchestrator = configuration.number_of_vnfs_per_orchestrator
        self.list_orchestrators = load_orchestrators(local_deployment)
        self.current_queues_number = 0
        self.list_vnf_components = list()
        self.vnf_data = load_vnf_raw_data()
        self.list_name_of_experiments = list()
        # TODO: This is only for local deployments
        self.vnf_port = 5500
        self.local_deployment = local_deployment
        self.port_vnfs = 3001

    def add_vnfs_to_orchestrators(self):
        for orchestrator in self.list_orchestrators:
            remaining_vnfs_per_orchestrator = self.number_of_vnfs_per_orchestrator
            while remaining_vnfs_per_orchestrator > 0:
                if self.local_deployment:
                    new_vnf = self.generate_random_vnf_local(orchestrator)
                else:
                    new_vnf = self.generate_random_vnf(orchestrator)
                orchestrator.add_vnf(new_vnf)
                remaining_vnfs_per_orchestrator -= 1
            self.port_vnfs = 3001

    def generate_random_vnf(self, orchestrator):
        random_index = generate_random_integer(0, len(self.vnf_data) - 1)
        vnf_data = self.vnf_data[random_index]
        with open(vnf_data['file']) as json_file:
            vnf_blue_print = json.load(json_file)
        vnf_configuration = VNFDefinitionConfiguration(vnf_blue_print['operation'],
                                                       orchestrator.get_new_ip(),
                                                       self.port_vnfs,
                                                       orchestrator.id,
                                                       self.current_queues_number,
                                                       orchestrator.constraints)
        new_vnf = VNFDefinition(vnf_configuration)
        self.current_queues_number += 3
        self.port_vnfs += 1
        return new_vnf

    def generate_random_vnf_local(self, orchestrator):
        random_index = generate_random_integer(0, len(self.vnf_data) - 1)
        vnf_data = self.vnf_data[random_index]
        with open(vnf_data['file']) as json_file:
            vnf_blue_print = json.load(json_file)
        vnf_configuration = VNFDefinitionConfiguration(vnf_blue_print['operation'],
                                                       '127.0.0.1',
                                                       self.vnf_port,
                                                       orchestrator.id,
                                                       self.current_queues_number,
                                                       orchestrator.constraints)
        new_vnf = VNFDefinition(vnf_configuration)
        self.current_queues_number += 3
        self.vnf_port += 2
        return new_vnf

    def change_random_seeds(self, experiment):
        random.seed(self.random_seed_list[experiment])
        np.random.seed(self.random_np_seed_list[experiment])

    def generate_service_entry(self, orchestrator):
        new_service = ServiceDefinition(orchestrator)
        remaining_vnfc_components = 1 + generate_random_integer(1, self.length_of_vnfs)
        vnfs_managed_by_orchestrator = self.create_list_of_vnf_components(orchestrator.get_vnfs())
        while remaining_vnfc_components > 0:
            new_vnfc_index = generate_random_index_from_vnf_components(vnfs_managed_by_orchestrator, new_service)
            new_service.add_vnf_component(vnfs_managed_by_orchestrator[new_vnfc_index])
            remaining_vnfc_components -= 1
            self.remaining_vnfc_components = remaining_vnfc_components
        self.list_vnf_components.append(new_service)
        return new_service

    def create_list_of_vnf_components(self, orchestrator_list):
        new_list_of_components = list()
        for element in orchestrator_list:
            new_list_of_components.append(element)
        for element in self.list_vnf_components:
            new_list_of_components.append(element)
        return new_list_of_components

    def create_json_file_for_experiment(self, experiment_number):
        dir_name = 'experiments/experiment_' + str(experiment_number)
        file_name = dir_name + '/experiment_' + str(experiment_number) + '.json'
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        new_experiment = self.create_experiment_as_json_directory()
        self.list_name_of_experiments.append(str(experiment_number))
        with open(file_name, 'w') as json_file:
            json.dump(new_experiment, json_file)

    def create_experiment_as_json_directory(self):
        new_experiment = dict()
        new_experiment['orchestrators'] = list()
        for orchestrator in self.list_orchestrators:
            new_orchestrator_json_encoded = orchestrator.create_dictionary_specification()
            new_experiment['orchestrators'].append(new_orchestrator_json_encoded)
        return new_experiment

    def get_random_orchestrator(self):
        random_index = generate_random_integer(0, len(self.list_orchestrators) - 1)
        return self.list_orchestrators[random_index]

    def add_services_to_experiment(self, new_experiment):
        for service_count in range(self.number_of_services):
            orchestrator = self.get_random_orchestrator()
            new_service = self.generate_service_entry(orchestrator)
            orchestrator.add_service(new_service)
            new_experiment['services'].append(new_service)

    def generate_experiment(self):
        for experiment_counter in range(self.number_of_experiments):
            self.change_random_seeds(experiment_counter)
            self.add_vnfs_to_orchestrators()
            new_experiment = create_empty_experiment_entry()
            self.add_services_to_experiment(new_experiment)
            self.create_json_file_for_experiment(experiment_counter)
            self.list_vnf_components = []
            self.clear_orchestrator_vnfs()
        return self.list_name_of_experiments

    def clear_orchestrator_vnfs(self):
        for orchestrator in self.list_orchestrators:
            orchestrator.clear_all()
