#!/bin/bash

killall python
killall python3
pkill python

kill -9 $(ps aux | grep "[o]rchestrator" | awk '{print $2}')
kill -9 $(ps aux | grep "[v]nf_script.py" | awk '{print $2}')

sleep 1