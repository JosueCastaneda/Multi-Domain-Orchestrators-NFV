#!/bin/bash

python3 message_factory.py --type do_asynchronous_updates --host 127.0.0.1 --port 4437 &
python3 message_factory.py --type do_asynchronous_updates --host 127.0.0.1 --port 4439 &
python3 message_factory.py --type do_asynchronous_updates --host 127.0.0.1 --port 4441 &
python3 message_factory.py --type do_asynchronous_updates --host 127.0.0.1 --port 4443 &
python3 message_factory.py --type do_asynchronous_updates --host 127.0.0.1 --port 4445 &
