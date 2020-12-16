import asyncio
import json

from aiohttp import web

from communication_entities.messages.vnf_forwarding_graph.get_vnf_fg_message import GetVNFFGMessage
from utilities.life_cycle_management_update import send_message
from utilities.logger import *


async def init_capture(experiment_file):
    app = web.Application()
    orchestrators_ips = load_orchestrators(experiment_file)
    unique_vnf_forwarding_graph_entry = list()
    inconsistencies = 0
    for orchestrator in orchestrators_ips:
        new_vnf_forwarding_graph_list = await get_new_vnf_forwarding_graph_list_from_orchestrator(orchestrator)
        res = json.loads(new_vnf_forwarding_graph_list)
        unique_vnf_forwarding_graph_entry, new_inconsistencies = add_unique_vnf_forwarding_entry(
            unique_vnf_forwarding_graph_entry,
            res['result'])
        inconsistencies += new_inconsistencies
    log.info('Inconsistencies: ' + str(inconsistencies))
    return app

def main():
    experiment_file = 0
    server_host = '127.0.0.1'
    server_port = 4444
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_capture(experiment_file))
    web.run_app(app, host=server_host, port=server_port)


async def get_new_vnf_forwarding_graph_list_from_orchestrator(orchestrator):
    data = dict()
    message = GetVNFFGMessage(orchestrator['ip'], orchestrator['port'], data)
    results = await send_message(message)
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
