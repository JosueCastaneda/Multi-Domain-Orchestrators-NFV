class MigrationConfiguration:

    def __init__(self, migration_vnf, topology_migration_vnf):
        self.migration_vnf = migration_vnf
        self.topology_migration_vnf = topology_migration_vnf

    def get_migration_vnf(self):
        return self.migration_vnf

    def get_topology_migration_vnf(self):
        return self.topology_migration_vnf
