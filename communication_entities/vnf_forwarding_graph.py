from communication_entities.classifier import Classifier
from communication_entities.matching_attribute import MatchingAttribute
from communication_entities.rendered_service_path import RenderedServicePath
from communication_entities.vnf_connection_point_reference import VNFConnectionPointReference


class VNFForwardingGraph:

    def __init__(self,
                 identifier,
                 name='',
                 short_name='',
                 is_shared=False,
                 service_identifier=''):
        self.identifier = identifier
        self.name = name
        self.short_name = short_name
        self.rendered_service_paths = list()
        self.classification_rules = list()
        self.is_shared = is_shared
        self.set_unique_orchestrators = list()
        self.service_identifier = service_identifier

    def get_identifier(self):
        return self.identifier

    def get_name(self):
        return self.name

    def get_short_name(self):
        return self.short_name

    def get_rendered_service_paths(self):
        return self.rendered_service_paths

    def list_classification_rules(self):
        return self.classification_rules

    def append_rendered_service_path(self, new_rsp: RenderedServicePath):
        self.rendered_service_paths.append(new_rsp)

    def append_classification(self, new_classification_rule:Classifier):
        self.classification_rules.append(new_classification_rule)

    def get_rendered_service_path_by_position(self, position: int):
        return self.rendered_service_paths[position]

    def get_rendered_service_path_by_index(self, new_rsp_id):
        for rendered_service_path in self.rendered_service_paths:
            if rendered_service_path.get_id() == new_rsp_id:
                return rendered_service_path

    def get_rendered_service_path_by_name(self, name):
        for rendered_service_path in self.rendered_service_paths:
            if rendered_service_path.get_name() == name:
                return rendered_service_path

    def update(self, another_vnf_forwarding_graph):
        self.identifier = another_vnf_forwarding_graph.identifier
        self.name = another_vnf_forwarding_graph.name
        self.short_name = another_vnf_forwarding_graph.short_name
        self.rendered_service_paths = another_vnf_forwarding_graph.rendered_service_paths
        self.classification_rules = another_vnf_forwarding_graph.list_classification_rules

    def update_classification_rule(self):
        print('Update classification rule')

    def update_rendered_service_path(self,
                                     rendered_service_path: RenderedServicePath,
                                     vnf_connection_point_reference: VNFConnectionPointReference):
        for rsp in self.rendered_service_paths:
            if rendered_service_path.get_id() == rsp.get_id():
                rsp.update_vnf_connection_point(vnf_connection_point_reference)

    async def update_unique_rendered_service_path(self, new_vnf_connection_point_reference: VNFConnectionPointReference):
        await self.rendered_service_paths[0].update_vnf_connection_point(new_vnf_connection_point_reference)

    async def update_unique_classifier_rule(self, new_matching_attribute: MatchingAttribute):
        await self.classification_rules[0].update_matching_attribute(new_matching_attribute)

    def as_dictionary(self):
        vnf_forwarding_graph_as_dictionary = dict()
        vnf_forwarding_graph_as_dictionary['identifier'] = self.identifier
        vnf_forwarding_graph_as_dictionary['name'] = self.name
        vnf_forwarding_graph_as_dictionary['short_name'] = self.short_name
        vnf_forwarding_graph_as_dictionary['rendered_service_paths'] = list()
        vnf_forwarding_graph_as_dictionary['classification_rules'] = list()
        vnf_forwarding_graph_as_dictionary['is_shared'] = self.is_shared
        vnf_forwarding_graph_as_dictionary['service_identifier'] = self.service_identifier
        vnf_forwarding_graph_as_dictionary['unique_orchestrators'] = list()
        for rendered_service_path in self.rendered_service_paths:
            rendered_service_path_dict_entry = rendered_service_path.as_dictionary()
            vnf_forwarding_graph_as_dictionary['rendered_service_paths'].append(rendered_service_path_dict_entry)

        for classification_rule in self.classification_rules:
            classification_rule_dict_entry = classification_rule.as_dictionary()
            vnf_forwarding_graph_as_dictionary['classification_rules'].append(classification_rule_dict_entry)

        for orchestrator in self.set_unique_orchestrators:
            vnf_forwarding_graph_as_dictionary['unique_orchestrators'].append(orchestrator)
        return vnf_forwarding_graph_as_dictionary

    def get_first_rendered_service_path(self):
        return self.rendered_service_paths[0]

    def get_first_rendered_service_path_id(self):
        return self.rendered_service_paths[0].get_id()

    def instantiate_rendered_service_path(self, vnf_fg_entry):
        for rendered_service_path_entry in vnf_fg_entry['rendered_service_paths']:
            new_rendered_service_path = RenderedServicePath(rendered_service_path_entry['rsp_id'],
                                                            rendered_service_path_entry['name'])
            for vnf_descriptor_connection_point in rendered_service_path_entry['vnf_descriptor_connection_points']:
                new_connection_point = VNFConnectionPointReference(vnf_descriptor_connection_point['vnf_identifier'],
                                                                   vnf_descriptor_connection_point['order'],
                                                                   vnf_descriptor_connection_point[
                                                                       'ingress_connection_point'],
                                                                   vnf_descriptor_connection_point[
                                                                       'egress_connection_point'])

                new_rendered_service_path.append_vnf_connection_point_reference(new_connection_point)
            self.append_rendered_service_path(new_rendered_service_path)

    def instantiate_classification_rules(self, vnf_fg_entry):
        for classification_rule_entry in vnf_fg_entry['classification_rules']:
            new_classifier = Classifier(classification_rule_entry['identifier'],
                                        classification_rule_entry['name'],
                                        classification_rule_entry['rsp_identifier'])
            for matching_attribute_entry in classification_rule_entry['matching_attributes']:
                new_matching_attribute = MatchingAttribute(matching_attribute_entry['identifier'],
                                                           matching_attribute_entry['ip_proto'],
                                                           matching_attribute_entry['source_ip'],
                                                           matching_attribute_entry['destination_ip'],
                                                           matching_attribute_entry['source_port'],
                                                           matching_attribute_entry['destination_port'])
                new_classifier.append_matching_attributes(new_matching_attribute)
            self.append_classification(new_classifier)

    def add_unique_orchestrators(self, orchestrators):
        for orchestrator in orchestrators:
            self.set_unique_orchestrators.append(orchestrator)
