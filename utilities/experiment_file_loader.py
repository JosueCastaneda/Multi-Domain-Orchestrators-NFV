import json
import os

from experiments.experiment_generator.classes.constraints.orchestrator_definition import OrchestratorDefinition
from experiments.experiment_generator.classes.experiment_constraints import ExperimentConstraints
from utilities.random_integer_generation import generate_unique_identifier


def load_orchestrators(is_external=False):
    my_path = os.path.dirname(os.path.realpath(__file__))
    full_path = my_path + '/../experiments/experiment_generator/orchestrator_definitions/'
    if is_external:
        file_path = full_path + 'orchestrator.json'
    else:
        file_path = full_path + 'orchestrator_local.json'
    list_of_orchestrators = list()
    with open(file_path) as json_file:
        raw_data = json.load(json_file)
    for orchestrator in raw_data['orchestrators']:
        constraints = ExperimentConstraints(orchestrator['vnf_constraints']['delay'],
                                            orchestrator['vnf_constraints']['bandwidth'],
                                            orchestrator['vnf_constraints']['loss'],
                                            orchestrator['vnf_constraints']['jitter'])
        new_orchestrator = OrchestratorDefinition(orchestrator['ip'],
                                                  orchestrator['port'],
                                                  orchestrator['location'],
                                                  constraints)
        list_of_orchestrators.append(new_orchestrator)
    return list_of_orchestrators


def load_vnf_raw_data():
    my_path = os.path.dirname(os.path.realpath(__file__))
    # print(my_path)
    full_path = my_path + '/../experiments/experiment_generator/'
    # print(full_path)
    with open(full_path + 'vnf_info.json') as json_file:
        raw_data = json.load(json_file)
        vnf_data = raw_data['vnf']
    return vnf_data


def create_empty_experiment_entry():
    experiment = dict()
    experiment['id'] = generate_unique_identifier()
    experiment['services'] = []
    return experiment
