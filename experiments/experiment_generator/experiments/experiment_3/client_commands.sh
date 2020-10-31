#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 1107c8a1-1b7b-11eb-9945-525400e0bd2a --seed 36780
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 1107c8df-1b7b-11eb-9945-525400e0bd2a --seed 35770
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 1107c849-1b7b-11eb-9945-525400e0bd2a --seed 29717
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 1107cad5-1b7b-11eb-9945-525400e0bd2a --seed 66337
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

