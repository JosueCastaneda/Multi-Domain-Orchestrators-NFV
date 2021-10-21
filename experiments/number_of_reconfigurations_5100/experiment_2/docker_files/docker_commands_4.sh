#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 4 -e 2 -h '127.0.0.1' -p 4445 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x b067e80e-324e-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x b067e80f-324e-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x b067e810-324e-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x b067e811-324e-11ec-a929-04ea56f99520

