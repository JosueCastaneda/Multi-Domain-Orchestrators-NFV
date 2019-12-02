#!/bin/sh
vim-emu compute start -d dc2 -n vnf_ROTATE_new --image vnf_experiment --net '(id=input,ip=10.0.0.229/24)'
vim-emu compute start -d dc2 -n vnf_CROP_new --image vnf_experiment --net '(id=input,ip=10.0.0.182/24)'
vim-emu compute start -d dc1 -n vnf_PAINTING_new --image vnf_experiment --net '(id=input,ip=10.0.0.244/24)'
vim-emu compute start -d dc2 -n vnf_RESIZE_new --image vnf_experiment --net '(id=input,ip=10.0.0.195/24)'
vim-emu compute start -d dc1 -n vnf_BLACK_WHITE_new --image vnf_experiment --net '(id=input,ip=10.0.0.251/24)'
vim-emu compute start -d dc1 -n vnf_ANNOTATE_new --image vnf_experiment --net '(id=input,ip=10.0.0.238/24)'
vim-emu compute start -d dc1 -n vnf_MIRROR_X_new --image vnf_experiment --net '(id=input,ip=10.0.0.233/24)'
vim-emu compute start -d dc1 -n vnf_INVERT_COLORS_new --image vnf_experiment --net '(id=input,ip=10.0.0.217/24)'
vim-emu compute start -d dc2 -n vnf_FADE_OUT_new --image vnf_experiment --net '(id=input,ip=10.0.0.153/24)'
vim-emu compute start -d dc2 -n vnf_SPEED_UP_new --image vnf_experiment --net '(id=input,ip=10.0.0.209/24)'
vim-emu compute start -d dc1 -n vnf_FADE_IN_new --image vnf_experiment --net '(id=input,ip=10.0.0.249/24)'
vim-emu compute start -d dc2 -n vnf_COMPOSITE_new --image vnf_experiment --net '(id=input,ip=10.0.0.181/24)'
vim-emu compute start -d dc1 -n vnf_MIRROR_Y_new --image vnf_experiment --net '(id=input,ip=10.0.0.156/24)'

docker exec -it mn.vnf_ROTATE_new python vnf_script.py -h 10.0.0.229 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_ROTATE_new --topology 9,18,2,7 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 387 &
docker exec -it mn.vnf_CROP_new python vnf_script.py -h 10.0.0.182 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_CROP_new --topology 15,40,7,4 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 246 &
docker exec -it mn.vnf_PAINTING_new python vnf_script.py -h 10.0.0.244 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_PAINTING_new --topology 16,17,3,5 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 432 &
docker exec -it mn.vnf_RESIZE_new python vnf_script.py -h 10.0.0.195 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_RESIZE_new --topology 5,66,10,6 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 285 &
docker exec -it mn.vnf_BLACK_WHITE_new python vnf_script.py -h 10.0.0.251 -v 4437 -o 10.0.0.36 -q 5461 -n vnf_BLACK_WHITE_new --topology 4,48,5,3 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 453 &
docker exec -it mn.vnf_ANNOTATE_new python vnf_script.py -h 10.0.0.238 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_ANNOTATE_new --topology 8,7,9,9 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 414 &
docker exec -it mn.vnf_MIRROR_X_new python vnf_script.py -h 10.0.0.233 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_MIRROR_X_new --topology 15,6,1,1 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 399 &
docker exec -it mn.vnf_INVERT_COLORS_new python vnf_script.py -h 10.0.0.217 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_INVERT_COLORS_new --topology 4,50,0,7 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 351 &
docker exec -it mn.vnf_FADE_OUT_new python vnf_script.py -h 10.0.0.153 -v 4437 -o 10.0.0.32 -q 5461 -n vnf_FADE_OUT_new --topology 17,13,9,3 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 159 &
docker exec -it mn.vnf_SPEED_UP_new python vnf_script.py -h 10.0.0.209 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_SPEED_UP_new --topology 4,11,5,10 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 327 &
docker exec -it mn.vnf_FADE_IN_new python vnf_script.py -h 10.0.0.249 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_FADE_IN_new --topology 1,19,6,10 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 447 &
docker exec -it mn.vnf_COMPOSITE_new python vnf_script.py -h 10.0.0.181 -v 4437 -o 10.0.0.30 -q 5461 -n vnf_COMPOSITE_new --topology 4,58,9,2 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 243 &
docker exec -it mn.vnf_MIRROR_Y_new python vnf_script.py -h 10.0.0.156 -v 4437 -o 10.0.0.34 -q 5461 -n vnf_MIRROR_Y_new --topology 4,16,0,0 --migration_ip 127.0.0.1 --migration_topology 0,0,0,0 --services 160,472,64,32,104,264,0,24,80,480,64,64 --initial 168 &

docker exec -it mn.source python message_factory.py -t migration -h 10.0.0.34 -p 5461 -n vnf_ROTATE -m new -v none --vnf_port none
