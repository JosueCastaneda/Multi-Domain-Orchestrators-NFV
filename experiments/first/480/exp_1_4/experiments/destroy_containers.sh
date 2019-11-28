#!/bin/sh
vim-emu compute stop -d dc1 -n orch_1 
vim-emu compute stop -d dc2 -n orch_2 
vim-emu compute stop -d dc1 -n orch_1 
vim-emu compute stop -d dc2 -n orch_2 

vim-emu compute stop -d dc2 -n vnf_ROTATE 
vim-emu compute stop -d dc2 -n vnf_CROP 
vim-emu compute stop -d dc1 -n vnf_PAINTING 
vim-emu compute stop -d dc2 -n vnf_RESIZE 
vim-emu compute stop -d dc1 -n vnf_BLACK_WHITE 
vim-emu compute stop -d dc1 -n vnf_ANNOTATE 
vim-emu compute stop -d dc1 -n vnf_MIRROR_X 
vim-emu compute stop -d dc1 -n vnf_INVERT_COLORS 
vim-emu compute stop -d dc2 -n vnf_FADE_OUT 
vim-emu compute stop -d dc2 -n vnf_SPEED_UP 
vim-emu compute stop -d dc1 -n vnf_FADE_IN 
vim-emu compute stop -d dc2 -n vnf_COMPOSITE 
vim-emu compute stop -d dc1 -n vnf_MIRROR_Y 
