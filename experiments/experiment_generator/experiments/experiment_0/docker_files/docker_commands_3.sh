#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 3 -e 0 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 40.127.108.223 --vnf_port 5001 -x 91258594-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.229.37.237 --vnf_port 5002 -x 91258595-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.141.61.172 --vnf_port 5003 -x 91258596-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.151.70.54 --vnf_port 5005 -x 91258598-bd3a-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 3 -e 0 &
python vnf_script.py -i 1 -o 3 -e 0 &
python vnf_script.py -i 2 -o 3 -e 0 &
python vnf_script.py -i 3 -o 3 -e 0 &
python vnf_script.py -i 4 -o 3 -e 0 &

