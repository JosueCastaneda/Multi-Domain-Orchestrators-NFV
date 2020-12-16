from communication_entities.vnf_connection_point_reference import VNFConnectionPointReference
from utilities.logger import *


class RenderedServicePath:

    def __init__(self, rsp_id, name):
        self.rsp_id = rsp_id
        self.name = name
        self.vnf_descriptor_connection_points = list()

    def update(self, another_rendered_service_path):
        self.rsp_id = another_rendered_service_path.rsp_id
        self.name = another_rendered_service_path.name
        self.vnf_descriptor_connection_points = another_rendered_service_path.vnf_descriptor_connection_points()

    def get_id(self):
        return self.rsp_id

    def get_name(self):
        return self.name

    def get_vnf_by_position(self, position: int):
        return self.vnf_descriptor_connection_points[position]

    def get_vnf_by_identifier(self, identifier):
        for connection_point in self.vnf_descriptor_connection_points:
            if connection_point.get_vnf_identifier() == identifier:
                return connection_point

    def append_vnf_connection_point_reference(self, new_vnf_connection_point_reference: VNFConnectionPointReference):
        self.vnf_descriptor_connection_points.append(new_vnf_connection_point_reference)

    def update_vnf_connection_point_reference_by_position(self,
                                                          vnf_connection_point_reference: VNFConnectionPointReference,
                                                          position: int):
        self.vnf_descriptor_connection_points[position].update_all_with_new_vnf_connection(vnf_connection_point_reference)

    def update_vnf_connection_point_reference_by_index(self,
                                                       new_vnf_connection_point_reference: VNFConnectionPointReference):
        for connection_point in self.vnf_descriptor_connection_points:
            if connection_point.get_vnf_identifier() == new_vnf_connection_point_reference.get_vnf_identifier():
                connection_point.update_all_with_new_vnf_connection(new_vnf_connection_point_reference)

    def as_dictionary(self):
        rendered_service_path_dictionary = dict()
        rendered_service_path_dictionary['rsp_id'] = self.rsp_id
        rendered_service_path_dictionary['name'] = self.name
        rendered_service_path_dictionary['vnf_descriptor_connection_points'] = list()
        for vnf_connection_point in self.vnf_descriptor_connection_points:
            vnf_connection_point_dict_entry = vnf_connection_point.as_dictionary()
            rendered_service_path_dictionary['vnf_descriptor_connection_points'].append(vnf_connection_point_dict_entry)
        return rendered_service_path_dictionary

    async def update_vnf_connection_point(self, vnf_connection_point_reference: VNFConnectionPointReference,
                                          vnffg_identifier,
                                          orch_log,
                                          was_called_by_caller=False):
        result = dict()
        result['update_result'] = False
        result['connection_point'] = None
        result['new_counter'] = -1
        for cp in self.vnf_descriptor_connection_points:
            if cp.get_vnf_identifier() == vnf_connection_point_reference.get_vnf_identifier():
                new_result = cp.update(vnf_connection_point_reference,
                                       orch_log,
                                       was_called_by_caller)
                result['update_result'] = True
                result['connection_point'] = cp.as_dictionary()
                result['new_counter'] = new_result['counter']
                result['new_max_counter'] = new_result['new_max_counter']
                result['vnffg_identifier'] = vnffg_identifier[0:8]
                result['change_identifier'] = cp.vnf_identifier[0:8]
                return result
        return result

    def get_counter_from_entry_connection_point(self, new_entry, orch_log):
        for cp in self.vnf_descriptor_connection_points:
            if cp.get_vnf_identifier() == new_entry['change_identifier']:
                return cp.get_counter()
        return -1

    def get_current_max_index_from_entry_connection_point(self, new_entry, orch_log):
        for cp in self.vnf_descriptor_connection_points:
            if cp.get_vnf_identifier() == new_entry['change_identifier']:
                return cp.get_current_max_orchestrator_index()
        return -1
