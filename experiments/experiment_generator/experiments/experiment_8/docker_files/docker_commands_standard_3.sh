#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 3 -e 8 -h '127.0.0.1' -p 4443 -r 276529 -a 1 &

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x f8dc8aaa-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x f8dc8aab-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x f8dc8aac-54fe-11eb-bec1-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x f8dc8aae-54fe-11eb-bec1-04ea56f99520

python3 vnf_script.py -i 0 -o 3 -e 8 -h '127.0.0.1' -p 3031 &
python3 vnf_script.py -i 1 -o 3 -e 8 -h '127.0.0.1' -p 3032 &
python3 vnf_script.py -i 2 -o 3 -e 8 -h '127.0.0.1' -p 3033 &
python3 vnf_script.py -i 3 -o 3 -e 8 -h '127.0.0.1' -p 3034 &
python3 vnf_script.py -i 4 -o 3 -e 8 -h '127.0.0.1' -p 3035 &
python3 vnf_script.py -i 5 -o 3 -e 8 -h '127.0.0.1' -p 3036 &
python3 vnf_script.py -i 6 -o 3 -e 8 -h '127.0.0.1' -p 3037 &
python3 vnf_script.py -i 7 -o 3 -e 8 -h '127.0.0.1' -p 3038 &
python3 vnf_script.py -i 8 -o 3 -e 8 -h '127.0.0.1' -p 3039 &
python3 vnf_script.py -i 9 -o 3 -e 8 -h '127.0.0.1' -p 3040 &

