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

# Add VNFs to service 7
python3 message_factory.py -t add_chain -h 10.0.0.17 -p 4443 -n none -m none -v 10.0.0.18 --vnf_port 4445
python3 message_factory.py -t add_chain -h 10.0.0.18 -p 4445 -n none -m none -v 10.0.0.20 --vnf_port 4449
python3 message_factory.py -t add_chain -h 10.0.0.20 -p 4449 -n none -m none -v 10.0.0.68 --vnf_port 4523
python3 message_factory.py -t add_chain -h 10.0.0.68 -p 4523 -n none -m none -v 10.0.0.19 --vnf_port 4447

# Add VNFs to service 8
python3 message_factory.py -t add_chain -h 10.0.0.19 -p 4447 -n none -m none -v 10.0.0.21 --vnf_port 4453
python3 message_factory.py -t add_chain -h 10.0.0.21 -p 4453 -n none -m none -v 10.0.0.13 --vnf_port 4433
python3 message_factory.py -t add_chain -h 10.0.0.13 -p 4433 -n none -m none -v 10.0.0.14 --vnf_port 4437
python3 message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4439

# Add VNFs to service 9
python3 message_factory.py -t add_chain -h 10.0.0.68 -p 4523 -n none -m none -v 10.0.0.15 --vnf_port 4439
python3 message_factory.py -t add_chain -h 10.0.0.15 -p 4439 -n none -m none -v 10.0.0.21 --vnf_port 4451
python3 message_factory.py -t add_chain -h 10.0.0.21 -p 4451 -n none -m none -v 10.0.0.18 --vnf_port 4445
python3 message_factory.py -t add_chain -h 10.0.0.18 -p 4445 -n none -m none -v 10.0.0.16 --vnf_port 4441

# Send the processing message

#Test migration

