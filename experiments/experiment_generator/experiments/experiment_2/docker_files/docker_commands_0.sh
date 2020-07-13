#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 0 -e 2 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 52.229.37.237 --vnf_port 5002 -x 000f6095-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 52.141.61.172 --vnf_port 5003 -x 000f6096-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 20.185.45.222 --vnf_port 5004 -x 000f6097-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5001 -n none -m none --vnf_host 52.151.70.54 --vnf_port 5005 -x 000f6098-c031-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 0 -e 2 &
python vnf_script.py -i 1 -o 0 -e 2 &
python vnf_script.py -i 2 -o 0 -e 2 &
python vnf_script.py -i 3 -o 0 -e 2 &
python vnf_script.py -i 4 -o 0 -e 2 &

