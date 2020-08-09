#!/bin/sh

# Dependencies 4
python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 2750eba7-da2a-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 2750ebb1-da2a-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 4
python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i ece37923-da2d-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i ece3792d-da2d-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 4
python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 0399ab33-da2e-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 5
python3 message_factory.py -t request_scaling_of_service -h 40.127.108.223 -p 5001 -i 0399ab3d-da2e-11ea-b222-04ea56f99520
python3 message_factory.py -r external
# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external
