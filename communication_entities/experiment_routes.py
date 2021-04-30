from aiohttp import web

from communication_entities.experiment_handler import ExperimentHandler


def init_routes(app: web.Application, handler: ExperimentHandler) -> None:
    add_route = app.router.add_route
    add_route('GET', '/', handler.index, name='index')
    add_route('POST', '/', handler.index, name='index')
    add_route('POST', '/info', handler.index, name='info')
    add_route('POST', '/run_orchestrator', handler.run_orchestrator, name='run_orchestrator')
    add_route('GET', '/run_orchestrator', handler.run_orchestrator, name='run_orchestrator')
    add_route('POST', '/stop_orchestrator', handler.stop_orchestrator, name='stop_orchestrator')
    add_route('GET', '/stop_orchestrator', handler.stop_orchestrator, name='stop_orchestrator')
    add_route('POST', '/run_all_experiments_zero_touch', handler.run_all_experiments_zero_touch, name='run_all_experiments_zero_touch')
    add_route('GET', '/run_all_experiments_zero_touch', handler.run_all_experiments_zero_touch, name='run_all_experiments_zero_touch')






