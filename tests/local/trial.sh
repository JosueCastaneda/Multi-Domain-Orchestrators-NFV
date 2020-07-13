#!/bin/bash

./launch_orchestrators.sh
sleep 2
./launch_vnfs.sh
./message_factory_orchi.sh
./add_vnfs.sh

#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69aa-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69af-8a3d-11ea-aa9d-04ea56f99520 --seed 857280

#SIMPLE CASE 
#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i e5ea69a9-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
#NEW
#python3 message_factory.py -t request_scaling_of_service -h 127.0.0.1 -p 5003 -i e5ea69a9-8a3d-11ea-aa9d-04ea56f99520 --seed 857280


#SINGLE SERVICE
#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69aa-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
#python3 message_factory.py -t request_scaling_of_service -h 127.0.0.1 -p 5002 -i e5ea69aa-8a3d-11ea-aa9d-04ea56f99520 --seed 857280

#TWO SERVICE
#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69ae-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
#python3 message_factory.py -t request_scaling_of_service -h 127.0.0.1 -p 5002 -i e5ea69ae-8a3d-11ea-aa9d-04ea56f99520 --seed 857280


#Triple Service
#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i e5ea69af-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
#python3 message_factory.py -t request_scaling_of_service -h 127.0.0.1 -p 5005 -i e5ea69af-8a3d-11ea-aa9d-04ea56f99520 --seed 857280
