#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 1 -e 9 -h '127.0.0.1' -p 4439 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 6869e6d2-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x 6869e6d4-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x 6869e6d5-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 6869e6d6-a99c-11eb-8771-04ea56f99520

# Instantiate the orchestrator's VNFs 
sleep 2
python3 vnf_script.py -i 0 -o 1 -e 9 -h '127.0.0.1' -p 3011 -u $5 &
python3 vnf_script.py -i 1 -o 1 -e 9 -h '127.0.0.1' -p 3012 -u $5 &
python3 vnf_script.py -i 2 -o 1 -e 9 -h '127.0.0.1' -p 3013 -u $5 &
python3 vnf_script.py -i 3 -o 1 -e 9 -h '127.0.0.1' -p 3014 -u $5 &
python3 vnf_script.py -i 4 -o 1 -e 9 -h '127.0.0.1' -p 3015 -u $5 &
python3 vnf_script.py -i 5 -o 1 -e 9 -h '127.0.0.1' -p 3016 -u $5 &
python3 vnf_script.py -i 6 -o 1 -e 9 -h '127.0.0.1' -p 3017 -u $5 &
python3 vnf_script.py -i 7 -o 1 -e 9 -h '127.0.0.1' -p 3018 -u $5 &
python3 vnf_script.py -i 8 -o 1 -e 9 -h '127.0.0.1' -p 3019 -u $5 &
python3 vnf_script.py -i 9 -o 1 -e 9 -h '127.0.0.1' -p 3020 -u $5 &

