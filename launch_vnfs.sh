python3 vnf_script.py -v 1 -o 0 -e 0 -h 127.0.0.1 -p 3001 &
python3 vnf_script.py -v 0 -o 1 -e 0 -h 127.0.0.1 -p 3002 &
python3 vnf_script.py -v 1 -o 1 -e 0 -h 127.0.0.1 -p 3003 &
python3 vnf_script.py -v 2 -o 1 -e 0 -h 127.0.0.1 -p 3004 &
python3 vnf_script.py -v 3 -o 1 -e 0 -h 127.0.0.1 -p 3005 &

python3 vnf_script.py -v 1 -o 2 -e 0 -h 127.0.0.1 -p 3006 &
python3 vnf_script.py -v 2 -o 2 -e 0 -h 127.0.0.1 -p 3007 &
python3 vnf_script.py -v 4 -o 2 -e 0 -h 127.0.0.1 -p 3008 &

python3 vnf_script.py -v 0 -o 4 -e 0 -h 127.0.0.1 -p 3009 &
python3 vnf_script.py -v 2 -o 4 -e 0 -h 127.0.0.1 -p 3010 &