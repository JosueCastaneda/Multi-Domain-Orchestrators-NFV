# Destroy all
vim-emu compute stop -d dc1 -n orch_1
vim-emu compute stop -d dc2 -n orch_2
vim-emu compute stop -d dc1 -n orch_3
vim-emu compute stop -d dc2 -n orch_4

vim-emu compute stop -d dc1 -n source

#vim-emu compute stop -d dc2 -n vnf42_painting
#vim-emu compute stop -d dc1 -n vnf39_rotate
#vim-emu compute stop -d dc3 -n vnf44_mirror_x
#vim-emu compute stop -d dc2 -n vnf41_fade_in
#vim-emu compute stop -d dc3 -n vnf46_fade_out
#vim-emu compute stop -d dc4 -n vnf49_composite_stadium
#
#vim-emu compute stop -d dc1 -n vnf39_rotate
#vim-emu compute stop -d dc2 -n vnf43_mirror_y
#vim-emu compute stop -d dc3 -n vnf45_annotate
#vim-emu compute stop -d dc1 -n vnf38_crop
#vim-emu compute stop -d dc4 -n vnf48_invert_colors
#vim-emu compute stop -d dc4 -n vnf47_black_white
#vim-emu compute stop -d dc4 -n vnf50_speed

vim-emu compute stop -d dc2 -n vnf42_painting
vim-emu compute stop -d dc1 -n vnf39_rotate
vim-emu compute stop -d dc1 -n vnf44_mirror_x
vim-emu compute stop -d dc2 -n vnf41_fade_in
vim-emu compute stop -d dc1 -n vnf46_fade_out
vim-emu compute stop -d dc2 -n vnf49_composite_stadium

vim-emu compute stop -d dc1 -n vnf39_rotate
vim-emu compute stop -d dc2 -n vnf43_mirror_y
vim-emu compute stop -d dc1 -n vnf45_annotate
vim-emu compute stop -d dc1 -n vnf38_crop
vim-emu compute stop -d dc2 -n vnf48_invert_colors

vim-emu compute stop -d dc2 -n vnf47_black_white
vim-emu compute stop -d dc2 -n vnf50_speed
