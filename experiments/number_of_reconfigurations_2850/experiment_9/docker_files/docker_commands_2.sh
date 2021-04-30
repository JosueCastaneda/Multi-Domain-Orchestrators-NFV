#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 2 -e 9 -h '127.0.0.1' -p 4441 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 85ef2118-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 85ef2119-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x 85ef211b-a99c-11eb-8771-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 85ef211c-a99c-11eb-8771-04ea56f99520

# Instantiate the orchestrator's VNFs 
sleep 2
python3 vnf_script.py -i 0 -o 2 -e 9 -h '127.0.0.1' -p 3021 -u $5 &
python3 vnf_script.py -i 1 -o 2 -e 9 -h '127.0.0.1' -p 3022 -u $5 &
python3 vnf_script.py -i 2 -o 2 -e 9 -h '127.0.0.1' -p 3023 -u $5 &
python3 vnf_script.py -i 3 -o 2 -e 9 -h '127.0.0.1' -p 3024 -u $5 &
python3 vnf_script.py -i 4 -o 2 -e 9 -h '127.0.0.1' -p 3025 -u $5 &
python3 vnf_script.py -i 5 -o 2 -e 9 -h '127.0.0.1' -p 3026 -u $5 &
python3 vnf_script.py -i 6 -o 2 -e 9 -h '127.0.0.1' -p 3027 -u $5 &
python3 vnf_script.py -i 7 -o 2 -e 9 -h '127.0.0.1' -p 3028 -u $5 &
python3 vnf_script.py -i 8 -o 2 -e 9 -h '127.0.0.1' -p 3029 -u $5 &
python3 vnf_script.py -i 9 -o 2 -e 9 -h '127.0.0.1' -p 3030 -u $5 &

