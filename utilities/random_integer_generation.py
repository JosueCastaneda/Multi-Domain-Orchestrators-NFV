import random
import uuid


def generate_random_integer(low, high):
    return random.randint(low, high)


def generate_unique_identifier():
    return str(uuid.uuid1())


def generate_random_seeds(number, number_of_services):
    directory_path = 'random_seeds/size_' + str(number)
    random_seed_list = []
    random_np_seed_list = []
    file = open(directory_path + '/seed_list.txt', 'r')
    file_np = open(directory_path + '/np_seed_list.txt', 'r')
    counter = 0
    for line in file:
        # if counter >= number_of_services:
        #     counter = 0
        #     break
        random_seed_list.append(int(line))
        counter += 1

    for line in file_np:
        # if counter >= number_of_services:
        #     break
        random_np_seed_list.append(int(line))
        counter += 1
    return random_seed_list, random_np_seed_list


def generate_random_index_from_vnf_components(vnf_components, service):
    index = generate_random_integer(0, len(vnf_components) - 1)
    number_of_trials = 0
    while is_new_index_invalid(vnf_components[index], service) and number_of_trials < 10:
        index = generate_random_integer(0, len(vnf_components) - 1)
        number_of_trials += 1
    if number_of_trials >= 10:
        return None
    return index


def is_new_index_invalid(new_vnf_component, service):
    is_unique = service.is_new_vnf_component_unique(new_vnf_component)
    if is_unique:
        if new_vnf_component.type == 'VNF':
            return False
        return service.is_new_vnf_component_in_a_loop(new_vnf_component)
    return True
