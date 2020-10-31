#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 91e88c44-1ad8-11eb-9945-525400e0bd2a --seed 46335
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 920770b6-1ad8-11eb-9945-525400e0bd2a --seed 65671
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 91e88c04-1ad8-11eb-9945-525400e0bd2a --seed 11581
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 92077046-1ad8-11eb-9945-525400e0bd2a --seed 54880
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 91e88b7e-1ad8-11eb-9945-525400e0bd2a --seed 54502
python3 message_factory.py -r external

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

