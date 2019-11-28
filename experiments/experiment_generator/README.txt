This files are used to generate experiments.

To deploy experiment, the order of execution is the following

1) Run experiment_generator.py
2) Run vnf_migration_generator.py
3) Run setup_container_generator.py
4) Run destroy_container_generator.py
5) Run docker_commands_generator.py
6) Run update_vnf_information_with_migration_generator.py
7) Run update_service_with_migration_generator.py
8) Run validator_generator.py
