#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 23e5880c-ce65-11ea-9f26-04ea56f99520 --seed 7009439
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 23e58805-ce65-11ea-9f26-04ea56f99520 --seed 188037
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 23e5880d-ce65-11ea-9f26-04ea56f99520 --seed 2434822
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 23e58812-ce65-11ea-9f26-04ea56f99520 --seed 635768

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

