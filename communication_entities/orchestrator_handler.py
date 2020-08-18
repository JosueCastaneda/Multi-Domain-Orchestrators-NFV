import asyncio
import datetime
import json
import traceback

from aiohttp import web
from aiohttp.web_response import Response

from communication_entities.vector_clock import VectorClock
from entities.vnf_entities.vnf_information import VnfInformation


class OrchestratorHandler:

    def __init__(self, orchestrator, ):
        self.orchestrator = orchestrator
        self._loop = asyncio.get_event_loop()

    async def index(self, request: web.Request) -> Response:
        return web.json_response(self.orchestrator.entry_as_dictionary())

    async def get_services(self, request: web.Request) -> Response:
        try:
            result = await self.orchestrator.get_services()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def add_orchestrator(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.add_orchestrator(data)
            if not result['success']:
                return web.json_response(result)
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def add_vnf(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            vnf_information = VnfInformation(host=data['ip'],
                                             port=data['port'],
                                             name=data['name'],
                                             topology=data['topology'],
                                             migration_ip=data['migration_vnf_ip'],
                                             topology_migration=data['topology_migration_vnf'],
                                             connection_points=data['connection_points'],
                                             dependency_list=data['dependency_list'],
                                             unique_id=data['id'])
            result = await self.orchestrator.add_vnf(vnf_information)
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def grant_service_migration(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            original_service_data = data['original_service']
            original_service = json.loads(original_service_data)
            start_time_formated = datetime.datetime.strptime(original_service['start_time'], "%Y-%m-%d %H:%M:%S")
            original_service['start_time'] = start_time_formated
            sender_vector_clock = VectorClock()
            sender_vector_clock.create_from_list(data['sender_vector_clock'])
            result = await self.orchestrator.wait_before_delivery_grant(data['vnf_component_to_scale_id'],
                                                                        data['operation'],
                                                                        original_service,
                                                                        sender_vector_clock)
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def request_scaling_of_service(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.request_service_scale(data['service_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def notify_scaling_has_ended(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.wait_before_notification(data['vector_clock'],
                                                                      data['orchestrator_sender_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def notify_update_of_vector_clock(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.wait_before_notification(data['vector_clock'],
                                                                      data['orchestrator_sender_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def scale_of_service_has_ended(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.life_cycle_manager.scale_confirmation(data['vnf_component_id'],
                                                                                   data['original_service_id'],
                                                                                   data['orchestrator_sender_id'],
                                                                                   data['original_orchestrator_id'],
                                                                                   data['vector_clock'],
                                                                                   data['service_sender_id'])
            # self.print_good_result(result)
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)
            # self.print_generic_exception(e)

    async def get_vnfs(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.get_vnfs()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_pending_operations(self, request: web.Request) -> Response:
        try:
            result = await self.orchestrator.get_pending_operations()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_orchestrators(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.get_orchestrators()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def clear_inconsistencies(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            self.orchestrator.inconsistencies = 0
            result = await self.orchestrator.entry_as_dictionary()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_log_file(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.get_log_file()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_vector_clock(self, request: web.Request) -> Response:
        try:
            data = await request.post()
            result = await self.orchestrator.vector_clock.as_string()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_inconsistencies(self, request: web.Request) -> Response:
        try:
            result = await self.orchestrator.get_inconsistencies()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_messages_sent(self, request: web.Request) -> Response:
        try:
            result = await self.orchestrator.get_messages_sent()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    async def get_time_elapsed(self, request: web.Request) -> Response:
        try:
            result = await self.orchestrator.get_time_elapsed_reconfiguration()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            return web.json_response(response)

    def print_good_result(self, result) -> Response:
        answer = {'status': 'Good', 'result': result}
        return web.json_response(answer)

    def print_generic_exception(self, e) -> Response:
        response = {'status': 'failed', 'message': str(e)}
        return web.json_response(response)
