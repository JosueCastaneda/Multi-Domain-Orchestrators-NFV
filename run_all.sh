#!/bin/bash

#Clean in case something was running
./clean2.sh

path_1="experiments/experiment_"
path_2="/docker_files/docker_commands_"
path_3=".sh"

# Orch 0
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
#sleep 3
#echo "Testing Parallel reconfiguration"
#sleep 1
#./test_reconfiguration_parallel.sh $EXPERIMENT_NUMBER

#sleep 10
if [ $5 -eq 0 ]
then
echo 'Testing asynchronous updates'
sleep 4
./test_asynchronous_vnffg_updates.sh
else
echo 'Testing sequential updates'
sleep 4
./test_sequential_vnffg_updates.sh
fi

