#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 3 -e 4 -h '0.0.0.0' -p 5004 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 13.91.23.61 --vnf_port 5001 -x 301ac1b6-ada7-11eb-8bfc-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 40.81.204.178 --vnf_port 5002 -x 301ac454-ada7-11eb-8bfc-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 20.84.67.101 --vnf_port 5003 -x 301ac4fe-ada7-11eb-8bfc-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.231.193.62 --vnf_port 5005 -x 301ac5da-ada7-11eb-8bfc-48d705d95785

