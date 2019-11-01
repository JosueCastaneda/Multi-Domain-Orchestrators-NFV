# Setup Orchestrators
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup VNF
vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'

vim-emu compute start -d dc2 -n vnf41_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.59/24)'
vim-emu compute start -d dc4 -n vnf48_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.66/24)'
vim-emu compute start -d dc3 -n vnf44_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.62/24)'

vim-emu compute start -d dc1 -n vnf39_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.57/24)'
vim-emu compute start -d dc2 -n vnf43_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.61/24)'
vim-emu compute start -d dc4 -n vnf49_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.67/24)'

vim-emu compute start -d dc3 -n vnf46_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.64/24)'
vim-emu compute start -d dc3 -n vnf45_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.63/24)'

# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source

vim-emu compute stop -d dc2 -n vnf41_fade_in
vim-emu compute stop -d dc4 -n vnf48_invert_colors
vim-emu compute stop -d dc3 -n vnf44_mirror_x

vim-emu compute stop -d dc1 -n vnf39_rotate
vim-emu compute stop -d dc2 -n vnf43_mirror_y
vim-emu compute stop -d dc4 -n vnf49_composite_stadium

vim-emu compute stop -d dc3 -n vnf46_fade_out
vim-emu compute stop -d dc3 -n vnf45_annotate
