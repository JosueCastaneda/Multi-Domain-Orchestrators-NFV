#!/bin/sh

#Add chains to services 
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 9125859a-bd3a-11ea-b335-04ea56f99520 -d 9125859a-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125859f-bd3a-11ea-b335-04ea56f99520 -d 9125859f-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125859e-bd3a-11ea-b335-04ea56f99520 -d 9125859e-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 912585a1-bd3a-11ea-b335-04ea56f99520 -d 912585a1-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 912585a0-bd3a-11ea-b335-04ea56f99520 -d 912585a0-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125859e-bd3a-11ea-b335-04ea56f99520 -d 9125859e-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125859f-bd3a-11ea-b335-04ea56f99520 -d 9125859f-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 912585a2-bd3a-11ea-b335-04ea56f99520 -d 912585a2-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 912585b1-bd3a-11ea-b335-04ea56f99520 -d 912585b1-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125859f-bd3a-11ea-b335-04ea56f99520 -d 9125859f-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 912585a5-bd3a-11ea-b335-04ea56f99520 -d 912585a5-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 912585a5-bd3a-11ea-b335-04ea56f99520 -d 912585a5-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 912585a5-bd3a-11ea-b335-04ea56f99520 -d 912585a5-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 912585a4-bd3a-11ea-b335-04ea56f99520 -d 912585a4-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 912585a8-bd3a-11ea-b335-04ea56f99520 -d 912585a8-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 912585a5-bd3a-11ea-b335-04ea56f99520 -d 912585a5-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 912585ae-bd3a-11ea-b335-04ea56f99520 -d 912585ae-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 912585ad-bd3a-11ea-b335-04ea56f99520 -d 912585ad-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125859e-bd3a-11ea-b335-04ea56f99520 -d 9125859e-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 912585a5-bd3a-11ea-b335-04ea56f99520 -d 912585a5-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 912585af-bd3a-11ea-b335-04ea56f99520 -d 912585af-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 912585b0-bd3a-11ea-b335-04ea56f99520 -d 912585b0-bd3a-11ea-b335-04ea56f99520

# Request updates (Commented) 
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 912585b6-bd3a-11ea-b335-04ea56f99520 --seed 695887
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 912585bb-bd3a-11ea-b335-04ea56f99520 --seed 370491
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 912585b7-bd3a-11ea-b335-04ea56f99520 --seed 958697
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 912585b4-bd3a-11ea-b335-04ea56f99520 --seed 857280
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 912585ba-bd3a-11ea-b335-04ea56f99520 --seed 703128
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 912585b7-bd3a-11ea-b335-04ea56f99520 --seed 173669
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 912585ba-bd3a-11ea-b335-04ea56f99520 --seed 534728
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 912585b9-bd3a-11ea-b335-04ea56f99520 --seed 112825
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 912585b5-bd3a-11ea-b335-04ea56f99520 --seed 393050
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 912585bc-bd3a-11ea-b335-04ea56f99520 --seed 767384

# Request scaling 
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 912585b6-bd3a-11ea-b335-04ea56f99520 --seed 695887
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 912585bb-bd3a-11ea-b335-04ea56f99520 --seed 370491
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 912585b7-bd3a-11ea-b335-04ea56f99520 --seed 958697
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 912585b4-bd3a-11ea-b335-04ea56f99520 --seed 857280
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 912585ba-bd3a-11ea-b335-04ea56f99520 --seed 703128
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 912585b7-bd3a-11ea-b335-04ea56f99520 --seed 173669
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 912585ba-bd3a-11ea-b335-04ea56f99520 --seed 534728
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 912585b9-bd3a-11ea-b335-04ea56f99520 --seed 112825
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 912585b5-bd3a-11ea-b335-04ea56f99520 --seed 393050
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 912585bc-bd3a-11ea-b335-04ea56f99520 --seed 767384

