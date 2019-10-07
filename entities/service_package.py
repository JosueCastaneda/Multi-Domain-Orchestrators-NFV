class ServicePackage:

    def __init__(self, bw=None, delay=None, jitter=None, loss=None):
        self.consumed_bandwidth = bw,
        self.delay = delay,
        self.jitter = jitter,
        self.loss = loss

    def create_from_topology(self, topology):
        self.consumed_bandwidth = topology.bw
        self.delay = topology.delay
        self.jitter = topology.jitter
        self.loss = topology.loss

    # TODO: Correct this function, for now always is valid
    def is_valid_bandwidth(self, new_bandwidth):
        # print("Self Bandwidth: ", self.consumed_bandwidth[0], " type: ", type(self.consumed_bandwidth[0] ))
        # print("New Bandwidth: ", new_bandwidth, " type: ", type(new_bandwidth))
        # new_bandwidth = int(new_bandwidth)
        if float(self.consumed_bandwidth[0]) > float(new_bandwidth):
            return False
        return True

    def is_valid_delay(self, new_delay):
        if self.delay[0] <= float(new_delay):
            return False
        return True

    def is_valid_jitter(self, new_jitter):
        if self.jitter[0] <= float(new_jitter):
            return False
        return True

    def is_valid_loss(self, new_loss):
        if self.loss <= float(new_loss):
            return False
        return True

    def is_new_vnf_valid_for_service(self, other):
        return self.is_valid_bandwidth(other.consumed_bandwidth) and \
               self.is_valid_delay(other.delay) and \
               self.is_valid_jitter(other.jitter) and \
               self.is_valid_loss(other.loss)
