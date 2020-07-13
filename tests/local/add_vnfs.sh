python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3003 -n none -m none -v 127.0.0.1 --vnf_port 3002
python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3002 -n none -m none -v 127.0.0.1 --vnf_port 3005
python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3005 -n none -m none -v 127.0.0.1 --vnf_port 3004
python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3004 -n none -m none -v 127.0.0.1 --vnf_port 3008

python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3007 -n none -m none -v 127.0.0.1 --vnf_port 3006
python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3006 -n none -m none -v 127.0.0.1 --vnf_port 3008
