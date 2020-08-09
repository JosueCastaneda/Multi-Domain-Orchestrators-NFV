#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 3 -e 16 -h '0.0.0.0' -p 5004 -r 31152 &

# Add orchestrator's informaton to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 40.127.108.223 --vnf_port 5001 -x fec471fe-da2d-11ea-b222-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.229.37.237 --vnf_port 5002 -x fec471ff-da2d-11ea-b222-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.141.61.172 --vnf_port 5003 -x fec47200-da2d-11ea-b222-04ea56f99520
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5004 -n none -m none --vnf_host 52.151.70.54 --vnf_port 5005 -x fec47202-da2d-11ea-b222-04ea56f99520

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 3 -e 16 -h '0.0.0.0' -p 3001 &
python vnf_script.py -i 1 -o 3 -e 16 -h '0.0.0.0' -p 3002 &
python vnf_script.py -i 2 -o 3 -e 16 -h '0.0.0.0' -p 3003 &
python vnf_script.py -i 3 -o 3 -e 16 -h '0.0.0.0' -p 3004 &
python vnf_script.py -i 4 -o 3 -e 16 -h '0.0.0.0' -p 3005 &
python vnf_script.py -i 5 -o 3 -e 16 -h '0.0.0.0' -p 3006 &
python vnf_script.py -i 6 -o 3 -e 16 -h '0.0.0.0' -p 3007 &
python vnf_script.py -i 7 -o 3 -e 16 -h '0.0.0.0' -p 3008 &
python vnf_script.py -i 8 -o 3 -e 16 -h '0.0.0.0' -p 3009 &
python vnf_script.py -i 9 -o 3 -e 16 -h '0.0.0.0' -p 3010 &

