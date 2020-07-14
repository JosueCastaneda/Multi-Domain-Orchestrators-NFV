import asyncio
import getopt
import json
import sys
from aiohttp import web

from communication_entities.orchestrator import Orchestrator
from communication_entities.orchestrator_handler import OrchestratorHandler
from communication_entities.orchestrator_routes import init_routes


async def init_app(experiment_index, orchestrator_index, server_host, server_port) -> web.Application:
    app = web.Application()
    orchestrator = Orchestrator(orchestrator_index=orchestrator_index,
                                experiment_index=experiment_index,
                                server_host=server_host,
                                server_port=server_port,
                                causal_delivery=True)
    handler = OrchestratorHandler(orchestrator)
    init_routes(app, handler)
    return app


def get_server_and_port(experiment_index, orchestrator_index):
    orch_index = int(orchestrator_index)
    experiment_name = 'experiment_' + experiment_index
    directory_path = 'experiments/experiment_generator/experiments/experiment_' + experiment_index + '/'
    with open(directory_path + experiment_name + '.json') as json_file:
        raw_data = json.load(json_file)
    server = raw_data['orchestrators'][orch_index]['ip']
    port = raw_data['orchestrators'][orch_index]['port']
    return server,port


def main(argv) -> None:
    orchestrator_index = '0'
    experiment_index = '0'
    server_host = ''
    server_port = 0
    debug = True

    if debug:
        orchestrator_index = '0'
        experiment_index = '0'
        server_host = '127.0.0.1'
        server_port = 5001
    try:
        opts, args = getopt.getopt(argv, "i:e:h:p:", ["service_id=", "experiment_id=", "host=", "port="])
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

    if server_host == '' and server_port == 0:
        server_host, server_port = get_server_and_port(experiment_index, orchestrator_index)

    print('Sever host: ' + str(server_host))
    print('Server port: ' + str(server_port))

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(experiment_index,
                                           orchestrator_index,
                                           server_host,
                                           server_port))
    web.run_app(app, host=server_host, port=server_port)


if __name__ == "__main__":
    main(sys.argv[1:])
