#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 4 -e 4 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5005 -n none -m none --vnf_host 40.127.108.223 --vnf_port 5001 -x 91258594-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5005 -n none -m none --vnf_host 52.229.37.237 --vnf_port 5002 -x 91258595-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5005 -n none -m none --vnf_host 52.141.61.172 --vnf_port 5003 -x 91258596-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5005 -n none -m none --vnf_host 20.185.45.222 --vnf_port 5004 -x 91258597-bd3a-11ea-b335-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 4 -e 4 &
python vnf_script.py -i 1 -o 4 -e 4 &
python vnf_script.py -i 2 -o 4 -e 4 &
python vnf_script.py -i 3 -o 4 -e 4 &
python vnf_script.py -i 4 -o 4 -e 4 &

