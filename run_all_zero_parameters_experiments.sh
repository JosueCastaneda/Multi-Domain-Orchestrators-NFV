#!/bin/bash

### 64 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 64
./run_all_experiments.sh 64 120 10 0
./run_all_experiments.sh 64 120 30 0
./run_all_experiments.sh 64 120 30 10
./run_all_experiments.sh 64 120 30 30
./run_all_experiments.sh 64 120 30 50
./run_all_experiments.sh 64 120 60 0
sleep 5

## 128
python3 experiments/experiment_generator/main_experiment_generator.py local 128
./run_all_experiments.sh 128 120 10 0
./run_all_experiments.sh 128 120 30 0
./run_all_experiments.sh 128 120 30 10
./run_all_experiments.sh 128 120 30 30
./run_all_experiments.sh 128 120 30 50
./run_all_experiments.sh 128 120 60 0
sleep 5

## 192 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 192
./run_all_experiments.sh 192 120 10 0
./run_all_experiments.sh 192 120 30 0
./run_all_experiments.sh 192 120 30 10
./run_all_experiments.sh 192 120 30 30
./run_all_experiments.sh 192 120 30 50
./run_all_experiments.sh 192 120 60 0
sleep 5

##256
python3 experiments/experiment_generator/main_experiment_generator.py local 256
./run_all_experiments.sh 256 120 10 0
./run_all_experiments.sh 256 120 30 0
./run_all_experiments.sh 256 120 30 10
./run_all_experiments.sh 256 120 30 30
./run_all_experiments.sh 256 120 30 50
./run_all_experiments.sh 256 120 60 0
sleep 5

## 320 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 320
./run_all_experiments.sh 320 120 10 0
./run_all_experiments.sh 320 120 30 0
./run_all_experiments.sh 320 120 30 10
./run_all_experiments.sh 320 120 30 30
./run_all_experiments.sh 320 120 30 50
./run_all_experiments.sh 320 120 60 0
sleep 5

## 384 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 384
./run_all_experiments.sh 384 120 10 0
./run_all_experiments.sh 384 120 30 0
./run_all_experiments.sh 384 120 30 10
./run_all_experiments.sh 384 120 30 30
./run_all_experiments.sh 384 120 30 50
./run_all_experiments.sh 384 120 60 0
sleep 5

## 448 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 448
./run_all_experiments.sh 448 120 10 0
./run_all_experiments.sh 448 120 30 0
./run_all_experiments.sh 448 120 30 10
./run_all_experiments.sh 448 120 30 30
./run_all_experiments.sh 448 120 30 50
./run_all_experiments.sh 448 120 60 0
sleep 5

# 512 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 512
./run_all_experiments.sh 512 120 10 0
./run_all_experiments.sh 512 120 30 0
./run_all_experiments.sh 512 120 30 10
./run_all_experiments.sh 512 120 30 30
./run_all_experiments.sh 512 120 30 50
./run_all_experiments.sh 512 120 60 0
sleep 5

## 576 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 576
./run_all_experiments.sh 576 120 10 0
./run_all_experiments.sh 576 120 30 0
./run_all_experiments.sh 576 120 30 10
./run_all_experiments.sh 576 120 30 30
./run_all_experiments.sh 576 120 30 50
./run_all_experiments.sh 576 120 60 0
sleep 5

### 640 Concurrent messages
python3 experiments/experiment_generator/main_experiment_generator.py local 640
./run_all_experiments.sh 640 120 10 0
./run_all_experiments.sh 640 120 30 0
./run_all_experiments.sh 640 120 30 10
./run_all_experiments.sh 640 120 30 30
./run_all_experiments.sh 640 120 30 50
./run_all_experiments.sh 640 120 60 0

## MAX: 800 Concurrent updates
#python3 experiments/experiment_generator/main_experiment_generator.py local 800
#./run_all_experiments.sh 800 120 10 0
#./run_all_experiments.sh 800 120 30 0
#./run_all_experiments.sh 800 120 30 10
#./run_all_experiments.sh 800 120 30 30
#./run_all_experiments.sh 800 120 30 50
#./run_all_experiments.sh 800 120 60 0