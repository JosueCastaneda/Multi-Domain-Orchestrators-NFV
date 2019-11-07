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
docker exec -it mn.vnf26_rotate python vnf_script.py -h 10.0.0.46 -v 4437 -o 10.0.0.30 -q 5461 -n rotate --topology 0.1757,0,0,0 --initial 81 &
docker exec -it mn.vnf30_mirror_y python vnf_script.py -h 10.0.0.50 -v 4437 -o 10.0.0.32 -q 5463 -n mirror_y --topology 0.1716,0,0,0 --initial 93 &
docker exec -it mn.vnf36_composite_stadium python vnf_script.py -h 10.0.0.104 -v 4437 -o 10.0.0.36 -q 5467 -n composite_stadium --topology 0.6939,0,0,0 --initial 111 &

docker exec -it mn.vnf28_fade_in python vnf_script.py -h 10.0.0.48 -v 4437 -o 10.0.0.32 -q 5463 -n fade_in --topology 0.1948,0,0,0 --initial 87 &
docker exec -it mn.vnf35_invert_colors python vnf_script.py -h 10.0.0.55 -v 4437 -o 10.0.0.36 -q 5467 -n invert_colors --topology 0.1829,0,0,0 --initial 108 &
docker exec -it mn.vnf31_mirror_x python vnf_script.py -h 10.0.0.51 -v 4437 -o 10.0.0.34 -q 5465 -n mirror_x --topology 0.1728,0,0,0 --initial 96 &

docker exec -it mn.vnf33_fade_out python vnf_script.py -h 10.0.0.53 -v 4437 -o 10.0.0.34 -q 5465 -n fade_out --topology 0.1571,0,0,0 --initial 102 &
docker exec -it mn.vnf32_annotate python vnf_script.py -h 10.0.0.52 -v 4437 -o 10.0.0.34 -q 5465 -n annotate --topology 0.6488,0,0,0 --initial 99 &

# Add VNFs to service 1
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.104 -p 4437 -n none -m none -v 10.0.0.50 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.50 -p 4437 -n none -m none -v 10.0.0.46 --vnf_port 4437

# Add VNFs to service 2
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.51 -p 4437 -n none -m none -v 10.0.0.55 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.55 -p 4437 -n none -m none -v 10.0.0.48 --vnf_port 4437

# Add VNFs to service 3
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.52 -p 4437 -n none -m none -v 10.0.0.53 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.53 -p 4437 -n none -m none -v 10.0.0.51 --vnf_port 4437

# Run command to be sure its working
docker exec -it mn.source python message_factory.py -t process -h 10.0.0.46 -p 4437 -n none -m none -v none --vnf_port none