#!/bin/bash

# This script is to test the local and external orchestrators with a
# well defined test suite for single, double, triple cases.
# In the case of local test, this can be executed

echo -n "Please type if local or external test: "
read TEST_TYPE

case $TEST_TYPE in

  local)
    message=$'Local test environment\n'
    echo -n "$message"
    ./tests/local/client_commands.sh
    ;;

  external)
    message=$'External test environment\n'
    echo -n "$message"
    ./tests/external/client_commands.sh
    ;;

  "run local")
    echo -n "Please type orchestrator (0-4): "
    read ORCHESTRATOR_INDEX
    path_1="tests/local/trial_"$ORCHESTRATOR_INDEX
    path_3=".sh"
    complete_file=$path_1$path_3

    # Activate the virtual environment
    source my_env/bin/activate

    # Change permission
    chmod +x $complete_file

    # Run all the python files
    ./$complete_file
    ;;

  "run local normal")
    echo -n "Please type orchestrator (0-4): "
    read ORCHESTRATOR_INDEX
    path_1="tests/local/trial_"$ORCHESTRATOR_INDEX
    path_3="_normal.sh"
    complete_file=$path_1$path_3

    # Activate the virtual environment
    source my_env/bin/activate

    # Change permission
    chmod +x $complete_file

    # Run all the python files
    ./$complete_file
    ;;

  "run local all")
    echo -n "Running all local orchestrators "
    path_0="tests/local/trial_0.sh"
    path_1="tests/local/trial_1.sh"
    path_2="tests/local/trial_2.sh"
    path_3="tests/local/trial_3.sh"
    path_4="tests/local/trial_4.sh"

    # Activate the virtual environment
    source my_env/bin/activate

    # Run all the python files
    ./$path_0
    ./$path_1
    ./$path_2
    ./$path_3
    ./$path_4
    echo -n 'Finished'
    ;;

  "run local all normal")
    echo -n "Running all local orchestrators "
    path_0="tests/local/trial_0_normal.sh"
    path_1="tests/local/trial_1_normal.sh"
    path_2="tests/local/trial_2_normal.sh"
    path_3="tests/local/trial_3_normal.sh"
    path_4="tests/local/trial_4_normal.sh"

    # Activate the virtual environment
    source my_env/bin/activate

    # Run all the python files
    ./$path_0
    ./$path_1
    ./$path_2
    ./$path_3
    ./$path_4

    echo -n 'Finished'
    ;;

  "run external")
    echo -n "Please type orchestrator (0-4): "
    read ORCHESTRATOR_INDEX
    path_1="tests/external/trial_"$ORCHESTRATOR_INDEX
    path_3=".sh"
    complete_file=$path_1$path_3

    # Activate the virtual environment
    source my_env/bin/activate

    # Change permission
    chmod +x $complete_file

    # Run all the python files
    ./$complete_file
    ;;

  "run external normal")
    echo -n "Please type orchestrator (0-4): "
    read ORCHESTRATOR_INDEX
    path_1="tests/external/trial_"$ORCHESTRATOR_INDEX
    path_3="_normal.sh"
    complete_file=$path_1$path_3

    # Activate the virtual environment
    source my_env/bin/activate

    # Change permission
    chmod +x $complete_file

    # Run all the python files
    ./$complete_file
    ;;

  *)
    message=$'Using default external test environment\n'
    echo -n "$message"
    ./tests/external/client_commands.sh
    ;;
esac