#!/bin/bash

##Add chains to services
#python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3003 -n none -m none -v 127.0.0.1 --vnf_port 3002
#python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3002 -n none -m none -v 127.0.0.1 --vnf_port 3005
#python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3005 -n none -m none -v 127.0.0.1 --vnf_port 3004
#python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3004 -n none -m none -v 127.0.0.1 --vnf_port 3008
#
#python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3007 -n none -m none -v 127.0.0.1 --vnf_port 3006
#python3 message_factory.py -t add_chain -h 127.0.0.1 -p 3006 -n none -m none -v 127.0.0.1 --vnf_port 3008
#
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

# Request scaling

echo -n "Enter test: "
read TEST

message=$'Doing the experiment for $TEST\n'
echo -n "$message"

case $TEST in

  simple)
    message=$'Simple case\n'
    echo -n "$message"
    # Simple case (only internal dependencies)
    python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 000f60b3-c031-11ea-b335-04ea56f99520 --seed 857280
    ;;

  single)
    message=$'Single case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b4-c031-11ea-b335-04ea56f99520 --seed 857280
    ;;

  "single alternative")
    message=$'Single alternative case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 857280
    ;;

  double)
    message=$'Double case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b8-c031-11ea-b335-04ea56f99520 --seed 857280
    ;;

  triple)
    message=$'Triple case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 000f60b9-c031-11ea-b335-04ea56f9952 --seed 857280
    ;;

  *)
    message=$'Using default simple case\n'
    echo -n "$message"
    # Simple case (only internal dependencies)
    python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 000f60b3-c031-11ea-b335-04ea56f99520 --seed 857280
    ;;
esac

# Simple case (only internal dependencies)
#python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 000f60b3-c031-11ea-b335-04ea56f99520 --seed 857280

# Single dependency
#python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b4-c031-11ea-b335-04ea56f99520 --seed 857280
# Alternative
#python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 857280

# Two dependencies
#python message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b8-c031-11ea-b335-04ea56f99520 --seed 857280

# Triple dependencies
#python message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 000f60b9-c031-11ea-b335-04ea56f9952 --seed 857280
