#!/bin/bash

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
    python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
    ;;

  single)
    message=$'Single case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b4-c031-11ea-b335-04ea56f99520 --seed 857280
    python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
    ;;

  "single alternative")
    message=$'Single alternative case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b7-c031-11ea-b335-04ea56f99520 --seed 857280
    python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
    ;;

  double)
    message=$'Double case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.229.37.237 -p 5002 -i 000f60b8-c031-11ea-b335-04ea56f99520 --seed 857280
    python3 message_factory.py -h 52.229.37.237 -p 5002 -r external
    ;;

  triple)
    message=$'Triple case\n'
    echo -n "$message"
    python3 message_factory.py -t request_scaling_of_service -h 52.151.70.54 -p 5005 -i 000f60b9-c031-11ea-b335-04ea56f99520 --seed 857280
    python3 message_factory.py -h 52.151.70.54 -p 5005 -r external
    ;;

  all)
    message=$'All not implemented\n'
    echo -n "$message"
    ;;

  *)
    message=$'Using default simple case\n'
    echo -n "$message"
    # Simple case (only internal dependencies)
    python3 message_factory.py -t request_scaling_of_service -h 52.141.61.172 -p 5003 -i 000f60b3-c031-11ea-b335-04ea56f99520 --seed 857280
    python3 message_factory.py -h 52.141.61.172 -p 5003 -r external
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
