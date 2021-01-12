#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 1 -e 0 -h '127.0.0.1' -p 4439 -r 276529 -a 2 &

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x f8dc8aaa-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x f8dc8aac-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x f8dc8aad-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x f8dc8aae-54fe-11eb-bec1-04ea56f99520

python3 vnf_script.py -i 0 -o 1 -e 0 -h '127.0.0.1' -p 3011 &
python3 vnf_script.py -i 1 -o 1 -e 0 -h '127.0.0.1' -p 3012 &
python3 vnf_script.py -i 2 -o 1 -e 0 -h '127.0.0.1' -p 3013 &
python3 vnf_script.py -i 3 -o 1 -e 0 -h '127.0.0.1' -p 3014 &
python3 vnf_script.py -i 4 -o 1 -e 0 -h '127.0.0.1' -p 3015 &
python3 vnf_script.py -i 5 -o 1 -e 0 -h '127.0.0.1' -p 3016 &
python3 vnf_script.py -i 6 -o 1 -e 0 -h '127.0.0.1' -p 3017 &
python3 vnf_script.py -i 7 -o 1 -e 0 -h '127.0.0.1' -p 3018 &
python3 vnf_script.py -i 8 -o 1 -e 0 -h '127.0.0.1' -p 3019 &
python3 vnf_script.py -i 9 -o 1 -e 0 -h '127.0.0.1' -p 3020 &

