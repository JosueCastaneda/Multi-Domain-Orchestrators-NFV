import json


class VectorClock(dict):

    def __init__(self, orchestrator_id=''):
        super().__init__()
        self.clock_list = list()
        if orchestrator_id != '':
            self.add_clock(orchestrator_id)

    def compare_with_list_of_values(self, other_clock, sender_id, orch_log):
        difference_in_vectors = 0
        for clock_entry in self.clock_list:
            if clock_entry['id'] == sender_id:
                for received_clock_entry in other_clock.clock_list:
                    if received_clock_entry['id'] == sender_id:
                        difference_in_vectors += abs(clock_entry['value'] - received_clock_entry['value'])
                        return difference_in_vectors

    def create_from_list(self, vector_string) -> None:
        vector_as_json = json.loads(vector_string)
        for clock_entry in vector_as_json:
            entry_id = clock_entry['id']
            entry_value = clock_entry['value']
            self.add_clock(entry_id, int(entry_value))

    def to_json(self):
        return json.dumps(self.clock_list, default=lambda o: o.__dict__)

    def add_clock(self, orchestrator_id, value=0):
        clock_dictionary = dict()
        clock_dictionary['id'] = orchestrator_id
        clock_dictionary['value'] = value
        self.clock_list.append(clock_dictionary)
        self.clock_list = sorted(self.clock_list, key=lambda k: k['id'])

    def causal_ordering_check(self, other_clock, id_sender, orch_log):
        orch_log.info('My clock: ' + str(self.as_string()) + ' other clock: ' + str(other_clock.as_string()) + ' sender id: ' + str(id_sender[0:8]))
        difference_in_vectors = 0
        for clock_entry in self.clock_list:
            if clock_entry['id'] == id_sender:
                for received_clock_entry in other_clock.clock_list:
                    if received_clock_entry['id'] == id_sender:
                        difference_in_vectors += abs(clock_entry['value'] - received_clock_entry['value'])
                        return difference_in_vectors

    def check_transitive_causal_order(self, new_clock_list, invalid_index):
        for index in range(len(self.clock_list)):
            if index != invalid_index and new_clock_list[index]['value'] > self.clock_list[index]['value']:
                return False
        return True

    def are_different(self, other_clock_list):
        for i in range(len(other_clock_list)):
            my_value = self.clock_list[i]['value']
            new_value = other_clock_list[i]['value']
            if my_value != new_value:
                return True
        return False

    def is_equal(self, other_clock):
        for i in range(len(self.clock_list)):
            my_clock_value = self.clock_list[i]
            other_clock_value = other_clock.clock_list[i]
            if my_clock_value != other_clock_value:
                return False
        return True

    def is_greater_than_other(self, other_clock):
        for i in range(len(self.clock_list)):
            my_value = self.clock_list[i]['value']
            other_value = other_clock.clock_list[i]['value']
            if my_value <= other_value:
                return False
        return True

    def compare_clocks(self, other_clock, id_sender, is_causal_delivery=False, orch_log=None):
        if self.is_equal(other_clock):
            return 0
        if self.is_greater_than_other(other_clock):
            return 0
        if is_causal_delivery:
            return self.causal_ordering_check(other_clock, id_sender, orch_log)
        else:
            difference = 0
            for clock_index in range(len(self.clock_list)):
                first_value_clock = self.clock_list[clock_index]['value']
                second_value_clock = other_clock.clock_list[clock_index]['value']
                difference += abs(second_value_clock - first_value_clock)
            return difference

    def update_clock_with_a_string(self, other_vector_clock, orch_log):
        for clock_entry in self.clock_list:
            for other_clock_entry in other_vector_clock.clock_list:
                if clock_entry['id'] == other_clock_entry['id']:
                    my_value = clock_entry['value']
                    other_value = other_clock_entry['value']
                    max_value = max(my_value, other_value)
                    clock_entry['value'] = max_value
        orch_log.info('My clock after update: ' + str(self.as_string()))

    def update_clock(self, other_vector_clock, id_sender, orch_log=None):
        orch_log.info('My clock: ' + str(self.as_string()))
        orch_log.info('Other clock: ' + str(other_vector_clock.as_string()))
        for i in range(len(self.clock_list)):
            is_smaller_clock = self.clock_list[i]['value'] < other_vector_clock.clock_list[i]['value']
            if id_sender == self.clock_list[i]['id'] and is_smaller_clock:
                self.clock_list[i]['value'] = max(self.clock_list[i]['value'], other_vector_clock.clock_list[i]['value'])
        orch_log.info('Updated VT: ' + self.as_string())

    def as_string(self):
        str_log = 'VT: ['
        for clock in self.clock_list:
            str_log += str(clock['value']) + ','
        str_log += ']'
        return str_log

    def as_string_other(self, other):
        str_log = 'VT: ['
        for clock in other:
            str_log += str(clock['value']) + ','
        str_log += ']'
        return str_log

    def to_json_list(self):
        list_entries = list()
        for clock in self.clock_list:
            list_entries.append(str(clock['value']))
        list_as_string = ', '.join(list_entries)
        return list_as_string

    def check_single_difference(self, other_clock):
        differences = 0
        orchestrator_sender_id = ''
        for i in range(len(self.clock_list)):
            my_value = self.clock_list[i]['value']
            other_value = other_clock.clock_list[i]['value']
            if other_value > my_value and other_value == (my_value + 1):
                differences += 1
                orchestrator_sender_id = self.clock_list[i]['id']
        if differences == 1:
            return differences, orchestrator_sender_id
        return differences, ''

    def compare_stored_clock(self, other_clock, is_causal_delivery=False):
        if is_causal_delivery:
            return self.is_equal(other_clock) or self.causal_ordering_stored_check(other_clock)
        else:
            return True

    def causal_ordering_stored_check(self, other_clock):
        for index in range(len(other_clock.clock_list)):
            new_clock_value = other_clock.clock_list[index]['value']
            my_clock_value = self.clock_list[index]['value']
            if not (my_clock_value >= new_clock_value or my_clock_value + 1 == new_clock_value):
                return False
        return True

    def increment_clock(self, orchestrator_id):
        for clock in self.clock_list:
            if clock['id'] == orchestrator_id:
                clock['value'] += 1
                return
