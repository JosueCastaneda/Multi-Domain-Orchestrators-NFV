#!/bin/sh

# Request scaling 
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 23db6feb-ce65-11ea-9f26-04ea56f99520 --seed 8164220
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 23db6fe7-ce65-11ea-9f26-04ea56f99520 --seed 6005304
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 23db6fed-ce65-11ea-9f26-04ea56f99520 --seed 8872738
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 23db6fe1-ce65-11ea-9f26-04ea56f99520 --seed 9969444
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 23db6fdf-ce65-11ea-9f26-04ea56f99520 --seed 4339766
python3 message_factory.py -r external

# Add results 
#python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
#python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
#python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
#python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
#python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

