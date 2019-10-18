class ParameterFade:

    """
    This class represents the parameters required for annotating a video using MoviePy

    ...

    Attributes
    ----------
    text = string
        The text inserted in the video
    font_size = int
        The size is font
    color = string
        The name of the color for the text
    duration = int
        The time to display the text
    """

    def __init__(self, duration=2):
        """

        :param text: The text inserted in the video
        :param duration: The time to display the text
        :param font_size: The size is font
        :param color: The name of the color for the text
        """
        self.duration = duration
