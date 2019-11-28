#!/bin/sh
python message_factory.py -t migration -h 10.0.0.34 -p 5461 -n vnf_ROTATE -m new -v none --vnf_port none
python message_factory.py -t migration -h 10.0.0.34 -p 5461 -n vnf_PAINTING -m new -v none --vnf_port none
python message_factory.py -t migration -h 10.0.0.30 -p 5461 -n vnf_COMPOSITE -m new -v none --vnf_port none
