#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 1 -e 5 -h '0.0.0.0' -p 5002 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 13.91.23.61 --vnf_port 5001 -x e6a425a6-ae44-11eb-a1e2-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 20.84.67.101 --vnf_port 5003 -x e6a42966-ae44-11eb-a1e2-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 20.68.168.123 --vnf_port 5004 -x e6a429f2-ae44-11eb-a1e2-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 52.231.152.194 --vnf_port 5005 -x e6a42a9c-ae44-11eb-a1e2-48d705d95785

