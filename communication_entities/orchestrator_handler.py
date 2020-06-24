import asyncio
import datetime

from aiohttp import web
from aiohttp.web_response import Response

from communication_entities.vector_clock import VectorClock
from entities.vnf_entities.vnf_information import VnfInformation
from utilities.logger import log
import traceback
import json
from utilities.json_loader import my_date_converter

class OrchestratorHandler:

    def __init__(self, orchestrator, ):
        self.orchestrator = orchestrator
        self._loop = asyncio.get_event_loop()

    async def index(self, request: web.Request) -> Response:
        data = self.orchestrator.name
        data_json = {'name': data}
        return web.json_response(data_json)

    async def get_services(self, request: web.Request) -> Response:
        log.info('Getting services')
        try:
            result = await self.orchestrator.get_services()
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)

    async def add_orchestrator(self, request: web.Request) -> Response:
        log.info('Adding orchestrator')
        try:
            data = await request.post()
            result = await self.orchestrator.add_orchestrator(data)
            if not result['success']:
                return web.json_response(result)
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return response

    async def add_vnf(self, request: web.Request) -> Response:
        log.info('Adding VNF')
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
            print(traceback.format_exc())
            return web.json_response(response)

    async def grant_service_migration(self, request: web.Request) -> Response:
        log.info('Granting to service')
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
            print(traceback.format_exc())
            return web.json_response(response)

    async def request_scaling_of_service(self, request: web.Request) -> Response:
        log.info('Requesting to scale service')
        try:
            data = await request.post()
            log.info('Requested Scaling of service ' + str(data['service_id']))
            result = await self.orchestrator.request_service_scale(data['service_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)

    async def notify_scaling_has_ended(self, request: web.Request) -> Response:
        log.info('Notifying...')
        try:
            data = await request.post()
            result = await self.orchestrator.wait_before_notification(data['vector_clock'],
                                                                      data['orchestrator_sender_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)

    async def notify_update_of_vector_clock(self, request: web.Request) -> Response:
        log.info('Notifying update of clock...')
        try:
            data = await request.post()
            result = await self.orchestrator.wait_before_notification(data['vector_clock'],
                                                                      data['orchestrator_sender_id'])
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
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
            answer = {'status': 'Good', 'result': result}
            return web.json_response(answer)
        except Exception as e:
            response = {'status': 'failed', 'message': str(e)}
            print(traceback.format_exc())
            return web.json_response(response)