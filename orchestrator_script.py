import asyncio
import getopt
import json
import sys
from aiohttp import web

from communication_entities.orchestrator import Orchestrator
from communication_entities.orchestrator_handler import OrchestratorHandler
from communication_entities.orchestrator_routes import init_routes


async def init_app(experiment_index, orchestrator_index, server_host, server_port, random_seed, index_algorithm) -> web.Application:
    algorithm_type = 'causal'
    # print('Index Algorithms I got: ' + str(index_algorithm))
    if index_algorithm == 0:
        algorithm_type = 'causal'
    elif index_algorithm == 1:
        algorithm_type = 'standard'
    elif index_algorithm == 2:
        algorithm_type = 'last_writer_wins'
    elif index_algorithm == 3:
        algorithm_type = 'multi_value'
    # print(algorithm_type)
    app = web.Application()
    orchestrator = Orchestrator(orchestrator_index=orchestrator_index,
                                experiment_index=experiment_index,
                                server_host=server_host,
                                server_port=server_port,
                                random_seed=random_seed,
                                causal_delivery=False,
                                algorithm_type=algorithm_type)
    handler = OrchestratorHandler(orchestrator)
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
    orchestrator_index = '0'
    experiment_index = '0'
    server_host = ''
    server_port = 0
    random_seed = 1000
    debug = True
    algorithm_index = 0
    if debug:
        orchestrator_index = '4'
        experiment_index = '0'
        server_host = '127.0.0.1'
        server_port = 4445
    try:
        valid_arguments_as_string = "i:e:h:p:r:a:"
        list_valid_arguments = ["service_id=", "experiment_id=", "host=", "port=", "random_seed=", "algorithm="]
        opts, args = getopt.getopt(argv, valid_arguments_as_string, list_valid_arguments)
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--service_id"):
            orchestrator_index = arg
        elif opt in ("-e", "--experiment_id"):
            experiment_index = arg
        elif opt in ("-h", "--host"):
            server_host = arg
        elif opt in ("-p", "--port"):
            server_port = arg
        elif opt in ("-r", "--random_seed"):
            random_seed = arg
        elif opt in ("-a", "--algorithm"):
            algorithm_index = arg

    if server_host == '' and server_port == 0:
        server_host, server_port = get_server_and_port(experiment_index, orchestrator_index)

    print('Sever host: ' + str(server_host))
    print('Server port: ' + str(server_port))
    print('Algorithm index: ' + str(algorithm_index))

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(experiment_index,
                                           orchestrator_index,
                                           server_host,
                                           server_port,
                                           random_seed,
                                           int(algorithm_index)))
    web.run_app(app, host=server_host, port=server_port)


if __name__ == "__main__":
    main(sys.argv[1:])
