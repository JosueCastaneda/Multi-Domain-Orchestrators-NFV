import asyncio
import traceback

from aiohttp import web
from aiohttp.web_response import Response

from communication_entities.generic_vnf import GenericVNF


class VirtualNetworkFunctionHandler:

    def __init__(self, virtual_network_function: GenericVNF):
        self.virtual_network_function = virtual_network_function
        self._loop = asyncio.get_event_loop()

    async def scale_vnf(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.virtual_network_function.scale(data['vnf_component_id'],
                                                               data['original_service_id'],
                                                               data['orchestrator_sender_id'],
                                                               data['original_orchestrator_id'],
                                                               data['vector_clock'],
                                                               data['service_sender_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)

    async def add_chain(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.virtual_network_function.add_affected_vnf(data['ip'],
                                                                          data['port'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)

    async def index(self, request: web.Request) -> Response:
        return web.json_response(self.virtual_network_function.entry_as_dictionary())
