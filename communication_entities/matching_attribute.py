import json

from communication_entities.vector_clock import VectorClock
from definitions import ROOT_DIR
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
                 current_max_orchestrator_index=-1,
                 orchestrator_sender_id='',
                 list_of_orchestrator_id=[]):
        self.identifier = identifier
        self.ip_proto = ip_proto
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.counter = counter
        self.current_max_orchestrator_index = current_max_orchestrator_index
        self.orchestrator_sender_id = orchestrator_sender_id
        self.vector_clock = VectorClock()
        self.list_of_orchestrator_id = list_of_orchestrator_id
        # if experiment != -1:
        #     self.add_clocks(experiment)
        self.add_clocks()

    def add_clocks(self):
        # print('My IDS')
        # print(self.list_of_orchestrator_id)
        if len(self.list_of_orchestrator_id) > 0:
            for id in self.list_of_orchestrator_id:
                self.vector_clock.add_clock(id)
            # print('Line 41 - MatchingAttribute- My clock: ' + self.vector_clock.as_string())
        # else:
        #     list_of_orchestrator_id = ["671fd36c-673a-11eb-b240-04ea56f99520",
        #                                "671fd36d-673a-11eb-b240-04ea56f99520",
        #                                "671fd36e-673a-11eb-b240-04ea56f99520",
        #                                "671fd36f-673a-11eb-b240-04ea56f99520",
        #                                "671fd370-673a-11eb-b240-04ea56f99520"]
        #     self.vector_clock.add_clock(list_of_orchestrator_id[0])
        #     self.vector_clock.add_clock(list_of_orchestrator_id[1])
        #     self.vector_clock.add_clock(list_of_orchestrator_id[2])
        #     self.vector_clock.add_clock(list_of_orchestrator_id[3])
        #     self.vector_clock.add_clock(list_of_orchestrator_id[4])
        #     print('Line 53 - MatchingAttribute- My clock: ' + self.vector_clock.as_string())
        # print('Line 54 - MatchingAttribute- My clock: '+ self.vector_clock.as_string())
        #     orchestrators_ids = self.list_of_orchestrator_id

        # #TODO: Need to read the list from the json experiment...
        # list_of_orchestrator_id = self.load_orchestrators_ids(experiment)
        # print('List of orchestrators')
        # print(list_of_orchestrator_id)

    def load_orchestrators_ids(self, experiment):
        orchestrators = []
        string_1= ROOT_DIR + '/' + 'experiments/experiment_generator/experiments/experiment_'
        directory_path = string_1 + str(experiment) + '/' + 'experiment_' + str(experiment)
        print(directory_path)
        with open(directory_path + '.json') as json_file:
            raw_data = json.load(json_file)
        for orchestrator in raw_data['orchestrators']:
            orchestrators.append(orchestrator['id'])
        return orchestrators

    def set_counter(self, val):
        self.counter = val

    def get_vector_clock(self):
        return self.vector_clock

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

    def update(self, other_matching_attribute, was_called_by_caller=None):
        if was_called_by_caller is None:
            was_called_by_caller = dict()
            was_called_by_caller['first_call'] = False
            was_called_by_caller['caller'] = other_matching_attribute.orchestrator_sender_id

        self.ip_proto = other_matching_attribute.ip_proto
        self.source_ip = other_matching_attribute.source_ip
        self.destination_ip = other_matching_attribute.destination_ip
        self.source_port = other_matching_attribute.source_port
        self.destination_port = other_matching_attribute.destination_port

        if was_called_by_caller['first_call']:
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
        # print('Before increment: ' + str(self.vector_clock.as_string()) + ' Caller: ' + str(was_called_by_caller['caller']))
        self.vector_clock.increment_clock(was_called_by_caller['caller'])
        # print('After increment: ' + self.vector_clock.as_string())
        result = dict()
        result['counter'] = self.get_counter()
        result['new_max_couter'] = self.get_current_max_orchestrator_index()
        result['vector_clock'] = self.vector_clock.to_json()
        result['vector_clock_s'] = self.vector_clock.as_string()
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
