#!/bin/sh
docker exec -it mn.orch_0 python orchestrator_script.py -i 0 -e 3 &
docker exec -it mn.orch_1 python orchestrator_script.py -i 1 -e 3 &
docker exec -it mn.orch_2 python orchestrator_script.py -i 2 -e 3 &
docker exec -it mn.orch_3 python orchestrator_script.py -i 3 -e 3 &
docker exec -it mn.orch_4 python orchestrator_script.py -i 4 -e 3 &

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

docker exec -it mn.e5ea69fb-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 0 -e 3 &
docker exec -it mn.e5ea69fc-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 0 -e 3 &
docker exec -it mn.e5ea69fd-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 0 -e 3 &
docker exec -it mn.e5ea69fe-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 0 -e 3 &
docker exec -it mn.e5ea69ff-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 0 -e 3 &
docker exec -it mn.e5ea6a00-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 1 -e 3 &
docker exec -it mn.e5ea6a01-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 1 -e 3 &
docker exec -it mn.e5ea6a02-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 1 -e 3 &
docker exec -it mn.e5ea6a03-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 1 -e 3 &
docker exec -it mn.e5ea6a04-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 1 -e 3 &
docker exec -it mn.e5ea6a05-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 2 -e 3 &
docker exec -it mn.e5ea6a06-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 2 -e 3 &
docker exec -it mn.e5ea6a07-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 2 -e 3 &
docker exec -it mn.e5ea6a08-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 2 -e 3 &
docker exec -it mn.e5ea6a09-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 2 -e 3 &
docker exec -it mn.e5ea6a0a-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 3 -e 3 &
docker exec -it mn.e5ea6a0b-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 3 -e 3 &
docker exec -it mn.e5ea6a0c-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 3 -e 3 &
docker exec -it mn.e5ea6a0d-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 3 -e 3 &
docker exec -it mn.e5ea6a0e-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 3 -e 3 &
docker exec -it mn.e5ea6a0f-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 0 -o 4 -e 3 &
docker exec -it mn.e5ea6a10-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 1 -o 4 -e 3 &
docker exec -it mn.e5ea6a11-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 2 -o 4 -e 3 &
docker exec -it mn.e5ea6a12-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 3 -o 4 -e 3 &
docker exec -it mn.e5ea6a13-8a3d-11ea-aa9d-04ea56f99520 python vnf_script.py -i 4 -o 4 -e 3 &

docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5664 -n none -m none -v 127.0.0.1 --vnf_port 5666
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5666 -n none -m none -v 127.0.0.1 --vnf_port 5662
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5662 -n none -m none -v 127.0.0.1 --vnf_port 5668
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5660 -n none -m none -v 127.0.0.1 --vnf_port 5668
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5694
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5694 -n none -m none -v 127.0.0.1 --vnf_port 5668
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5668 -n none -m none -v 127.0.0.1 --vnf_port 5688
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5672
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5664
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5664 -n none -m none -v 127.0.0.1 --vnf_port 5672
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5686
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5686 -n none -m none -v 127.0.0.1 --vnf_port 5680
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5680 -n none -m none -v 127.0.0.1 --vnf_port 5688
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5694
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5694 -n none -m none -v 127.0.0.1 --vnf_port 5672
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5672 -n none -m none -v 127.0.0.1 --vnf_port 5686
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5686 -n none -m none -v 127.0.0.1 --vnf_port 5682
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5690 -n none -m none -v 127.0.0.1 --vnf_port 5696
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5696 -n none -m none -v 127.0.0.1 --vnf_port 5668
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5668 -n none -m none -v 127.0.0.1 --vnf_port 5672
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5672 -n none -m none -v 127.0.0.1 --vnf_port 5694
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5696
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5696 -n none -m none -v 127.0.0.1 --vnf_port 5668
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5668 -n none -m none -v 127.0.0.1 --vnf_port 5692
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 5682 -n none -m none -v 127.0.0.1 --vnf_port 5682

docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea6a1d-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i e5ea6a1a-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea6a16-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea6a19-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a1e-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i e5ea6a16-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a1e-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a1c-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i e5ea6a18-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i e5ea6a1b-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea6a1d-8a3d-11ea-aa9d-04ea56f99520 --seed 695887
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i e5ea6a1a-8a3d-11ea-aa9d-04ea56f99520 --seed 370491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea6a16-8a3d-11ea-aa9d-04ea56f99520 --seed 958697
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea6a19-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a1e-8a3d-11ea-aa9d-04ea56f99520 --seed 703128
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea6a16-8a3d-11ea-aa9d-04ea56f99520 --seed 173669
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a1e-8a3d-11ea-aa9d-04ea56f99520 --seed 534728
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a1c-8a3d-11ea-aa9d-04ea56f99520 --seed 112825
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea6a18-8a3d-11ea-aa9d-04ea56f99520 --seed 393050
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i e5ea6a1b-8a3d-11ea-aa9d-04ea56f99520 --seed 767384

