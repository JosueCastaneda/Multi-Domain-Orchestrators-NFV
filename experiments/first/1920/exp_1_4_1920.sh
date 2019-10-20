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

# Add VNFs to service 40
python3 message_factory.py -t add_chain -h 10.0.0.58 -p 4503 -n none -m none -v 10.0.0.60 --vnf_port 4507
python3 message_factory.py -t add_chain -h 10.0.0.60 -p 4507 -n none -m none -v 10.0.0.56 --vnf_port 4499
python3 message_factory.py -t add_chain -h 10.0.0.56 -p 4499 -n none -m none -v 10.0.0.57 --vnf_port 4501

# Add VNFs to service 41
python3 message_factory.py -t add_chain -h 10.0.0.63 -p 4513 -n none -m none -v 10.0.0.56 --vnf_port 4499
python3 message_factory.py -t add_chain -h 10.0.0.56 -p 4499 -n none -m none -v 10.0.0.60 --vnf_port 4507
python3 message_factory.py -t add_chain -h 10.0.0.60 -p 4507 -n none -m none -v 10.0.0.65 --vnf_port 4517

# Add VNFs to service 42
python3 message_factory.py -t add_chain -h 10.0.0.64 -p 4515 -n none -m none -v 10.0.0.66 --vnf_port 4519
python3 message_factory.py -t add_chain -h 10.0.0.66 -p 4519 -n none -m none -v 10.0.0.57 --vnf_port 4501
python3 message_factory.py -t add_chain -h 10.0.0.57 -p 4501 -n none -m none -v 10.0.0.62 --vnf_port 4511

# Send the processing message

#Test migration

