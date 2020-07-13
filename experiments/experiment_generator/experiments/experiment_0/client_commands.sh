#!/bin/sh

#Add chains to services (Commented)
#python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 000f609a-c031-11ea-b335-04ea56f99520 -d 000f609a-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f609f-c031-11ea-b335-04ea56f99520 -d 000f609f-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f609e-c031-11ea-b335-04ea56f99520 -d 000f609e-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f60a1-c031-11ea-b335-04ea56f99520 -d 000f60a1-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f60a0-c031-11ea-b335-04ea56f99520 -d 000f60a0-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f609e-c031-11ea-b335-04ea56f99520 -d 000f609e-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f609f-c031-11ea-b335-04ea56f99520 -d 000f609f-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f60a2-c031-11ea-b335-04ea56f99520 -d 000f60a2-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f60b1-c031-11ea-b335-04ea56f99520 -d 000f60b1-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f609f-c031-11ea-b335-04ea56f99520 -d 000f609f-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f60a5-c031-11ea-b335-04ea56f99520 -d 000f60a5-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f60a5-c031-11ea-b335-04ea56f99520 -d 000f60a5-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f60a5-c031-11ea-b335-04ea56f99520 -d 000f60a5-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f60a4-c031-11ea-b335-04ea56f99520 -d 000f60a4-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f60a8-c031-11ea-b335-04ea56f99520 -d 000f60a8-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f60a5-c031-11ea-b335-04ea56f99520 -d 000f60a5-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f60ae-c031-11ea-b335-04ea56f99520 -d 000f60ae-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f60ad-c031-11ea-b335-04ea56f99520 -d 000f60ad-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f609e-c031-11ea-b335-04ea56f99520 -d 000f609e-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f60a5-c031-11ea-b335-04ea56f99520 -d 000f60a5-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f60af-c031-11ea-b335-04ea56f99520 -d 000f60af-c031-11ea-b335-04ea56f99520
#python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f60b0-c031-11ea-b335-04ea56f99520 -d 000f60b0-c031-11ea-b335-04ea56f99520

# Request updates (Commented) 
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f60b6-c031-11ea-b335-04ea56f99520 --seed 695887
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f60bb-c031-11ea-b335-04ea56f99520 --seed 370491
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 958697
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f60b4-c031-11ea-b335-04ea56f99520 --seed 857280
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f60ba-c031-11ea-b335-04ea56f99520 --seed 703128
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 173669
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f60ba-c031-11ea-b335-04ea56f99520 --seed 534728
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f60b9-c031-11ea-b335-04ea56f99520 --seed 112825
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f60b5-c031-11ea-b335-04ea56f99520 --seed 393050
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 000f60bc-c031-11ea-b335-04ea56f99520 --seed 767384

# Request scaling 
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f60b6-c031-11ea-b335-04ea56f99520 --seed 695887
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f60bb-c031-11ea-b335-04ea56f99520 --seed 370491
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 958697
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f60b4-c031-11ea-b335-04ea56f99520 --seed 857280
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f60ba-c031-11ea-b335-04ea56f99520 --seed 703128
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 173669
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f60ba-c031-11ea-b335-04ea56f99520 --seed 534728
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f60b9-c031-11ea-b335-04ea56f99520 --seed 112825
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f60b5-c031-11ea-b335-04ea56f99520 --seed 393050
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 000f60bc-c031-11ea-b335-04ea56f99520 --seed 767384

