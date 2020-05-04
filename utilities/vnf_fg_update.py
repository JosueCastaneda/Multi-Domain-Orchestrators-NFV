from utilities.random_integer_generation import generate_random_integer
import random
import string


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
    name = ''
    for i in range(10):
        name += random.choice(letters)
    return name
