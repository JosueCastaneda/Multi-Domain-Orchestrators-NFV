import sys

sys.path.append('../')


from communication_entities.matching_attribute import MatchingAttribute


class ClassifierRule:

    def __init__(self, identifier, name='', rsp_identifier=''):
        self.identifier = identifier
        self.name = name
        self.rsp_identifier = rsp_identifier
        self.matching_attributes = list()

    def append_matching_attributes(self, matching_attribute):
        self.matching_attributes.append(matching_attribute)

    def get_identifier(self):
        return self.identifier

    def get_name(self):
        return self.name

    def get_rsp_identifier(self):
        return self.rsp_identifier

    def update_rule(self, another_classifier):
        self.identifier = another_classifier.identifier
        self.name = another_classifier.name
        self.rsp_identifier = another_classifier.rsp_identifier
        self.matching_attributes = another_classifier.matching_attributes

    async def update_matching_attribute(self, new_matching_attribute: MatchingAttribute, vnffg_identifier: str, log, was_called_by_caller=False):
        result = dict()
        result['update_result'] = False
        result['matching_attribute'] = None
        result['new_counter'] = -1
        for matching_attribute in self.matching_attributes:
            if matching_attribute.get_identifier() == new_matching_attribute.get_identifier():
                new_result = matching_attribute.update(new_matching_attribute,
                                                       was_called_by_caller)
                result['update_result'] = True
                result['matching_attribute'] = matching_attribute.as_dictionary()
                result['new_counter'] = new_result['counter']
                result['new_max_counter'] = new_result['new_max_couter']
                result['vnffg_identifier'] = vnffg_identifier[0:8]
                result['change_identifier'] = matching_attribute.identifier[0:8]
                return result
        return result

    def as_dictionary(self):
        classifier_as_dictionary = dict()
        classifier_as_dictionary['identifier'] = self.identifier
        classifier_as_dictionary['name'] = self.name
        classifier_as_dictionary['rsp_identifier'] = self.rsp_identifier
        classifier_as_dictionary['matching_attributes'] = list()

        for matching_attribute in self.matching_attributes:
            if isinstance(matching_attribute, dict):
                classifier_as_dictionary['matching_attributes'].append(matching_attribute)
            else:
                classifier_as_dictionary['matching_attributes'].append(matching_attribute.as_dictionary())
        return classifier_as_dictionary

    def get_counter_from_entry_rule(self, new_entry, orch_log):
        for ma in self.matching_attributes:
            if ma.get_identifier() == new_entry['change_identifier']:
                return ma.get_counter()
        return -1

    def get_current_max_index_from_entry_rule(self, new_entry, orch_log):
        for ma in self.matching_attributes:
            if ma.get_identifier() == new_entry['change_identifier']:
                return ma.get_current_max_orchestrator_index()
        return -1