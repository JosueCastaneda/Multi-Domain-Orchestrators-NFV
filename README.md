# Multi-domain Orchestrators
## Description

This vnfs are simple video processing functions to test the chaining of VNFs.

Supports multi-domain using OSM emulator for local tests

This files are used to generate experiments.

# Deploying experiments

## 0. Change permissions for the following files
chmod +x create_experiments.sh

## 1. Setup files
0) Edit file experiment_constraint.json in path "experiments/experiment_generator/experiment_constraint.json"
1) Install numpy~=1.18.5
2) Install moviepy~=1.0.3
3) Install aiohttp~=3.6.2

## 2. Create random services by running create_experiments.sh and setup.sh
./create_experiments.sh
./setup.sh

## 3. Run experiments

### 3.1 Local/External ETSI standard
/.run_normal.sh

### 3.2 Local/External Causal delivery
/.run.sh

# Run specific tests (To do)


# Cloud orchestrators
0) Claire 
1) Duracell
2) Jill
3) Ada
4) Rebecca

If you have any questions, please email me at: jcastane@laas.fr