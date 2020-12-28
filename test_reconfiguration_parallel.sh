#echo -n "Please type experiment: "
#read EXPERIMENT_NUMBER
path_1="experiments/experiment_generator/experiments/experiment_"$1
path_3="/updates_vnf_forwarding_graphs.sh"
complete_file=$path_1$path_3

# Activate the virtual environment
source my_env/bin/activate

# Change permission
chmod +x $complete_file

# Run all the python files
./$complete_file

#python message_factory.py --type update_vnffg_rsp --host 127.0.0.1 --port 4443 --vnf_identifier c6caebae-4210-11eb-93fb-04ea56f99520 --order 1 --ingress_connection_point c745c6bb-4210-11eb-93fb-04ea56f99520 --egress_connection_point c745c6bc-4210-11eb-93fb-04ea56f99520 &

#python message_factory.py --type update_vnffg_classifier --host 127.0.0.1 --port 4441 --match_identifier c6d28da0-4210-11eb-93fb-04ea56f99520 --ip_proto c745c6bd-4210-11eb-93fb-04ea56f99520 --source_ip c745c6be-4210-11eb-93fb-04ea56f99520 --destination_ip c745c6bf-4210-11eb-93fb-04ea56f99520 --source_port c745c6c0-4210-11eb-93fb-04ea56f99520 --destination_port c745c6c1-4210-11eb-93fb-04ea56f99520 &

#python message_factory.py --type update_vnffg_rsp --host 127.0.0.1 --port 4439 --vnf_identifier c6caeb30-4210-11eb-93fb-04ea56f99520 --order 6 --ingress_connection_point c745c6c2-4210-11eb-93fb-04ea56f99520 --egress_connection_point c745c6c3-4210-11eb-93fb-04ea56f99520 &
#
#python message_factory.py --type update_vnffg_rsp --host 127.0.0.1 --port 4437 --vnf_identifier c6caebcc-4210-11eb-93fb-04ea56f99520 --order 7 --ingress_connection_point c745c6c4-4210-11eb-93fb-04ea56f99520 --egress_connection_point c745c6c5-4210-11eb-93fb-04ea56f99520 &
#
#python message_factory.py --type update_vnffg_rsp --host 127.0.0.1 --port 4445 --vnf_identifier c6caea97-4210-11eb-93fb-04ea56f99520 --order 7 --ingress_connection_point c745c6c6-4210-11eb-93fb-04ea56f99520 --egress_connection_point c745c6c7-4210-11eb-93fb-04ea56f99520 &
#
#python message_factory.py --type update_vnffg_rsp --host 127.0.0.1 --port 4439 --vnf_identifier c6caeb84-4210-11eb-93fb-04ea56f99520 --order 7 --ingress_connection_point c745c6c8-4210-11eb-93fb-04ea56f99520 --egress_connection_point c745c6c9-4210-11eb-93fb-04ea56f99520 &
