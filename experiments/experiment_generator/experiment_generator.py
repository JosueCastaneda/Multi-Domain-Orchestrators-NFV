import json
import logging
import os
import random

import numpy as np

from communication_entities.classifier_rule import ClassifierRule
from communication_entities.rendered_service_path import RenderedServicePath
from communication_entities.vnf_connection_point_reference import ConnectionPointReference
from communication_entities.vnf_forwarding_graph import VNFForwardingGraph
from experiments.experiment_generator.classes.constraints.service_definition import ServiceDefinition
from experiments.experiment_generator.classes.constraints.vnf_definition import VNFDefinition
from experiments.experiment_generator.classes.constraints.vnf_definition_configuration import VNFDefinitionConfiguration
from utilities.experiment_file_loader import load_orchestrators, create_empty_experiment_entry, load_vnf_raw_data
from utilities.random_integer_generation import generate_random_integer, generate_random_index_from_vnf_components, \
    generate_unique_identifier, generate_random_port, generate_random_ip


class ExperimentGenerator:

    def __init__(self, configuration):
        self.number_of_experiments = configuration.number_of_experiments
        self.log = None
        self.set_up_my_logger()
        self.number_of_services = configuration.number_of_services
        self.length_of_vnfs = configuration.number_of_vnf_components
        self.number_of_vnf = configuration.number_of_vnfs
        self.algorithm_index = configuration.algorithm_index
        self.path = configuration.path
        self.random_seed_list = configuration.random_seed_list
        self.random_np_seed_list = configuration.random_np_seed_list
        self.number_of_updates = configuration.number_of_updates
        self.number_of_vnfs_per_orchestrator = configuration.number_of_vnfs_per_orchestrator
        self.list_orchestrators = load_orchestrators(configuration.is_external)
        self.current_queues_number = 0
        self.list_vnf_components = list()
        self.vnf_data = load_vnf_raw_data()
        self.list_name_of_experiments = list()
        self.remaining_vnfc_components = 0
        # TODO: This is only for local deployments
        self.vnf_port = 5500
        self.port_vnfs = 3001
        self.is_external = configuration.is_external
        self.unique_identifiers = list()

    def add_vnfs_to_orchestrators(self):
        for orchestrator in self.list_orchestrators:
            remaining_vnfs_per_orchestrator = self.number_of_vnfs_per_orchestrator
            while remaining_vnfs_per_orchestrator > 0:
                if self.is_external:
                    new_vnf = self.generate_random_vnf(orchestrator)
                else:
                    new_vnf = self.generate_random_vnf_local(orchestrator)
                # if self.local_deployment:
                #     new_vnf = self.generate_random_vnf_local(orchestrator)
                # else:
                #     new_vnf = self.generate_random_vnf(orchestrator)
                orchestrator.add_vnf(new_vnf)
                remaining_vnfs_per_orchestrator -= 1
            self.port_vnfs = 3001

    def generate_random_vnf(self, orchestrator):
        random_index = generate_random_integer(0, len(self.vnf_data) - 1)
        vnf_data = self.vnf_data[random_index]
        my_path = os.path.dirname(os.path.realpath(__file__))
        with open(my_path + '/' + vnf_data['file']) as json_file:
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
        my_path = os.path.dirname(os.path.realpath(__file__))
        with open(my_path + '/' + vnf_data['file']) as json_file:
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
            if new_vnfc_index is not None:
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

    def add_services_and_vnf_forwading_graph_to_experiment(self, new_experiment):
        for service_count in range(self.number_of_services):
            orchestrator = self.get_random_orchestrator()
            new_service = self.generate_service_entry(orchestrator)
            orchestrator.add_service(new_service)
            vnf_forwarding_graph = self.generate_vnf_forwarding_from_service(new_service)
            self.add_vnf_forwarding_graph_to_orchestrators(vnf_forwarding_graph)
            new_experiment['services'].append(new_service)
            if not self.test_unique_vnf_forwarding_graph_for_every_orchestrator():
                print('Error creating the VNFFGs')

    # REMOVE: Just checking if now orchestrator have the same VNFFG
    def test_unique_vnf_forwarding_graph_for_every_orchestrator(self):
        for orchestrator in self.list_orchestrators:
            unique_list_vnf_forwarding_graph = list()
            for vnf_forwarding_graph in orchestrator.vnf_forwarding_graphs:
                if vnf_forwarding_graph['identifier'] in unique_list_vnf_forwarding_graph:
                    return False
                else:
                    unique_list_vnf_forwarding_graph.append(vnf_forwarding_graph['identifier'])
        return True

    def generate_vnf_forwarding_from_service(self, new_service: ServiceDefinition):
        vnf_forwarding_graph = self.create_emtpy_vnf_forwarding_graph(new_service.id)
        self.add_rendered_service_path_of_vnf_forwarding_graph(vnf_forwarding_graph)
        unique_orchestrators = self.add_connection_points_to_reference_service_path(vnf_forwarding_graph.get_first_rendered_service_path(), new_service.list_of_vnf_components)
        self.add_classifier_rules_to_vnf_forwarding_graph(vnf_forwarding_graph)
        unique_orchestrators.add(new_service.orchestrator_id)
        vnf_forwarding_graph.set_unique_orchestrators = unique_orchestrators
        return vnf_forwarding_graph.as_dictionary()

    def add_dependencies_to_vnf_forwarding_graph(self, vnf_forwarding_graph):
        pass

    def set_up_my_logger(self):
        file_name = 'logs/file_experiment_generator.log'
        other_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..//..', file_name))
        logging.basicConfig(filename=other_folder)
        self.log = logging.getLogger('logger')
        self.log.propagate = False
        self.log.setLevel(logging.WARNING)
        log_str = '%(message)s'
        formatter = logging.Formatter(log_str)
        fh = logging.FileHandler(other_folder, mode='w', encoding='utf-8')
        fh.setLevel(logging.WARNING)
        fh.setFormatter(formatter)
        self.log.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        self.log.addHandler(ch)

    def generate_unrepeated_unique_identifier(self):
        new_value = generate_unique_identifier()
        while new_value in self.unique_identifiers:
            new_value = generate_unique_identifier()
        self.unique_identifiers.append(new_value)
        self.log.info(new_value)
        return new_value

    def add_classifier_rules_to_vnf_forwarding_graph(self, vnf_forwarding_graph):
        classifier_identifier = self.generate_unrepeated_unique_identifier()
        classifier_name = self.generate_unrepeated_unique_identifier()
        rsp_id = vnf_forwarding_graph.get_first_rendered_service_path_id()
        classifier = ClassifierRule(classifier_identifier, classifier_name, rsp_id)
        vnf_forwarding_graph.append_classification(classifier)
        vnf_connection_points = vnf_forwarding_graph.rendered_service_paths[0].vnf_descriptor_connection_points
        self.add_matching_attributes_to_classifier(classifier, vnf_connection_points)

    def add_matching_attributes_to_classifier(self, classifier:ClassifierRule, vnf_descriptor_connection_points):
        for vnf_connection_point in vnf_descriptor_connection_points:
            new_matching_attribute_as_dictionary = dict()
            new_matching_attribute_as_dictionary['identifier'] = self.generate_unrepeated_unique_identifier()
            new_matching_attribute_as_dictionary['ip_proto'] = self.generate_unrepeated_unique_identifier()
            new_matching_attribute_as_dictionary['source_ip'] = generate_random_ip()
            new_matching_attribute_as_dictionary['destination_ip'] = generate_random_ip()
            new_matching_attribute_as_dictionary['source_port'] = generate_random_port()
            new_matching_attribute_as_dictionary['destination_port'] = generate_random_port()
            new_matching_attribute_as_dictionary['vnf_identifier'] = vnf_connection_point.vnf_identifier
            classifier.append_matching_attributes(new_matching_attribute_as_dictionary)

    def add_rendered_service_path_of_vnf_forwarding_graph(self, vnf_forwarding_graph):
        name_rsp = self.generate_unrepeated_unique_identifier()
        rsp_id = self.generate_unrepeated_unique_identifier()
        rendered_service_path = RenderedServicePath(rsp_id, name_rsp)
        vnf_forwarding_graph.append_rendered_service_path(rendered_service_path)

    def create_emtpy_vnf_forwarding_graph(self, new_service_id):
        vnf_forwarding_graph_identifier = self.generate_unrepeated_unique_identifier()
        vnf_forwarding_graph_name = self.generate_unrepeated_unique_identifier()
        vnf_forwarding_graph_short_name = self.generate_unrepeated_unique_identifier()
        vnf_forwarding_graph_service_identifier = new_service_id
        vnf_forwarding_graph = VNFForwardingGraph(identifier=vnf_forwarding_graph_identifier,
                                                  name=vnf_forwarding_graph_name,
                                                  short_name=vnf_forwarding_graph_short_name,
                                                  service_identifier=vnf_forwarding_graph_service_identifier)
        return vnf_forwarding_graph

    def add_connection_points_to_reference_service_path(self, rendered_service_path, list_of_vnf_components):
        vnf_component_counter = 0
        unique_orchestrators = set()
        for vnf_component in list_of_vnf_components:
            new_connection_point = self.create_new_connection_point_reference_from_vnf_component(vnf_component,
                                                                                                 vnf_component_counter,
                                                                                                 unique_orchestrators)
            rendered_service_path.append_vnf_connection_point_reference(new_connection_point)
            vnf_component_counter += 1
        return unique_orchestrators

    def create_new_connection_point_reference_from_vnf_component(self, vnf_component, counter, unique_orchestrators):
        vnf_component_identifier = vnf_component.id
        vnf_component_order = counter
        vnf_component_ingress_connection_point = vnf_component.id + self.generate_unrepeated_unique_identifier()
        vnf_component_egress_connection_point = vnf_component.id + self.generate_unrepeated_unique_identifier()

        if vnf_component.type == 'Service':
            vnf_service_component_id_first = self.get_vnf_service_component_id_first(
                vnf_component.list_of_vnf_components[0])
            last_index = len(vnf_component.list_of_vnf_components) - 1
            vnf_service_component_id_last = self.get_vnf_service_component_id_first(
                vnf_component.list_of_vnf_components[last_index])
            vnf_component_ingress_connection_point = vnf_service_component_id_first + self.generate_unrepeated_unique_identifier()
            vnf_component_egress_connection_point = vnf_service_component_id_last + self.generate_unrepeated_unique_identifier()
            unique_orchestrators.add(vnf_component.orchestrator_id)
        new_connection_point_reference = ConnectionPointReference(vnf_component_identifier,
                                                                  vnf_component_order,
                                                                  vnf_component_ingress_connection_point,
                                                                  vnf_component_egress_connection_point)
        return new_connection_point_reference

    def get_vnf_service_component_id_first(self, vnf_component):
        if vnf_component.type == 'VNF':
            return vnf_component.id
        return self.get_vnf_service_component_id_first(vnf_component.list_of_vnf_components[0])

    def add_vnf_forwarding_graph_to_orchestrators(self, new_vnf_forwarding_graph):
        for orchestrator_entry in new_vnf_forwarding_graph['unique_orchestrators']:
            orchestrator = self.find_orchestrator_by_id(orchestrator_entry)
            orchestrator.add_vnf_forwarding_graph(new_vnf_forwarding_graph)

    # TODO: Change the return type
    def find_orchestrator_by_id(self, orchestrator_id):
        for orchestrator in self.list_orchestrators:
            if orchestrator.id == orchestrator_id:
                return orchestrator
        return None

    def generate_experiment(self):
        for experiment_counter in range(self.number_of_experiments):
            self.change_random_seeds(experiment_counter)
            self.add_vnfs_to_orchestrators()
            new_experiment = create_empty_experiment_entry()
            self.add_services_and_vnf_forwading_graph_to_experiment(new_experiment)
            self.create_json_file_for_experiment(experiment_counter)
            self.list_vnf_components = []
            self.clear_orchestrator_vnfs()
        return self.list_name_of_experiments

    def clear_orchestrator_vnfs(self):
        for orchestrator in self.list_orchestrators:
            orchestrator.clear_all()
