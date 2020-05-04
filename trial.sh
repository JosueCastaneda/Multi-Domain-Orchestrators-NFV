#!/bin/bash

./launch_orchestrators.sh
sleep .5
./launch_vnfs.sh
sleep .5
./message_factory_orchi.sh
sleep .5
./add_vnfs.sh
#python3 message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i e5ea69aa-8a3d-11ea-aa9d-04ea56f99520 --seed 857280