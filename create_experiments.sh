#!/bin/bash

type_of_deployment=$1
path_1="experiments/experiment_generator/main_experiment_generator.py "$type_of_deployment

python "$path_1"