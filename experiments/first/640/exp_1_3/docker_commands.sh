#Run orchestrators
docker exec -it mn.orch_1 python orchestrator_script.py -h 10.0.0.30 -p 5461 -n orch_1 &
docker exec -it mn.orch_2 python orchestrator_script.py -h 10.0.0.32 -p 5463 -n orch_2 &
docker exec -it mn.orch_3 python orchestrator_script.py -h 10.0.0.34 -p 5465 -n orch_3 &
docker exec -it mn.orch_4 python orchestrator_script.py -h 10.0.0.36 -p 5467 -n orch_4 &

# Add orchestrators to first orchestrator
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5465
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add orchestrators to second orchestrator
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5465
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add orchestrators to third orchestrator
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add orchestrators to fourth orchestrator
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5467 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5467 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
docker exec -it mn.source python message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5467 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# ============================== VNFS ===============================
# Run all VNFs from containers
docker exec -it mn.vnf4_fade_in python vnf_script.py -h 10.0.0.26 -v 4437 -o 10.0.0.32 -q 5463 -n fade_in --topology 0.1128,0,0,0 --initial 48 &
docker exec -it mn.vnf22_invert_colors python vnf_script.py -h 10.0.0.43 -v 4437 -o 10.0.0.36 -q 5467 -n invert_colors --topology 0.1087,0,0,0 --initial 69 &
docker exec -it mn.vnf18_mirror_x python vnf_script.py -h 10.0.0.29 -v 4437 -o 10.0.0.34 -q 5465 -n mirror_x --topology 0.1112,0,0,0 --initial 57 &
docker exec -it mn.vnf13_rotate python vnf_script.py -h 10.0.0.24 -v 4437 -o 10.0.0.30 -q 5461 -n rotate --topology 0.1065,0,0,0 --initial 42 &
docker exec -it mn.vnf17_mirror_y python vnf_script.py -h 10.0.0.28 -v 4437 -o 10.0.0.32 -q 5463 -n mirror_y --topology 0.1102,0,0,0 --initial 54 &
docker exec -it mn.vnf23_composite_stadium python vnf_script.py -h 10.0.0.102 -v 4437 -o 10.0.0.36 -q 5467 -n composite_stadium --topology 0.2236,0,0,0 --initial 72 &
docker exec -it mn.vnf20_fade_out python vnf_script.py -h 10.0.0.41 -v 4437 -o 10.0.0.34 -q 5465 -n fade_out --topology 0.0841,0,0,0 --initial 63 &
docker exec -it mn.vnf19_annotate python vnf_script.py -h 10.0.0.40 -v 4437 -o 10.0.0.34 -q 5465 -n annotate --topology 0.2608,0,0,0 --initial 60 &

# Add VNFs to service 1
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.29 -p 4437 -n none -m none -v 10.0.0.43 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.43 -p 4437 -n none -m none -v 10.0.0.26 --vnf_port 4437

# Add VNFs to service 2
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.102 -p 4437 -n none -m none -v 10.0.0.28 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.28 -p 4437 -n none -m none -v 10.0.0.24 --vnf_port 4437

# Add VNFs to service 3
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.40 -p 4437 -n none -m none -v 10.0.0.41 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.41 -p 4437 -n none -m none -v 10.0.0.29 --vnf_port 4437

# Run command to be sure its working
docker exec -it mn.source python message_factory.py -t process -h 10.0.0.13 -p 4437 -n none -m none -v none --vnf_port none