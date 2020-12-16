#!/bin/bash

#Clean in case something was running
./clean.sh

# This script launches an orchestrator based on the auto-generated experiments
# In the case of external use (cloud) this is the main file to run orchestrators

# REMOVE COMMENTS ONLY FOR DEBUG PURPOSES
#echo -n "Please type number of experiment: "
# shellcheck disable=SC2162
#read EXPERIMENT_NUMBER
EXPERIMENT_NUMBER=0

echo -n "Please type number of orchestrator: "
# shellcheck disable=SC2162
read ORCHESTRATOR_NUMBER

#experiment=$1
#orchestrator=$2

path_1="experiments/experiment_generator/experiments/experiment_"
path_2="/docker_files/docker_commands_"
path_3=".sh"

complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3

# Activate the virtual environment
source ../my_env/bin/activate
source my_env/bin/activate

# Change the permissions of the files
./setup.sh $EXPERIMENT_NUMBER

# Run all the python files
./$complete_file