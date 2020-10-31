import sys

sys.path.append('../')


from communication_entities.matching_attribute import MatchingAttribute
# from utilities.logger import *


class Classifier:

    def __init__(self, identifier, name='',rsp_identifier=''):
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

    def update(self, another_classifier):
        self.identifier = another_classifier.identifier
        self.name = another_classifier.name
        self.rsp_identifier = another_classifier.rsp_identifier
        self.matching_attributes = another_classifier.matching_attributes

    async def update_matching_attribute(self, new_matching_attribute:MatchingAttribute):
        for matching_attribute in self.matching_attributes:
            if matching_attribute.get_identifier() == new_matching_attribute.get_identifier():
                matching_attribute.update(new_matching_attribute)
                return
        log.info('No Matching attribute with ID was found!')

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
