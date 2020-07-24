# Multi-domain Orchestrators
## Description

This vnfs are simple video processing functions to test the chaining of VNFs.

Supports multi-domain using OSM emulator for local tests

This files are used to generate experiments.

## New way to deploy experiments
0) Edit file experiment_constraint.json in path "experiments/experiment_generator/experiment_constraint.json"
1) Run create_experiments.sh (local, external)
2) Run run.sh by specifying experiment and orchestrator

## Orchestrators
0) Claire 
1) Duracell
2) Jill
3) Ada
4) Rebecca

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