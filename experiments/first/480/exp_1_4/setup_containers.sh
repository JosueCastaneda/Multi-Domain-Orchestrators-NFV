# Setup Orchestrators
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup VNF
vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'

vim-emu compute start -d dc1 -n vnf2_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.13/24)'
vim-emu compute start -d dc1 -n vnf1_crop --image vnf_experiment --net '(id=input,ip=10.0.0.12/24)'
vim-emu compute start -d dc2 -n vnf5_painting --image vnf_experiment --net '(id=input,ip=10.0.0.15/24)'
vim-emu compute start -d dc1 -n vnf3_resize --image vnf_experiment --net '(id=input,ip=10.0.0.101/24)'

vim-emu compute start -d dc4 -n vnf9_black_white --image vnf_experiment --net '(id=input,ip=10.0.0.20/24'
vim-emu compute start -d dc1 -n vnf7_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.18/24)'

vim-emu compute start -d dc1 -n vnf6_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.17/24)'
vim-emu compute start -d dc2 -n vnf10_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.21/24)'
vim-emu compute start -d dc1 -n vnf8_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.19/24)'


# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source

vim-emu compute stop -d dc1 -n vnf2_rotate
vim-emu compute stop -d dc1 -n vnf1_crop
vim-emu compute stop -d dc2 -n vnf5_painting
vim-emu compute stop -d dc1 -n vnf3_resize

vim-emu compute stop -d dc4 -n vnf9_black_white
vim-emu compute stop -d dc1 -n vnf7_annotate

vim-emu compute stop -d dc1 -n vnf6_mirror_x
vim-emu compute stop -d dc2 -n vnf10_invert_colors
vim-emu compute stop -d dc1 -n vnf8_fade_out

