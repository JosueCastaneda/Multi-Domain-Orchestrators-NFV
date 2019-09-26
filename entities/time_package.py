class TimePackage:
    """
    A class that packages the required information to apply multiple operations involving time frames.

    ...

    Attributes
    ----------
    begin : int
        the time to begin the operation
    end : int
        the time to end the operation
    """

    def __init__(self, begin_time, end_time):
        """
        Parameters
        ----------
        :param begin_time: The time to start the operation
        :param end_time: The time to end the operation
        """

        self.begin = begin_time
        self.end = end_time
