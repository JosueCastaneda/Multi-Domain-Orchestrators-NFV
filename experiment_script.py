import asyncio
import getopt
import json
import sys

from aiohttp import web

from communication_entities.experiment_handler import ExperimentHandler
from communication_entities.experiment_routes import init_routes


async def init_app(port) -> web.Application:
    print('Server running in 0.0.0.0:' + str(port))
    app = web.Application()
    handler = ExperimentHandler()
    init_routes(app, handler)
    return app


def get_server_and_port(experiment_index, orchestrator_index):
    orchestrator_index_as_integer = int(orchestrator_index)
    experiment_name = 'experiment_' + experiment_index
    directory_path = 'experiments/experiment_generator/experiments/experiment_' + experiment_index + '/'
    with open(directory_path + experiment_name + '.json') as json_file:
        raw_data = json.load(json_file)
    server = raw_data['orchestrators'][orchestrator_index_as_integer]['ip']
    port = raw_data['orchestrators'][orchestrator_index_as_integer]['port']
    return server, port


def main(argv) -> None:
    server_port = 0
    server_host = '0.0.0.0'
    debug = True
    if debug:
        server_port = 7001
    try:
        valid_arguments_as_string = "p:"
        list_valid_arguments = ["port="]
        opts, args = getopt.getopt(argv, valid_arguments_as_string, list_valid_arguments)
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-p", "--port"):
            server_port = arg
    # print('Sever host: ' + str(server_host))
    # print('Server port: ' + str(server_port))
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(server_port))
    web.run_app(app, host=server_host, port=server_port)


if __name__ == "__main__":
    main(sys.argv[1:])
