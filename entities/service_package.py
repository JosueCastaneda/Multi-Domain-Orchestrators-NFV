class ServicePackage:

    def __init__(self, bw=None, delay=None, jitter=None, loss=None, service_threshold=None):
        self.consumed_bandwidth = bw,
        self.delay = delay,
        self.jitter = jitter,
        self.loss = loss
        self.consumed_bandwidth_threshold = service_threshold.consumed_bandwidth
        self.delay_threshold = service_threshold.delay
        self.jitter_threshold = service_threshold.jitter
        self.loss_threshold = service_threshold.loss

    def create_from_topology(self, topology):
        self.consumed_bandwidth = topology.bw
        self.delay = topology.delay
        self.jitter = topology.jitter
        self.loss = topology.loss

    # TODO: Correct this function, for now always is valid
    def is_valid_bandwidth(self, new_bandwidth, previous_bandwidth):
        result_bandwidth = float(self.consumed_bandwidth[0]) - float(previous_bandwidth) + float(new_bandwidth)
        if result_bandwidth <= float(self.consumed_bandwidth_threshold[0]):
            return False
        return True

    def is_new_delay_less_or_equal_than_previous_delay(self, new_delay, previous_delay):
        if float(self.delay[0]) - float(previous_delay) + float(new_delay) <= float(self.delay_threshold[0]):
            return True
        return False

    def is_new_jitter_less_or_equal_to_previous_jitter(self, new_jitter, previous_jitter):
        if float(self.jitter[0]) - float(previous_jitter) + float(new_jitter) <= float(self.jitter_threshold[0]):
            return True
        return False

    def is_new_loss_less_or_equal_than_previous_loss(self, new_loss, previous_loss):
        if float(self.loss[0]) - float(previous_loss) + float(new_loss) <= self.loss_threshold[0]:
            return True
        return False

    def is_new_vnf_valid_for_service(self, new_vnf, previous_vnf):
        return self.is_valid_bandwidth(new_vnf.consumed_bandwidth, previous_vnf.consumed_bandwidht) and \
               self.is_new_delay_less_or_equal_than_previous_delay(new_vnf.delay, previous_vnf.delay) and \
               self.is_new_jitter_less_or_equal_to_previous_jitter(new_vnf.jitter, previous_vnf.jitter) and \
               self.is_new_loss_less_or_equal_than_previous_loss(new_vnf.loss, previous_vnf.loss)
