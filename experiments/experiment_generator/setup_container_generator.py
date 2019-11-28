import json
import random


class SetupContainerGenerator:

    def __init__(self, number_of_domains, number_of_orchestrators, begin_ip, path):
        self.number_of_domains = number_of_domains
        self.number_of_orchestrators = number_of_orchestrators
        self.current_ip = begin_ip
        self.orchestrator_count = 1
        self.path = path
        self.file_orchestrator = open(self.path + "containers_orchestrator.sh", "w+")
        self.file_vnfs = open(self.path + "containers_vnfs.sh", "w+")
        self.number_of_vnfs = 2
        self.vnf_list = []
        random.seed(5)

    def close_file(self):
        self.file_orchestrator.close()
        self.file_vnfs.close()

    def write_new_line_to_file(self):
        new_line = '\n'
        self.file_orchestrator.write(new_line)
        self.file_vnfs.write(new_line)

    def generate_random_indexes(self):
        return random.randint(1, self.number_of_domains)

    def setup_containers(self):
        print('Begin setup containers')
        self.load_list_vnf()
        self.write_first_line_to_file()
        self.set_up_orchestrators()
        self.write_new_line_to_file()
        self.set_up_vnfs()
        self.close_file()
        print('End setup containers')

    def write_first_line_to_file(self):
        header = '#!/bin/sh'
        new_line = '\n'
        self.file_orchestrator.write(header + new_line)
        self.file_vnfs.write(header + new_line)

    def load_list_vnf(self):
        with open('vnf_info.json') as json_file:
            raw_data = json.load(json_file)
            self.vnf_list = raw_data['vnf']

    def set_up_orchestrators(self):
        data_center_index = 0
        new_line = '\n'
        print('Writing Orchestrators')
        for i in range(self.number_of_orchestrators):
            data_center = data_center_index + 1
            first_string = 'vim-emu compute start -d dc' + str(data_center) + ' -n orch_' + str(data_center)
            second_string = ' --image vnf_experiment --net '
            third_string = '\'(id=output,ip=10.0.0.' + str(self.current_ip) + '/24)\''
            self.file_orchestrator.write(first_string + second_string + third_string + new_line)
            self.current_ip += 2
            data_center_index += 1
            data_center_index %= self.number_of_domains
        print('Finish writing Orchestrators')

    def set_up_vnfs(self):
        print('Writing VNFS')
        new_line = '\n'
        for vnf in self.vnf_list:
            data_center = self.generate_random_indexes()
            first_string = 'vim-emu compute start -d dc' + str(data_center) + ' -n vnf_' + vnf['operation']
            second_string = ' --image vnf_experiment --net \'(id=input,ip=' + vnf['server'] + '/24)\''
            self.file_vnfs.write(first_string + second_string + new_line)
        print('Finish writing VNFS')


def main():
    number_of_domains = 2
    number_of_orchestrators = 4
    begin_ip = 30
    length_of_vnfs = 4
    video_definition = 480
    experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'

    exp_gen = SetupContainerGenerator(number_of_domains, number_of_orchestrators, begin_ip, experiment_path)
    exp_gen.setup_containers()


if __name__ == main():
    main()
