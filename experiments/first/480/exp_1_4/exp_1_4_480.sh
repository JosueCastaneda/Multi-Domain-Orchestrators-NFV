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

# Add VNFs to service 4
python3 message_factory.py -t add_chain -h 10.0.0.101 -p 4435 -n none -m none -v 10.0.0.15 --vnf_port 4439
python3 message_factory.py -t add_chain -h 10.0.0.15 -p 4439 -n none -m none -v 10.0.0.12 --vnf_port 4431
python3 message_factory.py -t add_chain -h 10.0.0.12 -p 4431 -n none -m none -v 10.0.0.13 --vnf_port 4433

# Add VNFs to service 5
python3 message_factory.py -t add_chain -h 10.0.0.18 -p 4445 -n none -m none -v 10.0.0.12 --vnf_port 4431
python3 message_factory.py -t add_chain -h 10.0.0.12 -p 4431 -n none -m none -v 10.0.0.15 --vnf_port 4439
python3 message_factory.py -t add_chain -h 10.0.0.15 -p 4439 -n none -m none -v 10.0.0.20 --vnf_port 4449

# Add VNFs to service 6
python3 message_factory.py -t add_chain -h 10.0.0.19 -p 4447 -n none -m none -v 10.0.0.21 --vnf_port 4451
python3 message_factory.py -t add_chain -h 10.0.0.21 -p 4451 -n none -m none -v 10.0.0.13 --vnf_port 4433
python3 message_factory.py -t add_chain -h 10.0.0.13 -p 4433 -n none -m none -v 10.0.0.17 --vnf_port 4443

# Send the processing message

#Test migration

