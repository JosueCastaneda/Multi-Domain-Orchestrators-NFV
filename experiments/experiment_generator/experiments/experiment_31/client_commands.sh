#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i b45592fb-1900-11eb-9945-525400e0bd2a --seed 11072
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i b45594c1-1900-11eb-9945-525400e0bd2a --seed 92319
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i b45594ff-1900-11eb-9945-525400e0bd2a --seed 83216
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i b45594a7-1900-11eb-9945-525400e0bd2a --seed 57685
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i b45594e5-1900-11eb-9945-525400e0bd2a --seed 56363
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

