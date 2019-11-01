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

# Add VNFs to service 8
python3 message_factory.py -t add_chain -h 10.0.0.19 -p 4447 -n none -m none -v 10.0.0.21 --vnf_port 4453
python3 message_factory.py -t add_chain -h 10.0.0.21 -p 4453 -n none -m none -v 10.0.0.13 --vnf_port 4433
python3 message_factory.py -t add_chain -h 10.0.0.13 -p 4433 -n none -m none -v 10.0.0.14 --vnf_port 4437
python3 message_factory.py -t add_chain -h 10.0.0.14 -p 4437 -n none -m none -v 10.0.0.15 --vnf_port 4439

# Add VNFs to service 20
python3 message_factory.py -t add_chain -h 10.0.0.41 -p 4471 -n none -m none -v 10.0.0.44 --vnf_port 4477
python3 message_factory.py -t add_chain -h 10.0.0.44 -p 4477 -n none -m none -v 10.0.0.24 --vnf_port 4457
python3 message_factory.py -t add_chain -h 10.0.0.24 -p 4457 -n none -m none -v 10.0.0.26 --vnf_port 4461
python3 message_factory.py -t add_chain -h 10.0.0.26 -p 4461 -n none -m none -v 10.0.0.27 --vnf_port 4463

# Add VNFs to service 22
python3 message_factory.py -t add_chain -h 10.0.0.44 -p 4477 -n none -m none -v 10.0.0.69 --vnf_port 4525
python3 message_factory.py -t add_chain -h 10.0.0.69 -p 4525 -n none -m none -v 10.0.0.27 --vnf_port 4463
python3 message_factory.py -t add_chain -h 10.0.0.27 -p 4563 -n none -m none -v 10.0.0.42 --vnf_port 4473
python3 message_factory.py -t add_chain -h 10.0.0.42 -p 4473 -n none -m none -v 10.0.0.29 --vnf_port 4467
python3 message_factory.py -t add_chain -h 10.0.0.29 -p 4467 -n none -m none -v 10.0.0.26 --vnf_port 4461

# Add VNFs to service 24
python3 message_factory.py -t add_chain -h 10.0.0.44 -p 4477 -n none -m none -v 10.0.0.41 --vnf_port 4471
python3 message_factory.py -t add_chain -h 10.0.0.41 -p 4471 -n none -m none -v 10.0.0.26 --vnf_port 4461
python3 message_factory.py -t add_chain -h 10.0.0.26 -p 4461 -n none -m none -v 10.0.0.29 --vnf_port 4467
python3 message_factory.py -t add_chain -h 10.0.0.29 -p 4467 -n none -m none -v 10.0.0.24 --vnf_port 4457
python3 message_factory.py -t add_chain -h 10.0.0.24 -p 4457 -n none -m none -v 10.0.0.27 --vnf_port 4463

# Add VNFs to service 27
python3 message_factory.py -t add_chain -h 10.0.0.52 -p 4491 -n none -m none -v 10.0.0.53 --vnf_port 4493
python3 message_factory.py -t add_chain -h 10.0.0.53 -p 4493 -n none -m none -v 10.0.0.51 --vnf_port 4491

# Add VNFs to service 30
python3 message_factory.py -t add_chain -h 10.0.0.53 -p 4493 -n none -m none -v 10.0.0.55 --vnf_port 4497
python3 message_factory.py -t add_chain -h 10.0.0.55 -p 4497 -n none -m none -v 10.0.0.46 --vnf_port 4481
python3 message_factory.py -t add_chain -h 10.0.0.46 -p 4481 -n none -m none -v 10.0.0.51 --vnf_port 4491

# Add VNFs to service 35
python3 message_factory.py -t add_chain -h 10.0.0.53 -p 4493 -n none -m none -v 10.0.0.55 --vnf_port 4497
python3 message_factory.py -t add_chain -h 10.0.0.55 -p 4497 -n none -m none -v 10.0.0.45 --vnf_port 4479
python3 message_factory.py -t add_chain -h 10.0.0.45 -p 4479 -n none -m none -v 10.0.0.52 --vnf_port 4529
python3 message_factory.py -t add_chain -h 10.0.0.52 -p 4529 -n none -m none -v 10.0.0.50 --vnf_port 4489
python3 message_factory.py -t add_chain -h 10.0.0.50 -p 4489 -n none -m none -v 10.0.0.46 --vnf_port 4481

# Add VNFs to service 37
python3 message_factory.py -t add_chain -h 10.0.0.62 -p 4511 -n none -m none -v 10.0.0.66 --vnf_port 4519
python3 message_factory.py -t add_chain -h 10.0.0.66 -p 4519 -n none -m none -v 10.0.0.59 --vnf_port 4505

# Send the processing message

#Test migration

