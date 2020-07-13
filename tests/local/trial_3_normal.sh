#!/bin/bash

# Launch orchestrator
python orchestrator_script_normal.py -i 3 -e 0 -h '127.0.0.1' -p 5004 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5004 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5001 -x 000f6094-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5004 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5002 -x 000f6095-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5004 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5003 -x 000f6096-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5004 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5005 -x 000f6098-c031-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs

