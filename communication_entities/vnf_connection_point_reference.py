from utilities.logger import *


class VNFConnectionPointReference:

    def __init__(self,
                 identifier,
                 order=0,
                 ingress_connection_point='',
                 egress_connection_point='',
                 counter=0,
                 current_max_orchestrator_index=-1):
        self.vnf_identifier = identifier
        self.order = order
        self.ingress_connection_point = ingress_connection_point
        self.egress_connection_point = egress_connection_point
        self.counter = counter
        self.current_max_orchestrator_index = current_max_orchestrator_index

    def set_current_max_orchestrator_index(self, val):
        self.current_max_orchestrator_index = val

    def get_current_max_orchestrator_index(self):
        return self.current_max_orchestrator_index

    def set_counter(self, val):
        self.counter = val

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

    def update(self, new_vnf_connection, orch_log=None, was_called_by_caller=False):

        self.order = new_vnf_connection.get_order()
        self.egress_connection_point = new_vnf_connection.get_egress_connection_point()
        self.ingress_connection_point = new_vnf_connection.get_ingress_connection_point()

        if was_called_by_caller:
            # orch_log.info('Was called by loger')
            self.increase_counter()
            self.current_max_orchestrator_index = -1
            # self.current_max_orchestrator_index = -1
        else:
            other_max_counter = int(new_vnf_connection.get_current_max_orchestrator_index())

            if int(new_vnf_connection.get_counter()) > int(self.counter):
                self.counter = int(new_vnf_connection.get_counter())
                self.set_current_max_orchestrator_index(other_max_counter)
            elif other_max_counter > self.current_max_orchestrator_index:
                self.set_current_max_orchestrator_index(other_max_counter)
            elif self.current_max_orchestrator_index == -1:
                self.increase_counter()
        result = dict()
        result['counter'] = self.get_counter()
        result['new_max_counter'] = self.get_current_max_orchestrator_index()
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
