from communication_entities.classifier_rule import ClassifierRule
from communication_entities.matching_attribute import MatchingAttribute
from communication_entities.rendered_service_path import RenderedServicePath
from communication_entities.vnf_connection_point_reference import VNFConnectionPointReference


class VNFForwardingGraph:

    def __init__(self,
                 identifier,
                 name='',
                 short_name='',
                 is_shared=False,
                 service_identifier='',
                 my_orchestrator=''):
        self.identifier = identifier
        self.name = name
        self.short_name = short_name
        self.rendered_service_paths = list()
        self.classification_rules = list()
        self.is_shared = is_shared
        self.set_unique_orchestrators = list()
        self.service_identifier = service_identifier
        self.my_orchestrator = my_orchestrator
        self.type_of_change = ''

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

    def append_classification(self, new_classification_rule: ClassifierRule):
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

    async def update_unique_rendered_service_path(self, new_vnf_connection_point_reference: VNFConnectionPointReference,
                                                  orch_log,
                                                  orch_index,
                                                  was_called_by_caller=False):

        replicas_to_send_notifications = list()
        path = self.rendered_service_paths[0]
        update_result_as_dictionary = dict()
        result = await path.update_vnf_connection_point(new_vnf_connection_point_reference,
                                                        self.identifier,
                                                        orch_log,
                                                        was_called_by_caller)
        self.type_of_change = 'rsp'
        vnf_fg_as_dict = self.as_dictionary()
        self.type_of_change = ''
        if result['update_result']:
            for orchestrator_replica in self.set_unique_orchestrators:
                if orchestrator_replica != self.my_orchestrator:
                    replicas_to_send_notifications.append(orchestrator_replica)
            vnf_fg_as_dict['change_identifier'] = result['connection_point']['vnf_identifier']
            vnf_fg_as_dict['change_order'] = result['connection_point']['order']
            vnf_fg_as_dict['change_ingress_connection_point'] = result['connection_point']['ingress_connection_point']
            vnf_fg_as_dict['change_egress_connection_point'] = result['connection_point']['egress_connection_point']
            vnf_fg_as_dict['vnffg_counter'] = result['new_counter']
            update_result_as_dictionary['new_counter'] = result['new_counter']
            update_result_as_dictionary['new_max_counter'] = result['new_max_counter']
            update_result_as_dictionary['vnffg_identifier'] = result['vnffg_identifier']
            update_result_as_dictionary['change_identifier'] = result['change_identifier']

        update_result_as_dictionary['is_positive_result'] = result['update_result']
        update_result_as_dictionary['replicas'] = replicas_to_send_notifications
        update_result_as_dictionary['vnffg'] = vnf_fg_as_dict
        return update_result_as_dictionary

    async def update_unique_classifier_rule(self,
                                            new_matching_attribute: MatchingAttribute,
                                            orch_log,
                                            was_called_by_caller=False):
        replicas_to_send_notifications = list()
        rule = self.classification_rules[0]
        update_result_as_dictionary = dict()
        self.type_of_change = 'classifier_rule'
        vnf_fg_as_dictionary = self.as_dictionary()
        self.type_of_change = ''
        result = await rule.update_matching_attribute(new_matching_attribute,
                                                      self.identifier,
                                                      orch_log,
                                                      was_called_by_caller)
        if result['update_result']:
            for orchestrator_replica in self.set_unique_orchestrators:
                if orchestrator_replica != self.my_orchestrator:
                    replicas_to_send_notifications.append(orchestrator_replica)
            vnf_fg_as_dictionary['change_identifier'] = result['matching_attribute']['identifier']
            vnf_fg_as_dictionary['change_ip_proto'] = result['matching_attribute']['ip_proto']
            vnf_fg_as_dictionary['change_source_ip'] = result['matching_attribute']['source_ip']
            vnf_fg_as_dictionary['change_destination_ip'] = result['matching_attribute']['destination_ip']
            vnf_fg_as_dictionary['change_source_port'] = result['matching_attribute']['source_port']
            vnf_fg_as_dictionary['change_destination_port'] = result['matching_attribute']['destination_port']
            vnf_fg_as_dictionary['vnffg_counter'] = result['new_counter']
            update_result_as_dictionary['new_counter'] = result['new_counter']
            update_result_as_dictionary['new_max_counter'] = result['new_max_counter']
            update_result_as_dictionary['vnffg_identifier'] = result['vnffg_identifier']
            update_result_as_dictionary['change_identifier'] = result['change_identifier']

        update_result_as_dictionary['is_positive_result'] = result['update_result']
        update_result_as_dictionary['replicas'] = replicas_to_send_notifications
        update_result_as_dictionary['vnffg'] = vnf_fg_as_dictionary
        return update_result_as_dictionary

    def as_dictionary(self):
        vnf_forwarding_graph_as_dictionary = dict()
        vnf_forwarding_graph_as_dictionary['identifier'] = self.identifier
        vnf_forwarding_graph_as_dictionary['name'] = self.name
        vnf_forwarding_graph_as_dictionary['short_name'] = self.short_name
        vnf_forwarding_graph_as_dictionary['type_of_change'] = self.type_of_change
        vnf_forwarding_graph_as_dictionary['rendered_service_paths'] = list()
        vnf_forwarding_graph_as_dictionary['classification_rules'] = list()
        vnf_forwarding_graph_as_dictionary['is_shared'] = self.is_shared
        vnf_forwarding_graph_as_dictionary['service_identifier'] = self.service_identifier
        vnf_forwarding_graph_as_dictionary['my_orchestrator'] = self.my_orchestrator
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
            new_classifier = ClassifierRule(classification_rule_entry['identifier'],
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

    def get_counter_of_entry(self, new_entry, orch_log):
        my_counter = -1
        if new_entry['type_of_change'] == 'rsp':
            path = self.rendered_service_paths[0]
            my_counter = path.get_counter_from_entry_connection_point(new_entry, orch_log)
        if new_entry['type_of_change'] == 'classifier_rule':
            rule = self.classification_rules[0]
            my_counter = rule.get_counter_from_entry_rule(new_entry, orch_log)
        return my_counter

    def get_current_max_index_of_entry(self, new_entry, orch_log):
        my_current_max_index = -1
        if new_entry['type_of_change'] == 'rsp':
            path = self.rendered_service_paths[0]
            my_current_max_index = path.get_current_max_index_from_entry_connection_point(new_entry, orch_log)
        if new_entry['type_of_change'] == 'classifier_rule':
            rule = self.classification_rules[0]
            my_current_max_index = rule.get_current_max_index_from_entry_rule(new_entry, orch_log)
        return my_current_max_index
