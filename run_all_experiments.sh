#!/bin/bash

################################# Concurrent updates #################################

# First
./clean2.sh
./run_all.sh 0 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 0 $1 causal $3 $4
sleep $2
./clean2.sh
#
#### Second
./clean2.sh
./run_all.sh 1 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 1 $1 causal $3 $4
sleep $2
./clean2.sh
#
### Third
./clean2.sh
./run_all.sh 2 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 2 $1 causal $3 $4
sleep $2
./clean2.sh
#
## Fourth
./clean2.sh
./run_all.sh 3 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 3 $1 causal $3 $4
sleep $2
./clean2.sh
#
## Fifth
./clean2.sh
./run_all.sh 4 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 4 $1 causal $3 $4
sleep $2
./clean2.sh

################################# Sequential updates #################################
./clean2.sh
./run_all.sh 0 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 0 $1 causal $3 $4
sleep $2
./clean2.sh

## Second
./clean2.sh
./run_all.sh 1 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 1 $1 causal $3 $4
sleep $2
./clean2.sh

## Third
./clean2.sh
./run_all.sh 2 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 2 $1 causal $3 $4
sleep $2
./clean2.sh

## Fourth
./clean2.sh
./run_all.sh 3 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 3 $1 causal $3 $4
sleep $2
./clean2.sh

# Fifth
./clean2.sh
./run_all.sh 4 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 4 $1 causal $3 $4
sleep $2
./clean2.sh

##./clean2.sh
##./run_all.sh 5 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 5 $1 causal $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all.sh 6 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 6 $1 causal $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all.sh 7 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 7 $1 causal $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all.sh 8 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 8 $1 causal $3 $4
##sleep $2
##./clean2.sh
###
##./clean2.sh
##./run_all.sh 9 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 9 $1 causal $3 $4
##sleep $2
##./clean2.sh
###
########################################## First with all the standard algorithms

# First
./clean2.sh
./run_all_standard.sh 0 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 0 $1 standard $3 $4
sleep $2
./clean2.sh

## Second
./clean2.sh
./run_all_standard.sh 1 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 1 $1 standard $3 $4
sleep $2
./clean2.sh
#
## Third
./clean2.sh
./run_all_standard.sh 2 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 2 $1 standard $3 $4
sleep $2
./clean2.sh

# Fourth
./clean2.sh
./run_all_standard.sh 3 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 3 $1 standard $3 $4
sleep $2
./clean2.sh

# Fifth
./clean2.sh
./run_all_standard.sh 4 $1 $3 $4 0
sleep $2
python3 get_results_vnffg_updates.py 4 $1 standard $3 $4
sleep $2
./clean2.sh

################################# Sequential updates #################################
./clean2.sh
./run_all_standard.sh 0 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 0 $1 standard $3 $4
sleep $2
./clean2.sh
#
## Second
./clean2.sh
./run_all_standard.sh 1 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 1 $1 standard $3 $4
sleep $2
./clean2.sh

# Third
./clean2.sh
./run_all_standard.sh 2 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 2 $1 standard $3 $4
sleep $2
./clean2.sh

# Fourth
./clean2.sh
./run_all_standard.sh 3 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 3 $1 standard $3 $4
sleep $2
./clean2.sh

# Fifth
./clean2.sh
./run_all_standard.sh 4 $1 $3 $4 1
sleep $2
python3 get_results_vnffg_updates.py 4 $1 standard $3 $4
sleep $2
./clean2.sh

##./clean2.sh
##./run_all_standard.sh 5 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 5 $1 standard $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all_standard.sh 6 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 6 $1 standard $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all_standard.sh 7 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 7 $1 standard $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all_standard.sh 8 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 8 $1 standard $3 $4
##sleep $2
##./clean2.sh
##
##./clean2.sh
##./run_all_standard.sh 9 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 9 $1 standard $3 $4
##sleep $2
##./clean2.sh
#
######################################## First with all the standard algorithms
##./run_all_last_writer.sh 0 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 0 $1 last_writer
##sleep 1
##
##./run_all_last_writer.sh 1 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 1 $1 last_writer
##
##./run_all_last_writer.sh 2 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 2 $1 last_writer
##
##./run_all_last_writer.sh 3 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 3 $1 last_writer
##
##./run_all_last_writer.sh 4 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 4 $1 last_writer
##
##./run_all_last_writer.sh 5 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 5 $1 last_writer
##
##./run_all_last_writer.sh 6 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 6 $1 last_writer
##
##./run_all_last_writer.sh 7 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 7 $1 last_writer
##
##./run_all_last_writer.sh 8 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 8 $1 last_writer
#
##./run_all_last_writer.sh 9 $1 $3 $4
##sleep $2
##python3 get_results_vnffg_updates.py 9 $1 last_writer
#
#echo 'Finish'