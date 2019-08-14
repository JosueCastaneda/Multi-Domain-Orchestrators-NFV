class ParameterFilePackage:
    """
        A class that packages the required information to work with source videos

        ...

        Attributes
        ----------
        name : str
            the name of the original file
        format : str
            the desired format for the processed file
        process_name: str
            the desired name of the processed file
    """
    def __init__(self, name: str, file_format: str, process_name: str):
        """
        Parameters
        ----------
        :param name: the name of the original file
        :param file_format: the desired format for the processed file
        :param process_name: the desired name of the processed file
        """
        self.name = name
        self.format = file_format
        self.process_name = process_name

    def full_name_original(self) -> str:
        """
            Return the name with format of the source file
        :return: name plus format of source file
        """
        return ''.join([self.name, self.format])

    def full_name_processed(self):
        """
            Return the name with format of the processed file
        :return: names plus format of processed file
        """
        return ''.join([self.process_name, self.format])
