sleep 1
python3 vnf_script.py -i 1 -o 0 -e 0 &
sleep 1
python3 vnf_script.py -i 0 -o 1 -e 0 &
sleep 1
python3 vnf_script.py -i 1 -o 1 -e 0 &
sleep 1
python3 vnf_script.py -i 2 -o 1 -e 0 &
sleep 1
python3 vnf_script.py -i 3 -o 1 -e 0 &

sleep 1
python3 vnf_script.py -i 1 -o 2 -e 0 &
sleep 1
python3 vnf_script.py -i 2 -o 2 -e 0 &
sleep 1
python3 vnf_script.py -i 4 -o 2 -e 0 &
sleep 1

python3 vnf_script.py -i 0 -o 4 -e 0 &
sleep 1
python3 vnf_script.py -i 2 -o 4 -e 0 &