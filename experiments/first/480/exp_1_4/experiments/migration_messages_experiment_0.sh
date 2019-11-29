#!/bin/sh
vim-emu compute start -d dc2 -n vnf_ROTATE_new --image vnf_experiment--net '(id=input,ip=10.0.0.229/24)'
vim-emu compute start -d dc1 -n vnf_PAINTING_new --image vnf_experiment--net '(id=input,ip=10.0.0.244/24)'
vim-emu compute start -d dc2 -n vnf_COMPOSITE_new --image vnf_experiment--net '(id=input,ip=10.0.0.181/24)'

docker exec -it mn.vnf_ROTATE_new python vnf_script.py -h 10.0.0.229 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_ROTATE_new --topology 9,18,2,7 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 0,236,12,40,60,124,24,32,24,208,16,8 --initial 387 &
docker exec -it mn.vnf_PAINTING_new python vnf_script.py -h 10.0.0.244 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_PAINTING_new --topology 16,17,3,5 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 0,236,12,40,60,124,24,32,24,208,16,8 --initial 432 &
docker exec -it mn.vnf_COMPOSITE_new python vnf_script.py -h 10.0.0.181 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_COMPOSITE_new --topology 4,58,9,2 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 0,236,12,40,60,124,24,32,24,208,16,8 --initial 243 &

python message_factory.py -t migration -h 10.0.0.34 -p 5461 -n vnf_ROTATE -m new -v none --vnf_port none
python message_factory.py -t migration -h 10.0.0.34 -p 5461 -n vnf_PAINTING -m new -v none --vnf_port none
python message_factory.py -t migration -h 10.0.0.30 -p 5461 -n vnf_COMPOSITE -m new -v none --vnf_port none
