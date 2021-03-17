import asyncio
import csv
import json
import sys

from aiohttp import web

from communication_entities.messages.get_orchestrator_information import GetOrchestratorInformation
from communication_entities.messages.vnf_forwarding_graph.get_vnf_fg_message import GetVNFFGMessage
from utilities.life_cycle_management_update import send_message
from utilities.logger import *


def append_entry_result_to_file(experiment_file, results, algorithm_type):
    directory_path = 'results/results_experiment_' + str(experiment_file)
    csv_columns = ['inconsistencies', 'messages_sent', 'time_for_experimentation']
    csv_file = directory_path + '/result_' + algorithm_type + '.csv'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
        except IOError:
            print("I/O error")
    try:
        with open(csv_file, 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for data in results:
                writer.writerow(data)
    except IOError:
        print("I/O error")


async def init_capture(experiment_file, number_of_updates, algorithm_type):
    app = web.Application()
    # print(experiment_file)
    # print(number_of_updates)
    # await test_all_and_save()
    orchestrators_ips = load_orchestrators(experiment_file)
    unique_vnf_forwarding_graph_entry = list()
    inconsistencies = 0
    list_entry = list()
    experiment_entry = dict()
    experiment_entry['inconsistencies'] = 0
    experiment_entry['messages_sent'] = 0
    experiment_entry['time_for_experimentation'] = 0
    for orchestrator in orchestrators_ips:
        entry_result = await get_orchestrator_information(orchestrator)
        experiment_entry['inconsistencies'] += entry_result['inconsistencies']
        experiment_entry['messages_sent'] += entry_result['messages_sent']
        experiment_entry['time_for_experimentation'] += round(entry_result['total_time_for_experimentation'], 3)
        new_vnf_forwarding_graph_list = await get_new_vnf_forwarding_graph_list_from_orchestrator(orchestrator)
        res = json.loads(new_vnf_forwarding_graph_list)
        unique_vnf_forwarding_graph_entry, new_inconsistencies = add_unique_vnf_forwarding_entry(
            unique_vnf_forwarding_graph_entry,
            res['result'])
        inconsistencies += new_inconsistencies
    experiment_entry['inconsistencies'] += inconsistencies
    log.info('Result: ')
    log.info(experiment_entry)
    list_entry.append(experiment_entry)
    append_entry_result_to_file(number_of_updates, list_entry, algorithm_type)
    return app


def main():

    experiment_number = sys.argv[1]
    print(f'Sending test email to {experiment_number}')
    experiment_file = experiment_number
    number_of_updates = 4
    algorithm_type = 'standard'
    server_host = '127.0.0.1'
    server_port = 4444
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_capture(experiment_file, number_of_updates, algorithm_type))
    web.run_app(app, host=server_host, port=server_port)

async def get_new_vnf_forwarding_graph_list_from_orchestrator(orchestrator):
    data = dict()
    message = GetVNFFGMessage(orchestrator['ip'], orchestrator['port'], data)
    results = await send_message(message)
    return results


async def get_orchestrator_information(orchestrator):
    data = dict()
    message = GetOrchestratorInformation(orchestrator['ip'], orchestrator['port'], data)
    raw_results = await send_message(message)
    results = json.loads(raw_results)
    return results

def load_orchestrators(experiment_number):
    base_dir = os.path.dirname(__file__)
    file_path = base_dir + '/experiments/experiment_'+ str(experiment_number)
    file_name = '/experiment_' + str(experiment_number) + '.json'
    complete_file_path_name = file_path + file_name
    with open(complete_file_path_name ) as json_file:
        raw_data = json.load(json_file)
    return raw_data['orchestrators']

def get_inconsistencies_from_entry(first_entry, second_entry):
    new_inconsistencies = 0
    number_of_elements = len(first_entry['rendered_service_paths'][0]['vnf_descriptor_connection_points'])
    for index in range(0, number_of_elements):
        first_connection_entry = first_entry['rendered_service_paths'][0]['vnf_descriptor_connection_points'][index]
        second_connection_entry = second_entry['rendered_service_paths'][0]['vnf_descriptor_connection_points'][index]
        new_inconsistencies += count_how_many_differences_between_connection_points(first_connection_entry,
                                                                                    second_connection_entry)

        first_connection_entry = first_entry['classification_rules'][0]['matching_attributes'][index]
        second_connection_entry = second_entry['classification_rules'][0]['matching_attributes'][index]
        new_inconsistencies += count_how_many_differences_between_matching_attributes(first_connection_entry,
                                                                                      second_connection_entry)
        sum_lol = 0
        # if new_inconsistencies == 10:
        #     print('Inconsistentencies: ' + str(new_inconsistencies))
    return new_inconsistencies

def count_how_many_differences_between_connection_points(first, second):
    differences = 0
    if first['order'] != second['order']:
        differences += 1
    if first['ingress_connection_point'] != second['ingress_connection_point']:
        differences += 1
    if first['egress_connection_point'] != second['egress_connection_point']:
        differences += 1
    # TODO: This change was done to correspond to the code that computes inconsistencies so all equal 1
    if differences > 1:
        differences = 1
    return differences


def count_how_many_differences_between_matching_attributes(first, second):
    differences = 0
    if first['ip_proto'] != second['ip_proto']:
        differences += 1
    if first['source_ip'] != second['source_ip']:
        differences += 1
    if first['destination_ip'] != second['destination_ip']:
        differences += 1
    if first['source_port'] != second['source_port']:
        differences += 1
    if first['destination_port'] != second['destination_port']:
        differences += 1
    if differences > 1:
        differences = 1
    return differences


def get_old_entry_from_list(vnffg_entry, unique_vnf_forwarding_graph_entries):
    for old_entry in unique_vnf_forwarding_graph_entries:
        if old_entry['identifier'] == vnffg_entry['identifier']:
            # log.info('Found the same identifier: ' + str(old_entry['identifier']))
            return old_entry
    return None

def add_unique_vnf_forwarding_entry(unique_vnf_forwarding_graph_entries, new_vnf_forwarding_graph_list):
    new_inconsistencies = 0
    for vnffg_entry in new_vnf_forwarding_graph_list:
        old_entry = get_old_entry_from_list(vnffg_entry, unique_vnf_forwarding_graph_entries)
        if old_entry is None:
            unique_vnf_forwarding_graph_entries.append(vnffg_entry)
        else:
            new_inconsistencies += get_inconsistencies_from_entry(vnffg_entry, old_entry)
    return unique_vnf_forwarding_graph_entries, new_inconsistencies


if __name__ == "__main__":
    main()