#!/bin/bash

## 32 Concurrent messages
#python3 experiments/experiment_generator/main_experiment_generator.py local 2
#sleep 5
## Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
#./run_all_experiments.sh 32 50 10 0
#./run_all_experiments.sh 64 500 30 0
#./run_all_experiments.sh 64 500 30 10
#./run_all_experiments.sh 64 500 30 30
#./run_all_experiments.sh 64 500 30 50
#./run_all_experiments.sh 576 500 60 0


## 64 Concurrent messages
#python3 experiments/experiment_generator/main_experiment_generator.py local 64
#sleep 30
## Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
#./run_all_experiments.sh 64 10 10 0
#./run_all_experiments.sh 64 500 30 0
#./run_all_experiments.sh 64 500 30 10
#./run_all_experiments.sh 64 500 30 30
#./run_all_experiments.sh 64 500 30 50
#./run_all_experiments.sh 576 500 60 0

## 128

## 192 Concurrent messages
#python3 experiments/experiment_generator/main_experiment_generator.py local 192
#sleep 5
## Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
#./run_all_experiments.sh 192 150 10 0
#./run_all_experiments.sh 576 500 30 0
#./run_all_experiments.sh 576 500 30 10
#./run_all_experiments.sh 576 500 30 30
##./run_all_experiments.sh 192 150 30 50
#./run_all_experiments.sh 576 500 60 0

##256

### 320 Concurrent messages
#python3 experiments/experiment_generator/main_experiment_generator.py local 1
#sleep 10
### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
#./run_all_experiments.sh 320 150 10 0
##./run_all_experiments.sh 576 500 30 0
##./run_all_experiments.sh 576 500 30 10
#./run_all_experiments.sh 576 500 30 30
./run_all_experiments.sh 1 150 30 50
##./run_all_experiments.sh 576 500 60 0
#
### 384 Concurrent messages
#python3 experiments/experiment_generator/main_experiment_generator.py local 384
#sleep 10
### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
#./run_all_experiments.sh 384 150 10 0
##./run_all_experiments.sh 576 500 30 0
##./run_all_experiments.sh 576 500 30 10
##./run_all_experiments.sh 576 500 30 30
###./run_all_experiments.sh 384 150 30 50
##./run_all_experiments.sh 576 500 60 0
#
### 448 Concurrent messages
#python3 experiments/experiment_generator/main_experiment_generator.py local 448
#sleep 10
### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
#./run_all_experiments.sh 448 150 10 0
##./run_all_experiments.sh 576 500 30 0
##./run_all_experiments.sh 576 500 30 10
##./run_all_experiments.sh 576 500 30 30
###./run_all_experiments.sh 448 150 30 50
##./run_all_experiments.sh 576 500 60 0
#
## 512 Concurrent messages
##python3 experiments/experiment_generator/main_experiment_generator.py local 512
##sleep 5
#### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
##./run_all_experiments.sh 512 150 10 0
###./run_all_experiments.sh 512 100 30 0
###./run_all_experiments.sh 512 100 30 10
###./run_all_experiments.sh 512 100 30 30
##./run_all_experiments.sh 512 150 30 50
###./run_all_experiments.sh 512 100 60 0
##
#
### 576 Concurrent messages
##python3 experiments/experiment_generator/main_experiment_generator.py local 576
##sleep 5
### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
##./run_all_experiments.sh 576 150 10 0
##./run_all_experiments.sh 576 500 30 0
##./run_all_experiments.sh 576 500 30 10
##./run_all_experiments.sh 576 500 30 30
##./run_all_experiments.sh 576 150 30 50
##./run_all_experiments.sh 576 500 60 0
#
### 640 Concurrent messages
##python3 experiments/experiment_generator/main_experiment_generator.py local 640
##sleep 10
### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
##./run_all_experiments.sh 640 500 10 0
##./run_all_experiments.sh 576 500 30 0
##./run_all_experiments.sh 576 500 30 10
##./run_all_experiments.sh 576 500 30 30
##./run_all_experiments.sh 640 150 30 50
##./run_all_experiments.sh 576 500 60 0
#
#
### 800 Concurrent messages
### Set the Maximum delay to 30 seconds and variate probability of messages from 10 to 50
##./run_all_experiments.sh 800 60 30 10
##./run_all_experiments.sh 800 60 30 30
##./run_all_experiments.sh 800 60 30 50