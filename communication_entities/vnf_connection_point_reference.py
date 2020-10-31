# from utilities.logger import *


class VNFConnectionPointReference:

    def __init__(self,
                 identifier,
                 order=0,
                 ingress_connection_point='',
                 egress_connection_point=''):
        self.vnf_identifier = identifier
        self.order = order
        self.ingress_connection_point = ingress_connection_point
        self.egress_connection_point = egress_connection_point

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

    def update(self, new_vnf_connection):
        log.info('Before update')
        self.log_information()
        self.order = new_vnf_connection.get_order()
        self.egress_connection_point = new_vnf_connection.get_egress_connection_point()
        self.ingress_connection_point = new_vnf_connection.get_ingress_connection_point()
        log.info('After update')
        self.log_information()

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
        return vnf_connection_point_reference_dictionary
