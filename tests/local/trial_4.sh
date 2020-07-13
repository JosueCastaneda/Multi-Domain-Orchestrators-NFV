#!/bin/bash

# Launch orchestrator
python orchestrator_script.py -i 4 -e 0 -h '127.0.0.1' -p 5005 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5005 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5001 -x 000f6094-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5005 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5002 -x 000f6095-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5005 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5003 -x 000f6096-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5005 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5004 -x 000f6097-c031-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs
python vnf_script.py -i 0 -o 4 -e 0 -h '127.0.0.1' -p 3040 &
python vnf_script.py -i 1 -o 4 -e 0 -h '127.0.0.1' -p 3041 &
python vnf_script.py -i 2 -o 4 -e 0 -h '127.0.0.1' -p 3042 &
python vnf_script.py -i 3 -o 4 -e 0 -h '127.0.0.1' -p 3043 &
python vnf_script.py -i 4 -o 4 -e 0 -h '127.0.0.1' -p 3044 &