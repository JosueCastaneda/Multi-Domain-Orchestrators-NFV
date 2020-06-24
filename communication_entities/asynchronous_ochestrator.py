import json

from aiohttp import web

from communication_entities.orchestrator import Orchestrator

orchestrator_index = "2"
experiment_index = "0"
orchestrator = Orchestrator(orchestrator_index=orchestrator_index,
                            experiment_index=experiment_index,
                            causal_delivery=True)

async def handle(request):
    response_obj = {'status': 'success'}
    orchestrator.print_state_vnf()
    return web.Response(text=json.dumps(response_obj))

async def print_hello(request):
    response_obj = {'status': 'Hello'}
    return web.Response(text=json.dumps(response_obj))


app = web.Application()
app.router.add_get('/', handle)

web.run_app(app, port=5432)