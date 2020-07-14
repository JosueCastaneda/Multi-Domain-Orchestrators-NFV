import json

from utilities.logger import log


class VectorClock(dict):

    def __init__(self, orchestrator_id=''):
        super().__init__()
        self.clock_list = list()
        if orchestrator_id != '':
            self.add_clock(orchestrator_id)

    def create_from_list(self, vector_string) -> None:
        vector_without_brackets = vector_string.strip('][').split(',')
        correct_index = 0
        for i in range(int(len(vector_without_brackets)/2)):
            id_string = vector_without_brackets[correct_index].strip('"{id":" "')
            id_value = vector_without_brackets[correct_index + 1].strip(' "value":}')
            self.add_clock(id_string, int(id_value))
            correct_index += 2

    def to_json(self):
        return json.dumps(self.clock_list, default=lambda o: o.__dict__)

    def add_clock(self, orchestrator_id, value=0):
        clock_dictionary = dict()
        clock_dictionary['id'] = orchestrator_id
        clock_dictionary['value'] = value
        self.clock_list.append(clock_dictionary)
        self.clock_list = sorted(self.clock_list, key=lambda k: k['id'])

    def causal_ordering_check(self, other_clock, id_sender):
        for index in range(len(other_clock.clock_list)):
            if id_sender == other_clock.clock_list[index]['id']:
                new_clock_value = other_clock.clock_list[index]['value']
                my_clock_value = self.clock_list[index]['value']
                respect_fifo_order = self.check_fifo_order(new_clock_value, my_clock_value)
                respect_transitive_causal_order = self.check_transitive_causal_order(other_clock.clock_list, index)
                if respect_fifo_order and respect_transitive_causal_order:
                    return 0
                return 2
        return 100

    def check_transitive_causal_order(self, new_clock_list, invalid_index):
        for index in range(len(self.clock_list)):
            if index != invalid_index and new_clock_list[index]['value'] > self.clock_list[index]['value']:
                return False
        return True

    def check_fifo_order(self, new_value, my_value):
        return new_value == my_value + 1
        # return new_value == self.clock_list[id_sender]['value'] + 1

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
            if my_value < other_value:
                return False
        return True

    def compare_clocks(self, other_clock, id_sender, is_causal_delivery=False):
        if self.is_equal(other_clock):
            return 0
        if self.is_greater_than_other(other_clock):
            return 0
        if is_causal_delivery:
            return self.causal_ordering_check(other_clock, id_sender)
        else:
            difference = 0
            for clock_index in range(len(self.clock_list)):
                first_value_clock = self.clock_list[clock_index]['value']
                second_value_clock = other_clock.clock_list[clock_index]['value']
                difference += abs(second_value_clock - first_value_clock)
            return difference

    def update_clock(self, other_vector_clock, id_sender, is_causal_delivery=False):
        if is_causal_delivery:
            for i in range(len(self.clock_list)):
                if id_sender == self.clock_list[i]['id'] and self.clock_list[i]['value'] < other_vector_clock.clock_list[i]['value']:
                    self.clock_list[i]['value'] += 1
        else:
            for clock in self.clock_list:
                for other_clock in other_vector_clock.clock_list:
                    if clock['id'] == other_clock['id'] and other_clock['value'] > clock['value']:
                        clock['value'] = other_clock['value']
        log.info('Updated VT: ' + self.as_string())

    def as_string(self):
        str_log = 'VT: ['
        for clock in self.clock_list:
            str_log += str(clock['value']) + ','
        str_log += ']'
        return str_log

    def check_single_difference(self, other_clock):
        differences = 0
        orchestrator_sender_id = ''
        for i in range(len(self.clock_list)):
            my_value = self.clock_list[i]['value']
            other_value = other_clock.clock_list[i]['value']
            if other_value > my_value and other_value == (my_value + 1):
                differences+=1
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
