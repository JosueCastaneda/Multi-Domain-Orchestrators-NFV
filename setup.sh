#!/bin/bash

experiment=$1

path_1="experiments/experiment_generator/experiments/experiment_"$experiment
dock_commands_0="/docker_files/docker_commands_0.sh"
dock_commands_1="/docker_files/docker_commands_1.sh"
dock_commands_2="/docker_files/docker_commands_2.sh"
dock_commands_3="/docker_files/docker_commands_3.sh"
dock_commands_4="/docker_files/docker_commands_4.sh"

dock_commands_normal_0="/docker_files/docker_commands_normal_0.sh"
dock_commands_normal_1="/docker_files/docker_commands_normal_1.sh"
dock_commands_normal_2="/docker_files/docker_commands_normal_2.sh"
dock_commands_normal_3="/docker_files/docker_commands_normal_3.sh"
dock_commands_normal_4="/docker_files/docker_commands_normal_4.sh"

# Give permissions to the docker file
chmod +x "$path_1$dock_commands_0"
chmod +x "$path_1$dock_commands_1"
chmod +x "$path_1$dock_commands_2"
chmod +x "$path_1$dock_commands_3"
chmod +x "$path_1$dock_commands_4"

# Give permissions to the docker normal file
chmod +x "$path_1$dock_commands_normal_0"
chmod +x "$path_1$dock_commands_normal_1"
chmod +x "$path_1$dock_commands_normal_2"
chmod +x "$path_1$dock_commands_normal_3"
chmod +x "$path_1$dock_commands_normal_4"