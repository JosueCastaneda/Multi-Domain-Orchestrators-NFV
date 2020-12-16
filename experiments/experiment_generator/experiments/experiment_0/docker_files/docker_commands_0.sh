#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 0 -e 0 -h '127.0.0.1' -p 4437 -r 44257 &

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x c86c735b-3efe-11eb-bde0-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x c86c735c-3efe-11eb-bde0-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x c86c735d-3efe-11eb-bde0-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x c86c735e-3efe-11eb-bde0-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 0 -e 0 -h '127.0.0.1' -p 3001 &
python vnf_script.py -i 1 -o 0 -e 0 -h '127.0.0.1' -p 3002 &
python vnf_script.py -i 2 -o 0 -e 0 -h '127.0.0.1' -p 3003 &
python vnf_script.py -i 3 -o 0 -e 0 -h '127.0.0.1' -p 3004 &
python vnf_script.py -i 4 -o 0 -e 0 -h '127.0.0.1' -p 3005 &
python vnf_script.py -i 5 -o 0 -e 0 -h '127.0.0.1' -p 3006 &
python vnf_script.py -i 6 -o 0 -e 0 -h '127.0.0.1' -p 3007 &
python vnf_script.py -i 7 -o 0 -e 0 -h '127.0.0.1' -p 3008 &
python vnf_script.py -i 8 -o 0 -e 0 -h '127.0.0.1' -p 3009 &
python vnf_script.py -i 9 -o 0 -e 0 -h '127.0.0.1' -p 3010 &

