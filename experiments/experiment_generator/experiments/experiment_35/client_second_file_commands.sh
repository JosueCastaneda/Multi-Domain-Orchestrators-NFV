#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i cb8d50d6-da29-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 3
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 2750ea63-da2a-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 2750ea67-da2a-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 3
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i ebbdb34c-da2d-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i ebbdb350-da2d-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 3
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 024de155-da2e-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 024de159-da2e-11ea-b222-04ea56f99520
python3 message_factory.py -r external
# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external