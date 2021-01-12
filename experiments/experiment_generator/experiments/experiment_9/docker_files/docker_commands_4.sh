#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 4 -e 9 -h '127.0.0.1' -p 4445 -r 276529 -a 0 &

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x f8dc8aaa-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x f8dc8aab-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x f8dc8aac-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x f8dc8aad-54fe-11eb-bec1-04ea56f99520

# Instantiate the orchestrator's VNFs 
python3 vnf_script.py -i 0 -o 4 -e 9 -h '127.0.0.1' -p 3041 &
python3 vnf_script.py -i 1 -o 4 -e 9 -h '127.0.0.1' -p 3042 &
python3 vnf_script.py -i 2 -o 4 -e 9 -h '127.0.0.1' -p 3043 &
python3 vnf_script.py -i 3 -o 4 -e 9 -h '127.0.0.1' -p 3044 &
python3 vnf_script.py -i 4 -o 4 -e 9 -h '127.0.0.1' -p 3045 &
python3 vnf_script.py -i 5 -o 4 -e 9 -h '127.0.0.1' -p 3046 &
python3 vnf_script.py -i 6 -o 4 -e 9 -h '127.0.0.1' -p 3047 &
python3 vnf_script.py -i 7 -o 4 -e 9 -h '127.0.0.1' -p 3048 &
python3 vnf_script.py -i 8 -o 4 -e 9 -h '127.0.0.1' -p 3049 &
python3 vnf_script.py -i 9 -o 4 -e 9 -h '127.0.0.1' -p 3050 &

