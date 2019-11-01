# Setup Orchestrators
vim-emu compute start -d dc1 -n orch_1 --image vnf_experiment --net '(id=output,ip=10.0.0.30/24)'
vim-emu compute start -d dc2 -n orch_2 --image vnf_experiment --net '(id=output,ip=10.0.0.32/24)'
vim-emu compute start -d dc3 -n orch_3 --image vnf_experiment --net '(id=output,ip=10.0.0.34/24)'
vim-emu compute start -d dc4 -n orch_4 --image vnf_experiment --net '(id=output,ip=10.0.0.36/24)'

# Setup VNF
vim-emu compute start -d dc1 -n source --image vnf_experiment --net '(id=input,ip=10.0.0.3/24)'

vim-emu compute start -d dc2 -n vnf4_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.14/24)'
vim-emu compute start -d dc4 -n vnf10_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.21/24)'
vim-emu compute start -d dc3 -n vnf6_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.17/24)'
vim-emu compute start -d dc1 -n vnf2_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.13/24)'
vim-emu compute start -d dc2 -n vnf6_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.16/24)'
vim-emu compute start -d dc4 -n vnf10_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.100/24)'
vim-emu compute start -d dc3 -n vnf8_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.19/24)'
vim-emu compute start -d dc3 -n vnf7_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.18/24)'
vim-emu compute start -d dc1 -n vnf1_crop --image vnf_experiment --net '(id=input,ip=10.0.0.12/24)'
vim-emu compute start -d dc2 -n vnf5_painting --image vnf_experiment --net '(id=input,ip=10.0.0.15/24)'
vim-emu compute start -d dc1 -n vnf3_resize --image vnf_experiment --net '(id=input,ip=10.0.0.101/24)'
vim-emu compute start -d dc4 -n vnf9_black_white --image vnf_experiment --net '(id=input,ip=10.0.0.20/24)'
vim-emu compute start -d dc4 -n vnf11_speed --image vnf_experiment --net '(id=input,ip=10.0.0.68/24)'

# 640 All
vim-emu compute start -d dc4 -n vnf24_speed --image vnf_experiment --net '(id=input,ip=10.0.0.103/24)'
vim-emu compute start -d dc4 -n vnf23_composite_stadium --image vnf_experiment --net '(id=input,ip=10.0.0.102/24)'
vim-emu compute start -d dc4 -n vnf22_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.43/24)'
vim-emu compute start -d dc4 -n vnf21_black_white --image vnf_experiment --net '(id=input,ip=10.0.0.42/24)'
vim-emu compute start -d dc3 -n vnf20_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.41/24)'
vim-emu compute start -d dc3 -n vnf19_annotate --image vnf_experiment --net '(id=input,ip=10.0.0.40/24)'
vim-emu compute start -d dc3 -n vnf18_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.29/24)'
vim-emu compute start -d dc2 -n vnf17_mirror_y --image vnf_experiment --net '(id=input,ip=10.0.0.28/24)'
vim-emu compute start -d dc2 -n vnf16_painting --image vnf_experiment --net '(id=input,ip=10.0.0.27/24)'
vim-emu compute start -d dc2 -n vnf15_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.26/24)'
vim-emu compute start -d dc1 -n vnf14_resize --image vnf_experiment --net '(id=input,ip=10.0.0.25/24)'
vim-emu compute start -d dc1 -n vnf13_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.24/24)'
vim-emu compute start -d dc1 -n vnf12_crop --image vnf_experiment --net '(id=input,ip=10.0.0.23/24)'

#1280
vim-emu compute start -d dc2 -n vnf28_fade_in --image vnf_experiment --net '(id=input,ip=10.0.0.48/24)'
vim-emu compute start -d dc4 -n vnf35_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.55/24)'
vim-emu compute start -d dc3 -n vnf31_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.51/24)'

vim-emu compute start -d dc1 -n vnf26_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.46/24)'
vim-emu compute start -d dc3 -n vnf33_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.53/24)'

#1920
vim-emu compute start -d dc3 -n vnf44_mirror_x --image vnf_experiment --net '(id=input,ip=10.0.0.62/24)'
vim-emu compute start -d dc1 -n vnf39_rotate --image vnf_experiment --net '(id=input,ip=10.0.0.57/24)'
vim-emu compute start -d dc4 -n vnf48_invert_colors --image vnf_experiment --net '(id=input,ip=10.0.0.66/24)'
vim-emu compute start -d dc3 -n vnf46_fade_out --image vnf_experiment --net '(id=input,ip=10.0.0.64/24)'

# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source


vim-emu compute stop -d dc2 -n vnf4_fade_in
vim-emu compute stop -d dc4 -n vnf10_invert_colors
vim-emu compute stop -d dc3 -n vnf6_mirror_x
vim-emu compute stop -d dc1 -n vnf2_rotate
vim-emu compute stop -d dc2 -n vnf6_mirror_y
vim-emu compute stop -d dc4 -n vnf10_composite_stadium
vim-emu compute stop -d dc3 -n vnf8_fade_out
vim-emu compute stop -d dc3 -n vnf7_annotate
vim-emu compute stop -d dc1 -n vnf1_crop
vim-emu compute stop -d dc2 -n vnf5_painting
vim-emu compute stop -d dc1 -n vnf3_resize
vim-emu compute stop -d dc4 -n vnf9_black_white
vim-emu compute stop -d dc4 -n vnf11_speed


vim-emu compute stop -d dc4 -n vnf24_speed
vim-emu compute stop -d dc4 -n vnf23_composite_stadium
vim-emu compute stop -d dc4 -n vnf22_invert_colors
vim-emu compute stop -d dc4 -n vnf21_black_white
vim-emu compute stop -d dc3 -n vnf20_fade_out
vim-emu compute stop -d dc3 -n vnf19_annotate
vim-emu compute stop -d dc3 -n vnf18_mirror_x
vim-emu compute stop -d dc2 -n vnf17_mirror_y
vim-emu compute stop -d dc2 -n vnf16_painting
vim-emu compute stop -d dc2 -n vnf15_fade_in
vim-emu compute stop -d dc1 -n vnf14_resize
vim-emu compute stop -d dc1 -n vnf13_rotate
vim-emu compute stop -d dc1 -n vnf12_crop

vim-emu compute stop -d dc2 -n vnf28_fade_in
vim-emu compute stop -d dc4 -n vnf35_invert_colors
vim-emu compute stop -d dc3 -n vnf31_mirror_x

vim-emu compute stop -d dc1 -n vnf26_rotate
vim-emu compute stop -d dc3 -n vnf33_fade_out

vim-emu compute stop -d dc3 -n vnf44_mirror_x
vim-emu compute stop -d dc1 -n vnf39_rotate
vim-emu compute stop -d dc4 -n vnf48_invert_colors
vim-emu compute stop -d dc3 -n vnf46_fade_out
