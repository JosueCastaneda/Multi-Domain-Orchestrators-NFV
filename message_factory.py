import asyncio
import getopt
import json
import sys

import aiohttp

from utilities.logger import log

sys.path.append('../')

from entities.message_generator import MessageGenerator
from utilities.command_package import CommandPackage


def generate_messages(command):
    m = MessageGenerator(command, command.experiment)
    return m.generate_message()


def read_parameters(argv):
    command = CommandPackage()
    debug = False

    if debug:
        command.host = '127.0.0.1'
        command.port = 5002
        command.name = None
        command.new_name = None
        command.vnf_host = '127.0.0.1'
        command.vnf_port = 5002
        command.orchestrator_id = 'e5ea698b-8a3d-11ea-aa9d-04ea56f99520'
        command.message_type = 'request_sc'
        command.results = 'local'
        command.vnf_identifier = 'vnf1'
        command.order = '0'
        command.ingress_connection_point = 'x1'
        command.egress_connection_point = 'x2'

    try:
        str_var = "t:h:p:n:m:v:w:e:s:i:x:r:vi:or:icp:ecp:mi:ipp:sip:dip:sp:dp:"
        opts, args = getopt.getopt(argv, str_var,
                                   ["type=",
                                    "host=",
                                    "port=",
                                    "name=",
                                    "new_name=",
                                    "vnf_host=",
                                    "vnf_port=",
                                    "experiment=",
                                    "seed=",
                                    "service_id=",
                                    "orchestrator_id=",
                                    "results=",
                                    "vnf_identifier=",
                                    "order=",
                                    "ingress_connection_point=",
                                    "egress_connection_point=",
                                    "match_identifier=",
                                    "ip_proto=",
                                    "source_ip=",
                                    "destination_ip=",
                                    "source_port=",
                                    "destination_port="])
    except getopt.GetoptError:
        print(command.help_message)
        sys.exit(2)
    for opt, arg in opts:
        if debug:
            print("Option: ", opt, " Argument: ", arg)
        if opt in ("-h", "--host"):
            command.host = arg
        elif opt in ("-p", "--port"):
            command.port = int(arg)
        elif opt in ("-n", "--name"):
            command.name = arg
        elif opt in ("-m", "--new_name"):
            command.new_name = arg
        elif opt in ("-t", "--type"):
            command.message_type = arg
        elif opt in ("-v", "--vnf_host"):
            command.vnf_host = arg
        elif opt in ("-w", "--vnf_port"):
            command.vnf_port = arg
            print('VNF PORT: ' + arg)
        elif opt in ("-e", "--experiment"):
            str_exp = 'experiments/first/480/exp_1_8/experiments/experiment_' + arg + '.json'
            command.experiment = str_exp
        elif opt in ("-s", "--seed"):
            command.seed = arg
        elif opt in ("-i", "--service_id"):
            command.service_id = arg
        elif opt in ("-x", "--orchestrator_id"):
            command.orchestrator_id = arg
        elif opt in ("-r", "--results"):
            command.results = arg
        elif opt in ("-vi", "--vnf_identifier"):
            command.vnf_identifier = arg
        elif opt in ("-or", "--order"):
            command.order = arg
        elif opt in ("-icp", "--ingress_connection_point"):
            command.ingress_connection_point = arg
        elif opt in ("-ecp", "--egress_connection_point"):
            command.egress_connection_point = arg
        elif opt in ("-mi", "--match_identifier"):
            command.match_identifier = arg
        elif opt in ("-ipp", "--ip_proto"):
            command.ip_proto = arg
        elif opt in ("-sip", "--source_ip"):
            command.source_ip = arg
        elif opt in ("-dip", "--destination_ip"):
            command.destination_ip = arg
        elif opt in ("-sp", "--source_port"):
            command.source_port = arg
        elif opt in ("-dp", "--destination_port"):
            command.destination_port = arg
    return command


async def get_all_results():
    first = await get_results_external('40.127.108.223', 5001)
    second = await get_results_external('52.229.37.237', 5002)
    third = await get_results_external('52.141.61.172', 5003)
    fourth = await get_results_external('20.185.45.222', 5004)
    fifth = await get_results_external('52.151.70.54', 5005)
    total_inconsistencies = first[0] + second[0] + third[0] + fourth[0] + fifth[0]
    messages_sent = first[1] + second[1] + third[1] + fourth[1] + fifth[1]
    elapsed_time = first[2] + second[2] + third[2] + fourth[2] + fifth[2]

    str_result_1 = 'Inconsistencies: ' + str(total_inconsistencies)
    str_result_2 = ' messages sent: ' + str(messages_sent)
    str_result_3 = ' elapsed time: ' + str(elapsed_time) + ' seconds'
    print(str_result_1 + str_result_2 + str_result_3)


async def send_message(command, message):
    print(message)
    url = 'http://' + command.host + ':' + str(command.port) + '/' + command.message_type
    print(url)
    try:
        timeout = aiohttp.ClientTimeout(total=60)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url, data=message.data) as resp:
                print(resp.status)
                print(await resp.text())
    except asyncio.TimeoutError as e:
        log.error('Scaling timeout, requesting results: ')
        await get_results_external('40.127.108.223', 5001)
        await get_results_external('52.229.37.237', 5002)
        await get_results_external('52.141.61.172', 5003)
        await get_results_external('20.185.45.222', 5004)
        await get_results_external('52.151.70.54', 5005)
        log.error(e)


async def send_message_local(port):
    url = 'http://0.0.0.0:' + str(port) + '/'
    print(url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            print(await resp.text())


async def get_results_local(orchestrator_ip='127.0.0.1', orchestrator_port=5001):
    total_inconsistencies = 0
    initial_port = 5001
    for i in range(5):
        url = 'http://127.0.0.1:' + str(initial_port) + '/get_inconsistencies'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, data='') as resp:
                inconsistency_as_text = await resp.text()
                inconsistency_decoded = json.loads(inconsistency_as_text)
                total_inconsistencies += int(inconsistency_decoded['result'])
        initial_port += 1

    url = 'http://' + str(orchestrator_ip) + ':' + str(orchestrator_port) + '/get_time_elapsed'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, data='') as resp:
            elapsed_time_encoded = await resp.text()
    elapsed_time_decoded = json.loads(elapsed_time_encoded)
    elapsed_time = elapsed_time_decoded['result']

    url = 'http://' + str(orchestrator_ip) + ':' + str(orchestrator_port) + '/get_messages_sent'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, data='') as resp:
            messages_sent_encoded = await resp.text()
    messages_sent_decoded = json.loads(messages_sent_encoded)
    messages_sent = messages_sent_decoded['result']
    str_result_1 = 'Inconsistencies: ' + str(total_inconsistencies)
    str_result_2 = ' messages sent: ' + str(messages_sent)
    str_result_3 = ' elapsed time: ' + str(elapsed_time) + ' seconds'
    print(str_result_1 + str_result_2 + str_result_3)


async def get_results_external(orchestrator_ip='0.0.0.0', orchestrator_port=5001):
    total_inconsistencies = 0
    initial_port = 5001
    url_list = list()
    url_list.append('40.127.108.223')
    url_list.append('52.229.37.237')
    url_list.append('52.141.61.172')
    url_list.append('20.185.45.222')
    url_list.append('52.151.70.54')
    for i in range(5):
        url = 'http://' + str(url_list[i]) + ':' + str(initial_port) + '/get_inconsistencies'
        async with aiohttp.ClientSession() as session:
            async with session.get(url, data='') as resp:
                inconsistency_as_text = await resp.text()
                inconsistency_decoded = json.loads(inconsistency_as_text)
                total_inconsistencies += int(inconsistency_decoded['result'])
        initial_port += 1

    url = 'http://' + str(orchestrator_ip) + ':' + str(orchestrator_port) + '/get_time_elapsed'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, data='') as resp:
            elapsed_time_encoded = await resp.text()
    elapsed_time_decoded = json.loads(elapsed_time_encoded)
    elapsed_time = elapsed_time_decoded['result']

    url = 'http://' + str(orchestrator_ip) + ':' + str(orchestrator_port) + '/get_messages_sent'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, data='') as resp:
            messages_sent_encoded = await resp.text()
    messages_sent_decoded = json.loads(messages_sent_encoded)
    messages_sent = messages_sent_decoded['result']
    str_result_1 = 'Inconsistencies: ' + str(total_inconsistencies)
    str_result_2 = ' messages sent: ' + str(messages_sent)
    str_result_3 = ' elapsed time: ' + str(elapsed_time) + ' seconds'
    print(str_result_1 + str_result_2 + str_result_3)
    return [total_inconsistencies, messages_sent, elapsed_time]


async def main(argv):
    command = read_parameters(argv)
    if command.results:
        if command.results == 'local':
            await get_results_local(command.host, command.port)
            return
        elif command.results == 'external':
            await get_all_results()
            return
        elif command.results == 'test':
            await send_message_local(command.port)
            return

    if command.is_valid():
        messages = generate_messages(command)
        if isinstance(messages, list):
            for m in messages:
                await send_message(command, m)
        else:
            await send_message(command, messages)
    else:
        print(command.help_message)


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
