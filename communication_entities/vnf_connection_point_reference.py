from heapq import heappush, heappop, heapify

from communication_entities.vector_clock import VectorClock
from utilities.logger import *


class ConnectionPointReference:

    def __init__(self,
                 identifier,
                 order=0,
                 ingress_connection_point='',
                 egress_connection_point='',
                 counter=0,
                 current_max_orchestrator_index=-1,
                 orchestrator_sender_id='',
                 list_of_orchestrator_id=None):
        self.vnf_identifier = identifier
        self.order = order
        self.ingress_connection_point = ingress_connection_point
        self.egress_connection_point = egress_connection_point
        self.counter = counter
        self.current_max_orchestrator_index = current_max_orchestrator_index
        self.messages_sent = 0
        self.save_messages = -1
        self.vector_clock = VectorClock()
        self.orchestrator_sender_id = orchestrator_sender_id
        # if experiment != -1:
        if list_of_orchestrator_id is None:
            self.list_of_orchestrator_id = []
        else:
            self.list_of_orchestrator_id = list_of_orchestrator_id
        self.list_positive_entries = []
        self.list_negative_entries = []
        self.add_clocks()

    def add_clocks(self):
        if len(self.list_of_orchestrator_id) > 0:
            for identifier in self.list_of_orchestrator_id:
                self.vector_clock.add_clock(identifier)

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

    def check_if_cp_item_is_negated(self, item, orchestrator_log):
        for entry in self.list_negative_entries:
            same_id = entry.get_vnf_identifier() == item['attribute_id']
            same_counter = entry.get_counter() == item['counter']
            same_max_orchestrator = entry.get_current_max_orchestrator_index() == item['current_max_orchestrator_index']
            if same_id and same_counter and same_max_orchestrator:
                return True
        return False

    def remove_item_from_positive_add_to_negative(self, item, orchestrator_log):
        element_is_not_found = True
        number_of_positive_entries = len(self.list_positive_entries)
        repetitions = 0
        entries_not_ordered = []
        while element_is_not_found and repetitions < number_of_positive_entries:
            entry = heappop(self.list_positive_entries)
            same_id = entry.get_vnf_identifier() == item['attribute_id']
            same_counter = entry.get_counter() == item['counter']
            same_max_orchestrator = entry.get_current_max_orchestrator_index() == item['current_max_orchestrator_index']
            if same_id and same_counter and same_max_orchestrator:
                element_is_not_found = False
                orchestrator_log.info('Pushing to negative')
                heappush(self.list_negative_entries, entry)
                break
            else:
                entries_not_ordered.append(entry)
            repetitions += 1
        orchestrator_log.info('Heapify again the union of positive elements and not_ordered')
        self.list_positive_entries.extend(entries_not_ordered)
        heapify(self.list_positive_entries)

        if len(self.list_positive_entries) > 0:
            my_top_value = self.list_positive_entries[0]
            str_top = ' [' + str(my_top_value.counter) + ' ,' + str(my_top_value.current_max_orchestrator_index) + '] '
            orchestrator_log.info('After removing: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries)) + str_top)
        else:
            orchestrator_log.info(
                'After removing: ' + str(len(self.list_positive_entries)) + ' ' + str(len(self.list_negative_entries)) + ' Empty positives')

    def check_if_item_is_accepted(self, item, orchestrator_log):
        for entry in self.list_positive_entries:
            same_id = entry.get_vnf_identifier() == item['attribute_id']
            same_counter = entry.get_counter() == item['counter']
            same_max_orchestrator = entry.get_current_max_orchestrator_index() == item['current_max_orchestrator_index']
            if same_id and same_counter and same_max_orchestrator:
                orchestrator_log.info('ITEM IS IN POSITIVE ENTRIES')
                return True
        orchestrator_log.info('ITEM IS NOT IN POSITIVE ENTRIES')
        return False


    def try_to_update_cp_with_data(self, data, orchestrator_log):
        new_item = None
        if 'update' in data:
            new_item = self.update_heap_with_positive_entry(data, orchestrator_log)
        else:
            # orchestrator_log.info(data)
            data_counter = data['attribute_counter']
            data_max_counter = data['current_max_orchestrator_index']
            data_value = data['value']
            data_message_repetitions = data['messages_sent']
            # orchestrator_log.info(data_value)
            # orchestrator_log.info(data)
            new_is_greater = data_counter > self.counter
            equal_new_index_max = (self.counter == data_counter) and (data_max_counter > self.current_max_orchestrator_index)
            # This line because this algo contains the problem of sequential updates
            same_orchestrator_bigger_repetitions = (self.counter == data_counter) and (
                        data_max_counter == self.current_max_orchestrator_index) and data_message_repetitions > self.messages_sent
            str_before = 'Before update- ' + str(self.vnf_identifier[0:8]) + ' Counter: ' + str(self.counter) + ' Max ID: ' + str(
                self.current_max_orchestrator_index)
            orchestrator_log.info(str_before)

            str_me = 'My values (' + str(self.counter) + ',' + str(self.current_max_orchestrator_index) + ',' + str(
                self.messages_sent) + ')'
            str_new = ' New values (' + str(data_counter) + ',' + data_max_counter + ',' + str(
                data_message_repetitions) + ')'
            str_status = str_me + str_new
            orchestrator_log.info('Conditions are met? ' + str(new_is_greater or equal_new_index_max) + ' ' + str_status)
            if new_is_greater or equal_new_index_max or same_orchestrator_bigger_repetitions:
                orchestrator_log.info('Updating...')
                self.order = data_value['order']
                self.ingress_connection_point = data_value['ingress_connection_point']
                self.egress_connection_point = data_value['egress_connection_point']
                self.counter = data_counter
                self.current_max_orchestrator_index = data_max_counter
                self.save_messages = data_message_repetitions
                self.messages_sent = 0

            str_after = 'After update- ' + str(self.vnf_identifier) + ' Counter: ' + str(self.counter) + ' Max ID: ' + str(
                self.current_max_orchestrator_index)
            orchestrator_log.info(str_after)
        return new_item

    def update_heap_with_positive_entry(self, data, orchestrator_log):
        # orchestrator_log.info('Trying to update the heap...')
        new_matching_attribute = None
        if data['update'] == 'corrective':
            # orchestrator_log.info('Doing corrective')
            # orchestrator_log.info(data)
            # orchestrator_log.info(self.as_dictionary(orchestrator_log))
            new_matching_attribute = self.create_from_data(data)
            # orchestrator_log.info('New matching attribute')
            # orchestrator_log.info(new_matching_attribute.as_dictionary())
            orchestrator_log.info('Before adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries)))
            heappush(self.list_positive_entries, new_matching_attribute)
            my_top_value = self.list_positive_entries[0]
            str_top = ' [' + str(my_top_value.counter) + ' ,' + str(my_top_value.current_max_orchestrator_index) + '] '
            orchestrator_log.info('After adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries)) + str_top + ' value order: ' + str(my_top_value.order))
            # orchestrator_log.info('Done, printing result...')
            # orchestrator_log.info(self.as_dictionary(orchestrator_log))
            # orchestrator_log.info('Finish adding to heap')
        return new_matching_attribute

    def create_from_data(self, data):
        if len(self.list_positive_entries) == 0:
            my_counter = self.counter + 1
        else:
            top_attribute = self.list_positive_entries[0]
            my_counter = top_attribute.counter + 1

        if 'value' in data:
            data_value = data['value']
            new_matching_attribute = ConnectionPointReference(identifier=data_value['vnf_identifier'],
                                                              order=data_value['order'],
                                                              ingress_connection_point=data_value['ingress_connection_point'],
                                                              egress_connection_point=data_value['egress_connection_point'],
                                                              counter=my_counter,
                                                              current_max_orchestrator_index=data['current_max_orchestrator_index'])
        else:
            new_matching_attribute = ConnectionPointReference(identifier=data['vnf_identifier'],
                                                              order=data['order'],
                                                              ingress_connection_point=data['ingress_connection_point'],
                                                              egress_connection_point=data['egress_connection_point'],
                                                              counter=my_counter,
                                                              current_max_orchestrator_index=data['current_max_orchestrator_index'])
        return new_matching_attribute


    def update(self, new_vnf_connection, orchestrator_log=None, was_called_by_caller=None):
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
        self.vector_clock.increment_clock(was_called_by_caller['caller'])
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

    def as_dictionary(self, orchestrator_log=None):
        vnf_connection_point_reference_dictionary = dict()
        if len(self.list_positive_entries) == 0:
            vnf_connection_point_reference_dictionary['vnf_identifier'] = self.vnf_identifier
            vnf_connection_point_reference_dictionary['order'] = self.order
            vnf_connection_point_reference_dictionary['ingress_connection_point'] = self.ingress_connection_point
            vnf_connection_point_reference_dictionary['egress_connection_point'] = self.egress_connection_point
            vnf_connection_point_reference_dictionary['counter'] = self.counter
            vnf_connection_point_reference_dictionary['messages_sent'] = self.messages_sent
            vnf_connection_point_reference_dictionary['current_max_orchestrator_index'] = self.current_max_orchestrator_index
            vnf_connection_point_reference_dictionary['save_messages'] = self.save_messages
        else:
            if orchestrator_log:
                orchestrator_log.info('Getting latest value....')
            my_value = self.list_positive_entries[0]
            vnf_connection_point_reference_dictionary['vnf_identifier'] = my_value.vnf_identifier
            vnf_connection_point_reference_dictionary['order'] = my_value.order
            vnf_connection_point_reference_dictionary['ingress_connection_point'] = my_value.ingress_connection_point
            vnf_connection_point_reference_dictionary['egress_connection_point'] = my_value.egress_connection_point
            vnf_connection_point_reference_dictionary['counter'] = my_value.counter
            vnf_connection_point_reference_dictionary['messages_sent'] = my_value.messages_sent
            vnf_connection_point_reference_dictionary[
                'current_max_orchestrator_index'] = my_value.current_max_orchestrator_index
        return vnf_connection_point_reference_dictionary

    def update_sent_messages(self):
        self.messages_sent += 1
        # self.counter += 1
