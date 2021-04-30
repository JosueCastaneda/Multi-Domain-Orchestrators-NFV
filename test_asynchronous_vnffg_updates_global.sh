#!/bin/bash

FIRST_SERVER=42.123.124.4
SECOND_SERVER=8.3.55.13
THIRD_SERVER=12.32.32.145
FOURTH_SERVER=42.2.43.5
FIFTH_SERVER=53.345.5.6

python3 message_factory.py --type do_asynchronous_updates --host $FIRST_SERVER --port 4437 &
python3 message_factory.py --type do_asynchronous_updates --host $SECOND_SERVER --port 4439 &
python3 message_factory.py --type do_asynchronous_updates --host $THIRD_SERVER --port 4441 &
python3 message_factory.py --type do_asynchronous_updates --host $FOURTH_SERVER --port 4443 &
python3 message_factory.py --type do_asynchronous_updates --host $FIFTH_SERVER --port 4445 &
