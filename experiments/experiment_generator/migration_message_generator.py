import json
from utilities.json_parser import JsonParser


class MigrationMessageGenerator:

    def __init__(self, path, name_of_experiment):
        self.path = path
        self.name_experiment = name_of_experiment
        self.file_commands = open(self.path + 'migration_messages_' + self.name_experiment + '.sh', 'w+')
        # self.orchestrators = []
        self.migration_vnfs = []
        self.list_of_detailed_vnfs = []
        print('python message_factory.py -t migration -h 10.0.0.32 -p 5463 -n speed_up -m new -v none --vnf_port none')

    def generate(self):
        self.write_first_line_to_file()
        self.load_all_required_data()
        self.set_up_migration_messages()
        self.close_file()

    def set_up_migration_messages(self):
        new_line = '\n'
        for vnf_migration in self.migration_vnfs:
            for vnf in self.list_of_detailed_vnfs:
                if vnf['ip'] == vnf_migration:
                    first_str = 'python message_factory.py -t migration -h ' + vnf['orch_ip'] + ' -p '+ vnf['orch_port']
                    second_str = ' -n ' + vnf['name'] + ' -m new -v none --vnf_port none'
                    # test_str = first_str + second_str + new_line
                    self.file_commands.write(first_str + second_str + new_line)
                    break
            # self.write_new_line_to_file()
        print('Writing done!')

    def load_all_required_data(self):
        self.load_migration_vnfs()
        self.load_detailed_information_vnfs()

    def load_migration_vnfs(self):
        with open(self.path + self.name_experiment + '.json') as json_file:
            raw_data = json.load(json_file)
            self.migration_vnfs = raw_data['migrating_vnfs']

    def load_detailed_information_vnfs(self):
        file_container = open(self.path + 'docker_commands_' + self.name_experiment+'.sh', 'r+')
        for line in file_container:
            if 'mn.vnf' in line:
                vnf = dict()
                vnf['name'] = JsonParser.parse_for_name_vnf(line)
                vnf['orch_ip'] = JsonParser.parse_for_ip_orchestrator(line)
                vnf['orch_port'] = JsonParser.parse_for_port_orchestrator(line)
                vnf['ip'] = JsonParser.parse_for_ip_vnf(line)
                vnf['port'] = JsonParser.parse_for_port_vnf(line)
                self.list_of_detailed_vnfs.append(vnf)
        file_container.close()

    def write_new_line_to_file(self):
        new_line = '\n'
        self.file_commands.write(new_line)

    def write_first_line_to_file(self):
        header = '#!/bin/sh'
        new_line = '\n'
        self.file_commands.write(header + new_line)

    def close_file(self):
        self.file_commands.close()


def main():
    print('Begin')
    length_of_vnfs = 4
    video_definition = 480
    name_of_experiment = 'experiment_0'
    experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
    exp = MigrationMessageGenerator(path=experiment_path, name_of_experiment=name_of_experiment)
    exp.generate()

if __name__ == '__main__':
    main()
