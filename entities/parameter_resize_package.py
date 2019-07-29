class ParameterResizePackage:
    """
        A class that packages the required information to apply resize operation.

        ...

        Attributes
        ----------
        width : int
            the new width of the video
        height : int
            the new height of the video
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        :param width: the new width of the video
        :param height:  the new height of the video
        """

        self.width = width
        self.height = height

