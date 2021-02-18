#!/bin/bash

#Clean in case something was running
./clean2.sh

path_1="experiments/experiment_"
path_2="/docker_files/docker_commands_"
path_3=".sh"

## Activate the virtual environment
#source ../my_env/bin/activate
#source my_env/bin/activate

# Orch 0
#echo -n "Please type experiment: "
#read EXPERIMENT_NUMBER
EXPERIMENT_NUMBER=$1
ORCHESTRATOR_NUMBER=0
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
# Change the permissions of the files
./setup.sh $EXPERIMENT_NUMBER

# Run all the python files
./$complete_file $3 $4 &
sleep 3

# Orch 1
ORCHESTRATOR_NUMBER=1
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file $3 $4 &
sleep 3

# Orch 2
ORCHESTRATOR_NUMBER=2
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file $3 $4 &
sleep 3

# Orch 3
ORCHESTRATOR_NUMBER=3
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file $3 $4 &
sleep 3

# Orch 4
ORCHESTRATOR_NUMBER=4
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file $3 $4 &
sleep 3
echo "Testing Parallel reconfiguration"
sleep 1
./test_reconfiguration_parallel.sh $EXPERIMENT_NUMBER