from abc import ABC, abstractmethod

class ComunicationEntity(ABC):
    @abstractmethod
    def read_package(self, client, header_size):
        pass

    @abstractmethod
    def send_package(self, client, data):
        pass
