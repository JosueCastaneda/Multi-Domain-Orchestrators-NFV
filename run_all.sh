#!/bin/bash

#Clean in case something was running
./clean2.sh

path_1="experiments/experiment_"
path_2="/docker_files/docker_commands_"
path_3=".sh"

EXPERIMENT_NUMBER=$1
NUMBER_OF_UPDATES=$2
MAX_DELAY=$3
REPETITION_PROBABILITY=$4
TEST_STRING=$5
ALGO_TYPE=$6
NEGATION_PROBABILITY=$7

# Orch 0
EXPERIMENT_NUMBER=$1
ORCHESTRATOR_NUMBER=0
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
echo "Calling orchestator script algo_type $ALGO_TYPE neg_prob $NEGATION_PROBABILITY"
sleep 5
./$complete_file $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY &
sleep 3
#sleep 10

# Orch 1
ORCHESTRATOR_NUMBER=1
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
#./$complete_file $3 $4 $5 &
./$complete_file $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY &
sleep 3

# Orch 2
ORCHESTRATOR_NUMBER=2
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
#./$complete_file $3 $4 $5 &
./$complete_file $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY &
sleep 3

# Orch 3
ORCHESTRATOR_NUMBER=3
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
#./$complete_file $3 $4 $5 &
./$complete_file $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY &
sleep 3

# Orch 4
ORCHESTRATOR_NUMBER=4
complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
./$complete_file $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY &

if [ $TEST_STRING -eq 0 ]
then
echo 'Testing asynchronous updates'
sleep 4
./test_asynchronous_vnffg_updates.sh
else
echo 'Testing sequential updates'
sleep 4
./test_sequential_vnffg_updates.sh
fi

