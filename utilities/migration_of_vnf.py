import copy


def is_recursive_migration_required(new_vnf, previous_vnf, service_constraints):
    is_delay_valid = check_constraint(service_constraints['delay'], previous_vnf['delay'], new_vnf['delay'])
    is_loss_valid = check_constraint(service_constraints['loss'], previous_vnf['loss'], new_vnf['loss'])
    is_jitter_valid = check_constraint(service_constraints['jitter'], previous_vnf['jitter'], new_vnf['jitter'])
    is_bandwidth_valid = check_constraint(service_constraints['bandwidth'], previous_vnf['bandwidth'], new_vnf['bandwidth'])
    if is_bandwidth_valid and is_loss_valid and is_jitter_valid and is_delay_valid:
        return False
    return True


def check_constraint(constraint, previous, new):
    return (constraint + new - previous) <= constraint + (constraint * 0.3)


def exchange_queues_from_current_vnf_and_previous_vnf(current_vnf, previous_vnf):
    for val in previous_vnf['queue_p']:
        current_vnf['queue_p'].append(val)
    for val in previous_vnf['queue_q']:
        current_vnf['queue_q'].append(val)
    return current_vnf


def exchange_queues_from_current_vnf_and_new_vnf(current_vnf, new_vnf):
    for val in current_vnf['queue_p']:
        new_vnf['queue_p'].append(val)

    for val in current_vnf['queue_q']:
        new_vnf['queue_q'].append(val)

    for val in current_vnf['queue_r']:
        new_vnf['queue_r'].append(val)
    return new_vnf


def get_index_of_vnf_in_the_service(vnf, service):
    index = 0
    for server in service['host_servers']:
        if server == vnf['server']:
            return index
        index += 1
    return -1


def get_previous_vnf_from_service(index, service):
    return service['host_servers'][index]


def update_list_of_detailed_vnfs(current_vnf, new_vnf):
    new_vnf_copy = copy.deepcopy(new_vnf)
    current_vnf['queue_p'] = new_vnf_copy['queue_p']
    current_vnf['queue_q'] = new_vnf_copy['queue_q']
    current_vnf['queue_r'] = new_vnf_copy['queue_r']
    return current_vnf


def is_cycle_present(current_migration_list, previous_vnf):
    for vnf_in_migration in current_migration_list:
        if previous_vnf['operation'] == vnf_in_migration:
            return True
    return False
