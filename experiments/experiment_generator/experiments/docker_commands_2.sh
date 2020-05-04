#!/bin/sh
docker exec -it mn.orch_0 python orchestrator_script.py -i 0 -e 2 &
docker exec -it mn.orch_1 python orchestrator_script.py -i 1 -e 2 &
docker exec -it mn.orch_2 python orchestrator_script.py -i 2 -e 2 &
docker exec -it mn.orch_3 python orchestrator_script.py -i 3 -e 2 &
docker exec -it mn.orch_4 python orchestrator_script.py -i 4 -e 2 &

docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x e5ea698b-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x e5ea698c-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x e5ea698d-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4437 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x e5ea698e-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x e5ea698a-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x e5ea698c-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x e5ea698d-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4439 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x e5ea698e-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x e5ea698a-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x e5ea698b-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x e5ea698d-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4441 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x e5ea698e-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x e5ea698a-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x e5ea698b-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x e5ea698c-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4443 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4445 -x e5ea698e-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4437 -x e5ea698a-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4439 -x e5ea698b-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4441 -x e5ea698c-8a3d-11ea-aa9d-04ea56f99520
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 127.0.0.1 -p 4445 -n none -m none --vnf_host 127.0.0.1 --vnf_port 4443 -x e5ea698d-8a3d-11ea-aa9d-04ea56f99520

docker exec -it mn.e5ea69d7-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 0 -e 2 &
docker exec -it mn.e5ea69d8-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 0 -e 2 &
docker exec -it mn.e5ea69d9-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 0 -e 2 &
docker exec -it mn.e5ea69da-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 0 -e 2 &
docker exec -it mn.e5ea69db-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 0 -e 2 &
docker exec -it mn.e5ea69dc-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 1 -e 2 &
docker exec -it mn.e5ea69dd-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 1 -e 2 &
docker exec -it mn.e5ea69de-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 1 -e 2 &
docker exec -it mn.e5ea69df-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 1 -e 2 &
docker exec -it mn.e5ea69e0-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 1 -e 2 &
docker exec -it mn.e5ea69e1-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 2 -e 2 &
docker exec -it mn.e5ea69e2-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 2 -e 2 &
docker exec -it mn.e5ea69e3-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 2 -e 2 &
docker exec -it mn.e5ea69e4-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 2 -e 2 &
docker exec -it mn.e5ea69e5-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 2 -e 2 &
docker exec -it mn.e5ea69e6-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 3 -e 2 &
docker exec -it mn.e5ea69e7-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 3 -e 2 &
docker exec -it mn.e5ea69e8-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 3 -e 2 &
docker exec -it mn.e5ea69e9-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 3 -e 2 &
docker exec -it mn.e5ea69ea-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 3 -e 2 &
docker exec -it mn.e5ea69eb-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 4 -e 2 &
docker exec -it mn.e5ea69ec-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 4 -e 2 &
docker exec -it mn.e5ea69ed-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 4 -e 2 &
docker exec -it mn.e5ea69ee-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 4 -e 2 &
docker exec -it mn.e5ea69ef-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 4 -e 2 &

docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5602 -n none -m none -v 127.0.0.1 --vnf_port 5600
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5600 -n none -m none -v 127.0.0.1 --vnf_port 5608
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5602 -n none -m none -v 127.0.0.1 --vnf_port 5604
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5604 -n none -m none -v 127.0.0.1 --vnf_port 5644
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5644 -n none -m none -v 127.0.0.1 --vnf_port 5602
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5602 -n none -m none -v 127.0.0.1 --vnf_port 5600
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5602 -n none -m none -v 127.0.0.1 --vnf_port 5604
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5604 -n none -m none -v 127.0.0.1 --vnf_port 5640
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5614 -n none -m none -v 127.0.0.1 --vnf_port 5610
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5610 -n none -m none -v 127.0.0.1 --vnf_port 5644
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5602 -n none -m none -v 127.0.0.1 --vnf_port 5640
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5640 -n none -m none -v 127.0.0.1 --vnf_port 5648
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5648 -n none -m none -v 127.0.0.1 --vnf_port 5620
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5620 -n none -m none -v 127.0.0.1 --vnf_port 5642
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5648 -n none -m none -v 127.0.0.1 --vnf_port 5636
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5636 -n none -m none -v 127.0.0.1 --vnf_port 5640
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5640 -n none -m none -v 127.0.0.1 --vnf_port 5632
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5644 -n none -m none -v 127.0.0.1 --vnf_port 5640
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5640 -n none -m none -v 127.0.0.1 --vnf_port 5646
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5646 -n none -m none -v 127.0.0.1 --vnf_port 5642
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5648 -n none -m none -v 127.0.0.1 --vnf_port 5608
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5608 -n none -m none -v 127.0.0.1 --vnf_port 5642
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5642 -n none -m none -v 127.0.0.1 --vnf_port 5646
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5646 -n none -m none -v 127.0.0.1 --vnf_port 5600
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5600 -n none -m none -v 127.0.0.1 --vnf_port 5648
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5648 -n none -m none -v 127.0.0.1 --vnf_port 5640
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5648 -n none -m none -v 127.0.0.1 --vnf_port 5644
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5644 -n none -m none -v 127.0.0.1 --vnf_port 5644
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5644 -n none -m none -v 127.0.0.1 --vnf_port 5646
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5646 -n none -m none -v 127.0.0.1 --vnf_port 5642

docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69f7-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i e5ea69fa-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69f1-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69f4-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69f9-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69f1-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69f9-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69f5-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69f3-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69f2-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69f7-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i e5ea69fa-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69f1-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69f4-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69f9-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69f1-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69f9-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69f5-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69f3-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69f2-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

