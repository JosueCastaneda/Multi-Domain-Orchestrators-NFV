#!/bin/sh
docker exec -it mn.orch_0 python orchestrator_script.py -i 0 -e 0 &
docker exec -it mn.orch_1 python orchestrator_script.py -i 1 -e 0 &
docker exec -it mn.orch_2 python orchestrator_script.py -i 2 -e 0 &
docker exec -it mn.orch_3 python orchestrator_script.py -i 3 -e 0 &
docker exec -it mn.orch_4 python orchestrator_script.py -i 4 -e 0 &

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

docker exec -it mn.e5ea698f-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 0 -e 0 &
docker exec -it mn.e5ea6990-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 0 -e 0 &
docker exec -it mn.e5ea6991-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 0 -e 0 &
docker exec -it mn.e5ea6992-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 0 -e 0 &
docker exec -it mn.e5ea6993-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 0 -e 0 &
docker exec -it mn.e5ea6994-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 1 -e 0 &
docker exec -it mn.e5ea6995-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 1 -e 0 &
docker exec -it mn.e5ea6996-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 1 -e 0 &
docker exec -it mn.e5ea6997-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 1 -e 0 &
docker exec -it mn.e5ea6998-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 1 -e 0 &
docker exec -it mn.e5ea6999-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 2 -e 0 &
docker exec -it mn.e5ea699a-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 2 -e 0 &
docker exec -it mn.e5ea699b-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 2 -e 0 &
docker exec -it mn.e5ea699c-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 2 -e 0 &
docker exec -it mn.e5ea699d-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 2 -e 0 &
docker exec -it mn.e5ea699e-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 3 -e 0 &
docker exec -it mn.e5ea699f-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 3 -e 0 &
docker exec -it mn.e5ea69a0-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 3 -e 0 &
docker exec -it mn.e5ea69a1-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 3 -e 0 &
docker exec -it mn.e5ea69a2-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 3 -e 0 &
docker exec -it mn.e5ea69a3-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 4 -e 0 &
docker exec -it mn.e5ea69a4-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 4 -e 0 &
docker exec -it mn.e5ea69a5-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 4 -e 0 &
docker exec -it mn.e5ea69a6-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 4 -e 0 &
docker exec -it mn.e5ea69a7-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 4 -e 0 &

docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5502 -n none -m none -v 127.0.0.1 --vnf_port 5528
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5512 -n none -m none -v 127.0.0.1 --vnf_port 5510
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5510 -n none -m none -v 127.0.0.1 --vnf_port 5516
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5516 -n none -m none -v 127.0.0.1 --vnf_port 5514
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5514 -n none -m none -v 127.0.0.1 --vnf_port 5528
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5510 -n none -m none -v 127.0.0.1 --vnf_port 5512
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5512 -n none -m none -v 127.0.0.1 --vnf_port 5518
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5518 -n none -m none -v 127.0.0.1 --vnf_port 5548
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5548 -n none -m none -v 127.0.0.1 --vnf_port 5524
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5512 -n none -m none -v 127.0.0.1 --vnf_port 5510
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5524 -n none -m none -v 127.0.0.1 --vnf_port 5524
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5524 -n none -m none -v 127.0.0.1 --vnf_port 5544
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5524 -n none -m none -v 127.0.0.1 --vnf_port 5522
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5522 -n none -m none -v 127.0.0.1 --vnf_port 5528
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5530 -n none -m none -v 127.0.0.1 --vnf_port 5524
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5524 -n none -m none -v 127.0.0.1 --vnf_port 5548
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5542 -n none -m none -v 127.0.0.1 --vnf_port 5548
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5540 -n none -m none -v 127.0.0.1 --vnf_port 5510
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5510 -n none -m none -v 127.0.0.1 --vnf_port 5524
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5524 -n none -m none -v 127.0.0.1 --vnf_port 5544
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5544 -n none -m none -v 127.0.0.1 --vnf_port 5528
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5546 -n none -m none -v 127.0.0.1 --vnf_port 5544

docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea69ac-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea69b1-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69ad-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea69aa-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69b0-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69ad-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69b0-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69af-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69ab-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i e5ea69b2-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69ac-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69b1-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69ad-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69aa-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69b0-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69ad-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69b0-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69af-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69ab-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i e5ea69b2-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

