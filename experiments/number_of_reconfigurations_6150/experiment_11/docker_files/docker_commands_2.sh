#!/bin/sh

# Launch orchestrator
python3 orchestrator_script.py -i 2 -e 11 -h '127.0.0.1' -p 4441 -r 276529 -a $3 -x $1 -y $2 -w $4 -u $5 &
sleep 2

# Add orchestrator's information to my orchestrator
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x 3629a1d8-3260-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x 3629a1d9-3260-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x 3629a1db-3260-11ec-a929-04ea56f99520
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x 3629a1dc-3260-11ec-a929-04ea56f99520
