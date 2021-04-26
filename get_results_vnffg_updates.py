import asyncio
import csv
import json
import sys

from aiohttp import web

from communication_entities.messages.get_orchestrator_information import GetOrchestratorInformation
from communication_entities.messages.vnf_forwarding_graph.get_vnf_fg_message import GetVNFFGMessage
from definitions import ROOT_DIR
from utilities.life_cycle_management_update import send_message
from utilities.logger import *


def append_entry_result_to_file(exp_conf, results):
    directory_path = 'results/results_experiment_' + exp_conf['number_of_updates']
    csv_columns = ['inconsistencies', 'messages_sent', 'latency_per_operation', 'overhead_data_structure', 'overhead_per_message', 'number_of_reconfigurations', 'total_reconfiguration_time']
    str_1 = 'algorithm_*' + exp_conf['algorithm_type'] + '*_type_*' + exp_conf['save_type'] + '*_negationProbability_*' + exp_conf['probability_negation'] + '*_delay_*'
    str_2 = str(float(exp_conf['delay_time']) * 1000) + '*_repetitionProbability_*' + exp_conf['probability_repetitions'] + '*'
    name_file_extended = str_1 + str_2
    csv_file = directory_path + '/result_' + name_file_extended + '.csv'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
        except IOError:
            print("I/O error")
    try:
        if not os.path.isfile(csv_file):
            try:
                with open(csv_file, 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
            except IOError:
                print("I/O error")

        with open(csv_file, 'a+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for data in results:
                writer.writerow(data)
    except IOError:
        print("I/O error")


async def init_capture(experiment_file, experiment_configuration):
    app = web.Application()
    orchestrators_ips = load_orchestrators(experiment_file)
    unique_vnf_forwarding_graph_entry = list()
    inconsistencies = 0
    list_entry = list()
    experiment_entry = dict()
    experiment_entry['inconsistencies'] = 0
    experiment_entry['messages_sent'] = 0
    experiment_entry['overhead_data_structure'] = 0.0
    experiment_entry['latency_per_operation'] = 0.0
    experiment_entry['overhead_per_message'] = 0.0
    experiment_entry['number_of_reconfigurations'] = 0.0
    experiment_entry['total_reconfiguration_time'] = 0.0

    for orchestrator in orchestrators_ips:
        entry_result = await get_orchestrator_information(orchestrator)
        experiment_entry['inconsistencies'] += entry_result['inconsistencies']
        experiment_entry['messages_sent'] += entry_result['messages_sent']
        experiment_entry['overhead_data_structure'] += round(entry_result['overhead_data_structure'], 3)
        experiment_entry['latency_per_operation'] += round(entry_result['latency_per_operation'], 3)
        experiment_entry['overhead_per_message'] += round(entry_result['overhead_per_message'], 3)
        experiment_entry['number_of_reconfigurations'] += round(entry_result['number_of_reconfigurations'], 3)
        experiment_entry['total_reconfiguration_time'] += round(entry_result['total_reconfiguration_time'],3)
        new_vnf_forwarding_graph_list = await get_new_vnf_forwarding_graph_list_from_orchestrator(orchestrator)
        res = json.loads(new_vnf_forwarding_graph_list)
        unique_vnf_forwarding_graph_entry, new_inconsistencies = add_unique_vnf_forwarding_entry(
            unique_vnf_forwarding_graph_entry,
            res['result'])
        inconsistencies += new_inconsistencies
    experiment_entry['inconsistencies'] += inconsistencies
    list_entry.append(experiment_entry)
    append_entry_result_to_file(experiment_configuration, list_entry)
    exit()
    return app


def main():
    print(sys.argv)
    experiment_number = sys.argv[1]
    experiment_file = experiment_number
    number_of_updates = sys.argv[2]
    algorithm_type = sys.argv[3]
    delay_time = sys.argv[4]
    probability_repetitions = sys.argv[5]
    save_type = sys.argv[6]
    probability_negation = sys.argv[7]
    experiment_configuration = dict()
    experiment_configuration['number_of_updates'] = number_of_updates
    experiment_configuration['algorithm_type'] = algorithm_type
    experiment_configuration['delay_time'] = delay_time
    experiment_configuration['probability_repetitions'] = probability_repetitions
    experiment_configuration['save_type'] = save_type
    experiment_configuration['probability_negation'] = probability_negation

    server_host = '127.0.0.1'
    server_port = 4444
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_capture(experiment_file, experiment_configuration))
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
    file_path = ROOT_DIR + '/experiments/experiment_'+ str(experiment_number)
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
    return new_inconsistencies


def count_how_many_differences_between_connection_points(first, second):
    differences = 0
    if first['order'] != second['order']:
        differences += 1
    if first['ingress_connection_point'] != second['ingress_connection_point']:
        differences += 1
    if first['egress_connection_point'] != second['egress_connection_point']:
        differences += 1
    # TODO: This is because we have a different count
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
    # TODO: This is because we have a different count
    if differences > 1:
        differences = 1
    return differences


def get_old_entry_from_list(vnffg_entry, unique_vnf_forwarding_graph_entries):
    for old_entry in unique_vnf_forwarding_graph_entries:
        if old_entry['identifier'] == vnffg_entry['identifier']:
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
