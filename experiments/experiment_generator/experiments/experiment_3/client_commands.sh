#!/bin/sh

#Add chains to services 
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125860c-bd3a-11ea-b335-04ea56f99520 -d 9125860c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125860d-bd3a-11ea-b335-04ea56f99520 -d 9125860d-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125860b-bd3a-11ea-b335-04ea56f99520 -d 9125860b-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125860a-bd3a-11ea-b335-04ea56f99520 -d 9125860a-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125861b-bd3a-11ea-b335-04ea56f99520 -d 9125861b-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125860e-bd3a-11ea-b335-04ea56f99520 -d 9125860e-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 9125860c-bd3a-11ea-b335-04ea56f99520 -d 9125860c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 91258617-bd3a-11ea-b335-04ea56f99520 -d 91258617-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 91258614-bd3a-11ea-b335-04ea56f99520 -d 91258614-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 9125861b-bd3a-11ea-b335-04ea56f99520 -d 9125861b-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 91258610-bd3a-11ea-b335-04ea56f99520 -d 91258610-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 91258617-bd3a-11ea-b335-04ea56f99520 -d 91258617-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258619-bd3a-11ea-b335-04ea56f99520 -d 91258619-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125861c-bd3a-11ea-b335-04ea56f99520 -d 9125861c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125860e-bd3a-11ea-b335-04ea56f99520 -d 9125860e-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258610-bd3a-11ea-b335-04ea56f99520 -d 91258610-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125861c-bd3a-11ea-b335-04ea56f99520 -d 9125861c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125860e-bd3a-11ea-b335-04ea56f99520 -d 9125860e-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258615-bd3a-11ea-b335-04ea56f99520 -d 91258615-bd3a-11ea-b335-04ea56f99520

# Request updates (Commented) 
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 91258627-bd3a-11ea-b335-04ea56f99520 --seed 695887
# python message_factory.py -t request_update -h 52.141.61.172 -p 5003 -i 91258624-bd3a-11ea-b335-04ea56f99520 --seed 370491
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 91258620-bd3a-11ea-b335-04ea56f99520 --seed 958697
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 91258623-bd3a-11ea-b335-04ea56f99520 --seed 857280
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 91258628-bd3a-11ea-b335-04ea56f99520 --seed 703128
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 91258620-bd3a-11ea-b335-04ea56f99520 --seed 173669
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 91258628-bd3a-11ea-b335-04ea56f99520 --seed 534728
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 91258626-bd3a-11ea-b335-04ea56f99520 --seed 112825
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 91258622-bd3a-11ea-b335-04ea56f99520 --seed 393050
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 91258625-bd3a-11ea-b335-04ea56f99520 --seed 767384

# Request scaling 
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 91258627-bd3a-11ea-b335-04ea56f99520 --seed 695887
python message_factory.py -t request_scale -h 52.141.61.172 -p 5003 -i 91258624-bd3a-11ea-b335-04ea56f99520 --seed 370491
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 91258620-bd3a-11ea-b335-04ea56f99520 --seed 958697
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 91258623-bd3a-11ea-b335-04ea56f99520 --seed 857280
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 91258628-bd3a-11ea-b335-04ea56f99520 --seed 703128
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 91258620-bd3a-11ea-b335-04ea56f99520 --seed 173669
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 91258628-bd3a-11ea-b335-04ea56f99520 --seed 534728
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 91258626-bd3a-11ea-b335-04ea56f99520 --seed 112825
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 91258622-bd3a-11ea-b335-04ea56f99520 --seed 393050
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 91258625-bd3a-11ea-b335-04ea56f99520 --seed 767384

