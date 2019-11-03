# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source
vim-emu compute stop -d dc2 -n vnf4_fade_in
vim-emu compute stop -d dc2 -n vnf10_invert_colors
vim-emu compute stop -d dc1 -n vnf6_mirror_x
vim-emu compute stop -d dc2 -n vnf10_composite_stadium
vim-emu compute stop -d dc2 -n vnf6_mirror_y
vim-emu compute stop -d dc1 -n vnf2_rotate
vim-emu compute stop -d dc1 -n vnf7_annotate
vim-emu compute stop -d dc1 -n vnf8_fade_out