#!/bin/sh
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'
