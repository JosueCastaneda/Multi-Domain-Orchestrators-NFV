#!/bin/sh
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.30 -p 5461 -n orch_1 &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.32 -p 5461 -n orch_2 &
docker exec -it mn.orch_3 python orchestrator_script.py -h 10.0.0.34 -p 5461 -n orch_3 &
docker exec -it mn.orch_4 python orchestrator_script.py -h 10.0.0.36 -p 5461 -n orch_4 &

docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5461 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5461 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5461 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5463

docker exec -it mn.vnf_ROTATE  python vnf_script.py -h 10.0.0.13 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_ROTATE  --topology 11,67,0,7 --migration_ip 10.0.0.229 --migration_topology 9,18,2,7 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 1 &
docker exec -it mn.vnf_CROP  python vnf_script.py -h 10.0.0.12 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_CROP  --topology 20,6,2,1 --migration_ip 10.0.0.182 --migration_topology 15,40,7,4 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 4 &
docker exec -it mn.vnf_PAINTING  python vnf_script.py -h 10.0.0.15 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_PAINTING  --topology 15,31,6,8 --migration_ip 10.0.0.244 --migration_topology 16,17,3,5 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 7 &
docker exec -it mn.vnf_RESIZE  python vnf_script.py -h 10.0.0.101 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_RESIZE  --topology 18,31,0,3 --migration_ip 10.0.0.195 --migration_topology 5,66,10,6 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 10 &
docker exec -it mn.vnf_BLACK_WHITE  python vnf_script.py -h 10.0.0.20 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_BLACK_WHITE  --topology 8,23,6,2 --migration_ip 10.0.0.251 --migration_topology 4,48,5,3 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 13 &
docker exec -it mn.vnf_ANNOTATE  python vnf_script.py -h 10.0.0.18 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_ANNOTATE  --topology 4,56,2,2 --migration_ip 10.0.0.238 --migration_topology 8,7,9,9 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 16 &
docker exec -it mn.vnf_MIRROR_X  python vnf_script.py -h 10.0.0.17 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_MIRROR_X  --topology 0,26,3,2 --migration_ip 10.0.0.233 --migration_topology 15,6,1,1 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 19 &
docker exec -it mn.vnf_INVERT_COLORS  python vnf_script.py -h 10.0.0.21 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_INVERT_COLORS  --topology 9,40,3,8 --migration_ip 10.0.0.217 --migration_topology 4,50,0,7 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 22 &
docker exec -it mn.vnf_FADE_OUT  python vnf_script.py -h 10.0.0.19 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_FADE_OUT  --topology 5,25,6,4 --migration_ip 10.0.0.153 --migration_topology 17,13,9,3 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 25 &
docker exec -it mn.vnf_SPEED_UP  python vnf_script.py -h 10.0.0.68 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_SPEED_UP  --topology 11,53,2,2 --migration_ip 10.0.0.209 --migration_topology 4,11,5,10 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 28 &
docker exec -it mn.vnf_FADE_IN  python vnf_script.py -h 10.0.0.14 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_FADE_IN  --topology 2,42,4,9 --migration_ip 10.0.0.249 --migration_topology 1,19,6,10 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 31 &
docker exec -it mn.vnf_COMPOSITE  python vnf_script.py -h 10.0.0.100 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_COMPOSITE  --topology 19,43,1,4 --migration_ip 10.0.0.181 --migration_topology 4,58,9,2 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 34 &
docker exec -it mn.vnf_MIRROR_Y  python vnf_script.py -h 10.0.0.16 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_MIRROR_Y  --topology 9,61,5,2 --migration_ip 10.0.0.156 --migration_topology 4,16,0,0 --services 112,512,56,40,80,544,80,32,64,136,40,16 --initial 37 &

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.101 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.101 -p 4437 -n none -m none -v 10.0.0.13 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.13 -p 4437 -n none -m none -v 10.0.0.16 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.21 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.13 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.13 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.17 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.15 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.100 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.100 -p 4437 -n none -m none -v 10.0.0.14 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.100 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.100 -p 4437 -n none -m none -v 10.0.0.14 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.17 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.17 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.68 -p 4437 -n none -m none -v 10.0.0.19 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.19 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437

