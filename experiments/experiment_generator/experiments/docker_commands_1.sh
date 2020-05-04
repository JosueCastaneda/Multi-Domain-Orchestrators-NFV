#!/bin/sh
docker exec -it mn.orch_0 python orchestrator_script.py -i 0 -e 1 &
docker exec -it mn.orch_1 python orchestrator_script.py -i 1 -e 1 &
docker exec -it mn.orch_2 python orchestrator_script.py -i 2 -e 1 &
docker exec -it mn.orch_3 python orchestrator_script.py -i 3 -e 1 &
docker exec -it mn.orch_4 python orchestrator_script.py -i 4 -e 1 &

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

docker exec -it mn.e5ea69b3-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 0 -e 1 &
docker exec -it mn.e5ea69b4-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 0 -e 1 &
docker exec -it mn.e5ea69b5-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 0 -e 1 &
docker exec -it mn.e5ea69b6-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 0 -e 1 &
docker exec -it mn.e5ea69b7-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 0 -e 1 &
docker exec -it mn.e5ea69b8-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 1 -e 1 &
docker exec -it mn.e5ea69b9-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 1 -e 1 &
docker exec -it mn.e5ea69ba-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 1 -e 1 &
docker exec -it mn.e5ea69bb-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 1 -e 1 &
docker exec -it mn.e5ea69bc-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 1 -e 1 &
docker exec -it mn.e5ea69bd-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 2 -e 1 &
docker exec -it mn.e5ea69be-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 2 -e 1 &
docker exec -it mn.e5ea69bf-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 2 -e 1 &
docker exec -it mn.e5ea69c0-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 2 -e 1 &
docker exec -it mn.e5ea69c1-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 2 -e 1 &
docker exec -it mn.e5ea69c2-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 3 -e 1 &
docker exec -it mn.e5ea69c3-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 3 -e 1 &
docker exec -it mn.e5ea69c4-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 3 -e 1 &
docker exec -it mn.e5ea69c5-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 3 -e 1 &
docker exec -it mn.e5ea69c6-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 3 -e 1 &
docker exec -it mn.e5ea69c7-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 4 -e 1 &
docker exec -it mn.e5ea69c8-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 4 -e 1 &
docker exec -it mn.e5ea69c9-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 4 -e 1 &
docker exec -it mn.e5ea69ca-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 4 -e 1 &
docker exec -it mn.e5ea69cb-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 4 -e 1 &

docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5562 -n none -m none -v 127.0.0.1 --vnf_port 5556
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5556 -n none -m none -v 127.0.0.1 --vnf_port 5558
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5558 -n none -m none -v 127.0.0.1 --vnf_port 5550
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5550 -n none -m none -v 127.0.0.1 --vnf_port 5552
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5562 -n none -m none -v 127.0.0.1 --vnf_port 5564
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5564 -n none -m none -v 127.0.0.1 --vnf_port 5556
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5558 -n none -m none -v 127.0.0.1 --vnf_port 5564
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5584 -n none -m none -v 127.0.0.1 --vnf_port 5558
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5558 -n none -m none -v 127.0.0.1 --vnf_port 5584
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5584 -n none -m none -v 127.0.0.1 --vnf_port 5564
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5560 -n none -m none -v 127.0.0.1 --vnf_port 5560
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5560 -n none -m none -v 127.0.0.1 --vnf_port 5556
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5556 -n none -m none -v 127.0.0.1 --vnf_port 5584
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5562 -n none -m none -v 127.0.0.1 --vnf_port 5566
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5566 -n none -m none -v 127.0.0.1 --vnf_port 5568
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5568 -n none -m none -v 127.0.0.1 --vnf_port 5560
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5560 -n none -m none -v 127.0.0.1 --vnf_port 5562
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5562 -n none -m none -v 127.0.0.1 --vnf_port 5566
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5566 -n none -m none -v 127.0.0.1 --vnf_port 5568
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5568 -n none -m none -v 127.0.0.1 --vnf_port 5564
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5584 -n none -m none -v 127.0.0.1 --vnf_port 5566
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5584 -n none -m none -v 127.0.0.1 --vnf_port 5588
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5588 -n none -m none -v 127.0.0.1 --vnf_port 5564
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5564 -n none -m none -v 127.0.0.1 --vnf_port 5582
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5558 -n none -m none -v 127.0.0.1 --vnf_port 5596
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5596 -n none -m none -v 127.0.0.1 --vnf_port 5564
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5564 -n none -m none -v 127.0.0.1 --vnf_port 5552
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5552 -n none -m none -v 127.0.0.1 --vnf_port 5582

docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69d2-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69d5-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69ce-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69d1-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69d3-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea69ce-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea69d3-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i e5ea69d0-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea69d6-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea69cf-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69d2-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69d5-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69ce-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69d1-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69d3-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea69ce-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69d3-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i e5ea69d0-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69d6-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69cf-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

