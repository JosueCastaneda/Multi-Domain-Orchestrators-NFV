import asyncio
import getopt
import json
import sys

from aiohttp import web

from communication_entities.generic_vnf import GenericVNF
from communication_entities.virtual_network_function_handler import VirtualNetworkFunctionHandler
from communication_entities.virtual_network_function_routes import init_routes
from utilities.logger import log


async def init_app(experiment_index, orchestrator_index, vnf_index, server_host, server_port) -> web.Application:
    app = web.Application()
    vnf = GenericVNF(orchestrator_index=orchestrator_index,
                     experiment_index=experiment_index,
                     vnf_index=vnf_index,
                     server_host=server_host,
                     server_port=server_port)
    await vnf.set_up_to_orchestrator()
    handler = VirtualNetworkFunctionHandler(vnf)
    init_routes(app, handler)
    return app


def get_server_and_port(experiment_index, orchestrator_index, vnf_index):
    orchestrator_index_as_integer = int(orchestrator_index)
    vnf_index = int(vnf_index)
    experiment_name = 'experiment_' + experiment_index
    directory_path = 'experiments/experiment_generator/experiments/experiment_' + experiment_index + '/'
    with open(directory_path + experiment_name + '.json') as json_file:
        raw_data = json.load(json_file)
    my_vnf = raw_data['orchestrators'][orchestrator_index_as_integer]['vnfs'][vnf_index]
    server = my_vnf['server']
    port = my_vnf['port']
    return server, port


def main(argv) -> None:
    orchestrator_index = '0'
    experiment_index = '0'
    vnf_index = '0'
    server_host = ''
    server_port = 0
    debug = False

    if debug:
        orchestrator_index = '0'
        experiment_index = '0'
        server_host = '127.0.0.1'
        vnf_index = '0'
        server_port = 3008

    try:
        string_arguments = 'v:o:e:h:p:i:'
        list_of_valid_arguments = ["vnf_id=", "orchestrator_id=", "experiment_id=", "host=", "port=", "index="]
        opts, args = getopt.getopt(argv, string_arguments, list_of_valid_arguments)
    except getopt.GetoptError:
        log.info('Error')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-v", "--vnf_id"):
            vnf_index = arg
        if opt in ("-o", "--orchestrator_id"):
            orchestrator_index = arg
        elif opt in ("-e", "--experiment_id"):
            experiment_index = arg
        elif opt in ("-h", "--host"):
            server_host = arg
        elif opt in ("-p", "--port"):
            server_port = arg
        elif opt in ("-i", "--index"):
            vnf_index = arg

    if server_host == '' and server_port == 0:
        server_host, server_port = get_server_and_port(experiment_index, orchestrator_index, vnf_index)

    print('Sever host: ' + str(server_host))
    print('Server port: ' + str(server_port))

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(experiment_index,
                                           orchestrator_index,
                                           vnf_index,
                                           server_host,
                                           server_port))
    web.run_app(app, host=server_host, port=server_port)


if __name__ == "__main__":
    main(sys.argv[1:])
