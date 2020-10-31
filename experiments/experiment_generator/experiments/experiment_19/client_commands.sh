#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 924b5649-1ad8-11eb-9945-525400e0bd2a --seed 56724
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 92719805-1ad8-11eb-9945-525400e0bd2a --seed 61351
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 9271979d-1ad8-11eb-9945-525400e0bd2a --seed 28571
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 92719789-1ad8-11eb-9945-525400e0bd2a --seed 27937
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 92719833-1ad8-11eb-9945-525400e0bd2a --seed 42550
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

