#!/bin/sh

#Add chains to services 
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f610c-c031-11ea-b335-04ea56f99520 -d 000f610c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f610d-c031-11ea-b335-04ea56f99520 -d 000f610d-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f610b-c031-11ea-b335-04ea56f99520 -d 000f610b-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f610a-c031-11ea-b335-04ea56f99520 -d 000f610a-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f611b-c031-11ea-b335-04ea56f99520 -d 000f611b-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 000f610e-c031-11ea-b335-04ea56f99520 -d 000f610e-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 000f610c-c031-11ea-b335-04ea56f99520 -d 000f610c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f6117-c031-11ea-b335-04ea56f99520 -d 000f6117-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f6114-c031-11ea-b335-04ea56f99520 -d 000f6114-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f611b-c031-11ea-b335-04ea56f99520 -d 000f611b-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f6110-c031-11ea-b335-04ea56f99520 -d 000f6110-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 000f6117-c031-11ea-b335-04ea56f99520 -d 000f6117-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6119-c031-11ea-b335-04ea56f99520 -d 000f6119-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f611c-c031-11ea-b335-04ea56f99520 -d 000f611c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f610e-c031-11ea-b335-04ea56f99520 -d 000f610e-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6110-c031-11ea-b335-04ea56f99520 -d 000f6110-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f611c-c031-11ea-b335-04ea56f99520 -d 000f611c-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f610e-c031-11ea-b335-04ea56f99520 -d 000f610e-c031-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 000f6115-c031-11ea-b335-04ea56f99520 -d 000f6115-c031-11ea-b335-04ea56f99520

# Request updates (Commented) 
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f6127-c031-11ea-b335-04ea56f99520 --seed 695887
# python message_factory.py -t request_update -h 52.141.61.172 -p 5003 -i 000f6124-c031-11ea-b335-04ea56f99520 --seed 370491
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f6120-c031-11ea-b335-04ea56f99520 --seed 958697
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f6123-c031-11ea-b335-04ea56f99520 --seed 857280
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f6128-c031-11ea-b335-04ea56f99520 --seed 703128
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 000f6120-c031-11ea-b335-04ea56f99520 --seed 173669
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f6128-c031-11ea-b335-04ea56f99520 --seed 534728
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f6126-c031-11ea-b335-04ea56f99520 --seed 112825
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 000f6122-c031-11ea-b335-04ea56f99520 --seed 393050
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 000f6125-c031-11ea-b335-04ea56f99520 --seed 767384

# Request scaling 
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f6127-c031-11ea-b335-04ea56f99520 --seed 695887
python message_factory.py -t request_scale -h 52.141.61.172 -p 5003 -i 000f6124-c031-11ea-b335-04ea56f99520 --seed 370491
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f6120-c031-11ea-b335-04ea56f99520 --seed 958697
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f6123-c031-11ea-b335-04ea56f99520 --seed 857280
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f6128-c031-11ea-b335-04ea56f99520 --seed 703128
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 000f6120-c031-11ea-b335-04ea56f99520 --seed 173669
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f6128-c031-11ea-b335-04ea56f99520 --seed 534728
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f6126-c031-11ea-b335-04ea56f99520 --seed 112825
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 000f6122-c031-11ea-b335-04ea56f99520 --seed 393050
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 000f6125-c031-11ea-b335-04ea56f99520 --seed 767384

