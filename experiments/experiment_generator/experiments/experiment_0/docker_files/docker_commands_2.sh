#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 2 -e 0 -h '127.0.0.1' -p 4441 -r 276529 -a 0 &

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 99dfba54-4919-11eb-954b-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 99dfba55-4919-11eb-954b-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x 99dfba57-4919-11eb-954b-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 99dfba58-4919-11eb-954b-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 2 -e 0 -h '127.0.0.1' -p 3021 &
python vnf_script.py -i 1 -o 2 -e 0 -h '127.0.0.1' -p 3022 &
python vnf_script.py -i 2 -o 2 -e 0 -h '127.0.0.1' -p 3023 &
python vnf_script.py -i 3 -o 2 -e 0 -h '127.0.0.1' -p 3024 &
python vnf_script.py -i 4 -o 2 -e 0 -h '127.0.0.1' -p 3025 &
python vnf_script.py -i 5 -o 2 -e 0 -h '127.0.0.1' -p 3026 &
python vnf_script.py -i 6 -o 2 -e 0 -h '127.0.0.1' -p 3027 &
python vnf_script.py -i 7 -o 2 -e 0 -h '127.0.0.1' -p 3028 &
python vnf_script.py -i 8 -o 2 -e 0 -h '127.0.0.1' -p 3029 &
python vnf_script.py -i 9 -o 2 -e 0 -h '127.0.0.1' -p 3030 &

