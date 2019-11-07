# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source
#
#vim-emu compute start -d dc2 -n vnf15_fade_in
#vim-emu compute start -d dc3 -n vnf18_mirror_x
#vim-emu compute start -d dc4 -n vnf21_black_white
#vim-emu compute start -d dc2 -n vnf16_painting
#vim-emu compute start -d dc4 -n vnf24_speed
#vim-emu compute start -d dc4 -n vnf23_composite_stadium
#
#vim-emu compute start -d dc1 -n vnf13_rotate
#vim-emu compute start -d dc2 -n vnf17_mirror_y
#vim-emu compute start -d dc3 -n vnf19_annotate
#vim-emu compute start -d dc1 -n vnf12_crop
#vim-emu compute start -d dc4 -n vnf22_invert_colors
#vim-emu compute start -d dc3 -n vnf20_fade_out

vim-emu compute stop -d dc2 -n vnf15_fade_in
vim-emu compute stop -d dc1 -n vnf18_mirror_x
vim-emu compute stop -d dc2 -n vnf21_black_white
vim-emu compute stop -d dc2 -n vnf16_painting
vim-emu compute stop -d dc2 -n vnf24_speed
vim-emu compute stop -d dc2 -n vnf23_composite_stadium

vim-emu compute stop -d dc1 -n vnf13_rotate
vim-emu compute stop -d dc2 -n vnf17_mirror_y
vim-emu compute stop -d dc1 -n vnf19_annotate
vim-emu compute stop -d dc1 -n vnf12_crop
vim-emu compute stop -d dc2 -n vnf22_invert_colors
vim-emu compute stop -d dc1 -n vnf20_fade_out