#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 1 -e 6 -h '127.0.0.1' -p 4439 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x abbfe18a-324e-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x abbfe18c-324e-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x abbfe18d-324e-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x abbfe18e-324e-11ec-a929-04ea56f99520

