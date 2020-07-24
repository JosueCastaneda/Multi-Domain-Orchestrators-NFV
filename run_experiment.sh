#!/bin/bash

# This script launches an orchestrator based on the auto-generated experiments
# In the case of external use (cloud) this is the main file to run orchestrators

echo -n "Please type number of experiment: "
# shellcheck disable=SC2162
read EXPERIMENT_NUMBER

# Activate the virtual environment
source ../my_env/bin/activate
source my_env/bin/activate

message=$'Testing experiment\n'
echo -n "$message"
chmod +x experiments/experiment_generator/experiments/experiment_$EXPERIMENT_NUMBER/client_commands.sh
./experiments/experiment_generator/experiments/experiment_$EXPERIMENT_NUMBER/client_commands.sh