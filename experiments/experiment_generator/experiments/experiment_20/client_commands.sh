#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 929b345e-1ad8-11eb-9945-525400e0bd2a --seed 48364
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 927199a8-1ad8-11eb-9945-525400e0bd2a --seed 27937
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 927199da-1ad8-11eb-9945-525400e0bd2a --seed 42550
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 929b34aa-1ad8-11eb-9945-525400e0bd2a --seed 94318
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

