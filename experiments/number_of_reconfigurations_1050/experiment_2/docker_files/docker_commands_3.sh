#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 3 -e 2 -h '0.0.0.0' -p 5004 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 13.91.23.61 --vnf_port 5001 -x f0357124-ae44-11eb-b9e8-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 40.81.204.178 --vnf_port 5002 -x f0357656-ae44-11eb-b9e8-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 20.84.67.101 --vnf_port 5003 -x f035773c-ae44-11eb-b9e8-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.231.152.194 --vnf_port 5005 -x f035784a-ae44-11eb-b9e8-48d705d95785

