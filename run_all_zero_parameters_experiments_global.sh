#!/bin/bash

repetitions=20
NUMBER_OF_UPDATES=150
MAX_DELAY_ARRAY=(0.001 0.1 1.0)
REPETITION_PROBABILITY_ARRAY=(0 5 10)
NEGATION_PROBABILITY_ARRAY=(0 5 10)
WAITING_TIME=30
EXPERIMENT_TYPE=global

for i in $( seq 0 $repetitions )
  do
    python3 experiments/experiment_generator/main_experiment_generator.py $EXPERIMENT_TYPE $NUMBER_OF_UPDATES
#    for item in ${MAX_DELAY_ARRAY[*]}
#      do
#        MAX_DELAY=$item
#        for item2 in ${REPETITION_PROBABILITY_ARRAY[*]}
#          do
#            REPETITION_PROBABILITY=$item2
#            for item3 in ${NEGATION_PROBABILITY_ARRAY[*]}
#              do
#                NEGATION_PROBABILITY=$item3
#                sleep 3
#                ./run_all_experiments.sh $NUMBER_OF_UPDATES $WAITING_TIME $MAX_DELAY $REPETITION_PROBABILITY $NEGATION_PROBABILITY $EXPERIMENT_TYPE
#              done
#          done
#      done
    ((NUMBER_OF_UPDATES=NUMBER_OF_UPDATES+150))
done