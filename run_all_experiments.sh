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

EXPERIMENT_NUMBER=0
ALGO_TYPE=0
TEST_TYPE=0
TEST_STRING=concurrent
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
sleep $2
./clean2.sh

##### Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
#### Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
##
### Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
### Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
##./run_all.sh 4 $1 $3 $4 0 0
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
##python3 get_results_vnffg_updates.py 4 $1 causal $3 $4
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

################################## Sequential - Causal ################################################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=0
TEST_TYPE=1
TEST_STRING=sequential

./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
sleep $2
./clean2.sh

## Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

### Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

### Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

## Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 causal $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
echo 'Finish Causal'

########################################### Concurrent - Standard ###################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=1
TEST_TYPE=0
TEST_STRING=concurrent

## First
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
sleep $2
./clean2.sh

## Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
#### Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
### Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
##
### Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

################################## Sequential - Standard #################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=1
TEST_TYPE=1
TEST_STRING=sequential

#First
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
sleep $2
./clean2.sh

### Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 standard $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
echo 'Finish Standard'

########################################### Concurrent - Preventive ###################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=4
TEST_TYPE=0
TEST_STRING=concurrent

## First
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
sleep $2
./clean2.sh

## Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

########################################### Sequential - Preventive ###################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=4
TEST_TYPE=1
TEST_STRING=sequential

## First
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
sleep $2
./clean2.sh

## Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 preventive $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
echo 'Finish Preventive'

########################################### Concurrent - Corrective ###################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=5
TEST_TYPE=0
TEST_STRING=concurrent

## First
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
sleep $2
./clean2.sh

## Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh

########################################### Sequential - Corrective ###################################
EXPERIMENT_NUMBER=0
ALGO_TYPE=5
TEST_TYPE=1
TEST_STRING=sequential

## First
./clean2.sh
./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
sleep $2
python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
sleep $2
./clean2.sh

## Second
#EXPERIMENT_NUMBER=1
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Third
#EXPERIMENT_NUMBER=2
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fourth
#EXPERIMENT_NUMBER=3
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
#
## Fifth
#EXPERIMENT_NUMBER=4
#./clean2.sh
#./run_all.sh $EXPERIMENT_NUMBER $1 $3 $4 $TEST_TYPE $ALGO_TYPE
#sleep $2
#python3 get_results_vnffg_updates.py $EXPERIMENT_NUMBER $1 corrective $3 $4 $TEST_STRING
#sleep $2
#./clean2.sh
echo 'Finish Corrective'


echo 'Finish all algorithms'