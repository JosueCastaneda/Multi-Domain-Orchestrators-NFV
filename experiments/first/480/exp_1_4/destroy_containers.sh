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
vim-emu compute stop -d dc2 -n vnf9_black_white
vim-emu compute stop -d dc1 -n vnf7_annotate
vim-emu compute stop -d dc1 -n vnf6_mirror_x
vim-emu compute stop -d dc2 -n vnf10_invert_colors
vim-emu compute stop -d dc1 -n vnf8_fade_out

#vim-emu compute stop -d dc1 -n source
#vim-emu compute stop -d dc1 -n vnf2_rotate
#vim-emu compute stop -d dc1 -n vnf1_crop
#vim-emu compute stop -d dc2 -n vnf5_painting
#vim-emu compute stop -d dc1 -n vnf3_resize
#vim-emu compute stop -d dc4 -n vnf9_black_white
#vim-emu compute stop -d dc1 -n vnf7_annotate
#vim-emu compute stop -d dc1 -n vnf6_mirror_x
#vim-emu compute stop -d dc2 -n vnf10_invert_colors
#vim-emu compute stop -d dc1 -n vnf8_fade_out