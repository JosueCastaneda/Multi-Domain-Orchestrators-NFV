import asyncio
import getopt
import sys
from aiohttp import web

from communication_entities.orchestrator import Orchestrator
from communication_entities.orchestrator_handler import OrchestratorHandler
from communication_entities.orchestrator_routes import init_routes


async def hello(request):
    return web.Response(text="Hello, world")


async def init_app(experiment_index, orchestrator_index, server_host, server_port) -> web.Application:
    app = web.Application()
    orchestrator = Orchestrator(orchestrator_index=orchestrator_index,
                                experiment_index=experiment_index,
                                server_host=server_host,
                                server_port=server_port,
                                causal_delivery=False)
    handler = OrchestratorHandler(orchestrator)
    init_routes(app, handler)
    return app


def main() -> None:
    orchestrator_index = '0'
    experiment_index = '0'
    server_host = ''
    server_port = 0
    debug = True

    if debug:
        orchestrator_index = '4'
        experiment_index = '0'
        server_host = '127.0.0.1'
        server_port = 5005
    try:
        opts, args = getopt.getopt(sys.argv, "i:e:h:p:", ["service_id=", "experiment_id=", "host=", "port="])
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

    # configuration = load_parameters(experiment_index, orchestrator_index)
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(experiment_index,
                                           orchestrator_index,
                                           server_host,
                                           server_port))
    web.run_app(app, host=server_host, port=server_port)


if __name__ == "__main__":
    main()
