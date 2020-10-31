#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 10fdb8d0-1b7b-11eb-9945-525400e0bd2a --seed 13796
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 11022f1a-1b7b-11eb-9945-525400e0bd2a --seed 55767
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 11022f32-1b7b-11eb-9945-525400e0bd2a --seed 52888
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 11022d92-1b7b-11eb-9945-525400e0bd2a --seed 97863
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 11022ddc-1b7b-11eb-9945-525400e0bd2a --seed 76860
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

