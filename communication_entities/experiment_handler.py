import asyncio
import json
import os
import subprocess
from sys import platform

import aiohttp
from aiohttp import web
from aiohttp.web_response import Response


class ExperimentHandler:

    def __init__(self, is_master=False):
        self._loop = asyncio.get_event_loop()
        self.current_directory = os.getcwd()
        self.list_of_orchestrators = []
        self.list_of_orchestrators.append({'host': '13.91.23.61',
                                           'port': 7037})
        self.list_of_orchestrators.append({'host': '40.81.204.178',
                                           'port': 7039})
        self.list_of_orchestrators.append({'host': '20.84.67.101',
                                           'port': 7041})
        self.list_of_orchestrators.append({'host': '20.68.168.123',
                                           'port': 7043})
        self.list_of_orchestrators.append({'host': '52.231.152.194',
                                           'port': 7045})
        self.single_execution = 0
        self.is_master = is_master

    async def index(self, request: web.Request) -> Response:
        return web.json_response('INDEX')

    async def info(self, request: web.Request) -> Response:
        return web.json_response('INFO')

    async def stop_orchestrator(self, request: web.Request) -> Response:
        try:
            print('Stopping orchestrator')
            data_raw = await request.json()
            data = json.loads(data_raw)
            print('Data is loaded...')

            orchestrator_number = data['orchestrator_number']
            port_number = -1

            # list_of_ports_for_vnfs = [3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010]
            # extra_list = []
            print('List of VNFs')
            if orchestrator_number == 0:
                port_number = '4437'
            elif orchestrator_number == 1:
                port_number = '4439'
                # extra_list = [3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020]
            elif orchestrator_number == 2:
                port_number = '4441'
                # extra_list = [3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030]
            elif orchestrator_number == 3:
                port_number = '4443'
                # extra_list = [3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040]
            elif orchestrator_number == 4:
                port_number = '4445'
                # extra_list = [3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050]
            # list_of_ports_for_vnfs.extend(extra_list)

            # print('Stoping the orchestrator')
            print('Stoping orchestrator')

            found_process = False
            if platform == "linux" or platform == "linux2":
                out = subprocess.check_output(["netstat", "-lpn", "|", "grep", str(port_number)])
                out_str = out.decode('UTF-8')
                for line in out_str.split('\n'):
                    if port_number in line:
                        line_split = line.split()
                        line_split_port_with_port = line_split[3]
                        line_split_port_with_port_split = line_split_port_with_port.split(':')
                        my_port_number = line_split_port_with_port_split[1]
                        if str(my_port_number) == str(port_number):
                            good_line = line_split[6]
                            index_score = good_line.find('/')
                            processus_identifier = good_line[0:index_score]
                            print('Stoping...')
                            subprocess.Popen(['kill', '-9', processus_identifier])
                            found_process = True
                            print('Stopped...')
                    if found_process:
                        break
            elif platform == "darwin":
                out = subprocess.check_output(["netstat", "-anv", "|", "grep", str(port_number)])
                out_str = out.decode('UTF-8')
                print('Now checking lines..')
                for line in out_str.split('\n'):
                    if port_number in line:
                        line_split = line.split()
                        line_with_port = line_split[3]
                        line_with_port_split = line_with_port.split('.')
                        port_line = line_with_port_split[4]
                        if port_line == port_number:
                            print(line_with_port)
                            good_line = line_split[8]
                            processus_identifier = good_line
                            print('Stopping...')
                            subprocess.Popen(['kill', '-9', processus_identifier])
                            print('Stopped...')
                        # break


            # print('Stoping the VNF')
            #
            # for vnf_port in list_of_ports_for_vnfs:
            #     if platform == "linux" or platform == "linux2":
            #         out = subprocess.check_output(["netstat", "-lpn", "|", "grep", str(vnf_port)])
            #     if platform == "darwin":
            #         out = subprocess.check_output(["netstat", "-anv", "|", "grep", str(vnf_port)])
            #     out_str = out.decode('UTF-8')
            #     processus_identifier = ''
            #     for line in out_str.split('\n'):
            #         if port_number in line:
            #             line_split = line.split()
            #             if platform == "linux" or platform == "linux2":
            #                 good_line = line_split[6]
            #                 index_score = good_line.find('/')
            #                 processus_identifier = good_line[0:index_score]
            #             elif platform == "darwin":
            #                 good_line = line_split[8]
            #                 processus_identifier = good_line
            #     subprocess.Popen(['kill', '-9', processus_identifier])
            # print('Finish with all')

            answer = {'status': 'Good', 'result': 'Good!'}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def send_message_with_json(self, message):
        url = 'http://' + message['host'] + ':' + str(message['port']) + '/' + message['type']
        print(url)
        data_encoded = json.dumps(message['data'])
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data_encoded) as resp:
                str_log_encoded = await (resp.text())
                print(str_log_encoded)

    # TODO: Implement this stub
    async def stop_all_orchestrators(self, data):
        print('Stoping all orchestrators')
        # concurrent_tasks = []
        for orchestrator in self.list_of_orchestrators:
            message = dict()
            message['type'] = 'stop_orchestrator'
            message['data'] = data
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
            await self.send_message_with_json(message)
            # concurrent_tasks.append(self.send_message_with_json(message))
        # await asyncio.gather(*concurrent_tasks)

    # TODO: Implement this stub
    async def run_all_orchestrators(self, data):
        print('Run all orchestrators')
        concurrent_tasks = []
        for orchestrator in self.list_of_orchestrators:
            message = dict()
            message['type'] = 'run_orchestrator'
            message['data'] = data
            message['host'] = orchestrator['host']
            message['port'] = orchestrator['port']
            if message['port'] == 7037:
                message['data']['orchestrator_number'] = 0
            elif message['port'] == 7039:
                message['data']['orchestrator_number'] = 1
            elif message['port'] == 7041:
                message['data']['orchestrator_number'] = 2
            elif message['port'] == 7043:
                message['data']['orchestrator_number'] = 3
            elif message['port'] == 7045:
                message['data']['orchestrator_number'] = 4
            await self.send_message_with_json(message)
            # concurrent_tasks.append(self.send_message_with_json(message))

        # print('Data for all')
        # await asyncio.gather(*concurrent_tasks)

    # await self.run_common_code(data, experiment_number, test_string, algo_name)
    async def run_common_code(self, data, experiment_number, test_string, algo_name):
        string_sleep_waiting_time = 'sleep ' + str(data['waiting_time'])
        subprocess.call(string_sleep_waiting_time, shell=True)
        # string_argument_1 = str(experiment_number) + ' ' + str(data['number_of_updates']) + ' ' + algo_name + ' '
        string_argument_1 = str(experiment_number) + ' ' + str(data['number_of_updates']) + ' ' + str(data['algo_name']) + ' '
        string_argument_2 = str(data['max_delay']) + ' ' + str(data['repetition_probability']) + ' '
        # string_argument_3 = str(test_string) + ' ' + ' ' + str(data['negation_probability'])
        string_argument_3 = str(data['test_string']) + ' ' + str(data['negation_probability'])
        string_arguments = string_argument_1 + string_argument_2 + string_argument_3
        string_results = 'python3 get_results_vnffg_updates.py ' + string_arguments
        print(string_results)
        print('Getting results and saving them...')
        subprocess.call(string_results, shell=True)
        print('Results are saved!')
        subprocess.call(string_sleep_waiting_time, shell=True)
        print('Trying to stop')
        await self.stop_all_orchestrators(data)
        print('Stopped?')

    async def run_causal_concurrent(self, data):
        algo_type = 0
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'causal'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_all_experiments_from_algorithm(self, data, algo_type, test_type, algo_name, test_string):
        data['algo_type'] = algo_type
        data['algo_name'] = algo_name
        data['test_string'] = test_string
        # for experiment_number in range(0, data['experiment_repetitions']):
        for experiment_number in range(0, 1):
            data['experiment_number'] = experiment_number
            await self.run_experiment(data, experiment_number, test_string, algo_name, test_type)

    async def run_experiment(self, data, experiment_number, test_string, algo_name, test_type):
        waiting_time_string = 'sleep ' + str(data['waiting_time'])
        await self.stop_all_orchestrators(data)
        await self.run_all_orchestrators(data)
        subprocess.call(waiting_time_string, shell=True)
        await self.run_test(data, test_type)
        print('Running common code')

        #         test_string = 'sequential'
        #         algo_name = 'causal'
        await self.run_common_code(data, experiment_number, test_string, algo_name)

    async def run_test(self, data, test_type):
        var_1 = 'global'
        if test_type == 0:
            if data['experiment_type'] == var_1:
                print('./test_asynchronous_vnffg_updates_global.sh')
                subprocess.call('sleep 20', shell=True)
                subprocess.call('./test_asynchronous_vnffg_updates_global.sh', shell=True)
            else:
                print('./test_asynchronous_vnffg_updates_local.sh')
                subprocess.call('sleep 20', shell=True)
                subprocess.call('./test_asynchronous_vnffg_updates_local.sh', shell=True)
        else:
            if data['experiment_type'] == var_1:
                print('./test_sequential_vnffg_updates_global.sh')
                subprocess.call('sleep 20', shell=True)
                subprocess.call('./test_sequential_vnffg_updates_global.sh', shell=True)
            else:
                print('./test_sequential_vnffg_updates_local.sh')
                subprocess.call('sleep 20', shell=True)
                subprocess.call('./test_sequential_vnffg_updates_local.sh', shell=True)

    async def run_causal_sequential(self, data):
        algo_type = 0
        test_type = 1
        test_string = 'sequential'
        algo_name = 'causal'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_standard_concurrent(self, data):
        algo_type = 1
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'standard'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_standard_sequential(self, data):
        algo_type = 1
        test_type = 1
        test_string = 'sequential'
        algo_name = 'standard'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_preventive_concurrent(self, data):
        algo_type = 4
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'preventive'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_preventive_sequential(self, data):
        algo_type = 4
        test_type = 1
        test_string = 'sequential'
        algo_name = 'preventive'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_corrective_concurrent(self, data):
        algo_type = 5
        test_type = 0
        test_string = 'concurrent'
        algo_name = 'corrective'
        data['algo_type'] = algo_type
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_corrective_sequential(self, data):
        algo_type = 5
        test_type = 1
        test_string = 'sequential'
        algo_name = 'corrective'
        await self.run_all_experiments_from_algorithm(data, algo_type, test_type, algo_name, test_string)

    async def run_all_experiments_zero_touch(self, request: web.Request) -> Response:
        try:
            repetitions = 20
            number_of_updates = 150
            max_delay_array = [0.001, 0.1, 1.0]
            repetition_probability_array = [0, 5, 10]
            negation_probability_array = [0, 5, 10]
            data = dict()
            data['experiment_type'] = 'global'
            data['waiting_time'] = 20
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
                        print('Updating repetition_probability')
                    print('Updating Max_delay')
                number_of_updates += 150
            answer = {'status': 'Good', 'result': 'Good!'}
            # return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            # return web.json_response(response)

    async def run_all_experiments(self, data):
        await self.run_causal_concurrent(data)
        await self.run_causal_sequential(data)
        await self.run_standard_concurrent(data)
        await self.run_standard_sequential(data)
        await self.run_preventive_concurrent(data)
        await self.run_preventive_sequential(data)
        await self.run_corrective_concurrent(data)
        await self.run_corrective_sequential(data)
        print('Finish running all experiments')

    async def run_orchestrator(self, request: web.Request) -> Response:
        # print('Running orchestrators.....')
        try:
            # print('Loading data')
            data_raw = await request.json()
            data = json.loads(data_raw)
            # print('Loaded data')
            current_directory = os.getcwd()
            # print(data)

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
            print(string_launch_orchestrator)
            subprocess.call(string_launch_orchestrator, shell=True)
            answer = {'status': 'Good', 'result': 'Good!'}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)
