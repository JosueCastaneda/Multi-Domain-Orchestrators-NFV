class VectorClock:

    def __init__(self, orchestrator_id):
        self.clock_list = list()
        self.add_clock(orchestrator_id)

    def add_clock(self, orchestrator_id):
        clock_dictionary = dict()
        clock_dictionary['id'] = orchestrator_id
        clock_dictionary['value'] = 0
        self.clock_list.append(clock_dictionary)
        self.clock_list = sorted(self.clock_list, key=lambda k: k['id'])
        # self.clock_list.sort(key=clock_dictionary['id'])

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

    def compare_clocks(self, other_clock, id_sender, is_causal_delivery=False):
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
                if id_sender == self.clock_list[i]['id']:
                    self.clock_list[i]['value'] += 1
        else:
            for clock in self.clock_list:
                for other_clock in other_vector_clock.clock_list:
                    if clock['id'] == other_clock['id'] and other_clock['value'] > clock['value']:
                        clock['value'] = other_clock['value']

    def compare_stored_clock(self, other_clock, is_causal_delivery=False):
        if is_causal_delivery:
            return self.causal_ordering_stored_check(other_clock)
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
