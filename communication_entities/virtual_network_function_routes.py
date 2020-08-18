from aiohttp import web

from communication_entities.virtual_network_function_handler import VirtualNetworkFunctionHandler


def init_routes(app: web.Application, handler: VirtualNetworkFunctionHandler) -> None:
    add_route = app.router.add_route
    add_route('GET', '/', handler.index, name='index')
    add_route('POST', '/scale_vnf', handler.scale_vnf, name='scale_vnf')
    add_route('POST', '/add_chain', handler.add_chain, name='add_chain')
