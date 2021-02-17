#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 2 -e 1 -h '127.0.0.1' -p 4441 -r 276529 -a 2 &
sleep 2

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 6cdf8e2a-70a7-11eb-9f1c-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 6cdf8e2b-70a7-11eb-9f1c-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x 6cdf8e2d-70a7-11eb-9f1c-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 6cdf8e2e-70a7-11eb-9f1c-04ea56f99520

# Instantiate the orchestrator's VNFs 
sleep 2
python3 vnf_script.py -i 0 -o 2 -e 1 -h '127.0.0.1' -p 3021 &
python3 vnf_script.py -i 1 -o 2 -e 1 -h '127.0.0.1' -p 3022 &
python3 vnf_script.py -i 2 -o 2 -e 1 -h '127.0.0.1' -p 3023 &
python3 vnf_script.py -i 3 -o 2 -e 1 -h '127.0.0.1' -p 3024 &
python3 vnf_script.py -i 4 -o 2 -e 1 -h '127.0.0.1' -p 3025 &
python3 vnf_script.py -i 5 -o 2 -e 1 -h '127.0.0.1' -p 3026 &
python3 vnf_script.py -i 6 -o 2 -e 1 -h '127.0.0.1' -p 3027 &
python3 vnf_script.py -i 7 -o 2 -e 1 -h '127.0.0.1' -p 3028 &
python3 vnf_script.py -i 8 -o 2 -e 1 -h '127.0.0.1' -p 3029 &
python3 vnf_script.py -i 9 -o 2 -e 1 -h '127.0.0.1' -p 3030 &

