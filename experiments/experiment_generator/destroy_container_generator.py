class DestroyContainerGenerator:

    def __init__(self, container_path):
        self.container_path = container_path
        self.file_container_orchestrator = open(self.container_path + "containers_orchestrator.sh", "r+")
        self.file_container_vnfs = open(self.container_path + "containers_vnfs.sh", "r+")
        self.file_destruction = open(self.container_path + "destroy_containers.sh", "w+")

    def generate_file(self):
        print('Begin destroy containers')
        self.write_first_line_to_file()
        self.set_up_orchestrators()
        self.write_new_line_to_file()
        self.set_up_vnfs_destruction()
        print('End destroy containers')

    def set_up_orchestrators(self):
        print('Setting orchestrators')
        new_line = '\n'
        for line in self.file_container_orchestrator:
            data_center = self.parse_for_data_center(line)
            if data_center != '\n':
                name = self.parse_for_name_orchestrator(line)
                first_string = 'vim-emu compute stop -d ' + data_center + ' -n ' + name
                self.file_destruction.write(first_string + new_line)
        print('Finish setting orchestrators')

    def set_up_vnfs_destruction(self):
        print('Setting vnfs')
        new_line = '\n'
        for line in self.file_container_vnfs:
            data_center = self.parse_for_data_center(line)
            if data_center != '\n':
                name = self.parse_for_name_vnf(line)
                print('Name: ', name)
                first_string = 'vim-emu compute stop -d ' + data_center + ' -n ' + name
                self.file_destruction.write(first_string + new_line)
        print('Finish setting vnfs')

    @staticmethod
    def parse_for_name_orchestrator(line):
        index = line.find('orch_')
        index_image = line.find('--image')
        sub_line = line[index:index_image]
        return sub_line

    @staticmethod
    def parse_for_name_vnf(line):
        index = line.find('vnf_')
        index_image = line.find('--image')
        sub_line = line[index:index_image]
        return sub_line

    def write_new_line_to_file(self):
        new_line = '\n'
        self.file_destruction.write(new_line)

    @staticmethod
    def parse_for_data_center(line):
        index = line.find('dc')
        sub_line = line[index:index+3]
        return sub_line

    def write_first_line_to_file(self):
        header = '#!/bin/sh'
        new_line = '\n'
        self.file_destruction.write(header + new_line)
        self.file_container_orchestrator.readline()
        self.file_container_vnfs.readline()


def main():
    print('Begin')
    length_of_vnfs = 4
    video_definition = 480
    container_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
    gen_exp = DestroyContainerGenerator(container_path)
    gen_exp.generate_file()


if __name__ == main():
    main()
