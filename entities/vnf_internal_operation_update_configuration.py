class VnfInternalOperationUpdateConfiguration:
    # TODO: Check why Now I am sending the hosts, ports, seeds and number of hosts as parameters
    def __init__(self,
                 service_index,
                 vnf_to_change_index,
                 value_to_change,
                 new_value,
                 wait_period,
                 name_vnf_to_update,
                 logical_clock,
                 hosts,
                 ports,
                 seeds,
                 number_of_hosts):
        self.list_hosts = hosts
        self.list_ports = ports
        self.list_seeds = seeds
        self.number_of_hosts = number_of_hosts
        self.service_index = service_index
        self.vnf_to_change_index = vnf_to_change_index
        self.value_to_change = value_to_change
        self.new_value = new_value
        self.wait_period = wait_period
        self.name_vnf_to_update = name_vnf_to_update
        self.logical_clock = logical_clock
