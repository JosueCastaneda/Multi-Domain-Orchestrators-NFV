import json
from heapq import heappush, heappop, heapify

from communication_entities.vector_clock import VectorClock
from definitions import ROOT_DIR
from utilities.logger import *


class MatchingAttribute:

    def __init__(self,
                 identifier,
                 ip_proto='',
                 source_ip='',
                 destination_ip='',
                 source_port='',
                 destination_port='',
                 counter=0,
                 current_max_orchestrator_index=-1,
                 orchestrator_sender_id='',
                 list_of_orchestrator_id=[]):
        self.identifier = identifier
        self.ip_proto = ip_proto
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.counter = counter
        self.current_max_orchestrator_index = current_max_orchestrator_index
        self.messages_sent = 0
        self.save_messages = -1
        self.orchestrator_sender_id = orchestrator_sender_id
        self.vector_clock = VectorClock()
        self.list_of_orchestrator_id = list_of_orchestrator_id
        self.list_positive_entries = []
        self.list_negative_entries = []
        self.max_counter = 0
        # if experiment != -1:
        #     self.add_clocks(experiment)
        self.add_clocks()

    def get_identifier(self):
        return self.identifier

    def add_clocks(self):
        if len(self.list_of_orchestrator_id) > 0:
            for id in self.list_of_orchestrator_id:
                self.vector_clock.add_clock(id)

    def check_if_item_is_negated(self, item, orchestrator_log):
        for entry in self.list_negative_entries:
            same_id = entry.get_identifier() == item['attribute_id']
            same_counter = entry.get_counter() == item['counter']
            same_max_orchestrator = entry.get_current_max_orchestrator_index() == item['current_max_orchestrator_index']
            if same_id and same_counter and same_max_orchestrator:
                return True
        return False

    def check_if_item_is_accepted(self, item, orchestrator_log):
        for entry in self.list_positive_entries:
            same_id = entry.get_identifier() == item['attribute_id']
            same_counter = entry.get_counter() == item['counter']
            same_max_orchestrator = entry.get_current_max_orchestrator_index() == item['current_max_orchestrator_index']
            if same_id and same_counter and same_max_orchestrator:
                # orchestrator_log.info('ITEM IS IN POSITIVE ENTRIES')
                return True
        # orchestrator_log.info('ITEM IS NOT IN POSITIVE ENTRIES')
        return False

    def update_heap_with_positive_entry(self, data, orchestrator_log):
        new_matching_attribute = None
        if data['update'] == 'corrective':
            if data['first_update'] == 'True':
                new_matching_attribute = self.create_initial_from_data(data)
            else:
                new_matching_attribute = self.create_from_data(data)

            if 'value' in data:
                data_value = data['value']
                identifier = data_value['identifier']
            else:
                identifier = data['identifier']

            str_before = 'Updating heap with a positive entry ' + str(identifier[0:8]) + ' . Before adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries))
            # orchestrator_log.info()
            heappush(self.list_positive_entries, new_matching_attribute)
            my_top_value = self.list_positive_entries[0]
            # str_top = ' [' + str(my_top_value.counter) + ' ,' + str(my_top_value.current_max_orchestrator_index) + '] '
            str_top = ''
            str_after = ' , After adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries)) + ' top: '

            for entry in self.list_positive_entries:
                str_top += ' [' + str(entry.counter) + ' ,' + str(entry.current_max_orchestrator_index) + '] '

            orchestrator_log.info(str_before + str_after + str_top)

            # orchestrator_log.info('Done, printing result...')
            # orchestrator_log.info(self.as_dictionary(orchestrator_log))
            # orchestrator_log.info('Finish adding to heap')
        return new_matching_attribute

    def add_invalid_corrective_update(self, data, orchestrator_log):
        # orchestrator_log.info('Creating from data')
        # orchestrator_log.info(data)
        new_matching_attribute = self.create_from_data(data)

        if 'value' in data:
            data_value = data['value']
            identifier = data_value['identifier']
        else:
            identifier = data['identifier']

        # orchestrator_log.info('New matching attribute')
        # orchestrator_log.info(new_matching_attribute.as_dictionary())
        str_before = 'Adding invalid corrective update ' + str(identifier[0:8]) + ' . Before adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
            len(self.list_negative_entries))
        # orchestrator_log.info(str_before)
        heappush(self.list_negative_entries, new_matching_attribute)
        if len(self.list_positive_entries) > 0:
            my_top_value = self.list_positive_entries[0]

            # str_top = ' [' + str(my_top_value.counter) + ' ,' + str(my_top_value.current_max_orchestrator_index) + '] '
            str_top = ' '
            for my_entry in self.list_positive_entries:
                str_top += ' [' + str(my_entry.counter) + ' ,' + str(my_entry.current_max_orchestrator_index) + '] '

            str_after = ' , After adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries))
            orchestrator_log.info(str_before + str_after + str_top)
        else:
            str_after = ' After adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries)) + ' No elements in top '
            orchestrator_log.info(str_before + str_after)

        # orchestrator_log.info('After adding: ' + str(len(self.list_positive_entries)) + ' ' + str(
        #     len(self.list_negative_entries)))
        return new_matching_attribute

    def try_to_update_with_data(self, data, orchestrator_log):
        new_item = None
        if 'update' in data:
            new_item = self.update_heap_with_positive_entry(data, orchestrator_log)
        else:
            data_counter = data['attribute_counter']
            data_max_counter = data['current_max_orchestrator_index']
            data_message_repetitions = data['messages_sent']
            data_value = data['value']
            new_is_greater = data_counter > self.counter
            equal_new_index_max = self.counter == data_counter and data_max_counter > self.current_max_orchestrator_index
            # This line because this algo contains the problem of sequential updates
            same_orchestrator_bigger_repetitions = (self.counter == data_counter) and (data_max_counter == self.current_max_orchestrator_index) and data_message_repetitions > self.messages_sent
            str_before = 'Before update- ' + str(self.identifier[0:8]) + ' Counter: ' + str(self.counter) + ' Max ID: ' + str(self.current_max_orchestrator_index)
            orchestrator_log.info(str_before)
            str_me = 'My values (' + str(self.counter) + ',' + str(self.current_max_orchestrator_index) + ',' + str(
                    self.messages_sent)+')'
            str_new = ' New values (' + str(data_counter)+',' + data_max_counter+',' + str(data_message_repetitions) + ')'
            str_status = str_me + str_new

            orchestrator_log.info('Conditions are met? ' + str(new_is_greater or equal_new_index_max) + ' ' + str_status)
            if new_is_greater or equal_new_index_max or same_orchestrator_bigger_repetitions:
                orchestrator_log.info('Updating...')
                self.ip_proto = data_value['ip_proto']
                self.source_ip = data_value['source_ip']
                self.destination_ip = data_value['destination_ip']
                self.source_port = data_value['source_port']
                self.destination_port = data_value['destination_port']
                self.counter = data_counter
                self.current_max_orchestrator_index = data_max_counter
                self.save_messages = data_message_repetitions
                self.messages_sent = 0
            #     GODZILLA
            str_after = 'After update- ' + str(self.identifier) + ' Counter:' + str(self.counter) + ' Max ID: ' + str(self.current_max_orchestrator_index)
            orchestrator_log.info(str_after)
        return new_item

    def load_orchestrators_ids(self, experiment):
        orchestrators = []
        string_1= ROOT_DIR + '/' + 'experiments/experiment_generator/experiments/experiment_'
        directory_path = string_1 + str(experiment) + '/' + 'experiment_' + str(experiment)
        print(directory_path)
        with open(directory_path + '.json') as json_file:
            raw_data = json.load(json_file)
        for orchestrator in raw_data['orchestrators']:
            orchestrators.append(orchestrator['id'])
        return orchestrators

    def set_counter(self, val):
        self.counter = val

    def get_vector_clock(self):
        return self.vector_clock

    def get_counter(self):
        return self.counter

    def get_current_max_orchestrator_index(self):
        return self.current_max_orchestrator_index

    def set_current_max_orchestrator_index(self, val):
        self.current_max_orchestrator_index = val

    # def get_current_max_orchestrator_index(self):
    #     return self.current_max_orchestrator_index

    def increase_counter(self):
        self.counter += 1

    def update_source_ip(self, new_ip):
        self.source_ip = new_ip

    def update_source_port(self, new_port):
        self.source_port = new_port

    def update_destination_ip(self, new_ip):
        self.destination_ip = new_ip

    def update_destination_port(self, new_port):
        self.destination_port = new_port

    def update(self, other_matching_attribute, was_called_by_caller=None):
        if was_called_by_caller is None:
            was_called_by_caller = dict()
            was_called_by_caller['first_call'] = False
            was_called_by_caller['caller'] = other_matching_attribute.orchestrator_sender_id

        self.ip_proto = other_matching_attribute.ip_proto
        self.source_ip = other_matching_attribute.source_ip
        self.destination_ip = other_matching_attribute.destination_ip
        self.source_port = other_matching_attribute.source_port
        self.destination_port = other_matching_attribute.destination_port

        if was_called_by_caller['first_call']:
            self.increase_counter()
            self.current_max_orchestrator_index = -1
        else:
            other_max_counter = int(other_matching_attribute.get_current_max_orchestrator_index())

            if int(other_matching_attribute.get_counter()) > int(self.counter):
                self.counter = int(other_matching_attribute.get_counter())
                self.set_current_max_orchestrator_index(other_max_counter)
            elif other_max_counter > self.current_max_orchestrator_index:
                self.set_current_max_orchestrator_index(other_max_counter)
            elif self.current_max_orchestrator_index == -1:
                self.increase_counter()
        self.vector_clock.increment_clock(was_called_by_caller['caller'])
        result = dict()
        result['counter'] = self.get_counter()
        result['new_max_couter'] = self.get_current_max_orchestrator_index()
        result['vector_clock'] = self.vector_clock.to_json()
        result['vector_clock_s'] = self.vector_clock.as_string()
        return result

    def log_information(self):
        log.info('IP Protocol: ' + str(self.ip_proto))
        log.info('Source IP: ' + str(self.source_ip))
        log.info('Destination IP: ' + str(self.destination_ip))
        log.info('Source Port: ' + str(self.source_port))
        log.info('Destination Port: ' + str(self.destination_port))

    def create_initial_from_data(self, data):
        # First we increment the value, then we check if there's a top value
        self.counter += 1
        if len(self.list_positive_entries) == 0:
            my_counter = self.counter
        else:
            top_attribute = self.list_positive_entries[0]
            my_counter = top_attribute.counter + self.counter

        if my_counter > self.max_counter:
            self.max_counter = my_counter
        else:
            self.max_counter += 1
            my_counter = self.max_counter
            self.counter += 1


        # if len(self.list_positive_entries) == 0:
        #     my_counter = self.counter + 1
        # else:
        #     top_attribute = self.list_positive_entries[0]
        #     my_counter = top_attribute.counter + 1
        #
        # self.counter += 1

        # if data['update'] == 'corrective' and data['first_update'] == 'True':
        #     # ERROR: This is because theres a case where the same identity is used
        #     self.counter += 1

        if 'value' in data:
            data_value = data['value']
            new_matching_attribute = MatchingAttribute(identifier=data_value['identifier'],
                                                       ip_proto=data_value['ip_proto'],
                                                       source_ip=data_value['source_ip'],
                                                       destination_ip=data_value['destination_ip'],
                                                       source_port=data_value['source_port'],
                                                       destination_port=data_value['destination_port'],
                                                       counter=my_counter,
                                                       current_max_orchestrator_index=data['current_max_orchestrator_index'])
        else:
            new_matching_attribute = MatchingAttribute(identifier=data['identifier'],
                                                       ip_proto=data['ip_proto'],
                                                       source_ip=data['source_ip'],
                                                       destination_ip=data['destination_ip'],
                                                       source_port=data['source_port'],
                                                       destination_port=data['destination_port'],
                                                       counter=my_counter,
                                                       current_max_orchestrator_index=data[
                                                           'current_max_orchestrator_index'])
        return new_matching_attribute

    # ERROR: This code is used for creating objects but also increasing, which makes bugs as messages get new ids or equal...
    def create_from_data(self, data):
        # if len(self.list_positive_entries) == 0:
        #     my_counter = self.counter + 1
        # else:
        #     top_attribute = self.list_positive_entries[0]
        #     my_counter = top_attribute.counter + 1
        #
        # if data['update'] == 'corrective' and data['first_update'] == 'True':
        #     # ERROR: This is because theres a case where the same identity is used
        #     self.counter += 1

        if 'value' in data:
            data_value = data['value']
            new_matching_attribute = MatchingAttribute(identifier=data_value['identifier'],
                                                       ip_proto=data_value['ip_proto'],
                                                       source_ip=data_value['source_ip'],
                                                       destination_ip=data_value['destination_ip'],
                                                       source_port=data_value['source_port'],
                                                       destination_port=data_value['destination_port'],
                                                       counter=data_value['counter'],
                                                       current_max_orchestrator_index=data['current_max_orchestrator_index'])
        else:
            new_matching_attribute = MatchingAttribute(identifier=data['identifier'],
                                                       ip_proto=data['ip_proto'],
                                                       source_ip=data['source_ip'],
                                                       destination_ip=data['destination_ip'],
                                                       source_port=data['source_port'],
                                                       destination_port=data['destination_port'],
                                                       counter=data['counter'],
                                                       current_max_orchestrator_index=data[
                                                           'current_max_orchestrator_index'])
        return new_matching_attribute

    def as_dictionary(self, orchestrator_log=None):
        matching_attribute_as_dictionary = dict()
        if len(self.list_positive_entries) == 0:
            matching_attribute_as_dictionary['identifier'] = self.identifier
            matching_attribute_as_dictionary['ip_proto'] = self.ip_proto
            matching_attribute_as_dictionary['source_ip'] = self.source_ip
            matching_attribute_as_dictionary['destination_ip'] = self.destination_ip
            matching_attribute_as_dictionary['source_port'] = self.source_port
            matching_attribute_as_dictionary['destination_port'] = self.destination_port
            matching_attribute_as_dictionary['counter'] = self.counter
            matching_attribute_as_dictionary['current_max_orchestrator_index'] = self.current_max_orchestrator_index
            matching_attribute_as_dictionary['messages_sent'] = self.messages_sent
            matching_attribute_as_dictionary['save_messages'] = self.save_messages
        else:
            if orchestrator_log:
                orchestrator_log.info('Getting latest value....')
            my_value = self.list_positive_entries[0]
            matching_attribute_as_dictionary['identifier'] = my_value.identifier
            matching_attribute_as_dictionary['ip_proto'] = my_value.ip_proto
            matching_attribute_as_dictionary['source_ip'] = my_value.source_ip
            matching_attribute_as_dictionary['destination_ip'] = my_value.destination_ip
            matching_attribute_as_dictionary['source_port'] = my_value.source_port
            matching_attribute_as_dictionary['destination_port'] = my_value.destination_port
            matching_attribute_as_dictionary['counter'] = my_value.counter
            matching_attribute_as_dictionary['current_max_orchestrator_index'] = my_value.current_max_orchestrator_index
            matching_attribute_as_dictionary['messages_sent'] = my_value.messages_sent
            # if orchestrator_log:
            #     orchestrator_log.info('My value')
            # print(my_value.as_dictionary())

        return matching_attribute_as_dictionary

    def remove_item_from_positive_add_to_negative(self, item, orchestrator_log):
        element_is_not_found = True
        number_of_positive_entries = len(self.list_positive_entries)
        repetitions = 0
        entries_not_ordered = []
        while element_is_not_found and repetitions < number_of_positive_entries:
            entry = heappop(self.list_positive_entries)
            same_id = entry.get_identifier() == item['attribute_id']
            same_counter = entry.get_counter() == item['counter']
            same_max_orchestrator = entry.get_current_max_orchestrator_index() == item['current_max_orchestrator_index']
            if same_id and same_counter and same_max_orchestrator:
                element_is_not_found = False
                orchestrator_log.info('Pushing ' + str(item['attribute_id'][0:8]) + ' to negative')
                heappush(self.list_negative_entries, entry)
                break
            else:
                entries_not_ordered.append(entry)
            repetitions += 1
        str_before = 'Heapify again the union of positive elements and not_ordered'
        # orchestrator_log.info(str_before)
        self.list_positive_entries.extend(entries_not_ordered)
        heapify(self.list_positive_entries)

        if len(self.list_positive_entries) > 0:
            my_top_value = self.list_positive_entries[0]
            # str_top = ' [' + str(my_top_value.counter) + ' ,' + str(my_top_value.current_max_orchestrator_index) + '] '
            str_top = ' '

            for my_entry in self.list_positive_entries:
                str_top += ' [' + str(my_entry.counter) + ' ,' + str(my_entry.current_max_orchestrator_index) + '] '

            str_after = ' After removing: ' + str(len(self.list_positive_entries)) + ' ' + str(
                len(self.list_negative_entries))
            orchestrator_log.info(str_before + str_after + str_top)
        else:
            str_after = ' After removing: ' + str(len(self.list_positive_entries)) + ' ' + str(len(self.list_negative_entries)) + ' Empty positives'
            orchestrator_log.info(str_before + str_after)

    def update_sent_messages(self):
        self.messages_sent += 1
        # self.counter += 1

    # Note: By default a heap stores the smallest element on top, so neet to change this because we want a max-heap
    def __lt__(self, cmp):
        """Overwrite this to do the opposite of what's
        expected"""
        is_my_counter_greater = self.counter > cmp.counter
        counters_are_equal = self.counter == cmp.counter
        is_my_max_orchestrator_greater = self.current_max_orchestrator_index >= cmp.current_max_orchestrator_index
        if is_my_counter_greater:
            return True
        elif counters_are_equal and is_my_max_orchestrator_greater:
            return True
        return False
        # return is_my_counter_greater and is_my_max_orchestrator_greater

# self.counter = counter
#         self.current_max_orchestrator_index = current_max_orchestrator_index
#         self.messages_sent = 0