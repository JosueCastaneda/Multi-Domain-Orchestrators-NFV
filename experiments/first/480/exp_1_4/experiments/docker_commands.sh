#!/bin/sh
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.30 -p 5461 -n orch_1 &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.32 -p 5461 -n orch_2 &
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.34 -p 5461 -n orch_1 &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.36 -p 5461 -n orch_2 &

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

docker exec -it mn.vnf_ROTATE  python vnf_script.py -h 10.0.0.13 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_ROTATE  --topology 11,67,0,7 --initial 1 &
docker exec -it mn.vnf_CROP  python vnf_script.py -h 10.0.0.12 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_CROP  --topology 20,6,2,1 --initial 4 &
docker exec -it mn.vnf_PAINTING  python vnf_script.py -h 10.0.0.15 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_PAINTING  --topology 15,31,6,8 --initial 7 &
docker exec -it mn.vnf_RESIZE  python vnf_script.py -h 10.0.0.101 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_RESIZE  --topology 18,31,0,3 --initial 10 &
docker exec -it mn.vnf_BLACK_WHITE  python vnf_script.py -h 10.0.0.20 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_BLACK_WHITE  --topology 8,23,6,2 --initial 13 &
docker exec -it mn.vnf_ANNOTATE  python vnf_script.py -h 10.0.0.18 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_ANNOTATE  --topology 4,56,2,2 --initial 16 &
docker exec -it mn.vnf_MIRROR_X  python vnf_script.py -h 10.0.0.17 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_MIRROR_X  --topology 0,26,3,2 --initial 19 &
docker exec -it mn.vnf_INVERT_COLORS  python vnf_script.py -h 10.0.0.21 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_INVERT_COLORS  --topology 9,40,3,8 --initial 22 &
docker exec -it mn.vnf_FADE_OUT  python vnf_script.py -h 10.0.0.19 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_FADE_OUT  --topology 5,25,6,4 --initial 25 &
docker exec -it mn.vnf_SPEED_UP  python vnf_script.py -h 10.0.0.68 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_SPEED_UP  --topology 11,53,2,2 --initial 28 &
docker exec -it mn.vnf_FADE_IN  python vnf_script.py -h 10.0.0.14 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_FADE_IN  --topology 2,42,4,9 --initial 31 &
docker exec -it mn.vnf_COMPOSITE  python vnf_script.py -h 10.0.0.100 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_COMPOSITE  --topology 19,43,1,4 --initial 34 &
docker exec -it mn.vnf_MIRROR_Y  python vnf_script.py -h 10.0.0.16 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_MIRROR_Y  --topology 9,61,5,2 --initial 37 &

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.19 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.20 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.20 -p 4437 -n none -m none -v 10.0.0.68 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.16 -p 4437 -n none -m none -v 10.0.0.101 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.101 -p 4437 -n none -m none -v 10.0.0.21 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.13 --vnf_port 4437

docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.21 -p 4437 -n none -m none -v 10.0.0.18 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.18 -p 4437 -n none -m none -v 10.0.0.12 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.12 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4437

