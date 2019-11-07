# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source

#vim-emu compute stop -d dc3 -n vnf33_fade_out
#vim-emu compute stop -d dc4 -n vnf37_speed
#vim-emu compute stop -d dc4 -n vnf34_black_white
#vim-emu compute stop -d dc3 -n vnf32_annotate
#vim-emu compute stop -d dc3 -n vnf31_mirror_x
#
#vim-emu compute stop -d dc2 -n vnf29_painting
#vim-emu compute stop -d dc2 -n vnf28_fade_in
#vim-emu compute stop -d dc1 -n vnf26_rotate
#vim-emu compute stop -d dc4 -n vnf36_composite_stadium
#vim-emu compute stop -d dc3 -n vnf33_fade_out
#
#vim-emu compute stop -d dc2 -n vnf30_mirror_y
#vim-emu compute stop -d dc4 -n vnf35_invert_colors

vim-emu compute stop -d dc1 -n vnf33_fade_out
vim-emu compute stop -d dc2 -n vnf37_speed
vim-emu compute stop -d dc2 -n vnf34_black_white
vim-emu compute stop -d dc1 -n vnf32_annotate
vim-emu compute stop -d dc1 -n vnf31_mirror_x

vim-emu compute stop -d dc2 -n vnf29_painting
vim-emu compute stop -d dc2 -n vnf28_fade_in
vim-emu compute stop -d dc1 -n vnf26_rotate
vim-emu compute stop -d dc2 -n vnf36_composite_stadium
vim-emu compute stop -d dc1 -n vnf33_fade_out

vim-emu compute stop -d dc2 -n vnf30_mirror_y
vim-emu compute stop -d dc2 -n vnf35_invert_colors