## Setup Orchestrators
#vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
#vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
#vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
#vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup Orchestrators
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc1 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc2 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup VNF
vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'
vim-emu compute start -d dc2 -n vnf4_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.14/24)'
vim-emu compute start -d dc2 -n vnf10_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.21/24)'
vim-emu compute start -d dc1 -n vnf6_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.17/24)'
vim-emu compute start -d dc2 -n vnf10_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.100/24)'
vim-emu compute start -d dc2 -n vnf6_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.16/24)'
vim-emu compute start -d dc1 -n vnf2_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.13/24)'
vim-emu compute start -d dc1 -n vnf7_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.18/24)'
vim-emu compute start -d dc1 -n vnf8_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.19/24)'

## Setup VNF
#vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'
#vim-emu compute start -d dc2 -n vnf4_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.14/24)'
#vim-emu compute start -d dc4 -n vnf10_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.21/24)'
#vim-emu compute start -d dc3 -n vnf6_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.17/24)'
#vim-emu compute start -d dc4 -n vnf10_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.21/24)'
#vim-emu compute start -d dc2 -n vnf6_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.16/24)'
#vim-emu compute start -d dc1 -n vnf2_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.13/24)'
#vim-emu compute start -d dc3 -n vnf7_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.18/24)'
#vim-emu compute start -d dc3 -n vnf8_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.19/24)'

