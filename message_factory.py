import asyncio
import getopt
import sys

import aiohttp

sys.path.append('../')

from entities.message_generator import MessageGenerator
from utilities.command_package import CommandPackage


def generate_messages(command):
    m = MessageGenerator(command, command.experiment)
    return m.generate_message()


def read_parameters(argv):
    command = CommandPackage()
    debug = True

    if debug:
        command.host = '127.0.0.1'
        command.port = 5002
        command.name = None
        command.new_name = None
        command.vnf_host = '127.0.0.1'
        command.vnf_port = 5002
        command.orchestrator_id = 'e5ea698b-8a3d-11ea-aa9d-04ea56f99520'
        command.message_type = 'request_sc'

    try:
        opts, args = getopt.getopt(argv, "t:h:p:n:m:v:w:e:s:i:x:",
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
                                    "orchestrator_id="])
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
    return command


async def send_message(command, message):
    url = 'http://' + command.host + ':' + str(command.port) + '/' + command.message_type
    print(url)
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=message.data) as resp:
            print(resp.status)
            print(await resp.text())


async def main(argv):
    command = read_parameters(argv)
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
