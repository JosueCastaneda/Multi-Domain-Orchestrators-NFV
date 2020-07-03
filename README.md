# Multi-domain Orchestrators
## Description

This vnfs are simple video processing functions to test the chaining of VNFs.

Supports multi-domain using OSM emulator

This files are used to generate experiments.

## Old way to deploy experiment
To deploy experiment, the order of execution is the following

1) Run experiment_generator.py
2) Run vnf_migration_generator.py
3) Run setup_container_generator.py
4) Run destroy_container_generator.py
5) Run docker_commands_generator.py
6) Run update_vnf_information_with_migration_generator.py
7) Run update_service_with_migration_generator.py
8) Run validator_generator.py
9) Run migration_message_generator.py

Note: To run experiments, manually move the following files to your folder of destination
- need containers_orchestrator.sh
- containers_vnfs.sh
- migration_vnfs.json
- vnf_info.json
- vnf_info_migration.json

Email me: