#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 0 -e 8 -h '0.0.0.0' -p 5001 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 40.81.204.178 --vnf_port 5002 -x 12eb89a6-ae45-11eb-a713-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 20.84.67.101 --vnf_port 5003 -x 12eb8a82-ae45-11eb-a713-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 20.68.168.123 --vnf_port 5004 -x 12eb8afa-ae45-11eb-a713-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 52.231.152.194 --vnf_port 5005 -x 12eb8bcc-ae45-11eb-a713-48d705d95785

