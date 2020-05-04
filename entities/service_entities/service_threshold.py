class ServiceThreshold:

    def __init__(self, consumed_bandwidth_threshold,
                 delay_threshold,
                 jitter_threshold,
                 loss_threshold):
        self.consumed_bandwidth = consumed_bandwidth_threshold
        self.delay = delay_threshold
        self.jitter = jitter_threshold
        self.loss = loss_threshold
