#!/bin/bash

repetitions=1
NUMBER_OF_UPDATES=300
MAX_DELAY_ARRAY=(0.001 0.1 1.0)
REPETITION_PROBABILITY_ARRAY=(0 5 10)
NEGATION_PROBABILITY_ARRAY=(0 5 10)
WAITING_TIME=30

for i in $( seq 0 $repetitions )
  do
    for item in ${MAX_DELAY_ARRAY[*]}
      do
        MAX_DELAY=$item
        for item2 in ${REPETITION_PROBABILITY_ARRAY[*]}
          do
            REPETITION_PROBABILITY=$item2
            for item3 in ${NEGATION_PROBABILITY_ARRAY[*]}
              do
                NEGATION_PROBABILITY=$item3
                python3 experiments/experiment_generator/main_experiment_generator.py local $NUMBER_OF_UPDATES
                sleep 5
                ./run_all_experiments.sh $NUMBER_OF_UPDATES $WAITING_TIME $MAX_DELAY $REPETITION_PROBABILITY $NEGATION_PROBABILITY
              done
          done
      done
    ((NUMBER_OF_UPDATES=NUMBER_OF_UPDATES+150))
done