class Topology:

    def __init__(self, delay, bandwidth, loss, jitter):
        self.delay = delay
        self.bw = bandwidth
        self.loss = loss
        self.jitter = jitter
        self.ip = None
        self.port = None

    def set_delay(self, val):
        self.delay = val

    def increase_delay(self, val):
        self.delay += val

    def decrease_delay(self, val):
        self.delay -= val

    def set_bandwidth(self, val):
        self.bw = val

    def increase_bandwidth(self, val):
        self.bw += val

    def decrease_bandwidth(self, val):
        self.bw -= val

    def set_loss(self, val):
        self.loss = val

    def increase_loss(self, val):
        self.loss += val

    def decrease_loss(self, val):
        self.loss -= val

    def set_jitter(self, val):
        self.jitter = val

    def increase_jitter(self, val):
        self.jitter += val

    def decrease_jitter(self, val):
        self.jitter -= val

    def to_string(self):
        return ''.join(["IP: ", self.ip,
                        " Port: ", str(self.port),
                        " Delay: ", str(self.delay),
                        " Bandwidth: ", str(self.bw),
                        " Loss: ", str(self.loss),
                        " Jitter: ", str(self.jitter)])
