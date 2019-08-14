from communication.messages.abstract_message import AbstractMessage
from utilities.logger import *


class VNFNotFound(AbstractMessage):

    def __init__(self, data):
        self.data = data

    def process_message(self):
        log.info("Not found!")
