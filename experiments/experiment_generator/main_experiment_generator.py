import os
import sys


# To add the correct path and not get a ModuleNotFoundError
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from experiments.experiment_generator.experiment_configuration import ExperimentConfiguration
from experiments.experiment_generator.docker_script_generator_external import DockerScriptGenerator
from experiments.experiment_generator.experiment_generator import ExperimentGenerator


def main():
    external_deployment = False
    number_of_updates = 10

    if len(sys.argv) >= 2 and sys.argv[1] == 'local':
        external_deployment = False
        number_of_updates = sys.argv[2]
    elif len(sys.argv) >= 2:
        external_deployment = True
        number_of_updates = sys.argv[2]

    experiment_configuration = ExperimentConfiguration('experiment_constraint.json', number_of_updates, external_deployment)
    exp_gen = ExperimentGenerator(experiment_configuration)
    list_name_experiments = exp_gen.generate_experiment()
    experiment_index = 0
    random_running_index = 0
    dock_gen = None
    for experiment_file in list_name_experiments:
        dock_gen = DockerScriptGenerator(experiment_file, experiment_configuration)
        for index in range(len(exp_gen.list_orchestrators)):
            dock_gen.set_index(index)
            random_running_index += dock_gen.generate_orchestrator_commands(experiment_index)
            experiment_index += 1
        dock_gen.generate_client_commands()
        dock_gen.generate_vnf_forwarding_graph_update()
    dock_gen.generate_second_experiment_client_commands()


if __name__ == "__main__":
    main()
