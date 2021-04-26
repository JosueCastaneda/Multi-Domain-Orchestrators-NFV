from communication_entities.classifier_rule import ClassifierRule
from communication_entities.matching_attribute import MatchingAttribute
from communication_entities.rendered_service_path import RenderedServicePath
from communication_entities.vnf_connection_point_reference import ConnectionPointReference


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
        self.set_unique_dependencies = list()
        self.service_identifier = service_identifier
        self.my_orchestrator = my_orchestrator
        self.type_of_change = ''

    def as_string(self):
        return self.identifier + ' ' + self.name + ' ' + self.short_name

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

    async def update_unique_rendered_service_path(self, new_vnf_connection_point_reference: ConnectionPointReference,
                                                  orch_log,
                                                  orch_index,
                                                  was_called_by_caller=None):
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
            update_result_as_dictionary['vector_clock'] = result['vector_clock']
            update_result_as_dictionary['identifier'] = result['identifier']
            update_result_as_dictionary['vnffg_identifier'] = self.identifier
            update_result_as_dictionary['vnffg_name'] = self.name
            update_result_as_dictionary['vnffg_short_name'] = self.short_name
            update_result_as_dictionary['type_of_change_attribute'] = 'connection_point'
            update_result_as_dictionary['running_time'] = result['running_time']

        update_result_as_dictionary['is_positive_result'] = result['update_result']
        update_result_as_dictionary['replicas'] = replicas_to_send_notifications
        update_result_as_dictionary['vnffg'] = vnf_fg_as_dict
        return update_result_as_dictionary

    async def remove_item_from_heap_and_reconfigure(self, item, orchestrator_log):
        if item['type'] == 'matching_attribute':
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == item['attribute_id']:
                    orchestrator_log.info('Removing item ' + str(item['attribute_id'][0:8]) + ' from attribute')
                    return matching_attribute.remove_item_from_positive_add_to_negative(item, orchestrator_log)
        if item['type'] == 'connection_point':
            path = self.rendered_service_paths[0]
            for connection_point in path.vnf_descriptor_connection_points:
                if connection_point.get_vnf_identifier() == item['attribute_id']:
                    orchestrator_log.info('Removing item from connection_point')
                    return connection_point.remove_item_from_positive_add_to_negative(item, orchestrator_log)

    def check_item_is_negated(self, item, orchestrator_log=None):
        if item['type'] == 'matching_attribute':
            # orchestrator_log.info('Checking if matching attribute for ' + str(item['attribute_id'][0:8]) +' is negated')
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == item['attribute_id']:
                    return matching_attribute.check_if_item_is_negated(item, orchestrator_log)

        if item['type'] == 'connection_point':
            orchestrator_log.info('Checking connection point for ' + str(item['attribute_id'][0:8]))
            path = self.rendered_service_paths[0]
            for connection_point in path.vnf_descriptor_connection_points:
                if connection_point.get_vnf_identifier() == item['attribute_id']:
                    return connection_point.check_if_cp_item_is_negated(item, orchestrator_log)
        return True

    def check_item_is_accepted(self, item, orchestrator_log=None):
        if item['type'] == 'matching_attribute':
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == item['attribute_id']:
                    # orchestrator_log.info(
                    #     'Checking if matching attribute for ' + str(item['attribute_id'][0:8]) + ' is accepted')
                    return matching_attribute.check_if_item_is_accepted(item, orchestrator_log)

        if item['type'] == 'connection_point':
            path = self.rendered_service_paths[0]
            for connection_point in path.vnf_descriptor_connection_points:
                if connection_point.get_vnf_identifier() == item['attribute_id']:
                    orchestrator_log.info('Checking if connection point for ' + str(item['attribute_id'][0:8]) + ' is accepted')
                    return connection_point.check_if_item_is_accepted(item, orchestrator_log)
        return True

    def has_item(self, item, orchestrator_log=None):
        # orchestrator_log.info('Has item')
        # orchestrator_log.info(item)
        if item['type'] == 'matching_attribute':
            # orchestrator_log.info('Checking matching attribute')
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                # orchestrator_log.info('Checking matching attribute AGAIN')
                if matching_attribute.get_identifier() == item['attribute_id']:
                    return True
        elif item['type'] == 'connection_point':
            path = self.rendered_service_paths[0]
            for connection_point in path.vnf_descriptor_connection_points:
                if connection_point.get_vnf_identifier() == item['attribute_id']:
                    return True
        return False

    # TODO: Implement this method
    async def add_item_to_negated_list(self, item, orchestrator_log):
        if item['type'] == 'matching_attribute':
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == item['attribute_id']:
                    return matching_attribute.add_invalid_corrective_update(item, orchestrator_log)
        if item['type'] == 'connection_point':
            # ERROR: IMPLEMENT GODZILLA
            orchestrator_log.info('Please implement me')

    # TODO: IMPLEMENT THIS FUNCTION NOW IS STUB
    def has_item_negated(self, item, orchestrator_log):
        if item['type'] == 'matching_attribute':
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == item['attribute_id']:
                    # orchestrator_log.info('Checking if item is negated....')
                    return matching_attribute.check_if_item_is_negated(item, orchestrator_log)
        elif item['type'] == 'connection_point':
            path = self.rendered_service_paths[0]
            for connection_point in path.vnf_descriptor_connection_points:
                if connection_point.get_vnf_identifier() == item['attribute_id']:
                    # orchestrator_log.info('Checking if item is negated....')
                    return connection_point.check_if_cp_item_is_negated(item, orchestrator_log)
        return True

    def has_matching_attribute(self, new_matching_attribute: MatchingAttribute):
        rule = self.classification_rules[0]
        for matching_attribute in rule.matching_attributes:
            if matching_attribute.get_identifier() == new_matching_attribute.get_identifier():
                return True
        return False

    def has_connection_point(self, new_connection_point: ConnectionPointReference):
        path = self.rendered_service_paths[0]
        for connection_point in path.vnf_descriptor_connection_points:
            if connection_point.get_vnf_identifier() == new_connection_point.get_vnf_identifier():
                return True
        return False

    def increase_message_for_connection_point(self, new_connection_point: ConnectionPointReference):
        path = self.rendered_service_paths[0]
        for connection_point in path.vnf_descriptor_connection_points:
            if connection_point.get_vnf_identifier() == new_connection_point.get_vnf_identifier():
                connection_point.update_sent_messages()

    def get_counter_for_connection_point(self, new_connection_point: ConnectionPointReference):
        path = self.rendered_service_paths[0]
        data = dict()
        for connection_point in path.vnf_descriptor_connection_points:
            if connection_point.get_vnf_identifier() == new_connection_point.get_vnf_identifier():
                data['attribute_counter'] = connection_point.counter
                data['current_max_orchestrator_index'] = connection_point.current_max_orchestrator_index
                data['messages_sent'] = connection_point.messages_sent
                if connection_point.messages_sent > 0:
                    data['attribute_counter'] += connection_point.messages_sent
                return data
        return data

    def get_affected_orchestrators(self):
        list_affected_orchestrators = []
        for orch in self.set_unique_orchestrators:
            list_affected_orchestrators.append(orch)
        for orch in self.set_unique_dependencies:
            list_affected_orchestrators.append(orch)
        # Remove duplicates
        list_affected_orchestrators = list(dict.fromkeys(list_affected_orchestrators))
        return list_affected_orchestrators

    def increase_message_for_attribute(self, new_matching_attribute: MatchingAttribute):
        rule = self.classification_rules[0]
        for matching_attribute in rule.matching_attributes:
            if matching_attribute.get_identifier() == new_matching_attribute.get_identifier():
                matching_attribute.update_sent_messages()

    def get_counter_for_attribute(self, new_matching_attribute: MatchingAttribute):
        rule = self.classification_rules[0]
        data = dict()
        for matching_attribute in rule.matching_attributes:
            if matching_attribute.get_identifier() == new_matching_attribute.get_identifier():
                data['attribute_counter'] = matching_attribute.counter
                data['current_max_orchestrator_index'] = matching_attribute.current_max_orchestrator_index
                data['messages_sent'] = matching_attribute.messages_sent
                if matching_attribute.messages_sent > 0:
                    data['attribute_counter'] += matching_attribute.messages_sent
                return data
        return data

    async def update_data(self, data, orchestrator_log):
        new_item = None
        if data['type'] == 'matching_attribute':
            rule = self.classification_rules[0]
            for matching_attribute in rule.matching_attributes:
                if matching_attribute.get_identifier() == data['attribute_id']:
                    new_item = matching_attribute.try_to_update_with_data(data, orchestrator_log)
                    break
        elif data['type'] == 'connection_point':
            path = self.rendered_service_paths[0]
            orchestrator_log.info('Got path + CP ID: ' + str(data['attribute_id'][0:8]))
            for connection_point in path.vnf_descriptor_connection_points:
                if connection_point.get_vnf_identifier() == data['attribute_id']:
                    orchestrator_log.info('Update connection point: ' + str(data['attribute_id']))
                    new_item = connection_point.try_to_update_cp_with_data(data, orchestrator_log)
                    break
        return new_item

    # TODO: Separate repeated functions, clean code
    async def update_unique_classifier_rule(self,
                                            new_matching_attribute: MatchingAttribute,
                                            orch_log,
                                            was_called_by_caller=None):
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
            update_result_as_dictionary['vector_clock'] = result['vector_clock']
            update_result_as_dictionary['identifier'] = result['identifier']
            update_result_as_dictionary['vector_clock_s'] = result['vector_clock_s']
            update_result_as_dictionary['vnffg_identifier'] = self.identifier
            update_result_as_dictionary['vnffg_name'] = self.name
            update_result_as_dictionary['vnffg_short_name'] = self.short_name
            update_result_as_dictionary['type_of_change_attribute'] = 'matching_attribute'
            update_result_as_dictionary['running_time'] = result['running_time']
            update_result_as_dictionary['initial_time'] = result['initial_time']
            update_result_as_dictionary['reconfiguration_time'] = result['reconfiguration_time']

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

    def get_first_classifier_rule(self):
        return self.classification_rules[0]

    def get_first_rendered_service_path_id(self):
        return self.rendered_service_paths[0].get_id()

    def instantiate_rendered_service_path(self, vnf_fg_entry, list_of_orchestrator_id):
        for rendered_service_path_entry in vnf_fg_entry['rendered_service_paths']:
            new_rendered_service_path = RenderedServicePath(rendered_service_path_entry['rsp_id'],
                                                            rendered_service_path_entry['name'])
            for vnf_descriptor_connection_point in rendered_service_path_entry['vnf_descriptor_connection_points']:
                new_connection_point = ConnectionPointReference(vnf_descriptor_connection_point['vnf_identifier'],
                                                                vnf_descriptor_connection_point['order'],
                                                                vnf_descriptor_connection_point[
                                                                       'ingress_connection_point'],
                                                                vnf_descriptor_connection_point[
                                                                       'egress_connection_point'],
                                                                list_of_orchestrator_id=list_of_orchestrator_id)

                new_rendered_service_path.append_vnf_connection_point_reference(new_connection_point)
            self.append_rendered_service_path(new_rendered_service_path)

    def instantiate_classification_rules(self, vnf_fg_entry, list_of_orchestrator_id):
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
                                                           matching_attribute_entry['destination_port'],
                                                           list_of_orchestrator_id=list_of_orchestrator_id)
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
