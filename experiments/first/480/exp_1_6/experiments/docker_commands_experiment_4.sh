#!/bin/sh
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.30 -p 5461 -n orch_1  --path /first/480/exp_1_6/experiments/ --experiment_name experiment_4.json  &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.32 -p 5461 -n orch_2  --path /first/480/exp_1_6/experiments/ --experiment_name experiment_4.json  &
docker exec -it mn.orch_3 python orchestrator_script.py -h 10.0.0.34 -p 5461 -n orch_3  --path /first/480/exp_1_6/experiments/ --experiment_name experiment_4.json  &
docker exec -it mn.orch_4 python orchestrator_script.py -h 10.0.0.36 -p 5461 -n orch_4  --path /first/480/exp_1_6/experiments/ --experiment_name experiment_4.json  &

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

docker exec -it mn.vnf_ROTATE  python vnf_script.py -h 10.0.0.13 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_ROTATE  --topology 11,67,0,7 --migration_ip 10.0.0.229 --migration_topology 9,18,2,7 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 1 &
docker exec -it mn.vnf_CROP  python vnf_script.py -h 10.0.0.12 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_CROP  --topology 20,6,2,1 --migration_ip 10.0.0.182 --migration_topology 15,40,7,4 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 4 &
docker exec -it mn.vnf_PAINTING  python vnf_script.py -h 10.0.0.15 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_PAINTING  --topology 15,31,6,8 --migration_ip 10.0.0.244 --migration_topology 16,17,3,5 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 7 &
docker exec -it mn.vnf_RESIZE  python vnf_script.py -h 10.0.0.101 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_RESIZE  --topology 18,31,0,3 --migration_ip 10.0.0.195 --migration_topology 5,66,10,6 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 10 &
docker exec -it mn.vnf_BLACK_WHITE  python vnf_script.py -h 10.0.0.20 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_BLACK_WHITE  --topology 8,23,6,2 --migration_ip 10.0.0.251 --migration_topology 4,48,5,3 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 13 &
docker exec -it mn.vnf_ANNOTATE  python vnf_script.py -h 10.0.0.18 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_ANNOTATE  --topology 4,56,2,2 --migration_ip 10.0.0.238 --migration_topology 8,7,9,9 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 16 &
docker exec -it mn.vnf_MIRROR_X  python vnf_script.py -h 10.0.0.17 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_MIRROR_X  --topology 0,26,3,2 --migration_ip 10.0.0.233 --migration_topology 15,6,1,1 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 19 &
docker exec -it mn.vnf_INVERT_COLORS  python vnf_script.py -h 10.0.0.21 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_INVERT_COLORS  --topology 9,40,3,8 --migration_ip 10.0.0.217 --migration_topology 4,50,0,7 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 22 &
docker exec -it mn.vnf_FADE_OUT  python vnf_script.py -h 10.0.0.19 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_FADE_OUT  --topology 5,25,6,4 --migration_ip 10.0.0.153 --migration_topology 17,13,9,3 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 25 &
docker exec -it mn.vnf_SPEED_UP  python vnf_script.py -h 10.0.0.68 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_SPEED_UP  --topology 11,53,2,2 --migration_ip 10.0.0.209 --migration_topology 4,11,5,10 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 28 &
docker exec -it mn.vnf_FADE_IN  python vnf_script.py -h 10.0.0.14 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_FADE_IN  --topology 2,42,4,9 --migration_ip 10.0.0.249 --migration_topology 1,19,6,10 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 31 &
docker exec -it mn.vnf_COMPOSITE  python vnf_script.py -h 10.0.0.100 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_COMPOSITE  --topology 19,43,1,4 --migration_ip 10.0.0.181 --migration_topology 4,58,9,2 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 34 &
docker exec -it mn.vnf_MIRROR_Y  python vnf_script.py -h 10.0.0.16 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_MIRROR_Y  --topology 9,61,5,2 --migration_ip 10.0.0.156 --migration_topology 4,16,0,0 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 37 &

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.20 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.17 -p 4437 -n none -m none -v 10.0.0.16 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.15 -p 4437 -n none -m none -v 10.0.0.21 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.21 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.14 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.101 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.101 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.15 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.15 -p 4437 -n none -m none -v 10.0.0.16 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.100 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.100 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.21 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.15 -p 4437 -n none -m none -v 10.0.0.16 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.20 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.20 -p 4437 -n none -m none -v 10.0.0.13 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.13 -p 4437 -n none -m none -v 10.0.0.100 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.100 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.101 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.101 -p 4437 -n none -m none -v 10.0.0.13 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.13 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.15 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.100 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.100 -p 4437 -n none -m none -v 10.0.0.14 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.13 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.13 -p 4437 -n none -m none -v 10.0.0.20 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.20 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.17 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.20 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.20 -p 4437 -n none -m none -v 10.0.0.100 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.101 -p 4437 -n none -m none -v 10.0.0.14 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.16 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.17 -p 4437 -n none -m none -v 10.0.0.21 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.16 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.14 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.20 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.17 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.19 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.19 -p 4437 -n none -m none -v 10.0.0.101 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.101 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437


docker exec -it mn.vnf_ROTATE  python vnf_script.py -h 10.0.0.13 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_ROTATE  --topology 15,22,0,4 --migration_ip 10.0.0.229 --migration_topology 9,18,2,7 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 1 &
docker exec -it mn.vnf_CROP  python vnf_script.py -h 10.0.0.12 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_CROP  --topology 0,45,6,0 --migration_ip 10.0.0.182 --migration_topology 15,40,7,4 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 4 &
docker exec -it mn.vnf_PAINTING  python vnf_script.py -h 10.0.0.15 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_PAINTING  --topology 17,53,5,6 --migration_ip 10.0.0.244 --migration_topology 16,17,3,5 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 7 &
docker exec -it mn.vnf_RESIZE  python vnf_script.py -h 10.0.0.101 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_RESIZE  --topology 18,1,7,0 --migration_ip 10.0.0.195 --migration_topology 5,66,10,6 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 10 &
docker exec -it mn.vnf_BLACK_WHITE  python vnf_script.py -h 10.0.0.20 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_BLACK_WHITE  --topology 5,25,1,3 --migration_ip 10.0.0.251 --migration_topology 4,48,5,3 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 13 &
docker exec -it mn.vnf_ANNOTATE  python vnf_script.py -h 10.0.0.18 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_ANNOTATE  --topology 14,44,8,5 --migration_ip 10.0.0.238 --migration_topology 8,7,9,9 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 16 &
docker exec -it mn.vnf_MIRROR_X  python vnf_script.py -h 10.0.0.17 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_MIRROR_X  --topology 16,32,7,1 --migration_ip 10.0.0.233 --migration_topology 15,6,1,1 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 19 &
docker exec -it mn.vnf_INVERT_COLORS  python vnf_script.py -h 10.0.0.21 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_INVERT_COLORS  --topology 18,47,4,0 --migration_ip 10.0.0.217 --migration_topology 4,50,0,7 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 22 &
docker exec -it mn.vnf_FADE_OUT  python vnf_script.py -h 10.0.0.19 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_FADE_OUT  --topology 13,11,3,5 --migration_ip 10.0.0.153 --migration_topology 17,13,9,3 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 25 &
docker exec -it mn.vnf_SPEED_UP  python vnf_script.py -h 10.0.0.68 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_SPEED_UP  --topology 16,46,2,5 --migration_ip 10.0.0.209 --migration_topology 4,11,5,10 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 28 &
docker exec -it mn.vnf_FADE_IN  python vnf_script.py -h 10.0.0.14 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_FADE_IN  --topology 8,69,1,4 --migration_ip 10.0.0.249 --migration_topology 1,19,6,10 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 31 &
docker exec -it mn.vnf_COMPOSITE  python vnf_script.py -h 10.0.0.100 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_COMPOSITE  --topology 10,39,2,1 --migration_ip 10.0.0.181 --migration_topology 4,58,9,2 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 34 &
docker exec -it mn.vnf_MIRROR_Y  python vnf_script.py -h 10.0.0.16 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_MIRROR_Y  --topology 20,19,4,7 --migration_ip 10.0.0.156 --migration_topology 4,16,0,0 --services 72,300,12,18,60,384,24,60,0,342,60,24,108,396,6,24,72,156,18,18,36,24,24,30,78,204,12,12,24,264,24,30,108,174,18,36,0,210,18,12 --initial 37 &

docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 70590
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 18095
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 43356
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.12 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 32702
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.100 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 89754
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 56754
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 31046
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 578
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.12 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 66698
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 45155
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 73390
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.100 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 63704
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 78014
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 75568
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.100 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 27470
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 29788
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 11590
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 16694
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 11992
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 26773
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 16313
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 55113
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.12 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 95072
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.12 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 20686
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 1210
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 651
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.100 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 13755
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 65195
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 36309
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 46406
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 17775
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 98074
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 47202
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.18 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 43721
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.18 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 19719
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 73689
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.12 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 2643
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 43449
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 93642
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 37095
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 64546
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 77716
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.15 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 29941
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 5284
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 7541
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.15 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 94796
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 18890
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 69453
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 6236
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 14654
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 60742
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.18 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 46285
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 31076
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.13 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 52786
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 74475
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.13 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 96516
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 20022
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.13 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 88432
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 97939
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.100 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 25746
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.15 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 423029848
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.15 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 895480730
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 692082621
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.18 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 867203644
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.13 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 45718306
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 744836797
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.100 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 872820326
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.12 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 888545133
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 467289156
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 752502411
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.15 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 474404819
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 753356850
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 182393063
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.101 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 802415045
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 304861714
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 514495235
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.21 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 228235555
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 152751996
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 502778453
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 521245228
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 844541416
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 842800110
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 472794730
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 912734960
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 292139339
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 227096389
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 489493218
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 37678719
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.68 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 733177228
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 412270653
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.16 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 334909242
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.13 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 204054956
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.14 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 262954244
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.19 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 495817807
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 715355487
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.18 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 734612929
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.17 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 462038900
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 861740776
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.15 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 503426923
docker exec -it mn.source python message_factory.py -t request_update -h 10.0.0.20 -p 4437 -n none -m none --vnf_host none --vnf_port none --seed 490437011

