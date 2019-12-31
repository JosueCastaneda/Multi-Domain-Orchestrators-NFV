import os
import pickle
import random
import string

from utilities.logger import log
from utilities.random_integer_generation import generate_random_integer


def generate_number_of_updates(value):
    return generate_random_integer(0, value)


def generate_waiting_period():
    return generate_random_integer(0, 10)


def generate_index_to_change():
    return generate_random_integer(1, 2)


def generate_index_to_change_by_value(value):
    return generate_random_integer(0, value)


def generate_random_orchestrator_index():
    return generate_random_integer(0, 3)


def generate_random_string_value():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


def save_update_time(total_time):
    if not os.path.exists('time_update.txt'):
        file = open('time_update.txt', 'w+')
    else:
        file = open('time_update.txt', 'a')
    file.write(str(total_time))
    file.write('\n')
    file.close()


def save_migration_time(total_time):
    log.info('Saving migration time')
    pickle.dump(total_time, open('migration_time.p', 'wb'))