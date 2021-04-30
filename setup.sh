#!/bin/bash

EXPERIMENT=$1
NUMBER_OF_UPDATES=$2
NEW_PATH_0="experiments/number_of_reconfigurations_"
NEW_PATH_1="/experiment_"$EXPERIMENT


path_1=$NEW_PATH_0$NUMBER_OF_UPDATES$NEW_PATH_1

#path_1="experiments/experiment_"$EXPERIMENT
dock_commands_0="/docker_files/docker_commands_0.sh"
dock_commands_1="/docker_files/docker_commands_1.sh"
dock_commands_2="/docker_files/docker_commands_2.sh"
dock_commands_3="/docker_files/docker_commands_3.sh"
dock_commands_4="/docker_files/docker_commands_4.sh"

# Give permissions to the docker file
chmod +x "$path_1$dock_commands_0"
chmod +x "$path_1$dock_commands_1"
chmod +x "$path_1$dock_commands_2"
chmod +x "$path_1$dock_commands_3"
chmod +x "$path_1$dock_commands_4"