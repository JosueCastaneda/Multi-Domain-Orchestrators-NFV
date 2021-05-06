#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 2 -e 0 -h '0.0.0.0' -p 5003 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 13.91.23.61 --vnf_port 5001 -x 55224fdc-ae8e-11eb-bef0-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 40.81.204.178 --vnf_port 5002 -x 552256a8-ae8e-11eb-bef0-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 20.68.168.123 --vnf_port 5004 -x 5522589c-ae8e-11eb-bef0-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 52.231.152.194 --vnf_port 5005 -x 55225978-ae8e-11eb-bef0-48d705d95785

