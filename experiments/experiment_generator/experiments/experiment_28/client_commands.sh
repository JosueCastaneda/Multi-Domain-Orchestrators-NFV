#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 23e587cc-ce65-11ea-9f26-04ea56f99520 --seed 2038958
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 23e587c5-ce65-11ea-9f26-04ea56f99520 --seed 7663581
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 23e587be-ce65-11ea-9f26-04ea56f99520 --seed 1992531
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 23e587c2-ce65-11ea-9f26-04ea56f99520 --seed 188037

# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

