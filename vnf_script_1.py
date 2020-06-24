import asyncio
import getopt
import sys

from aiohttp import web

from communication_entities.generic_vnf import GenericVNF
from communication_entities.virtual_network_function_handler import VirtualNetworkFunctionHandler
from communication_entities.virtual_network_function_routes import init_routes


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


def main(argv) -> None:
    orchestrator_index = '0'
    experiment_index = '0'
    vnf_index = '0'
    server_host = ''
    server_port = 0
    debug = True

    if debug:
        orchestrator_index = '1'
        experiment_index = '0'
        server_host = '127.0.0.1'
        vnf_index = '1'
        server_port = 3007
    try:
        opts, args = getopt.getopt(argv, "v:o:e:h:p:", ["vnf_id=","orchestrator_id=", "experiment_id=", "host=", "port="])
    except getopt.GetoptError:
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

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(experiment_index,
                                           orchestrator_index,
                                           vnf_index,
                                           server_host,
                                           server_port))
    web.run_app(app, host=server_host, port=server_port)


if __name__ == "__main__":
    main(sys.argv[1:])
