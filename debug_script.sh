# Add orchestrators

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5461 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5463
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5461 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5465

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5463 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5461
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5463 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5465

python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5465 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5461
python3 message_factory.py -t add_orchestrator -h 127.0.0.1 -p 5465 -n none -m none --vnf_host 127.0.0.1 --vnf_port 5463


# Add VNFs to chain

python3 message_factory.py -t add_chain -h 127.0.0.1 -p 4435 -n none -m none -v 127.0.0.1 --vnf_port 4433
python3 message_factory.py -t add_chain -h 127.0.0.1 -p 4433 -n none -m none -v 127.0.0.1 --vnf_port 4431

# Send the processing message
# Test video sending
#python3 message_factory.py -t process -h 127.0.0.1 -p 4431 -n none -m none -v none --vnf_port none

# Test migration
python3 message_factory.py -t migration -h 127.0.0.1 -p 5463 -n speed_up -m new -v none --vnf_port none