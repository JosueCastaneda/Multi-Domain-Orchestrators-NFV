from communication_entities.messages.migration_deactivate_message import MigrationDeactivateMessage
from entities.topology import Topology


def crete_new_vnf_from_topology(new_vnf_topology, new_vnf_ip):
    new_vnf = Topology(delay=new_vnf_topology[0],
                       bandwidth=new_vnf_topology[1],
                       loss=new_vnf_topology[2],
                       jitter=new_vnf_topology[3],
                       ip=new_vnf_ip,
                       port=4437)
    return new_vnf


def create_migration_deactivate_message(new_vnf, migrating_vnfs, host, ip):
    message = MigrationDeactivateMessage(new_vnf)
    migration_vnf = dict()
    migration_vnf['ip'] = host
    migration_vnf['mig_ip'] = ip
    message.migrating_vnfs.append(migration_vnf)
    if migrating_vnfs is not None:
        for vnf_mig in migrating_vnfs:
            message.migrating_vnfs.append(vnf_mig)
    return message