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
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.
docker exec -it mn.



# Add VNFs to service 1
docker exec -it mn.source python message_factory.py -t add_chain -h 10.0.0.106 -p 4437 -n none -m none -v 10.0.0.64 --vnf_port 4437

# Run command to be sure its working
docker exec -it mn.source python message_factory.py -t process -h 10.0.0.13 -p 4437 -n none -m none -v none --vnf_port none