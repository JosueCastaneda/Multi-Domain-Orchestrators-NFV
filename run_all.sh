#!/bin/bash

#Clean in case something was running
./clean2.sh

EXPERIMENT_NUMBER=$1
NUMBER_OF_UPDATES=$2
MAX_DELAY=$3
REPETITION_PROBABILITY=$4
TEST_STRING=$5
ALGO_TYPE=$6
NEGATION_PROBABILITY=$7
EXPERIMENT_TYPE=$8

NEW_PATH_0="experiments/number_of_reconfigurations_"
NEW_PATH_1="/experiment_"$EXPERIMENT_NUMBER
NEW_PATH_2="/docker_files/docker_commands_"
NEW_PATH_3=".sh"

# Orch 0
ORCHESTRATOR_NUMBER=0
complete_file_new=$NEW_PATH_0$NUMBER_OF_UPDATES$NEW_PATH_1$NEW_PATH_2$ORCHESTRATOR_NUMBER$NEW_PATH_3
./setup.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES
./$complete_file_new $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY $NUMBER_OF_UPDATES &
sleep 3

# Orch 1
ORCHESTRATOR_NUMBER=1
complete_file_new=$NEW_PATH_0$NUMBER_OF_UPDATES$NEW_PATH_1$NEW_PATH_2$ORCHESTRATOR_NUMBER$NEW_PATH_3
./setup.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES
./$complete_file_new $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY $NUMBER_OF_UPDATES &
sleep 3

# Orch 2
ORCHESTRATOR_NUMBER=2
complete_file_new=$NEW_PATH_0$NUMBER_OF_UPDATES$NEW_PATH_1$NEW_PATH_2$ORCHESTRATOR_NUMBER$NEW_PATH_3
./setup.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES
./$complete_file_new $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY $NUMBER_OF_UPDATES &
sleep 3

# Orch 3
ORCHESTRATOR_NUMBER=3
complete_file_new=$NEW_PATH_0$NUMBER_OF_UPDATES$NEW_PATH_1$NEW_PATH_2$ORCHESTRATOR_NUMBER$NEW_PATH_3
./setup.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES
./$complete_file_new $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY $NUMBER_OF_UPDATES &
sleep 3

# Orch 4
ORCHESTRATOR_NUMBER=4
complete_file_new=$NEW_PATH_0$NUMBER_OF_UPDATES$NEW_PATH_1$NEW_PATH_2$ORCHESTRATOR_NUMBER$NEW_PATH_3
./setup.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES
./$complete_file_new $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE $NEGATION_PROBABILITY $NUMBER_OF_UPDATES &

VAR1="global"
VAR2="local"

if [ $TEST_STRING -eq 0 ]; then
  if [ $EXPERIMENT_TYPE == $VAR1 ]; then
    echo './test_asynchronous_vnffg_updates_global.sh'
    sleep 10
    ./test_asynchronous_vnffg_updates_global.sh
  else
    echo './test_asynchronous_vnffg_updates_local.sh'
    sleep 10
    ./test_asynchronous_vnffg_updates_local.sh
  fi
else
  if [ $EXPERIMENT_TYPE == $VAR1 ]; then
#    echo './test_sequential_vnffg_updates_global.sh'
    sleep 10
    ./test_sequential_vnffg_updates_global.sh
  else
#    echo './test_sequential_vnffg_updates_local.sh'
    sleep 10
    ./test_sequential_vnffg_updates_local.sh
  fi
fi
sleep 45