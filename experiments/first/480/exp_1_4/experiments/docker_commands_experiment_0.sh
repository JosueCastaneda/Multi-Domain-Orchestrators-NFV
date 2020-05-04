#!/bin/sh
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.30 -p 5461 -n orch_1  --path /first/480/exp_1_4/experiments/ --experiment_name experiment_0.json  &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.32 -p 5461 -n orch_2  --path /first/480/exp_1_4/experiments/ --experiment_name experiment_0.json  &
docker exec -it mn.orch_3 python orchestrator_script.py -h 10.0.0.34 -p 5461 -n orch_3  --path /first/480/exp_1_4/experiments/ --experiment_name experiment_0.json  &
docker exec -it mn.orch_4 python orchestrator_script.py -h 10.0.0.36 -p 5461 -n orch_4  --path /first/480/exp_1_4/experiments/ --experiment_name experiment_0.json  &

docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5461 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5461 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5461 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5461

