import json

from experiments.experiment_generator.classes.constraints.orchestrator_definition import OrchestratorDefinition
from experiments.experiment_generator.classes.experiment_constraints import ExperimentConstraints
from utilities.random_integer_generation import generate_unique_identifier


def load_orchestrators(is_local=False):
    if is_local:
        file_path = 'orchestrator_definitions/orchestrator_local.json'
    else:
        file_path = 'orchestrator_definitions/orchestrator.json'
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
    with open('vnf_info.json') as json_file:
        raw_data = json.load(json_file)
        vnf_data = raw_data['vnf']
    return vnf_data


def create_empty_experiment_entry():
    experiment = dict()
    experiment['id'] = generate_unique_identifier()
    experiment['services'] = []
    return experiment
