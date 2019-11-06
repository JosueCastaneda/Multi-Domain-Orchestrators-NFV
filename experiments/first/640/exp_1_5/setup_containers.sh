# Setup Orchestrators
#vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
#vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
#vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
#vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc1 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc2 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup VNF
#vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'
#
#vim-emu compute start -d dc3 -n vnf20_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.41/24)'
#vim-emu compute start -d dc4 -n vnf24_speed --image vnf_experiment --net '(id=input,ip=10.0.0.103/24)'
#vim-emu compute start -d dc4 -n vnf21_black_white --image vnf_experiment --net '(id=input,ip=10.0.0.42/24)'
#vim-emu compute start -d dc3 -n vnf19_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.40/24)'
#vim-emu compute start -d dc3 -n vnf18_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.29/24)'
#
#vim-emu compute start -d dc2 -n vnf16_painting --image vnf_experiment --net '(id=input,ip=10.0.0.27/24)'
#vim-emu compute start -d dc2 -n vnf15_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.26/24)'
#vim-emu compute start -d dc1 -n vnf13_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.24/24)'
#vim-emu compute start -d dc4 -n vnf23_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.102/24)'
#
#vim-emu compute start -d dc2 -n vnf17_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.28/24)'
#vim-emu compute start -d dc4 -n vnf22_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.43/24)'

vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'

vim-emu compute start -d dc1 -n vnf20_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.41/24)'
vim-emu compute start -d dc2 -n vnf24_speed --image vnf_experiment --net '(id=input,ip=10.0.0.103/24)'
vim-emu compute start -d dc2 -n vnf21_black_white --image vnf_experiment --net '(id=input,ip=10.0.0.42/24)'
vim-emu compute start -d dc1 -n vnf19_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.40/24)'
vim-emu compute start -d dc1 -n vnf18_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.29/24)'

vim-emu compute start -d dc2 -n vnf16_painting --image vnf_experiment --net '(id=input,ip=10.0.0.27/24)'
vim-emu compute start -d dc2 -n vnf15_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.26/24)'
vim-emu compute start -d dc1 -n vnf13_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.24/24)'
vim-emu compute start -d dc2 -n vnf23_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.102/24)'

vim-emu compute start -d dc2 -n vnf17_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.28/24)'
vim-emu compute start -d dc2 -n vnf22_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.43/24)'
