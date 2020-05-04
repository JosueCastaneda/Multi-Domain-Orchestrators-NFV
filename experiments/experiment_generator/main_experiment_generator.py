from experiments.experiment_generator.classes.experiment_configuration import ExperimentConfiguration
from experiments.experiment_generator.docker_script_generator import DockerScriptGenerator
from experiments.experiment_generator.experiment_generator import ExperimentGenerator


def main():
    local_deployment = True
    experiment_configuration = ExperimentConfiguration('experiment_constraint.json')
    exp_gen = ExperimentGenerator(experiment_configuration, local_deployment)
    list_name_experiments = exp_gen.generate_experiment()
    for experiment_file in list_name_experiments:
        dock_gen = DockerScriptGenerator(experiment_file, experiment_configuration)
        dock_gen.generate_commands()


if __name__ == "__main__":
    main()