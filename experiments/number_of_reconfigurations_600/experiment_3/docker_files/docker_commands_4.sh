#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 4 -e 3 -h '127.0.0.1' -p 4445 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 6b5c4326-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 6b5c4327-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x 6b5c4328-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x 6b5c4329-a99c-11eb-8771-04ea56f99520

# Instantiate the orchestrator's VNFs 
sleep 2
python3 vnf_script.py -i 0 -o 4 -e 3 -h '127.0.0.1' -p 3041 -u $5 &
python3 vnf_script.py -i 1 -o 4 -e 3 -h '127.0.0.1' -p 3042 -u $5 &
python3 vnf_script.py -i 2 -o 4 -e 3 -h '127.0.0.1' -p 3043 -u $5 &
python3 vnf_script.py -i 3 -o 4 -e 3 -h '127.0.0.1' -p 3044 -u $5 &
python3 vnf_script.py -i 4 -o 4 -e 3 -h '127.0.0.1' -p 3045 -u $5 &
python3 vnf_script.py -i 5 -o 4 -e 3 -h '127.0.0.1' -p 3046 -u $5 &
python3 vnf_script.py -i 6 -o 4 -e 3 -h '127.0.0.1' -p 3047 -u $5 &
python3 vnf_script.py -i 7 -o 4 -e 3 -h '127.0.0.1' -p 3048 -u $5 &
python3 vnf_script.py -i 8 -o 4 -e 3 -h '127.0.0.1' -p 3049 -u $5 &
python3 vnf_script.py -i 9 -o 4 -e 3 -h '127.0.0.1' -p 3050 -u $5 &

