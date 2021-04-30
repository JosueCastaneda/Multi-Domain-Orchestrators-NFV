#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 3 -e 6 -h '127.0.0.1' -p 4443 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 7cdfaa20-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 7cdfaa21-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x 7cdfaa22-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 7cdfaa24-a99c-11eb-8771-04ea56f99520

# Instantiate the orchestrator's VNFs 
sleep 2
python3 vnf_script.py -i 0 -o 3 -e 6 -h '127.0.0.1' -p 3031 -u $5 &
python3 vnf_script.py -i 1 -o 3 -e 6 -h '127.0.0.1' -p 3032 -u $5 &
python3 vnf_script.py -i 2 -o 3 -e 6 -h '127.0.0.1' -p 3033 -u $5 &
python3 vnf_script.py -i 3 -o 3 -e 6 -h '127.0.0.1' -p 3034 -u $5 &
python3 vnf_script.py -i 4 -o 3 -e 6 -h '127.0.0.1' -p 3035 -u $5 &
python3 vnf_script.py -i 5 -o 3 -e 6 -h '127.0.0.1' -p 3036 -u $5 &
python3 vnf_script.py -i 6 -o 3 -e 6 -h '127.0.0.1' -p 3037 -u $5 &
python3 vnf_script.py -i 7 -o 3 -e 6 -h '127.0.0.1' -p 3038 -u $5 &
python3 vnf_script.py -i 8 -o 3 -e 6 -h '127.0.0.1' -p 3039 -u $5 &
python3 vnf_script.py -i 9 -o 3 -e 6 -h '127.0.0.1' -p 3040 -u $5 &

