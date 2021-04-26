#!/bin/bash

#Clean in case something was running
#./clean2.sh

# This script launches an orchestrator based on the auto-generated experiments
# In the case of external use (cloud) this is the main file to run orchestrators

# REMOVE COMMENTS ONLY FOR DEBUG PURPOSES
echo -n "Please type number of experiment: "
read EXPERIMENT_NUMBER

echo -n "Please type number of orchestrator: "
read ORCHESTRATOR_NUMBER

echo -n "Please type max delay: "
read MAX_DELAY

echo -n "Please type probability: "
read REPETITION_PROBABILITY

#ALGO_TYPE=0 Causal
#ALGO_TYPE=1 Standard
#ALGO_TYPE=2 Last-writer wins
#ALGO_TYPE=3 Multi-value
#ALGO_TYPE=4 Preventive
#ALGO_TYPE=5 Corrective

echo -n "Please type algorithm type 0 Causal | 1 Standard | 4 Preventive | 5 Corrective: "
read ALGO_TYPE

path_1="experiments/experiment_"
path_2="/docker_files/docker_commands_"
path_3=".sh"

complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3

# Activate the virtual environment
source ../my_env/bin/activate
source my_env/bin/activate

complete_file=$path_1$EXPERIMENT_NUMBER$path_2$ORCHESTRATOR_NUMBER$path_3
./setup.sh $EXPERIMENT_NUMBER
#./$complete_file $3 $4 $5 &
./$complete_file $MAX_DELAY $REPETITION_PROBABILITY $ALGO_TYPE &

#sleep 3
#
## Run all the python files
#./$complete_file