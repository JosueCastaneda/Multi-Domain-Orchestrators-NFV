#!/bin/sh

# Request scaling 
#python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 23d13607-ce65-11ea-9f26-04ea56f99520 --seed 359052
#python message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 23d13600-ce65-11ea-9f26-04ea56f99520 --seed 316597
python message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 23d1360c-ce65-11ea-9f26-04ea56f99520 --seed 132714
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 23d13606-ce65-11ea-9f26-04ea56f99520 --seed 357518
python3 message_factory.py -r external
python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 23d13601-ce65-11ea-9f26-04ea56f99520 --seed 771362
python3 message_factory.py -r external


# Add results 
#python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
#python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
#python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
#python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
#python3 message_factory.py -h 52.151.70.54 -p 5005 -r external

