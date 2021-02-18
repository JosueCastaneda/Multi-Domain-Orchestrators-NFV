#!/bin/bash

#Clean in case something was running
./clean2.sh

path_1="experiments/experiment_generator/experiments/experiment_"
path_2="/docker_files/docker_commands_standard_"
path_3=".sh"

# Activate the virtual environment
source ../my_env/bin/activate
source my_env/bin/activate

# Orch 0
#echo -n "Please type experiment: "
#read EXPERIMENT_NUMBER
EXPERIMENT_NUMBER=$1

ORCHESTRATOR_NUMBER=0
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3

# Change the permissions of the files
./setup.sh $EXPERIMENT_NUMBER

# Run all the python files
./$complete_file &

# Orch 1
ORCHESTRATOR_NUMBER=1
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file &

# Orch 2
ORCHESTRATOR_NUMBER=2
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file &

# Orch 3
ORCHESTRATOR_NUMBER=3
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file &

# Orch 4
ORCHESTRATOR_NUMBER=4
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file &

sleep 5
#
#./test_reconfiguration_parallel.sh $EXPERIMENT_NUMBER
echo 'Testing asynchronous updates'
sleep 2
./test_asynchronous_vnffg_updates.sh