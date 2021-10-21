#!/bin/bash

FIRST_SERVER=127.0.0.1
SECOND_SERVER=127.0.0.1
THIRD_SERVER=127.0.0.1
FOURTH_SERVER=127.0.0.1
FIFTH_SERVER=127.0.0.1

python3 message_factory.py --type do_sequential_updates --host $FIRST_SERVER --port 4437 &
python3 message_factory.py --type do_sequential_updates --host $SECOND_SERVER --port 4439 &
python3 message_factory.py --type do_sequential_updates --host $THIRD_SERVER --port 4441 &
python3 message_factory.py --type do_sequential_updates --host $FOURTH_SERVER --port 4443 &
python3 message_factory.py --type do_sequential_updates --host $FIFTH_SERVER --port 4445 &