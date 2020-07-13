#!/bin/sh

#Add chains to services 
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 000f612c-c031-11ea-b335-04ea56f99520 -d 000f612c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 000f612d-c031-11ea-b335-04ea56f99520 -d 000f612d-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 000f612b-c031-11ea-b335-04ea56f99520 -d 000f612b-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f612c-c031-11ea-b335-04ea56f99520 -d 000f612c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f612c-c031-11ea-b335-04ea56f99520 -d 000f612c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f6132-c031-11ea-b335-04ea56f99520 -d 000f6132-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f6131-c031-11ea-b335-04ea56f99520 -d 000f6131-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f612f-c031-11ea-b335-04ea56f99520 -d 000f612f-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6133-c031-11ea-b335-04ea56f99520 -d 000f6133-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6137-c031-11ea-b335-04ea56f99520 -d 000f6137-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6135-c031-11ea-b335-04ea56f99520 -d 000f6135-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6134-c031-11ea-b335-04ea56f99520 -d 000f6134-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6138-c031-11ea-b335-04ea56f99520 -d 000f6138-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f612c-c031-11ea-b335-04ea56f99520 -d 000f612c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f613a-c031-11ea-b335-04ea56f99520 -d 000f613a-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f612c-c031-11ea-b335-04ea56f99520 -d 000f612c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f613d-c031-11ea-b335-04ea56f99520 -d 000f613d-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6141-c031-11ea-b335-04ea56f99520 -d 000f6141-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6134-c031-11ea-b335-04ea56f99520 -d 000f6134-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f613d-c031-11ea-b335-04ea56f99520 -d 000f613d-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f612c-c031-11ea-b335-04ea56f99520 -d 000f612c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6140-c031-11ea-b335-04ea56f99520 -d 000f6140-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f613d-c031-11ea-b335-04ea56f99520 -d 000f613d-c031-11ea-b335-04ea56f99520

# Request updates (Commented) 
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f6149-c031-11ea-b335-04ea56f99520 --seed 695887
# python message_factory.py -t request_update -h 52.141.61.172 -p 5003 -i 000f6143-c031-11ea-b335-04ea56f99520 --seed 370491
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 000f6144-c031-11ea-b335-04ea56f99520 --seed 958697
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f6148-c031-11ea-b335-04ea56f99520 --seed 857280
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f614a-c031-11ea-b335-04ea56f99520 --seed 703128
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 000f6144-c031-11ea-b335-04ea56f99520 --seed 173669
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f614a-c031-11ea-b335-04ea56f99520 --seed 534728
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f6146-c031-11ea-b335-04ea56f99520 --seed 112825
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 000f614c-c031-11ea-b335-04ea56f99520 --seed 393050
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 000f6145-c031-11ea-b335-04ea56f99520 --seed 767384

# Request scaling 
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f6149-c031-11ea-b335-04ea56f99520 --seed 695887
python message_factory.py -t request_scale -h 52.141.61.172 -p 5003 -i 000f6143-c031-11ea-b335-04ea56f99520 --seed 370491
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 000f6144-c031-11ea-b335-04ea56f99520 --seed 958697
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f6148-c031-11ea-b335-04ea56f99520 --seed 857280
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f614a-c031-11ea-b335-04ea56f99520 --seed 703128
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 000f6144-c031-11ea-b335-04ea56f99520 --seed 173669
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f614a-c031-11ea-b335-04ea56f99520 --seed 534728
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f6146-c031-11ea-b335-04ea56f99520 --seed 112825
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 000f614c-c031-11ea-b335-04ea56f99520 --seed 393050
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 000f6145-c031-11ea-b335-04ea56f99520 --seed 767384

