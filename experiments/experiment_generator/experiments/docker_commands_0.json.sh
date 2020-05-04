#!/bin/sh
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.30 -p 5461 -n orch_1  --path periment_constraint.json --experiment_name 0.json.json  &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.32 -p 5461 -n orch_2  --path periment_constraint.json --experiment_name 0.json.json  &
docker exec -it mn.orch_3 python orchestrator_script.py -h 10.0.0.34 -p 5461 -n orch_3  --path periment_constraint.json --experiment_name 0.json.json  &
docker exec -it mn.orch_4 python orchestrator_script.py -h 10.0.0.36 -p 5461 -n orch_4  --path periment_constraint.json --experiment_name 0.json.json  &

