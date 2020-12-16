#!/bin/sh

#Add chains to services 
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6196 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6146
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6146 -n none -m none -v 127.0.0.1 --vnf_port 6120
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6120 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6132
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6132 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6110 -n none -m none -v 127.0.0.1 --vnf_port 6116
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6116 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6186
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6186 -n none -m none -v 127.0.0.1 --vnf_port 6102
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6102 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6108
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6108 -n none -m none -v 127.0.0.1 --vnf_port 6102
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6102 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6116
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6126 -n none -m none -v 127.0.0.1 --vnf_port 6132
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6132 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6128 -n none -m none -v 127.0.0.1 --vnf_port 6122
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6122 -n none -m none -v 127.0.0.1 --vnf_port 6176
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6176 -n none -m none -v 127.0.0.1 --vnf_port 6134
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6134 -n none -m none -v 127.0.0.1 --vnf_port 6120
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6132 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6128 -n none -m none -v 127.0.0.1 --vnf_port 6176
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6122 -n none -m none -v 127.0.0.1 --vnf_port 6130
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6130 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6132
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6132 -n none -m none -v 127.0.0.1 --vnf_port 6120
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6120 -n none -m none -v 127.0.0.1 --vnf_port 6186
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6186 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6128 -n none -m none -v 127.0.0.1 --vnf_port 6130
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6176
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6176 -n none -m none -v 127.0.0.1 --vnf_port 6122
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6120 -n none -m none -v 127.0.0.1 --vnf_port 6142
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6190
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6190 -n none -m none -v 127.0.0.1 --vnf_port 6122
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6124
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6140
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6140 -n none -m none -v 127.0.0.1 --vnf_port 6150
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6150 -n none -m none -v 127.0.0.1 --vnf_port 6146
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6156
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6156 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6146
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6146 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6140
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6140 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6122
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6142
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6128 -n none -m none -v 127.0.0.1 --vnf_port 6190
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6190 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6122
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6122
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6120 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6128 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6196
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6176
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6164
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6164 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6168 -n none -m none -v 127.0.0.1 --vnf_port 6172
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6172 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6164
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6164 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6164 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6120
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6120 -n none -m none -v 127.0.0.1 --vnf_port 6166
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6166 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6186
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6146
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6196 -n none -m none -v 127.0.0.1 --vnf_port 6120
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6120 -n none -m none -v 127.0.0.1 --vnf_port 6190
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6190 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6186
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6198
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6198 -n none -m none -v 127.0.0.1 --vnf_port 6180
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6180 -n none -m none -v 127.0.0.1 --vnf_port 6188
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6188 -n none -m none -v 127.0.0.1 --vnf_port 6186
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6186 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6192 -n none -m none -v 127.0.0.1 --vnf_port 6182
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6182 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6190 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6142 -n none -m none -v 127.0.0.1 --vnf_port 6194
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6194 -n none -m none -v 127.0.0.1 --vnf_port 6162
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6162 -n none -m none -v 127.0.0.1 --vnf_port 6146
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6146 -n none -m none -v 127.0.0.1 --vnf_port 6192
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6192 -n none -m none -v 127.0.0.1 --vnf_port 6176
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6154
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6130
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6154 -n none -m none -v 127.0.0.1 --vnf_port 6128
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6128 -n none -m none -v 127.0.0.1 --vnf_port 6192
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6192 -n none -m none -v 127.0.0.1 --vnf_port 6190
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6190 -n none -m none -v 127.0.0.1 --vnf_port 6170
docker exec -it mn.source python message_factory.py -t add_chain -h 127.0.0.1 -p 6170 -n none -m none -v 127.0.0.1 --vnf_port 6196

# Request updates (Commented) 
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 44257
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 49313
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 59379
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 26463
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 43053
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 63821
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 78979
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 5273
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 62506
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 70515
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 89454
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 88916
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 3437
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 70929
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 1950
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 38160
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 70003
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 98317
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 43373
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 58613
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 64396
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 52250
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 21919
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 50636
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 94203
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 25365
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 32544
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 70340
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 28879
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 11399
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 83887
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 41578
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 48731
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 12940
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 64565
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 37224
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 78751
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 18344
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 82996
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 5491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 71398
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 55153
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 11642
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 91554
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 29641
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 20835
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 79020
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 69625
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 6285
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 30278
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 50545
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 23072
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 56865
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 85850
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 92114
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 12920
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 65435
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 90835
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 26311
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 85707
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 24422
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 57859
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 46145
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 61693
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 26843
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 27214
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 24919
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 75903
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 54874
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 60682
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 49635
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 3713
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 74334
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 13052
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 13258
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 88863
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 20609
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 83639
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 77265
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 73229
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 16380
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 24220
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 94968
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 31152
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 29937
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 40720
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 57324
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 23532
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 70991
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 33309
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 5257
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 72120
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 26964
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 42598
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 30581
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 55090
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 13433
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 97164
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 28085
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 39661
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 58441
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 70767
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 90715
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 5585
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 74514
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 85317
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 73217
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 40538
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 58654
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 23474
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 22266
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 64711
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 53279
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 73563
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 37205
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 91934
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 43113
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 71617
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 86192
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 67205
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 56017
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 99135
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 26771
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 49546
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 43891
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 7728
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 47329
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 2900
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 96058
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 91271
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 87144
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 46418
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 24367
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 53313
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 69782
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 64570
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 76435
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 72306
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 55524
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 39413
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 13989
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 36139
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 56387
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 50775
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 19334
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 63207
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 79955
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 46633
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 85624
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 16590
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 98853
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 4102
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 71211
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 97121
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 90989
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 21046
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 45167
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 11644
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 97116
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 26712
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 93274
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 52891
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 33380
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 94242
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 57156
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 21367
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 80077
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 2395
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 39064
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 95411
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 5472
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 34374
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 53118
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 71576
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 74943
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 83400
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 43795
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 16778
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 28491
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 7441
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 15605
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 14546
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 43189
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 9955
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 14161
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 17139
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 67149
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 49611
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 92213
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 44870
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 78049
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 81955
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 77579
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 13393
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 44995
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 44403
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 10013
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 71033
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 32559
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 11117
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 8150
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 88526
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 39215
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 43792
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 83495
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 75749
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 95449
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 26687
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 25520
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 63502
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 28016
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 97036
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 60773
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 82090
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 75316
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 62430
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 65195
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 88551
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 20180
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 17689
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 83629
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 27872
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 73923
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 75920
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 79539
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 54814
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 47755
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 31254
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 65070
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 73757
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 5119
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 52232
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 13194
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 96902
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 57436
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 39963
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 5165
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 63608
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 77060
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 80081
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 96818
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 73338
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 8243
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 79087
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 32245
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 57760
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 36801
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 84502
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 62832
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 72371
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 40825
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 19916
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 29287
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 51683
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 56236
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 92938
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 56300
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 5511
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 30334
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 39985
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 27254
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 29347
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 89214
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 48969
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 64237
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 61841
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 47876
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 73036
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 38888
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 70521
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 7973
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 6911
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 35839
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 70962
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 51268
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 70296
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 7563
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 87917
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 5329
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 97502
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 57350
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 68196
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 71185
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 68611
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 75125
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 73875
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 39248
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 20222
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 22968
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 93866
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 3181
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 17287
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 80541
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 81828
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 74654
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 81406
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 89001
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 51368
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 38019
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 80215
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 71417
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 38053
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 99536
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 45583
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 83547
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 99404
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 94133
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 64523
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 60718
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 59529
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 81764
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 78142
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 25311
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 81474
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 55909
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 86967
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 14928
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 66693
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 73392
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 83760
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 81943
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 60462
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 30806
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 67437
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 46130
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 53752
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 42643
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 10600
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 62399
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 37269
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 13512
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 4083
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 69636
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 76588
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 35469
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 53324
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 87510
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 94873
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 72121
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 1754
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 15066
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 25451
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 8607
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 99372
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 6329
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 58708
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 89549
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 58649
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 49809
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 35546
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 53250
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 39999
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 61527
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 58571
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 23662
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 85962
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 71290
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 93449
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 68984
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 34726
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 52564
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 2951
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 80291
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 13103
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 67559
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 15797
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 73399
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 88999
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 6543
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 46146
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 33187
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 11898
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 25612
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 21804
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 44678
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 17473
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 99771
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 3989
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 54420
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 7358
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 69855
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 8752
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 65969
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 53239
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 71324
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 48558
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 37939
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 86760
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 35267
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 29694
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 94366
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 74904
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 61737
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 72062
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 36910
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 69883
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 48999
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 46502
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 85031
docker exec -it mn.source python message_factory.py -t request_update -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 27696

# Request scaling 
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 44257
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 49313
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 59379
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 26463
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 43053
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 63821
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 78979
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 5273
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 62506
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 70515
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 89454
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 88916
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 3437
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 70929
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 1950
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 38160
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 70003
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 98317
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 43373
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 58613
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 64396
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 52250
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 21919
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 50636
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 94203
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 25365
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 32544
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 70340
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 28879
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 11399
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 83887
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 41578
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 48731
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 12940
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 64565
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 37224
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 78751
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 18344
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 82996
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 5491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 71398
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 55153
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 11642
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 91554
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 29641
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 20835
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 79020
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 69625
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 6285
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 30278
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 50545
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 23072
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 56865
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 85850
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 92114
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 12920
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 65435
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 90835
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 26311
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 85707
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 24422
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 57859
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 46145
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 61693
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 26843
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 27214
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 24919
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 75903
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 54874
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 60682
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 49635
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 3713
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 74334
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 13052
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 13258
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 88863
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 20609
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 83639
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 77265
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 73229
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 16380
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 24220
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 94968
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 31152
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 29937
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 40720
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 57324
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 23532
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 70991
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 33309
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 5257
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 72120
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 26964
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 42598
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 30581
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 55090
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 13433
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 97164
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 28085
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 39661
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 58441
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 70767
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 90715
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 5585
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 74514
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 85317
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 73217
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 40538
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 58654
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 23474
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 22266
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 64711
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 53279
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 73563
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 37205
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 91934
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 43113
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 71617
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 86192
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 67205
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 56017
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 99135
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 26771
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 49546
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 43891
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 7728
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 47329
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 2900
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 96058
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 91271
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 87144
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 46418
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 24367
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 53313
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 69782
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 64570
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 76435
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 72306
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 55524
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 39413
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 13989
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 36139
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 56387
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 50775
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 19334
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 63207
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 79955
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 46633
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 85624
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 16590
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 98853
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 4102
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 71211
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 97121
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 90989
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 21046
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 45167
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 11644
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 97116
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 26712
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 93274
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 52891
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 33380
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 94242
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 57156
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 21367
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 80077
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 2395
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 39064
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 95411
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 5472
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 34374
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 53118
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 71576
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 74943
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 83400
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 43795
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 16778
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 28491
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 7441
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 15605
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 14546
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 43189
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 9955
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 14161
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 17139
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 67149
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 49611
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 92213
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 44870
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 78049
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 81955
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 77579
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 13393
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 44995
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 44403
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 10013
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 71033
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 32559
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 11117
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 8150
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 88526
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 39215
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 43792
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 83495
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 75749
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 95449
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 26687
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 25520
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 63502
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 28016
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 97036
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 60773
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 82090
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 75316
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 62430
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 65195
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 88551
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 20180
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 17689
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 83629
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 27872
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 73923
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 75920
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 79539
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 54814
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 47755
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 31254
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 65070
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 73757
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 5119
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 52232
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 13194
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 96902
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 57436
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 39963
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 5165
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 63608
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 77060
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 80081
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 96818
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 73338
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 8243
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 79087
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 32245
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 57760
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 36801
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 84502
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 62832
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 72371
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 40825
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 19916
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 29287
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 51683
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 56236
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 92938
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 56300
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 5511
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 30334
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 39985
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 27254
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 29347
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 89214
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 48969
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 64237
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 61841
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 47876
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 73036
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 38888
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 70521
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 7973
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 6911
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 35839
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 70962
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 51268
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 70296
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 7563
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 87917
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 5329
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 97502
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 57350
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0970-3efe-11eb-bde0-04ea56f99520 --seed 68196
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f09f2-3efe-11eb-bde0-04ea56f99520 --seed 71185
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 68611
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 75125
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 73875
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 39248
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 20222
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 22968
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 93866
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 3181
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 17287
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 80541
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 81828
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 74654
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 81406
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 89001
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 51368
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 38019
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 80215
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 71417
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 38053
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 99536
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 45583
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 83547
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 99404
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 94133
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 64523
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 60718
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 59529
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 81764
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 78142
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 25311
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 81474
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0996-3efe-11eb-bde0-04ea56f99520 --seed 55909
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 86967
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 14928
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 66693
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 73392
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 83760
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 81943
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 60462
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 30806
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 67437
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 46130
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 53752
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 42643
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 10600
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 62399
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 37269
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 13512
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 4083
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 69636
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 76588
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 35469
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 53324
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 87510
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 94873
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 72121
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 1754
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 15066
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 25451
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 8607
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f09bc-3efe-11eb-bde0-04ea56f99520 --seed 99372
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 6329
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 58708
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 89549
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 58649
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 49809
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 35546
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b0e-3efe-11eb-bde0-04ea56f99520 --seed 53250
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 39999
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89272f0-3efe-11eb-bde0-04ea56f99520 --seed 61527
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 58571
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892736e-3efe-11eb-bde0-04ea56f99520 --seed 23662
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 85962
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 71290
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 93449
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 68984
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 34726
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 52564
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 2951
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f08a6-3efe-11eb-bde0-04ea56f99520 --seed 80291
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 13103
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0b22-3efe-11eb-bde0-04ea56f99520 --seed 67559
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0a1a-3efe-11eb-bde0-04ea56f99520 --seed 15797
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 73399
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 88999
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 6543
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ace-3efe-11eb-bde0-04ea56f99520 --seed 46146
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f08ba-3efe-11eb-bde0-04ea56f99520 --seed 33187
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 11898
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c8927340-3efe-11eb-bde0-04ea56f99520 --seed 25612
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f08f6-3efe-11eb-bde0-04ea56f99520 --seed 21804
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 44678
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0aa8-3efe-11eb-bde0-04ea56f99520 --seed 17473
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 99771
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 3989
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f09ce-3efe-11eb-bde0-04ea56f99520 --seed 54420
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 7358
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 69855
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c89f0b34-3efe-11eb-bde0-04ea56f99520 --seed 8752
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 65969
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 53239
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89272e0-3efe-11eb-bde0-04ea56f99520 --seed 71324
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 48558
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0a46-3efe-11eb-bde0-04ea56f99520 --seed 37939
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a8a-3efe-11eb-bde0-04ea56f99520 --seed 86760
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c89f0950-3efe-11eb-bde0-04ea56f99520 --seed 35267
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4441 -i c8927316-3efe-11eb-bde0-04ea56f99520 --seed 29694
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 94366
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f093c-3efe-11eb-bde0-04ea56f99520 --seed 74904
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4437 -i c89f0910-3efe-11eb-bde0-04ea56f99520 --seed 61737
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0890-3efe-11eb-bde0-04ea56f99520 --seed 72062
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f08da-3efe-11eb-bde0-04ea56f99520 --seed 36910
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c89f0ae8-3efe-11eb-bde0-04ea56f99520 --seed 69883
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4445 -i c892732e-3efe-11eb-bde0-04ea56f99520 --seed 48999
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 46502
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4439 -i c89f0a70-3efe-11eb-bde0-04ea56f99520 --seed 85031
docker exec -it mn.source python message_factory.py -t request_scale -h 127.0.0.1 -p 4443 -i c892735e-3efe-11eb-bde0-04ea56f99520 --seed 27696

