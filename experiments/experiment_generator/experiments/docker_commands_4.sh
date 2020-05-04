#!/bin/sh
docker exec -it mn.orch_0 python orchestrator_script.py -i 0 -e 4 &
docker exec -it mn.orch_1 python orchestrator_script.py -i 1 -e 4 &
docker exec -it mn.orch_2 python orchestrator_script.py -i 2 -e 4 &
docker exec -it mn.orch_3 python orchestrator_script.py -i 3 -e 4 &
docker exec -it mn.orch_4 python orchestrator_script.py -i 4 -e 4 &

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

docker exec -it mn.e5ea6a1f-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 0 -e 4 &
docker exec -it mn.e5ea6a20-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 0 -e 4 &
docker exec -it mn.e5ea6a21-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 0 -e 4 &
docker exec -it mn.e5ea6a22-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 0 -e 4 &
docker exec -it mn.e5ea6a23-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 0 -e 4 &
docker exec -it mn.e5ea6a24-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 1 -e 4 &
docker exec -it mn.e5ea6a25-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 1 -e 4 &
docker exec -it mn.e5ea6a26-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 1 -e 4 &
docker exec -it mn.e5ea6a27-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 1 -e 4 &
docker exec -it mn.e5ea6a28-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 1 -e 4 &
docker exec -it mn.e5ea6a29-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 2 -e 4 &
docker exec -it mn.e5ea6a2a-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 2 -e 4 &
docker exec -it mn.e5ea6a2b-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 2 -e 4 &
docker exec -it mn.e5ea6a2c-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 2 -e 4 &
docker exec -it mn.e5ea6a2d-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 2 -e 4 &
docker exec -it mn.e5ea6a2e-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 3 -e 4 &
docker exec -it mn.e5ea6a2f-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 3 -e 4 &
docker exec -it mn.e5ea6a30-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 3 -e 4 &
docker exec -it mn.e5ea6a31-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 3 -e 4 &
docker exec -it mn.e5ea6a32-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 3 -e 4 &
docker exec -it mn.e5ea6a33-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 4 -e 4 &
docker exec -it mn.e5ea6a34-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 4 -e 4 &
docker exec -it mn.e5ea6a35-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 4 -e 4 &
docker exec -it mn.e5ea6a36-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 4 -e 4 &
docker exec -it mn.e5ea6a37-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 4 -e 4 &

docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5706 -n none -m none -v 127.0.0.1 --vnf_port 5708
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5708 -n none -m none -v 127.0.0.1 --vnf_port 5704
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5704 -n none -m none -v 127.0.0.1 --vnf_port 5722
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5706 -n none -m none -v 127.0.0.1 --vnf_port 5706
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5706 -n none -m none -v 127.0.0.1 --vnf_port 5714
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5718 -n none -m none -v 127.0.0.1 --vnf_port 5716
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5716 -n none -m none -v 127.0.0.1 --vnf_port 5712
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5712 -n none -m none -v 127.0.0.1 --vnf_port 5714
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5720 -n none -m none -v 127.0.0.1 --vnf_port 5728
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5728 -n none -m none -v 127.0.0.1 --vnf_port 5724
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5724 -n none -m none -v 127.0.0.1 --vnf_port 5722
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5722 -n none -m none -v 127.0.0.1 --vnf_port 5730
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5730 -n none -m none -v 127.0.0.1 --vnf_port 5720
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5706 -n none -m none -v 127.0.0.1 --vnf_port 5734
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5734 -n none -m none -v 127.0.0.1 --vnf_port 5730
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5706 -n none -m none -v 127.0.0.1 --vnf_port 5706
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5740 -n none -m none -v 127.0.0.1 --vnf_port 5748
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5748 -n none -m none -v 127.0.0.1 --vnf_port 5722
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5722 -n none -m none -v 127.0.0.1 --vnf_port 5730
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5740 -n none -m none -v 127.0.0.1 --vnf_port 5706
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5706 -n none -m none -v 127.0.0.1 --vnf_port 5746
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5746 -n none -m none -v 127.0.0.1 --vnf_port 5740
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5740 -n none -m none -v 127.0.0.1 --vnf_port 5714

docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea6a3f-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i e5ea6a39-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea6a3a-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea6a3e-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a40-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i e5ea6a3a-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a40-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a3c-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i e5ea6a42-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i e5ea6a3b-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea6a3f-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i e5ea6a39-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea6a3a-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea6a3e-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a40-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i e5ea6a3a-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a40-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a3c-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i e5ea6a42-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i e5ea6a3b-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

