import json

from utilities.json_loader import JsonLoader
from utilities.migration_of_vnf import is_recursive_migration_required, \
    exchange_queues_from_current_vnf_and_previous_vnf, exchange_queues_from_current_vnf_and_new_vnf, \
    get_index_of_vnf_in_the_service, get_previous_vnf_from_service, update_list_of_detailed_vnfs, is_cycle_present


class UpdateServiceWithMigrationGenerator:

    def __init__(self, experiment_path, experiment_name):
        self.experiment_path = experiment_path
        self.experiment_name = experiment_name
        self.json_loader = JsonLoader(experiment_path, experiment_name)
        self.service_list, self.migrating_vnf_list = self.json_loader.load_service_information()
        self.list_vnf_detailed_information = self.json_loader.load_detailed_vnf_information()
        self.list_of_migration_vnfs = self.json_loader.load_list_of_migration_vnfs()
        self.list_of_vnf_topology = self.json_loader.load_list_of_vnf_topology()
        self.list_of_updated_vnfs = []
        self.already_migrated = []

    def handle_migration_of_vnf(self, current_vnf, current_migration_list):
        new_vnf = self.get_migration_vnf(current_vnf['migration_vnf_ip'])
        affected_vnfs = self.get_affected_vnfs(current_vnf)
        if len(affected_vnfs) > 0:
            for affected in affected_vnfs:
                previous_vnf = self.get_vnf_using_ip(affected['ip'])
                if not is_cycle_present(current_migration_list, previous_vnf):
                    if is_recursive_migration_required(new_vnf, previous_vnf, affected['service']):
                        self.handle_recursive_migration_of_vnf(current_migration_list, previous_vnf)
                current_vnf = exchange_queues_from_current_vnf_and_previous_vnf(current_vnf, previous_vnf)
                new_vnf = exchange_queues_from_current_vnf_and_new_vnf(current_vnf, new_vnf)
        else:
            new_vnf = exchange_queues_from_current_vnf_and_new_vnf(current_vnf, new_vnf)
        current_vnf = update_list_of_detailed_vnfs(current_vnf, new_vnf)
        self.already_migrated.append(current_vnf)
        return current_vnf

    def handle_recursive_migration_of_vnf(self, current_migration_list, previous_vnf):
        already_migrated = False
        for vnf_already in self.already_migrated:
            if vnf_already['server'] == previous_vnf['server']:
                already_migrated = True
                break
        if not already_migrated:
            print('Recursive migration')
            current_migration_list.append(previous_vnf['operation'])
            self.handle_migration_of_vnf(previous_vnf, current_migration_list)

    def add_migration_information_to_services(self):
        self.add_constraints_to_detailed_vnf_information()
        # self.compute_service_constraints()
        self.update_services_with_migration()
        self.save_updated_vnf_information()

    def update_services_with_migration(self):
        for ip in self.migrating_vnf_list:
            vnf = self.get_detailed_vnf(ip)
            if vnf is not None:
                vnf = self.handle_migration_of_vnf(vnf, [vnf['operation']])
                self.list_of_updated_vnfs.append(vnf)

    def add_constraints_to_detailed_vnf_information(self):
        with open(self.experiment_path + 'vnf_info.json') as json_file:
            raw_data = json.load(json_file)
            vnf_list =  raw_data['vnf']
        for index in range(len(vnf_list)):
            self.list_vnf_detailed_information[index]['delay'] = vnf_list[index]['delay']
            self.list_vnf_detailed_information[index]['loss'] = vnf_list[index]['loss']
            self.list_vnf_detailed_information[index]['jitter'] = vnf_list[index]['jitter']
            self.list_vnf_detailed_information[index]['bandwidth'] = vnf_list[index]['bandwidth']

    def get_vnf_topology(self, ip):
        for vnf in self.list_of_vnf_topology:
            if vnf['ip'] == ip:
                return vnf['topology']
        return None

    def save_updated_vnf_information(self):
        detailed_vnfs = dict()
        detailed_vnfs['vnf'] = self.list_vnf_detailed_information
        file_location = self.experiment_path + self.experiment_name
        with open(file_location + '_vnf_info_final' + '.json', 'w') as json_file:
            json.dump(detailed_vnfs, json_file)

    def get_detailed_vnf(self, ip):
        for vnf in self.list_vnf_detailed_information:
            if vnf['server'] == ip:
                return vnf
        return None

    def compute_service_constraints(self):
        for service in self.service_list:
            service_constraints = dict()
            service_constraints['delay'] = 0.0
            service_constraints['loss'] = 0.0
            service_constraints['bandwidth'] = 0.0
            service_constraints['jitter'] = 0.0
            for vnf_host in service['host_servers']:
                vnf_detail = self.get_vnf_topology(vnf_host)
                if vnf_detail is not None:
                    service_constraints['delay'] += float(vnf_detail[0])
                    service_constraints['bandwidth'] += float(vnf_detail[1])
                    service_constraints['loss'] += float(vnf_detail[2])
                    service_constraints['jitter'] += float(vnf_detail[3])
            service['constraints'] = service_constraints


    def update_previous_vnf(self, previous_vnf):
        for vnf in self.list_of_updated_vnfs:
            if vnf['server'] == previous_vnf['server']:
                previous_vnf['queue_p'] = vnf['queue_p']
                previous_vnf['queue_q'] = vnf['queue_q']
                previous_vnf['queue_r'] = vnf['queue_r']
        return previous_vnf

    def get_affected_vnfs(self, vnf):
        affected_vnfs = []
        for service in self.service_list:
            index_vnf = get_index_of_vnf_in_the_service(vnf, service)
            if index_vnf >= 1:
                affected = get_previous_vnf_from_service(index_vnf - 1, service)
                if affected is not None:
                    affected_vnf= dict()
                    affected_vnf['ip'] = affected
                    affected_vnf['service'] = service['constraints']
                    affected_vnfs.append(affected_vnf)
        return affected_vnfs

    def get_vnf_using_ip(self, ip):
        for vnf in self.list_vnf_detailed_information:
            if vnf['server'] == ip:
                vnf = self.update_previous_vnf(vnf)
                return vnf
        return None

    def get_migration_vnf(self, server):
        for vnf in self.list_of_migration_vnfs:
            if vnf['server'] == server:
                return vnf
        return None


# def main():
#     length_of_vnfs = 4
#     video_definition = 480
#     experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
#     experiment_name = 'experiment_0'
#     up_service = UpdateServiceWithMigrationGenerator(experiment_path, experiment_name)
#     up_service.add_migration_information_to_services()
#     with open(experiment_path + experiment_name + '_vnf_info_final.json') as json_file:
#         parsed = json.load(json_file)
#     print(json.dumps(parsed, indent=2, sort_keys=True))
#     print('Finish creating up experiment!')


# if __name__ == main():
#     main()
