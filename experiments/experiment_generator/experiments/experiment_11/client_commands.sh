#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 91724d73-1ad8-11eb-9945-525400e0bd2a --seed 54515
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 9185f0f9-1ad8-11eb-9945-525400e0bd2a --seed 74059
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 9185f22b-1ad8-11eb-9945-525400e0bd2a --seed 91095
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 91724cb7-1ad8-11eb-9945-525400e0bd2a --seed 44600
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

