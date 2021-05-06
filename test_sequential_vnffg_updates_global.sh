#!/bin/bash

#FIRST_SERVER=42.123.124.4
#SECOND_SERVER=8.3.55.13
#THIRD_SERVER=12.32.32.145
#FOURTH_SERVER=42.2.43.5
#FIFTH_SERVER=53.345.5.6

FIRST_SERVER=13.91.23.61
SECOND_SERVER=40.81.204.178
THIRD_SERVER=20.84.67.101
FOURTH_SERVER=20.68.168.123
FIFTH_SERVER=52.231.152.194

python3 message_factory.py --type do_sequential_updates --host $FIRST_SERVER --port 5001 &
python3 message_factory.py --type do_sequential_updates --host $SECOND_SERVER --port 5002 &
python3 message_factory.py --type do_sequential_updates --host $THIRD_SERVER --port 5003 &
python3 message_factory.py --type do_sequential_updates --host $FOURTH_SERVER --port 5004 &
python3 message_factory.py --type do_sequential_updates --host $FIFTH_SERVER --port 5005 &
