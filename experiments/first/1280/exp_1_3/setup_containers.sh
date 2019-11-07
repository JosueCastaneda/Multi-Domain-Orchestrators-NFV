# Setup Orchestrators
#vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
#vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
#vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
#vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc1 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc2 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'


## Setup VNF
#vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'
#
#vim-emu compute start -d dc1 -n vnf26_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.46/24)'
#vim-emu compute start -d dc2 -n vnf30_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.50/24)'
#vim-emu compute start -d dc4 -n vnf36_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.104/24)'
#
#vim-emu compute start -d dc2 -n vnf28_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.48/24)'
#vim-emu compute start -d dc4 -n vnf35_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.55/24)'
#vim-emu compute start -d dc3 -n vnf31_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.51/24)'
#
#vim-emu compute start -d dc3 -n vnf33_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.53/24)'
#vim-emu compute start -d dc3 -n vnf32_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.52/24)'

vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'

vim-emu compute start -d dc1 -n vnf26_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.46/24)'
vim-emu compute start -d dc2 -n vnf30_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.50/24)'
vim-emu compute start -d dc2 -n vnf36_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.104/24)'

vim-emu compute start -d dc2 -n vnf28_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.48/24)'
vim-emu compute start -d dc2 -n vnf35_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.55/24)'
vim-emu compute start -d dc1 -n vnf31_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.51/24)'

vim-emu compute start -d dc1 -n vnf33_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.53/24)'
vim-emu compute start -d dc1 -n vnf32_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.52/24)'