#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 23db6e88-ce65-11ea-9f26-04ea56f99520 --seed 8106241
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 23db6e8a-ce65-11ea-9f26-04ea56f99520 --seed 2058391
#python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 23db6e85-ce65-11ea-9f26-04ea56f99520 --seed 9166286

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

