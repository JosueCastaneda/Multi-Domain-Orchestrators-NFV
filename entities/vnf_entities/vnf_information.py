from utilities.logger import log


class VnfInformation:

    def __init__(self,
                 host,
                 port,
                 name,
                 topology,
                 migration_ip,
                 topology_migration,
                 connection_points,
                 dependency_list,
                 unique_id):
        self.host = host
        self.port = port
        self.name = name
        self.topology = topology
        self.migration_ip = migration_ip
        self.topology_migration = topology_migration
        self.connection_points = connection_points
        self.dependency_list = dependency_list
        self.id = unique_id

    def print_information(self):
        str_log = 'VNF Name: ' \
                  + self.name \
                  + ' VNF Host: ' \
                  + self.host \
                  + ' Port: ' \
                  + str(self.port)
        log.info(str_log)
        log.info('Connection points: ')
        for cp in self.connection_points:
            log.info(''.join['Connection point: ', str(cp)])
        log.info('Dependency list: ')
        for dp in self.dependency_list:
            log.info(dp)
