def is_present(item, experiment_list):
    for exp_item in experiment_list:
        if exp_item == item:
            return True
    return False


def are_equal(item_val, item_exp):
    return item_val == item_exp


def is_valid_item(item):
    return item >= 50


# TODO: Work on this code, it could be simplified
def is_experiment_valid(experiment_size, valid_size):
    if experiment_size == 0 or valid_size == 0:
        return False
    if experiment_size < valid_size:
        return False
    return True


def compute_errors(experiment, valid):
    index_result = 0
    index_validation = 0
    errors = 0
    matches = 0
    while index_validation < len(valid):
        validation_item = valid[index_validation]
        experiment_item = experiment[index_result]
        if is_present(validation_item, experiment):
            if are_equal(validation_item, experiment_item):
                matches += 1
                index_validation += 1
                index_result += 1
            else:
                if is_valid_item(experiment_item):
                    index_result += 1
                else:
                    errors += 1
                    index_validation += 1
        else:
            errors += 1
            index_validation += 1
        if index_validation >= len(experiment):
            break
    error_score = len(experiment) - matches
    return error_score


def missing_elements(experiment, valid):
    repeated_missing_elements = []
    missing_elements_counter = 0
    for elem in valid:
        if elem not in experiment:
            if elem not in repeated_missing_elements:
                missing_elements_counter += 1
                repeated_missing_elements.append(elem)
    return missing_elements_counter


def main():
    experiment = [387, 1, 285, 10, 327, 28, 246, 4, 432, 7, 10, 327, 28, 246, 4, 432, 7, 28, 246, 4, 432, 7]
    valid = [387, 1, 285, 10, 327, 28, 4, 285, 10, 327, 28, 4]
    error_score = missing_elements(experiment, valid)
    print('Missing score: ', error_score)
    print('Length experiment: ', len(experiment))


if __name__ == main():
    main()
