import json
import random
import string

import aiohttp

from utilities.logger import log
from utilities.random_integer_generation import generate_random_integer


def generate_number_of_updates(value):
    return generate_random_integer(0, value)


def generate_waiting_period():
    return generate_random_integer(0, 10)


def return_success() -> json:
    data = dict()
    data['success'] = True
    data['message'] = 'Ok'
    return data


def return_in_process(message):
    data = dict()
    data['success'] = True
    data['message'] = message
    return data


async def send_message(message):
    url = 'http://' + message.host + ':' + str(message.port) + '/' + message.type
    log.info(url)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=message.data) as resp:
            str_log_encoded = await (resp.text())
            log.info(str_log_encoded)


def return_failure(message):
    data = dict()
    data['success'] = False
    data['message'] = message
    return data


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
