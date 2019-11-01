class FileNameParameters:
    def __init__(self, name: str, file_format: str, process_name: str):
        self.name = name
        self.format = file_format
        self.process_name = process_name

    def full_name_original(self) -> str:
        return ''.join([self.name, self.format])

    def full_name_processed(self):
        return ''.join([self.process_name, self.format])
