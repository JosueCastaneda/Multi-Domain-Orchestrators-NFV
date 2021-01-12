#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 1 -e 0 -h '127.0.0.1' -p 4439 -r 276529 -a 0 &

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x b30550dc-54ec-11eb-bec1-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x b30550de-54ec-11eb-bec1-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x b30550df-54ec-11eb-bec1-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x b30550e0-54ec-11eb-bec1-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 1 -e 0 -h '127.0.0.1' -p 3011 &
python vnf_script.py -i 1 -o 1 -e 0 -h '127.0.0.1' -p 3012 &
python vnf_script.py -i 2 -o 1 -e 0 -h '127.0.0.1' -p 3013 &
python vnf_script.py -i 3 -o 1 -e 0 -h '127.0.0.1' -p 3014 &
python vnf_script.py -i 4 -o 1 -e 0 -h '127.0.0.1' -p 3015 &
python vnf_script.py -i 5 -o 1 -e 0 -h '127.0.0.1' -p 3016 &
python vnf_script.py -i 6 -o 1 -e 0 -h '127.0.0.1' -p 3017 &
python vnf_script.py -i 7 -o 1 -e 0 -h '127.0.0.1' -p 3018 &
python vnf_script.py -i 8 -o 1 -e 0 -h '127.0.0.1' -p 3019 &
python vnf_script.py -i 9 -o 1 -e 0 -h '127.0.0.1' -p 3020 &

