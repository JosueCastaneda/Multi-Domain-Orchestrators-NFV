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