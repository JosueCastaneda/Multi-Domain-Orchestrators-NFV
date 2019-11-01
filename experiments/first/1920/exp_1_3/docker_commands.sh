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
docker exec -it mn.vnf41_fade_in python vnf_script.py -h 10.0.0.59 -v 4505 -o 10.0.0.32 -q 5463 -n fade_in --topology 0.2739,0,0,0 --initial 126 &
docker exec -it mn.vnf48_invert_colors python vnf_script.py -h 10.0.0.66 -v 4519 -o 10.0.0.36 -q 5467 -n invert_colors --topology 0.2680,0,0,0 --initial 147 &
docker exec -it mn.vnf44_mirror_x python vnf_script.py -h 10.0.0.62 -v 4511 -o 10.0.0.34 -q 5465 -n mirror_x --topology 0.2493,0,0,0 --initial 135 &

docker exec -it mn.vnf39_rotate python vnf_script.py -h 10.0.0.57 -v 4501 -o 10.0.0.30 -q 5461 -n rotate --topology 0.2653,0,0,0 --initial 120 &
docker exec -it mn.vnf43_mirror_y python vnf_script.py -h 10.0.0.61 -v 4509 -o 10.0.0.32 -q 5463 -n mirror_y --topology 0.2507,0,0,0 --initial 132 &
docker exec -it mn.vnf49_composite_stadium python vnf_script.py -h 10.0.0.67 -v 4521 -o 10.0.0.106 -q 5467 -n composite_stadium -- topology 1.4645,0,0,0 --initial 150 &

docker exec -it mn.vnf46_fade_out python vnf_script.py -h 10.0.0.64 -v 4515 -o 10.0.0.34 -q 5465 -n fade_out --topology 0.2152,0,0,0 --initial 141 &
docker exec -it mn.vnf45_annotate python vnf_script.py -h 10.0.0.63 -v 4513 -o 10.0.0.34 -q 5465 -n annotate --topology 1.1528,0,0,0 --initial 138 &

# Add VNFs to service 1
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.62 -p 4437 -n none -m none -v 10.0.0.66 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.66 -p 4437 -n none -m none -v 10.0.0.59 --vnf_port 4437

# Add VNFs to service 2
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.67 -p 4437 -n none -m none -v 10.0.0.61 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.61 -p 4437 -n none -m none -v 10.0.0.57 --vnf_port 4437

# Add VNFs to service 3
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.63 -p 4437 -n none -m none -v 10.0.0.64 --vnf_port 4437
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.64 -p 4437 -n none -m none -v 10.0.0.62 --vnf_port 4437

# Run command to be sure its working
docker exec -it mn.source python message_factory.py -t process -h 10.0.0.13 -p 4437 -n none -m none -v none --vnf_port none