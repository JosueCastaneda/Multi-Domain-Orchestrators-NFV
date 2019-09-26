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

    def is_valid_bandwidth(self, new_bandwidth):
        if self.consumed_bandwidth[0] > new_bandwidth:
            return False
        return True

    def is_valid_delay(self, new_delay):
        if self.delay[0] <= new_delay:
            return False
        return True

    def is_valid_jitter(self, new_jitter):
        if self.jitter[0] <= new_jitter:
            return False
        return True

    def is_valid_loss(self, new_loss):
        if self.loss[0] <= new_loss:
            return False
        return True

    def is_new_vnf_valid_for_service(self, other):
        return self.is_valid_bandwidth(other.consumed_bandwidth) and \
               self.is_valid_delay(other.delay) and \
               self.is_valid_jitter(other.jitter) and \
               self.is_valid_loss(other.loss)
