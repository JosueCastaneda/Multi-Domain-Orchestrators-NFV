#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 3 -e 5 -h '127.0.0.1' -p 4443 -r 276529 -a 0 &

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 99dfba54-4919-11eb-954b-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 99dfba55-4919-11eb-954b-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x 99dfba56-4919-11eb-954b-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 99dfba58-4919-11eb-954b-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 3 -e 5 -h '127.0.0.1' -p 3031 &
python vnf_script.py -i 1 -o 3 -e 5 -h '127.0.0.1' -p 3032 &
python vnf_script.py -i 2 -o 3 -e 5 -h '127.0.0.1' -p 3033 &
python vnf_script.py -i 3 -o 3 -e 5 -h '127.0.0.1' -p 3034 &
python vnf_script.py -i 4 -o 3 -e 5 -h '127.0.0.1' -p 3035 &
python vnf_script.py -i 5 -o 3 -e 5 -h '127.0.0.1' -p 3036 &
python vnf_script.py -i 6 -o 3 -e 5 -h '127.0.0.1' -p 3037 &
python vnf_script.py -i 7 -o 3 -e 5 -h '127.0.0.1' -p 3038 &
python vnf_script.py -i 8 -o 3 -e 5 -h '127.0.0.1' -p 3039 &
python vnf_script.py -i 9 -o 3 -e 5 -h '127.0.0.1' -p 3040 &

