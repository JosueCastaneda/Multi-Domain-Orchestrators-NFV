#!/bin/bash

# Launch orchestrator
python orchestrator_script.py -i 0 -e 0 -h '127.0.0.1' -p 5001 &

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5001 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5002 -x 000f6095-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5001 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5003 -x 000f6096-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5001 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5004 -x 000f6097-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5001 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5005 -x 000f6098-c031-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs
python vnf_script.py -i 1 -o 0 -e 0 -h '127.0.0.1' -p 3001 &