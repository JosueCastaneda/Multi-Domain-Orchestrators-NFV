import os
import sys


# To add the correct path and not get a ModuleNotFoundError
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from experiments.experiment_generator.experiment_configuration import ExperimentConfiguration
from experiments.experiment_generator.docker_script_generator_external import DockerScriptGeneratorExternal
from experiments.experiment_generator.docker_script_generator_local import DockerScriptGeneratorLocal
from experiments.experiment_generator.experiment_generator import ExperimentGenerator


def main():
    local_deployment = False
    if len(sys.argv) >= 2 and sys.argv[1] == 'local':
        local_deployment = True
    experiment_configuration = ExperimentConfiguration('experiment_constraint.json')
    exp_gen = ExperimentGenerator(experiment_configuration, local_deployment)
    list_name_experiments = exp_gen.generate_experiment()
    experiment_index = 0
    random_running_index = 0
    dock_gen = None
    vnf_port_local = 3001
    for experiment_file in list_name_experiments:
        if local_deployment:
            dock_gen = DockerScriptGeneratorLocal(experiment_file, experiment_configuration, vnf_port_local)
        else:
            dock_gen = DockerScriptGeneratorExternal(experiment_file, experiment_configuration)
        for index in range(len(exp_gen.list_orchestrators)):
            dock_gen.set_index(index)
            random_running_index += dock_gen.generate_orchestrator_commands(experiment_index)
            experiment_index += 1
        dock_gen.generate_client_commands()
        dock_gen.generate_vnf_forwarding_graph_update()
    dock_gen.generate_second_experiment_client_commands()


if __name__ == "__main__":
    main()
