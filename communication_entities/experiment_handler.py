import asyncio
import json
import os
import subprocess

import aiohttp
from aiohttp import web
from aiohttp.web_response import Response


class ExperimentHandler:

    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self.current_directory = os.getcwd()
        self.list_of_orchestrators = []
        self.list_of_orchestrators.append({'host': '127.0.0.1',
                                           'port': 7037})
        self.list_of_orchestrators.append({'host': '127.0.0.1',
                                           'port': 7039})
        self.list_of_orchestrators.append({'host': '127.0.0.1',
                                           'port': 7041})
        self.list_of_orchestrators.append({'host': '127.0.0.1',
                                           'port': 7043})
        self.list_of_orchestrators.append({'host': '127.0.0.1',
                                           'port': 7045})

    async def index(self, request: web.Request) -> Response:
        return web.json_response('INDEX')

    async def info(self, request: web.Request) -> Response:
        return web.json_response('INFO')

    async def stop_orchestrator(self, request: web.Request) -> Response:
        try:
            print('Stopping orchestrator')
            data_raw = await request.json()
            data = json.loads(data_raw)

            orchestrator_number = data['orchestrator_number']
            port_number = -1

            if orchestrator_number == 0:
                port_number = '4437'
            elif orchestrator_number == 1:
                port_number = '4439'
            elif orchestrator_number == 2:
                port_number = '4441'
            elif orchestrator_number == 3:
                port_number = '4443'
            elif orchestrator_number == 4:
                port_number = '4445'

            # string_process = 'netstat -lpn | grep :7037'
            out = subprocess.check_output(["netstat", "-lpn", "|", "grep", str(port_number)])
            out_str = out.decode('UTF-8')
            processus_identifier = ''
            for line in out_str.split('\n'):
                if port_number in line:
                    line_split = line.split()
                    good_line = line_split[6]
                    index_score = good_line.find('/')
                    processus_identifier = good_line[0:index_score]
            subprocess.Popen(['kill', '-9', processus_identifier])
            answer = {'status': 'Good', 'result': 'Good!'}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def send_message_with_json(self, message):
        url = 'http://' + message['host'] + ':' + str(message['port']) + '/' + message['type']
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=message['data']) as resp:
                str_log_encoded = await (resp.text())

    # TODO: Implement this stub
    async def stop_all_orchestrators(self, data):
        print('Stoping all orchestrators')
        message = dict()
        message['type'] = 'stop_orchestrator'
        message['data'] = data
        concurrent_tasks = []
        for orchestrator in self.list_of_orchestrators:
            message['host'] = orchestrator['host']
            message['port'] = orchestrator['port']
            if message['port'] == 7037:
                data['orchestrator_number'] = 0
            elif message['port'] == 7039:
                data['orchestrator_number'] = 1
            elif message['port'] == 7041:
                data['orchestrator_number'] = 2
            elif message['port'] == 7043:
                data['orchestrator_number'] = 3
            elif message['port'] == 7045:
                data['orchestrator_number'] = 4
            concurrent_tasks.append(self.send_message_with_json(message))
        await asyncio.gather(*concurrent_tasks)

    # TODO: Implement this stub
    async def run_all_orchestrators(self, data):
        print('Run all orchestrators')
        message = dict()
        message['type'] = 'run_orchestrator'
        message['data'] = data
        concurrent_tasks = []
        for orchestrator in self.list_of_orchestrators:
            message['host'] = orchestrator['host']
            message['port'] = orchestrator['port']
            if message['port'] == 7037:
                data['orchestrator_number'] = 0
            elif message['port'] == 7039:
                data['orchestrator_number'] = 1
            elif message['port'] == 7041:
                data['orchestrator_number'] = 2
            elif message['port'] == 7043:
                data['orchestrator_number'] = 3
            elif message['port'] == 7045:
                data['orchestrator_number'] = 4
            concurrent_tasks.append(self.send_message_with_json(message))
        await asyncio.gather(*concurrent_tasks)

    async def run_common_code(self, data, experiment_number, test_string, algo_name):
        string_sleep_waiting_time = 'sleep ' + str(data['waiting_time'])
        subprocess.call(string_sleep_waiting_time, shell=True)
        string_argument_1 = str(experiment_number) + ' ' + str(data['number_of_updates']) + ' ' + algo_name + ' '
        string_argument_2 = str(data['max_delay']) + ' ' + str(data['repetition_probability']) + ' '
        string_argument_3 = str(test_string) + ' ' + ' ' + str(data['negation_probability'])
        string_arguments = string_argument_1 + string_argument_2 + string_argument_3
        string_results = 'python3 get_results_vnffg_updates.py ' + string_arguments
        subprocess.call(string_results, shell=True)
        subprocess.call(string_sleep_waiting_time, shell=True)
        await self.stop_all_orchestrators(data)

    async def run_causal_concurrent(self, data):
        algo_type = 0
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'causal'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_test(self, data, test_type):
        var_1 = 'global'
        if test_type == 0:
            print('Hello ')
            if data['experiment_type'] == var_1:
                print('./test_asynchronous_vnffg_updates_global.sh')
            else:
                print('./test_asynchronous_vnffg_updates_local.sh')
        else:
            print('Hello 2')
            if data['experiment_type'] == var_1:
                print('./test_sequential_vnffg_updates_global.sh')
            else:
                print('./test_sequential_vnffg_updates_local.sh')

    async def run_causal_sequential(self, data):
        algo_type = 0
        test_type = 1
        test_string = 'sequential'
        algo_name = 'causal'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_standard_concurrent(self, data):
        algo_type = 1
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'standard'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_standard_sequential(self, data):
        algo_type = 1
        test_type = 1
        test_string = 'sequential'
        algo_name = 'causal'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_preventive_concurrent(self, data):
        algo_type = 4
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'preventive'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_preventive_sequential(self, data):
        algo_type = 4
        test_type = 1
        test_string = 'sequential'
        algo_name = 'preventive'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_corrective_concurrent(self, data):
        algo_type = 5
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'corrective'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_corrective_sequential(self, data):
        algo_type = 5
        test_type = 1
        test_string = 'sequential'
        algo_name = 'corrective'
        data['algo_type'] = algo_type
        for experiment_number in range(0, data['experiment_repetitions']):
            await self.stop_all_orchestrators(data)
            await self.run_all_orchestrators(data)
            await self.run_test(data, test_type)
            await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_all_experiments_zero_touch(self, request: web.Request) -> Response:
        print('Hello')
        try:
            repetitions = 20
            number_of_updates = 150
            max_delay_array = [0.001, 0.1, 1.0]
            repetition_probability_array = [0, 5, 10]
            negation_probability_array = [0, 5, 10]
            data = dict()
            data['experiment_type'] = 'local'
            data['waiting_time'] = 30
            data['experiment_repetitions'] = 4

            for i in range(0, repetitions):
                data['number_of_updates'] = number_of_updates
                for max_delay in max_delay_array:
                    data['max_delay'] = max_delay
                    for repetition_probability in repetition_probability_array:
                        data['repetition_probability'] = repetition_probability
                        for negation_probability in negation_probability_array:
                            data['negation_probability'] = negation_probability
                            subprocess.call('sleep 3', shell=True)
                            await self.run_all_experiments(data)
                            break
                        break
                    break
                number_of_updates += 150
                break
            answer = {'status': 'Good', 'result': 'Good!'}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def run_all_experiments(self, data):
        print('Running all experiments')
        await self.run_causal_concurrent(data)
        await self.run_causal_sequential(data)
        print('Finish Causal')
        await self.run_standard_concurrent(data)
        await self.run_standard_sequential(data)
        print('Finish Sequential')
        await self.run_preventive_concurrent(data)
        await self.run_preventive_sequential(data)
        print('Finish preventive')
        await self.run_corrective_concurrent(data)
        await self.run_corrective_sequential(data)
        print('Finish corrective')

    async def run_orchestrator(self, request: web.Request) -> Response:
        try:
            data_raw = await request.json()
            data = json.loads(data_raw)
            current_directory = os.getcwd()

            experiment_number = data['experiment_number']
            number_of_updates = data['number_of_updates']
            max_delay = data['max_delay']
            repetition_probability = data['repetition_probability']
            algo_type = data['algo_type']
            negation_probability = data['negation_probability']
            orchestrator_number = data['orchestrator_number']

            str_0 = 'experiments/number_of_reconfigurations_'
            str_1 = '/experiment_' + str(experiment_number) + '/docker_files/docker_commands_'
            complete_file_new = str_0 + str(number_of_updates) + str_1 + str(orchestrator_number) + '.sh'
            print(complete_file_new)

            # Doing setup
            string_setup = current_directory + '/setup.sh ' + str(experiment_number) + ' ' + str(number_of_updates)
            subprocess.call(string_setup, shell=True)

            # Running docker yeah
            string_orch_1 = complete_file_new + ' ' + str(max_delay) + ' ' + str(repetition_probability) + ' '
            string_orch_2 = str(algo_type) + ' ' + str(negation_probability) + ' ' + str(number_of_updates) + ' &'
            string_launch_orchestrator = string_orch_1 + string_orch_2
            subprocess.call(string_launch_orchestrator, shell=True)
            answer = {'status': 'Good', 'result': 'Good!'}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)
