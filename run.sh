#!/bin/bash

# This script launches an orchestrator based on the auto-generated experiments
# In the case of external use (cloud) this is the main file to run orchestrators

echo -n "Please type number of experiment: "
# shellcheck disable=SC2162
read EXPERIMENT_NUMBER

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

#
#echo -n "Please type if local or external run: "
#read RUN_TYPE
#
#case $RUN_TYPE in
#
#  local)
#    message=$'Local run environment\n'
#    echo -n "$message"
#    path_1="experiments/experiment_generator/experiments/experiment_"
#    path_2="/docker_files/docker_commands_"
#    path_3=".sh"
#
#    complete_file=$path_1$experiment$path_2$orchestrator$path_3
#
#    # Activate the virtual environment
#    source my_env/bin/activate
#
#    # Change the permissions of the files
#    ./setup.sh $experiment
#
#    # Run all the python files
#    ./$complete_file
#    ;;
#
#  external)
#    message=$'External test environment\n'
#    echo -n "$message"
#    path_1="experiments/experiment_generator/experiments/experiment_"
#    path_2="/docker_files/docker_commands_"
#    path_3=".sh"
#
#    complete_file=$path_1$experiment$path_2$orchestrator$path_3
#
#    # Activate the virtual environment
#    source my_env/bin/activate
#
#    # Change the permissions of the files
#    ./setup.sh $experiment
#
#    # Run all the python files
#    ./$complete_file
#    ;;
#
#  *)
#    message=$'Using default external run environment\n'
#    echo -n "$message"
#    path_1="experiments/experiment_generator/experiments/experiment_"
#    path_2="/docker_files/docker_commands_"
#    path_3=".sh"
#
#    complete_file=$path_1$experiment$path_2$orchestrator$path_3
#
#    # Activate the virtual environment
#    source my_env/bin/activate
#
#    # Change the permissions of the files
#    ./setup.sh $experiment
#
#    # Run all the python files
#    ./$complete_file
#    ;;
#esac


#path_1="experiments/experiment_generator/experiments/experiment_"
#path_2="/docker_files/docker_commands_"
#path_3=".sh"
#
#complete_file=$path_1$experiment$path_2$orchestrator$path_3
#
## Activate the virtual environment
#source my_env/bin/activate
#
## Change the permissions of the files
#./setup.sh $experiment
#
## Run all the python files
#./$complete_file