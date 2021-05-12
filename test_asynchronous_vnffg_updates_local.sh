#!/bin/bash

FIRST_SERVER=127.0.0.1
SECOND_SERVER=127.0.0.1
THIRD_SERVER=127.0.0.1
FOURTH_SERVER=127.0.0.1
FIFTH_SERVER=127.0.0.1

python3 message_factory.py --type do_asynchronous_updates --host $FIRST_SERVER --port 4437 &
sleep 3
python3 message_factory.py --type do_asynchronous_updates --host $SECOND_SERVER --port 4439 &
sleep 3
python3 message_factory.py --type do_asynchronous_updates --host $THIRD_SERVER --port 4441 &
sleep 3
python3 message_factory.py --type do_asynchronous_updates --host $FOURTH_SERVER --port 4443 &
sleep 3
python3 message_factory.py --type do_asynchronous_updates --host $FIFTH_SERVER --port 4445 &
sleep 3
