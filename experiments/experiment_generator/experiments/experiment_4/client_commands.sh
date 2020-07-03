#!/bin/sh

#Add chains to services 
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 9125862c-bd3a-11ea-b335-04ea56f99520 -d 9125862c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 9125862d-bd3a-11ea-b335-04ea56f99520 -d 9125862d-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 40.127.108.223 -p 5001 -s 9125862b-bd3a-11ea-b335-04ea56f99520 -d 9125862b-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125862c-bd3a-11ea-b335-04ea56f99520 -d 9125862c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125862c-bd3a-11ea-b335-04ea56f99520 -d 9125862c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 91258632-bd3a-11ea-b335-04ea56f99520 -d 91258632-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 91258631-bd3a-11ea-b335-04ea56f99520 -d 91258631-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.229.37.237 -p 5002 -s 9125862f-bd3a-11ea-b335-04ea56f99520 -d 9125862f-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258633-bd3a-11ea-b335-04ea56f99520 -d 91258633-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258637-bd3a-11ea-b335-04ea56f99520 -d 91258637-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258635-bd3a-11ea-b335-04ea56f99520 -d 91258635-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258634-bd3a-11ea-b335-04ea56f99520 -d 91258634-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.141.61.172 -p 5003 -s 91258638-bd3a-11ea-b335-04ea56f99520 -d 91258638-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 9125862c-bd3a-11ea-b335-04ea56f99520 -d 9125862c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 9125863a-bd3a-11ea-b335-04ea56f99520 -d 9125863a-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 20.185.45.222 -p 5004 -s 9125862c-bd3a-11ea-b335-04ea56f99520 -d 9125862c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125863d-bd3a-11ea-b335-04ea56f99520 -d 9125863d-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258641-bd3a-11ea-b335-04ea56f99520 -d 91258641-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258634-bd3a-11ea-b335-04ea56f99520 -d 91258634-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125863d-bd3a-11ea-b335-04ea56f99520 -d 9125863d-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125862c-bd3a-11ea-b335-04ea56f99520 -d 9125862c-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 91258640-bd3a-11ea-b335-04ea56f99520 -d 91258640-bd3a-11ea-b335-04ea56f99520
python message_factory.py -t add_chain -h 52.151.70.54 -p 5005 -s 9125863d-bd3a-11ea-b335-04ea56f99520 -d 9125863d-bd3a-11ea-b335-04ea56f99520

# Request updates (Commented) 
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 91258649-bd3a-11ea-b335-04ea56f99520 --seed 695887
# python message_factory.py -t request_update -h 52.141.61.172 -p 5003 -i 91258643-bd3a-11ea-b335-04ea56f99520 --seed 370491
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 91258644-bd3a-11ea-b335-04ea56f99520 --seed 958697
# python message_factory.py -t request_update -h 52.229.37.237 -p 5002 -i 91258648-bd3a-11ea-b335-04ea56f99520 --seed 857280
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 9125864a-bd3a-11ea-b335-04ea56f99520 --seed 703128
# python message_factory.py -t request_update -h 40.127.108.223 -p 5001 -i 91258644-bd3a-11ea-b335-04ea56f99520 --seed 173669
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 9125864a-bd3a-11ea-b335-04ea56f99520 --seed 534728
# python message_factory.py -t request_update -h 52.151.70.54 -p 5005 -i 91258646-bd3a-11ea-b335-04ea56f99520 --seed 112825
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 9125864c-bd3a-11ea-b335-04ea56f99520 --seed 393050
# python message_factory.py -t request_update -h 20.185.45.222 -p 5004 -i 91258645-bd3a-11ea-b335-04ea56f99520 --seed 767384

# Request scaling 
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 91258649-bd3a-11ea-b335-04ea56f99520 --seed 695887
python message_factory.py -t request_scale -h 52.141.61.172 -p 5003 -i 91258643-bd3a-11ea-b335-04ea56f99520 --seed 370491
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 91258644-bd3a-11ea-b335-04ea56f99520 --seed 958697
python message_factory.py -t request_scale -h 52.229.37.237 -p 5002 -i 91258648-bd3a-11ea-b335-04ea56f99520 --seed 857280
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 9125864a-bd3a-11ea-b335-04ea56f99520 --seed 703128
python message_factory.py -t request_scale -h 40.127.108.223 -p 5001 -i 91258644-bd3a-11ea-b335-04ea56f99520 --seed 173669
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 9125864a-bd3a-11ea-b335-04ea56f99520 --seed 534728
python message_factory.py -t request_scale -h 52.151.70.54 -p 5005 -i 91258646-bd3a-11ea-b335-04ea56f99520 --seed 112825
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 9125864c-bd3a-11ea-b335-04ea56f99520 --seed 393050
python message_factory.py -t request_scale -h 20.185.45.222 -p 5004 -i 91258645-bd3a-11ea-b335-04ea56f99520 --seed 767384

