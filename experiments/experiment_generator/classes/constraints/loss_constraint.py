class LossConstraint:

    def __init__(self, low, high):
        self.low_value = low
        self.high_value = high

    def get_low(self):
        return self.low_value

    def get_high(self):
        return self.high_value

