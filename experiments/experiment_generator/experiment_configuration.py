import json

from experiments.experiment_generator.classes.constraints.bandwidth_constraint import BandwidthConstraint
from experiments.experiment_generator.classes.constraints.delay_constraint import DelayConstraint
from experiments.experiment_generator.classes.constraints.jitter_constraint import JitterConstraint
from experiments.experiment_generator.classes.constraints.loss_constraint import LossConstraint
from experiments.experiment_generator.classes.experiment_constraints import ExperimentConstraints
from utilities.random_integer_generation import generate_random_seeds


class ExperimentConfiguration:

    def __init__(self, path):
        self.path = path
        experiment = self.load_configuration_file()
        self.number_of_experiments = experiment['number_of_experiments']
        self.number_of_services = experiment['number_of_services']
        self.number_of_vnf_components = experiment['number_of_vnf_components']
        self.video_definition = experiment['video_definition']
        self.max_number_of_changes = experiment['max_number_of_changes']
        self.constraints = self.create_constraint_configuration(experiment)
        self.number_of_vnfs = experiment['number_of_vnfs']
        self.number_of_scalings = experiment['number_of_scalings']
        self.number_of_vnfs_per_orchestrator = experiment['number_of_vnfs_per_orchestrator']
        self.random_seed_list, self.random_np_seed_list = generate_random_seeds(self.number_of_vnf_components,
                                                                                self.number_of_services)

    def load_configuration_file(self):
        with open(self.path) as json_file:
            raw_data = json.load(json_file)
        return raw_data['experiment']

    def create_constraint_configuration(self, experiment):
        delay = self.create_delay_constraint(experiment['constraints']['delay'])
        bandwidth = self.create_delay_constraint(experiment['constraints']['bandwidth'])
        loss = self.create_delay_constraint(experiment['constraints']['loss'])
        jitter = self.create_delay_constraint(experiment['constraints']['jitter'])
        constraints = ExperimentConstraints(delay,
                                            bandwidth,
                                            loss,
                                            jitter)
        return constraints

    @staticmethod
    def create_delay_constraint(experiment):
        low_value = experiment['low']
        high_value = experiment['high']
        constraint = DelayConstraint(low_value, high_value)
        return constraint

    @staticmethod
    def create_jitter_constraint(experiment):
        low_value = experiment['low']
        high_value = experiment['high']
        constraint = JitterConstraint(low_value, high_value)
        return constraint

    @staticmethod
    def create_loss_constraint(experiment):
        low_value = experiment['low']
        high_value = experiment['high']
        constraint = LossConstraint(low_value, high_value)
        return constraint

    @staticmethod
    def create_bandwidth_constraint(experiment):
        low_value = experiment['low']
        high_value = experiment['high']
        constraint = BandwidthConstraint(low_value, high_value)
        return constraint
