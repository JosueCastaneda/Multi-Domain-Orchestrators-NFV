# Setup Orchestrators
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup VNF
vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'

vim-emu compute start -d dc4 -n vnf21_black_white --image vnf_experiment --net '(id=input,ip=10.0.0.42/24)'
vim-emu compute start -d dc2 -n vnf16_painting --image vnf_experiment --net '(id=input,ip=10.0.0.27/24)'
vim-emu compute start -d dc1 -n vnf12_crop --image vnf_experiment --net '(id=input,ip=10.0.0.23/24)'
vim-emu compute start -d dc3 -n vnf19_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.40/24)'

vim-emu compute start -d dc1 -n vnf13_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.24/24)'
#CROP
#PAINT
vim-emu compute start -d dc1 -n vnf14_resize --image vnf_experiment --net '(id=input,ip=10.0.0.25/24)'

vim-emu compute start -d dc3 -n vnf18_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.29/24)'
# ROTATE
vim-emu compute start -d dc4 -n vnf22_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.43/24)'
vim-emu compute start -d dc3 -n vnf20_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.41/24)'

# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source

vim-emu compute stop -d dc4 -n vnf21_black_white
vim-emu compute stop -d dc2 -n vnf16_painting
vim-emu compute stop -d dc1 -n vnf12_crop
vim-emu compute stop -d dc3 -n vnf19_annotate

vim-emu compute stop -d dc1 -n vnf13_rotate
vim-emu compute stop -d dc1 -n vnf14_resize

vim-emu compute stop -d dc3 -n vnf18_mirror_x
vim-emu compute stop -d dc4 -n vnf22_invert_colors
vim-emu compute stop -d dc3 -n vnf20_fade_out


