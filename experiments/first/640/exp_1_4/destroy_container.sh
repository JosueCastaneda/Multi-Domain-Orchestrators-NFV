# Destroy all
#vim-emu compute stop -d dc1 -n orch_1
#vim-emu compute stop -d dc2 -n orch_2
#vim-emu compute stop -d dc1 -n orch_3
#vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

#
#vim-emu compute stop -d dc1 -n source
#
#vim-emu compute stop -d dc4 -n vnf21_black_white
#vim-emu compute stop -d dc2 -n vnf16_painting
#vim-emu compute stop -d dc1 -n vnf12_crop
#vim-emu compute stop -d dc3 -n vnf19_annotate
#
#vim-emu compute stop -d dc1 -n vnf13_rotate
#vim-emu compute stop -d dc1 -n vnf14_resize
#
#vim-emu compute stop -d dc3 -n vnf18_mirror_x
#vim-emu compute stop -d dc4 -n vnf22_invert_colors
#vim-emu compute stop -d dc3 -n vnf20_fade_out

vim-emu compute stop -d dc2 -n vnf21_black_white
vim-emu compute stop -d dc2 -n vnf16_painting
vim-emu compute stop -d dc1 -n vnf12_crop
vim-emu compute stop -d dc1 -n vnf19_annotate

vim-emu compute stop -d dc1 -n vnf13_rotate
vim-emu compute stop -d dc1 -n vnf14_resize

vim-emu compute stop -d dc1 -n vnf18_mirror_x
vim-emu compute stop -d dc2 -n vnf22_invert_colors
vim-emu compute stop -d dc1 -n vnf20_fade_out