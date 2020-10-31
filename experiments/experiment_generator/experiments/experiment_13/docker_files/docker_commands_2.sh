#!/bin/sh

# Launch orchestrator
python orchestrator_script.py -i 2 -e 13 -h '0.0.0.0' -p 5003 -r 75903 &

# Add orchestrator's information to my orchestrator
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 40.127.108.223 --vnf_port 5001 -x 910cb928-1ad8-11eb-9945-525400e0bd2a
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 52.229.37.237 --vnf_port 5002 -x 910cb929-1ad8-11eb-9945-525400e0bd2a
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 20.185.45.222 --vnf_port 5004 -x 910cb92b-1ad8-11eb-9945-525400e0bd2a
python message_factory.py -t add_orchestrator -h 0.0.0.0 -p 5003 -n none -m none --vnf_host 52.151.70.54 --vnf_port 5005 -x 910cb92c-1ad8-11eb-9945-525400e0bd2a

# Instantiate the orchestrator's VNFs 
python vnf_script.py -i 0 -o 2 -e 13 -h '0.0.0.0' -p 3001 &
python vnf_script.py -i 1 -o 2 -e 13 -h '0.0.0.0' -p 3002 &
python vnf_script.py -i 2 -o 2 -e 13 -h '0.0.0.0' -p 3003 &
python vnf_script.py -i 3 -o 2 -e 13 -h '0.0.0.0' -p 3004 &
python vnf_script.py -i 4 -o 2 -e 13 -h '0.0.0.0' -p 3005 &
python vnf_script.py -i 5 -o 2 -e 13 -h '0.0.0.0' -p 3006 &
python vnf_script.py -i 6 -o 2 -e 13 -h '0.0.0.0' -p 3007 &
python vnf_script.py -i 7 -o 2 -e 13 -h '0.0.0.0' -p 3008 &
python vnf_script.py -i 8 -o 2 -e 13 -h '0.0.0.0' -p 3009 &
python vnf_script.py -i 9 -o 2 -e 13 -h '0.0.0.0' -p 3010 &

