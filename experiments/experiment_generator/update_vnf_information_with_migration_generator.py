import json
import random


class UpdateVnfInformationWithMigrationGenerator:

    def __init__(self, vnf_info_path, experiment_path):
        self.vnf_info_path = vnf_info_path
        self.experiment_path = experiment_path
        self.migration_vnf_list = []
        self.vnf_list = []
        random.seed(5)

    def update_service(self):
        self.load_vnf_information()
        self.load_service_information()
        self.add_migration_to_vnfs()
        self.save_new_service_information_file()

    def add_migration_to_vnfs(self):
        random_indexes = self.generate_random_indexes()
        current_index = 0
        for vnf in self.vnf_list:
            random_vnf = self.migration_vnf_list[random_indexes[current_index]]
            vnf['migration_vnf_ip'] = random_vnf['server']
            current_index += 1
            print(vnf)
            print('Hello')

    def save_new_service_information_file(self):
        vnf_list = dict()
        vnf_list['vnf'] = self.vnf_list
        with open(self.experiment_path + 'vnf_info_migration.json', 'w') as json_file:
            json.dump(vnf_list, json_file)

    def load_vnf_information(self):
        with open(self.vnf_info_path) as json_file:
            raw_data = json.load(json_file)
            self.vnf_list = raw_data['vnf']

    def load_service_information(self):
        with open(self.experiment_path + 'migration_vnfs.json') as json_file:
            self.migration_vnf_list = json.load(json_file)

    def generate_random_indexes(self):
        return random.sample(range(len(self.migration_vnf_list)), len(self.vnf_list))


# def main():
#     print('Hello')
#     length_of_vnfs = 4
#     video_definition = 480
#     experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
#     vnf_info_path = 'vnf_info.json'
#     up_gen = UpdateVnfInformationWithMigrationGenerator(vnf_info_path, experiment_path)
#     up_gen.update_service()
#
#
# if __name__ == main():
#     main()
