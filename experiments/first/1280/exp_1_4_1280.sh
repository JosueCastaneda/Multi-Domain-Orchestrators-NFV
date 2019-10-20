# Add orchestrators to first orchestrator
python3 message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
python3 message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5465
python3 message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add orchestrators to second orchestrator
python3 message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
python3 message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5465
python3 message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add orchestrators to third orchestrator
python3 message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
python3 message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
python3 message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add orchestrators to fourth orchestrator
python3 message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5467 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
python3 message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5467 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
python3 message_factory.py -t add_orchestrator -h 10.0.0.36 -p 5467 -n none -m none --vnf_host 10.0.0.36 --vnf_port 5467

# Add VNFs to service 28
python3 message_factory.py -t add_chain -h 10.0.0.47 -p 4483 -n none -m none -v 10.0.0.49 --vnf_port 4487
python3 message_factory.py -t add_chain -h 10.0.0.49 -p 4487 -n none -m none -v 10.0.0.45 --vnf_port 4479
python3 message_factory.py -t add_chain -h 10.0.0.45 -p 4479 -n none -m none -v 10.0.0.46 --vnf_port 4481

# Add VNFs to service 29
python3 message_factory.py -t add_chain -h 10.0.0.52 -p 4491 -n none -m none -v 10.0.0.45 --vnf_port 4479
python3 message_factory.py -t add_chain -h 10.0.0.45 -p 4479 -n none -m none -v 10.0.0.49 --vnf_port 4487
python3 message_factory.py -t add_chain -h 10.0.0.49 -p 4487 -n none -m none -v 10.0.0.54 --vnf_port 4495

# Add VNFs to service 30
python3 message_factory.py -t add_chain -h 10.0.0.53 -p 4493 -n none -m none -v 10.0.0.55 --vnf_port 4497
python3 message_factory.py -t add_chain -h 10.0.0.55 -p 4497 -n none -m none -v 10.0.0.46 --vnf_port 4481
python3 message_factory.py -t add_chain -h 10.0.0.46 -p 4481 -n none -m none -v 10.0.0.51 --vnf_port 4491

# Send the processing message

#Test migration

