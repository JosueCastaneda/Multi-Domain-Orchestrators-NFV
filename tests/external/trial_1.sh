#!/bin/bash

# Launch orchestrator
python orchestrator_script.py -i 1 -e 0 -h '0.0.0.0' -p 5002 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 40.127.108.223 --vnf_port 5001 -x 000f6094-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 52.141.61.172 --vnf_port 5003 -x 000f6096-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 20.185.45.222 --vnf_port 5004 -x 000f6097-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5002 -n none -m none --vnf_host 52.151.70.54 --vnf_port 5005 -x 000f6098-c031-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs
python vnf_script.py -i 0 -o 1 -e 0 &
python vnf_script.py -i 1 -o 1 -e 0 &
python vnf_script.py -i 2 -o 1 -e 0 &
python vnf_script.py -i 3 -o 1 -e 0 &