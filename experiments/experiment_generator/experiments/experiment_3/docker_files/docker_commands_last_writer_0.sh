#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 0 -e 3 -h '127.0.0.1' -p 4437 -r 276529 -a 2 &

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x f8dc8aab-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x f8dc8aac-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x f8dc8aad-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x f8dc8aae-54fe-11eb-bec1-04ea56f99520

python3 vnf_script.py -i 0 -o 0 -e 3 -h '127.0.0.1' -p 3001 &
python3 vnf_script.py -i 1 -o 0 -e 3 -h '127.0.0.1' -p 3002 &
python3 vnf_script.py -i 2 -o 0 -e 3 -h '127.0.0.1' -p 3003 &
python3 vnf_script.py -i 3 -o 0 -e 3 -h '127.0.0.1' -p 3004 &
python3 vnf_script.py -i 4 -o 0 -e 3 -h '127.0.0.1' -p 3005 &
python3 vnf_script.py -i 5 -o 0 -e 3 -h '127.0.0.1' -p 3006 &
python3 vnf_script.py -i 6 -o 0 -e 3 -h '127.0.0.1' -p 3007 &
python3 vnf_script.py -i 7 -o 0 -e 3 -h '127.0.0.1' -p 3008 &
python3 vnf_script.py -i 8 -o 0 -e 3 -h '127.0.0.1' -p 3009 &
python3 vnf_script.py -i 9 -o 0 -e 3 -h '127.0.0.1' -p 3010 &

