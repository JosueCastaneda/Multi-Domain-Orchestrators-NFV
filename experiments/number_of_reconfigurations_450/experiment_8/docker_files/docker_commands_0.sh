#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 0 -e 8 -h '0.0.0.0' -p 5001 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 40.81.204.178 --vnf_port 5002 -x de6b2812-ae44-11eb-838b-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 20.84.67.101 --vnf_port 5003 -x de6b28b2-ae44-11eb-838b-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 20.68.168.123 --vnf_port 5004 -x de6b292a-ae44-11eb-838b-48d705d95785
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 52.231.152.194 --vnf_port 5005 -x de6b2998-ae44-11eb-838b-48d705d95785

