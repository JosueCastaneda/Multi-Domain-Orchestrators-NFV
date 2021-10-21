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
EXPERIMENT_REPETITIONS=30
EXPERIMENT_REPETITIONS_PLUS_ONE=31
EXPERIMENT_TYPE=$6

#ALGO_TYPE=0
#TEST_TYPE=0
#TEST_STRING=concurrent
#ALGO_NAME=causal
#
#for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
#  do
#    ./clean2.sh
#    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
#    sleep $WAITING_TIME
#    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
#    sleep $WAITING_TIME
#    ./clean2.sh
#done


################################### Sequential - Causal ################################################################
#ALGO_TYPE=0
#TEST_TYPE=1
#TEST_STRING=sequential
#ALGO_NAME=causal
#
#for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
#  do
#    ./clean2.sh
#    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
#    sleep $WAITING_TIME
#    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
#    sleep $WAITING_TIME
#    ./clean2.sh
#done
#
#echo 'Finish Causal'
#
############################################ Concurrent - Standard ###################################
ALGO_TYPE=1
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=standard

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    NEW_DELAY=""
    if [ "$MAX_DELAY" == "0.001" ]
    then
      NEW_DELAY="1.0"
    elif [ "$MAX_DELAY" == "0.01" ]
    then
      NEW_DELAY="10.0"
    elif [ "$MAX_DELAY" == "0.1" ]
    then
      NEW_DELAY="100.0"
    elif [ "$MAX_DELAY" == "1.0" ]
    then
      NEW_DELAY="1000.0"
    fi
    FILE_PATH='/results/results_experiment_'$NUMBER_OF_UPDATES'/'
    FILE_NAME_1='result_algorithm_*'$ALGO_NAME'*_type_*'$TEST_STRING'*_negationProbability_*'$NEGATION_PROBABILITY
    FILE_NAME_2='*_delay_*'$NEW_DELAY'*_repetitionProbability_*'$REPETITION_PROBABILITY'*.csv'
    CURRENT_DIRECTORY=$PWD
    FILE=$CURRENT_DIRECTORY$FILE_PATH$FILE_NAME_1$FILE_NAME_2
    NUMBER_OF_WRITES=$(wc -l < "$FILE")
#    echo $NUMBER_OF_WRITES
#    if test -f "$FILE"; then
#      echo 'File exists'
#    fi
#
#    if [ $NUMBER_OF_WRITES -gt $EXPERIMENT_REPETITIONS ]; then
#      echo 'Already did all experiments'
#    fi

    if test -f "$FILE"  && [ $NUMBER_OF_WRITES -gt $EXPERIMENT_REPETITIONS_PLUS_ONE ]; then
      NEW_DELAY="222"
#      echo 'I dectect'
#      sleep 10000
    else
      echo "$FILE does not exist or lines lower than " "$EXPERIMENT_REPETITIONS_PLUS_ONE"
#      sleep 9999
      ./clean2.sh
      ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
      sleep $WAITING_TIME
      python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
      sleep $WAITING_TIME
      ./clean2.sh
    fi

done

################################### Sequential - Standard #################################
#ALGO_TYPE=1
#TEST_TYPE=1
#TEST_STRING=sequential
#ALGO_NAME=standard
#
#for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
#  do
#    ./clean2.sh
#    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
#    sleep $WAITING_TIME
#    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
#    sleep $WAITING_TIME
#    ./clean2.sh
#done
#
#echo 'Finish Standard'

############################################ Concurrent - Preventive ###################################
ALGO_TYPE=4
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=preventive

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    NEW_DELAY=""
    if [ "$MAX_DELAY" == "0.001" ]
    then
      NEW_DELAY="1.0"
    elif [ "$MAX_DELAY" == "0.01" ]
    then
      NEW_DELAY="10.0"
    elif [ "$MAX_DELAY" == "0.1" ]
    then
      NEW_DELAY="100.0"
    elif [ "$MAX_DELAY" == "1.0" ]
    then
      NEW_DELAY="1000.0"
    fi
    FILE_PATH='/results/results_experiment_'$NUMBER_OF_UPDATES'/'
    FILE_NAME_1='result_algorithm_*'$ALGO_NAME'*_type_*'$TEST_STRING'*_negationProbability_*'$NEGATION_PROBABILITY
    FILE_NAME_2='*_delay_*'$NEW_DELAY'*_repetitionProbability_*'$REPETITION_PROBABILITY'*.csv'
    CURRENT_DIRECTORY=$PWD
    FILE=$CURRENT_DIRECTORY$FILE_PATH$FILE_NAME_1$FILE_NAME_2
    NUMBER_OF_WRITES=$(wc -l < "$FILE")

    if test -f "$FILE" && [ $NUMBER_OF_WRITES -gt $EXPERIMENT_REPETITIONS_PLUS_ONE ]; then
#      echo "$FILE exists."
      NEW_DELAY="200"
    else
      echo "$FILE does not exist."
      ./clean2.sh
      ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
      sleep $WAITING_TIME
      python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
      sleep $WAITING_TIME
      ./clean2.sh
    fi
done

############################################ Sequential - Preventive ###################################
#ALGO_TYPE=4
#TEST_TYPE=1
#TEST_STRING=sequential
#ALGO_NAME=preventive
#
#for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
#  do
#    ./clean2.sh
#    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
#    sleep $WAITING_TIME
#    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
#    sleep $WAITING_TIME
#    ./clean2.sh
#done
#
#echo 'Finish Preventive'

############################################ Concurrent - Corrective ###################################
ALGO_TYPE=5
TEST_TYPE=0
TEST_STRING=concurrent
ALGO_NAME=corrective

for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
  do
    NEW_DELAY=""

    if [ "$MAX_DELAY" == "0.001" ]
    then
      NEW_DELAY="1.0"
    elif [ "$MAX_DELAY" == "0.01" ]
    then
      NEW_DELAY="10.0"
    elif [ "$MAX_DELAY" == "0.1" ]
    then
      NEW_DELAY="100.0"
    elif [ "$MAX_DELAY" == "1.0" ]
    then
      NEW_DELAY="1000.0"
    fi
    FILE_PATH='/results/results_experiment_'$NUMBER_OF_UPDATES'/'
    FILE_NAME_1='result_algorithm_*'$ALGO_NAME'*_type_*'$TEST_STRING'*_negationProbability_*'$NEGATION_PROBABILITY
    FILE_NAME_2='*_delay_*'$NEW_DELAY'*_repetitionProbability_*'$REPETITION_PROBABILITY'*.csv'
    CURRENT_DIRECTORY=$PWD
    FILE=$CURRENT_DIRECTORY$FILE_PATH$FILE_NAME_1$FILE_NAME_2
    NUMBER_OF_WRITES=$(wc -l < "$FILE")

    if test -f "$FILE" && [ $NUMBER_OF_WRITES -gt $EXPERIMENT_REPETITIONS_PLUS_ONE ]; then
      #echo "$FILE exists."
      NEW_DELAY=6
    else
      echo "$FILE does not exist."
      ./clean2.sh
      ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
      sleep $WAITING_TIME
      python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
      sleep $WAITING_TIME
      ./clean2.sh
    fi
done

############################################ Sequential - Corrective ###################################
#EXPERIMENT_NUMBER=0
#ALGO_TYPE=5
#TEST_TYPE=1
#TEST_STRING=sequential
#ALGO_NAME=corrective
#
#for EXPERIMENT_NUMBER in $( seq 0 $EXPERIMENT_REPETITIONS )
#  do
#    ./clean2.sh
#    ./run_all.sh $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $MAX_DELAY $REPETITION_PROBABILITY $TEST_TYPE $ALGO_TYPE $NEGATION_PROBABILITY $EXPERIMENT_TYPE
#    sleep $WAITING_TIME
#    python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $NUMBER_OF_UPDATES $ALGO_NAME $MAX_DELAY $REPETITION_PROBABILITY $TEST_STRING $NEGATION_PROBABILITY
#    sleep $WAITING_TIME
#    ./clean2.sh
#done
#
#echo 'Finish Corrective'
#echo 'Finish all algorithms'