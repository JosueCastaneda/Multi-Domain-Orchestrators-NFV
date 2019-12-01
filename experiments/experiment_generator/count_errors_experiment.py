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
    aciertos = 0
    # if is_experiment_valid(len(experiment), len(valid)):
    while index_validation < len(valid) :
        validation_item = valid[index_validation]
        experiment_item = experiment[index_result]
        if is_present(validation_item, experiment):
            if are_equal(validation_item, experiment_item):
                aciertos += 1
                index_validation += 1
                index_result += 1
            else:
                if is_valid_item(experiment_item):
                    index_validation += 1
                else:
                    errors += 1
                    index_validation += 1
        else:
            errors += 1
            index_validation += 1
        if index_validation > len(experiment):
            print('DSD')
            total_errors = errors + len(valid) - index_validation
            return total_errors, aciertos
    return errors, aciertos
    # return len(valid), 0


def main():
    experiment = [34, 37, 22, 168, 168]
    valid = [387, 1, 246, 4, 351, 22, 168, 37, 22, 22, 168, 37, 22, 327, 28, 1, 246, 4, 351, 22, 168, 37, 22, 22, 168, 37, 22, 327, 28, 10, 246, 4, 351, 22, 168, 37, 22, 22, 168, 37, 22, 327, 28, 351, 22, 168, 37, 22, 22, 168, 37, 22, 327, 28, 168, 37, 22, 10, 16]

    errores, aciertos = compute_errors(experiment, valid)
    print('Errores: ', errores)
    print('Aciertos: ', aciertos)

if __name__ == main():
    main()


