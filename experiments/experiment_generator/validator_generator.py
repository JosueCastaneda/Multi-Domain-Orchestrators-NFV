import json
import copy


class ValidatorGenerator:

    def __init__(self, experiment_file_name, experiment_file_path):
        self.experiment_file_name = experiment_file_name
        self.experiment_file_path = experiment_file_path
        self.list_of_vnfs = []
        self.vnf_data = []
        self.experiment_data = []

    def load_experiment_data(self):
        with open(self.experiment_file_path + self.experiment_file_name + '.json') as json_file:
            raw_data = json.load(json_file)
            self.experiment_data = raw_data

    def load_vnf_data(self):
        string_info = '_vnf_info_final.json'
        with open(self.experiment_file_path + self.experiment_file_name + string_info) as json_file:
            raw_data = json.load(json_file)
            self.vnf_data = raw_data['vnf']

    def validate_experiment(self):
        self.load_vnf_data()
        self.load_experiment_data()
        for experiment in self.experiment_data['services']:
            first_vnf = True
            previous_vnf = None
            for operation in experiment['operations']:
                s_vnf = self.get_vnf_from_list(operation)
                vnf_internal = self.get_vnf_internal(operation)
                if vnf_internal is None:
                    if first_vnf:
                        vnf_internal = self.create(s_vnf)
                        first_vnf = False
                    else:
                        vnf_internal = self.create(s_vnf)
                        vnf_internal = self.extend_with_previous_vnf(vnf_internal, previous_vnf)
                    self.list_of_vnfs.append(vnf_internal)
                else:
                    if previous_vnf:
                        vnf_internal = self.extend_with_previous_vnf(vnf_internal, previous_vnf)
                previous_vnf = vnf_internal
        self.save_experiment()

    def get_vnf_from_list(self, operation):
        for vnf in self.vnf_data:
            if vnf['operation'] == operation:
                return vnf

    def get_vnf_internal(self, operation):
        for vnf in self.list_of_vnfs:
            if vnf['operation'] == operation:
                return vnf
        return None

    def save_experiment(self):
        file_name = self.experiment_file_path + self.experiment_file_name + '_validate.json'
        with open(file_name, 'w') as json_file:
            json.dump(self.list_of_vnfs, json_file)
        print('Saved validation file!')

    @staticmethod
    def create(vnf):
        vnf_internal = copy.deepcopy(vnf)
        return vnf_internal

    @staticmethod
    def extend_with_previous_vnf(vnf, previous_vnf):
        previous_vnf_copy = copy.deepcopy(previous_vnf)
        while previous_vnf_copy['queue_p']:
            vnf['queue_p'].append(previous_vnf_copy['queue_p'].pop(0))
        while previous_vnf_copy['queue_q']:
            vnf['queue_q'].append(previous_vnf_copy['queue_q'].pop(0))
        while previous_vnf_copy['queue_r']:
            vnf['queue_r'].append(previous_vnf_copy['queue_r'].pop(0))
        return vnf


# def main():
#     length_of_vnfs = 4
#     video_definition = 480
#     experiment_file = 'experiment_0'
#     experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
#     print('Begin valid generation')
#     val_gen = ValidatorGenerator(experiment_file, experiment_path)
#     val_gen.validate_experiment()
#     print('End valid generation')
#     with open(experiment_path + experiment_file + '_validate.json') as json_file:
#         parsed = json.load(json_file)
#     print(json.dumps(parsed, indent=2, sort_keys=True))
#
#
# if __name__ == "__main__":
#     main()
