#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 1 -e 6 -h '0.0.0.0' -p 5002 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 13.91.23.61 --vnf_port 5001 -x 34a2b448-ae45-11eb-b46c-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 20.84.67.101 --vnf_port 5003 -x 34a2ba10-ae45-11eb-b46c-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 20.68.168.123 --vnf_port 5004 -x 34a2bae2-ae45-11eb-b46c-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 52.231.152.194 --vnf_port 5005 -x 34a2bb5a-ae45-11eb-b46c-48d705d95785

