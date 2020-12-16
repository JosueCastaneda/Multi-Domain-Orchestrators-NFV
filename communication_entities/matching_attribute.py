from utilities.logger import *


class MatchingAttribute:

    def __init__(self,
                 identifier,
                 ip_proto='',
                 source_ip='',
                 destination_ip='',
                 source_port='',
                 destination_port='',
                 counter=0,
                 current_max_orchestrator_index=-1):
        self.identifier = identifier
        self.ip_proto = ip_proto
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.counter = counter
        self.current_max_orchestrator_index = current_max_orchestrator_index

    def set_counter(self, val):
        self.counter = val

    def get_counter(self):
        return self.counter

    def set_current_max_orchestrator_index(self, val):
        self.current_max_orchestrator_index = val

    def get_current_max_orchestrator_index(self):
        return self.current_max_orchestrator_index

    def increase_counter(self):
        self.counter += 1

    def get_identifier(self):
        return self.identifier

    def update_source_ip(self, new_ip):
        self.source_ip = new_ip

    def update_source_port(self, new_port):
        self.source_port = new_port

    def update_destination_ip(self, new_ip):
        self.destination_ip = new_ip

    def update_destination_port(self, new_port):
        self.destination_port = new_port

    def update(self, other_matching_attribute, was_called_by_caller=False):
        self.ip_proto = other_matching_attribute.ip_proto
        self.source_ip = other_matching_attribute.source_ip
        self.destination_ip = other_matching_attribute.destination_ip
        self.source_port = other_matching_attribute.source_port
        self.destination_port = other_matching_attribute.destination_port

        if was_called_by_caller:
            self.increase_counter()
            self.current_max_orchestrator_index = -1
        else:
            other_max_counter = int(other_matching_attribute.get_current_max_orchestrator_index())

            if int(other_matching_attribute.get_counter()) > int(self.counter):
                self.counter = int(other_matching_attribute.get_counter())
                self.set_current_max_orchestrator_index(other_max_counter)
            elif other_max_counter > self.current_max_orchestrator_index:
                self.set_current_max_orchestrator_index(other_max_counter)
            elif self.current_max_orchestrator_index == -1:
                self.increase_counter()
        result = dict()
        result['counter'] = self.get_counter()
        result['new_max_couter'] = self.get_current_max_orchestrator_index()
        return result

    def log_information(self):
        log.info('IP Protocol: ' + str(self.ip_proto))
        log.info('Source IP: ' + str(self.source_ip))
        log.info('Destination IP: ' + str(self.destination_ip))
        log.info('Source Port: ' + str(self.source_port))
        log.info('Destination Port: ' + str(self.destination_port))

    def as_dictionary(self):
        matching_attribute_as_dictionary = dict()
        matching_attribute_as_dictionary['identifier'] = self.identifier
        matching_attribute_as_dictionary['ip_proto'] = self.ip_proto
        matching_attribute_as_dictionary['source_ip'] = self.source_ip
        matching_attribute_as_dictionary['destination_ip'] = self.destination_ip
        matching_attribute_as_dictionary['source_port'] = self.source_port
        matching_attribute_as_dictionary['destination_port'] = self.destination_port
        matching_attribute_as_dictionary['counter'] = self.counter
        return matching_attribute_as_dictionary
