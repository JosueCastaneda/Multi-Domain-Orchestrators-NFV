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

# Add VNFs to service 22
python3 message_factory.py -t add_chain -h 10.0.0.44 -p 4477 -n none -m none -v 10.0.0.69 --vnf_port 4525
python3 message_factory.py -t add_chain -h 10.0.0.69 -p 4525 -n none -m none -v 10.0.0.27 --vnf_port 4463
python3 message_factory.py -t add_chain -h 10.0.0.27 -p 4563 -n none -m none -v 10.0.0.42 --vnf_port 4473
python3 message_factory.py -t add_chain -h 10.0.0.42 -p 4473 -n none -m none -v 10.0.0.29 --vnf_port 4467
python3 message_factory.py -t add_chain -h 10.0.0.29 -p 4467 -n none -m none -v 10.0.0.26 --vnf_port 4461

# Add VNFs to service 23
python3 message_factory.py -t add_chain -h 10.0.0.41 -p 4471 -n none -m none -v 10.0.0.43 --vnf_port 4475
python3 message_factory.py -t add_chain -h 10.0.0.43 -p 4475 -n none -m none -v 10.0.0.23 --vnf_port 4455
python3 message_factory.py -t add_chain -h 10.0.0.23 -p 4455 -n none -m none -v 10.0.0.40 --vnf_port 4469
python3 message_factory.py -t add_chain -h 10.0.0.40 -p 4469 -n none -m none -v 10.0.0.28 --vnf_port 4465
python3 message_factory.py -t add_chain -h 10.0.0.28 -p 4465 -n none -m none -v 10.0.0.24 --vnf_port 4457

# Add VNFs to service 24
python3 message_factory.py -t add_chain -h 10.0.0.44 -p 4477 -n none -m none -v 10.0.0.41 --vnf_port 4471
python3 message_factory.py -t add_chain -h 10.0.0.41 -p 4471 -n none -m none -v 10.0.0.26 --vnf_port 4461
python3 message_factory.py -t add_chain -h 10.0.0.26 -p 4461 -n none -m none -v 10.0.0.29 --vnf_port 4467
python3 message_factory.py -t add_chain -h 10.0.0.29 -p 4467 -n none -m none -v 10.0.0.24 --vnf_port 4457
python3 message_factory.py -t add_chain -h 10.0.0.24 -p 4457 -n none -m none -v 10.0.0.27 --vnf_port 4463

# Send the processing message

#Test migration

