from aiohttp import web

from communication_entities.orchestrator_handler import OrchestratorHandler


def init_routes(app: web.Application, handler: OrchestratorHandler) -> None:
    add_route = app.router.add_route
    add_route('GET', '/', handler.index, name='index')
    add_route('POST', '/add_orchestrator', handler.add_orchestrator, name='add_orchestrator')
    add_route('POST', '/add_vnf', handler.add_vnf, name='add_vnf')
    add_route('POST', '/clear_inconsistencies', handler.clear_inconsistencies, name='clear_inconsistencies')
    add_route('POST', '/get_log_file', handler.get_log_file, name='get_log_file')
    add_route('POST', '/get_services', handler.get_services, name='get_services')
    add_route('POST', '/get_vnfs', handler.get_vnfs, name='get_vnfs')
    add_route('POST', '/get_orchestrators', handler.get_orchestrators, name='get_orchestrators')
    add_route('POST', '/get_vector_clock', handler.get_vector_clock, name='get_vector_clock')
    add_route('POST', '/grant_service_migration', handler.grant_service_migration, name='grant_service_migration')
    add_route('POST', '/notify_update_of_vector_clock', handler.notify_update_of_vector_clock, name='notify_update_of_vector_clock')
    add_route('POST', '/notify_scaling_has_ended', handler.notify_scaling_has_ended, name='notify_scaling_has_ended')
    add_route('POST', '/request_scaling_of_service', handler.request_scaling_of_service,
              name='request_scaling_of_service')
    add_route('POST', '/scale_of_service_has_ended', handler.scale_of_service_has_ended, name='scale_of_service_has_ended')
    add_route('GET', '/get_inconsistencies', handler.get_inconsistencies, name='get_inconsistencies')
    add_route('GET', '/get_time_elapsed', handler.get_time_elapsed, name='get_time_elapsed')
    add_route('GET', '/get_pending_operations', handler.get_pending_operations, name='get_pending_operations')
    add_route('GET', '/get_messages_sent', handler.get_messages_sent, name='get_messages_sent')



