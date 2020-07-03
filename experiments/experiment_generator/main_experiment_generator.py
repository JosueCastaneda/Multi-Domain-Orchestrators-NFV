from experiments.experiment_generator.classes.experiment_configuration import ExperimentConfiguration
from experiments.experiment_generator.docker_script_generator_external import DockerScriptGeneratorExternal
from experiments.experiment_generator.docker_script_generator_local import DockerScriptGeneratorLocal
from experiments.experiment_generator.experiment_generator import ExperimentGenerator


def main():
    local_deployment = False
    experiment_configuration = ExperimentConfiguration('experiment_constraint.json')
    exp_gen = ExperimentGenerator(experiment_configuration, local_deployment)
    list_name_experiments = exp_gen.generate_experiment()
    for experiment_file in list_name_experiments:
        if local_deployment:
            dock_gen = DockerScriptGeneratorLocal(experiment_file, experiment_configuration)
        else:
            dock_gen = DockerScriptGeneratorExternal(experiment_file, experiment_configuration)
        for index in range(len(exp_gen.list_orchestrators)):
            dock_gen.set_index(index)
            dock_gen.generate_orchestrator_commands()
        dock_gen.generate_client_commands()


if __name__ == "__main__":
    main()