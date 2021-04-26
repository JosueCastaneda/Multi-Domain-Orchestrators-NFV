#!/bin/bash

################################# Concurrent - Causal ################################################################
# Definition
#TEST_TYPE=0 Concurrent
#TEST_TYPE=1 Sequential

#ALGO_TYPE=0 Causal
#ALGO_TYPE=1 Standard
#ALGO_TYPE=2 Last-writer wins
#ALGO_TYPE=3 Multi-value
#ALGO_TYPE=4 Preventive
#ALGO_TYPE=5 Corrective

NUMBER_OF_UPDATES=$1
WAITING_TIME=$2
MAX_DELAY=$3
REPETITION_PROBABILITY=$4
NEGATION_PROBABILITY=$5
EXPERIMENT_REPETITIONS=4

#echo "NUMBER_OF_UPDATES $1  MAX_DELAY $3 REPETITION_PROBABILITY $4 NEGATION_PROBABILITY $5"
#echo "NUMBER_OF_UPDATES $NUMBER_OF_UPDATES  MAX_DELAY $MAX_DELAY REPETITION_PROBABILITY $REPETITION_PROBABILITY NEGATION_PROBABILITY $NEGATION_PROBABILITY"
#sleep 10

#EXPERIMENT_NUMBER=0

ALGO_TYPE=0
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=causal

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done


################################### Sequential - Causal ################################################################
ALGO_TYPE=0
TEST_TYPE=1
TEST_STRING=sequential
ALGO_NAME=causal

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

echo 'Finish Causal'
#
############################################ Concurrent - Standard ###################################
ALGO_TYPE=1
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=standard

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

################################### Sequential - Standard #################################
ALGO_TYPE=1
TEST_TYPE=1
TEST_STRING=sequential
ALGO_NAME=standard

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

echo 'Finish Standard'

############################################ Concurrent - Preventive ###################################
ALGO_TYPE=4
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=preventive

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

############################################ Sequential - Preventive ###################################
ALGO_TYPE=4
TEST_TYPE=1
TEST_STRING=sequential
ALGO_NAME=preventive

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

echo 'Finish Preventive'

############################################ Concurrent - Corrective ###################################
ALGO_TYPE=5
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=corrective

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

############################################ Sequential - Corrective ###################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=5
TEST_TYPE=1
TEST_STRING=sequential
ALGO_NAME=corrective

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    ./clean2.sh
    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
    sleep $WAITING_TIME
    ./clean2.sh
done

echo 'Finish Corrective'
echo 'Finish all algorithms'