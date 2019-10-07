# Add orchestrators

python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463
python message_factory.py -t add_orchestrator -h 10.0.0.30 -p 5461 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5465

python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
python message_factory.py -t add_orchestrator -h 10.0.0.32 -p 5463 -n none -m none --vnf_host 10.0.0.34 --vnf_port 5465

python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.30 --vnf_port 5461
python message_factory.py -t add_orchestrator -h 10.0.0.34 -p 5465 -n none -m none --vnf_host 10.0.0.32 --vnf_port 5463


# Add VNFs to chain

python message_factory.py -t add_chain -h 10.0.0.16 -p 4435 -n none -m none -v 10.0.0.13 --vnf_port 4433

python message_factory.py -t add_chain -h 10.0.0.13 -p 4433 -n none -m none -v 10.0.0.12 --vnf_port 4431

# Test migration
python message_factory.py -t migration -h 10.0.0.32 -p 5463 -n speed_up -m new -v none --vnf_port none
