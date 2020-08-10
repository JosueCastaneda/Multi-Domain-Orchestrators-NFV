#!/bin/sh

# Dependencies 0
python3 message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 12bf5f67-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 2
python3 message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 12bf5f7f-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 2
python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 12bf5f75-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 2
python3 message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 12bf5f71-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 3
python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 12bf5f69-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 3
python3 message_factory.py -t request_scaling_of_service -h 20.185.45.222 -p 5004 -i 12bf5f7e-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
#!/bin/sh

# Dependencies 4
python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 12bf5f6c-dafe-11ea-b222-04ea56f99520
python3 message_factory.py -r external
# Add results 
python3 message_factory.py -h 40.127.108.223 -p 5001 -r external
python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
python3 message_factory.py -h 20.185.45.222 -p 5004 -r external
python3 message_factory.py -h 52.151.70.54 -p 5005 -r external
