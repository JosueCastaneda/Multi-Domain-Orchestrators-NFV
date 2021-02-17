import json

from communication_entities.vector_clock import VectorClock
from definitions import ROOT_DIR
from utilities.logger import *


class VNFConnectionPointReference:

    def __init__(self,
                 identifier,
                 order=0,
                 ingress_connection_point='',
                 egress_connection_point='',
                 counter=0,
                 current_max_orchestrator_index=-1,
                 orchestrator_sender_id = '',
                 list_of_orchestrator_id=[]):
        self.vnf_identifier = identifier
        self.order = order
        self.ingress_connection_point = ingress_connection_point
        self.egress_connection_point = egress_connection_point
        self.counter = counter
        self.current_max_orchestrator_index = current_max_orchestrator_index
        self.vector_clock = VectorClock()
        self.orchestrator_sender_id = orchestrator_sender_id
        # if experiment != -1:
        self.list_of_orchestrator_id = list_of_orchestrator_id
        self.add_clocks()

    def add_clocks(self):
        if len(self.list_of_orchestrator_id) > 0:
            for id in self.list_of_orchestrator_id:
                self.vector_clock.add_clock(id)
            # print('Line 41 - MatchingAttribute- My clock: ' + self.vector_clock.as_string())
        # list_of_orchestrator_id = self.load_orchestrators_ids(experiment)
        # print('List of orchestrators')
        # print(list_of_orchestrator_id)
        # list_of_orchestrator_id = ["671fd36c-673a-11eb-b240-04ea56f99520",
        #                            "671fd36d-673a-11eb-b240-04ea56f99520",
        #                            "671fd36e-673a-11eb-b240-04ea56f99520",
        #                            "671fd36f-673a-11eb-b240-04ea56f99520",
        #                            "671fd370-673a-11eb-b240-04ea56f99520"]
        # print(self.list_of_orchestrator_id)
        # for id in self.list_of_orchestrator_id:
        #     self.vector_clock.add_clock(id)
        # self.vector_clock.add_clock(self.list_of_orchestrator_id[0])
        # self.vector_clock.add_clock(self.list_of_orchestrator_id[1])
        # self.vector_clock.add_clock(self.list_of_orchestrator_id[2])
        # self.vector_clock.add_clock(self.list_of_orchestrator_id[3])
        # self.vector_clock.add_clock(list_of_orchestrator_id[4])

    def load_orchestrators_ids(self, experiment):
        orchestrators = []
        string_1= ROOT_DIR + '/' + 'experiments/experiment_generator/experiments/experiment_'
        directory_path = string_1 + str(experiment) + '/' + 'experiment_' + str(experiment)
        # print(directory_path)
        with open(directory_path + '.json') as json_file:
            raw_data = json.load(json_file)
        for orchestrator in raw_data['orchestrators']:
            orchestrators.append(orchestrator['id'])
        return orchestrators

    def set_current_max_orchestrator_index(self, val):
        self.current_max_orchestrator_index = val

    def get_current_max_orchestrator_index(self):
        return self.current_max_orchestrator_index

    def set_counter(self, val):
        self.counter = val

    def get_vector_clock(self):
        return self.vector_clock

    def get_counter(self):
        return self.counter

    def increase_counter(self):
        self.counter += 1

    def get_vnf_identifier(self):
        return self.vnf_identifier

    def get_order(self):
        return self.order

    def get_egress_connection_point(self):
        return self.egress_connection_point

    def get_ingress_connection_point(self):
        return self.ingress_connection_point

    def update_ingress_connection_point(self, new_id_ingress_point):
        self.ingress_connection_point = new_id_ingress_point

    def update_egress_connection_point(self, new_id_egress_point):
        self.egress_connection_point = new_id_egress_point

    def update_order(self, new_order):
        self.order = new_order

    def update(self, new_vnf_connection, orch_log=None, was_called_by_caller=None):
        if was_called_by_caller is None:
            was_called_by_caller = dict()
            was_called_by_caller['first_call'] = False
            was_called_by_caller['caller'] = new_vnf_connection.orchestrator_sender_id

        self.order = new_vnf_connection.get_order()
        self.egress_connection_point = new_vnf_connection.get_egress_connection_point()
        self.ingress_connection_point = new_vnf_connection.get_ingress_connection_point()
        if was_called_by_caller['first_call']:
            self.increase_counter()
            self.current_max_orchestrator_index = -1
        else:
            other_max_counter = int(new_vnf_connection.get_current_max_orchestrator_index())

            if int(new_vnf_connection.get_counter()) > int(self.counter):
                self.counter = int(new_vnf_connection.get_counter())
                self.set_current_max_orchestrator_index(other_max_counter)
            elif other_max_counter > self.current_max_orchestrator_index:
                self.set_current_max_orchestrator_index(other_max_counter)
            elif self.current_max_orchestrator_index == -1:
                self.increase_counter()
        # print('Before increment: ' + str(self.vector_clock.as_string()) + ' Caller: ' + str(was_called_by_caller['caller']))
        self.vector_clock.increment_clock(was_called_by_caller['caller'])
        # print('After increment: ' + self.vector_clock.as_string())
        # self.vector_clock.increment_clock(was_called_by_caller['caller'])
        result = dict()
        result['counter'] = self.get_counter()
        result['new_max_counter'] = self.get_current_max_orchestrator_index()
        result['vector_clock'] = self.vector_clock.to_json()
        result['vector_clock_s'] = self.vector_clock.as_string()
        return result

    def log_information(self):
        log.info('Order: ' + str(self.order))
        log.info('Ingress Connection Point: ' + str(self.ingress_connection_point))
        log.info('Egress Connection Point: ' + str(self.egress_connection_point))

    def as_dictionary(self):
        vnf_connection_point_reference_dictionary = dict()
        vnf_connection_point_reference_dictionary['vnf_identifier'] = self.vnf_identifier
        vnf_connection_point_reference_dictionary['order'] = self.order
        vnf_connection_point_reference_dictionary['ingress_connection_point'] = self.ingress_connection_point
        vnf_connection_point_reference_dictionary['egress_connection_point'] = self.egress_connection_point
        vnf_connection_point_reference_dictionary['counter'] = self.counter
        return vnf_connection_point_reference_dictionary
