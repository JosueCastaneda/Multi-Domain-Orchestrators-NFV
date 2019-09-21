
# Add VNFs to chain

python3 message_factory.py -t add_chain -h 127.0.0.1 -p 4435 -n none -m none -v 127.0.0.1 --vnf_port 4433

python3 message_factory.py -t add_chain -h 127.0.0.1 -p 4433 -n none -m none -v 127.0.0.1 --vnf_port 4431

# Send the processing message

python3 message_factory.py -t process -h 127.0.0.1 -p 4431 -n none -m none -v none --vnf_port none