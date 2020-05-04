from entities.vnf_entities.vnf_state import VnfState
from utilities.logger import log


class VnfConfiguration:

    def __init__(self,
                 static_configuration,
                 service_package=None,
                 topology=None,
                 orchestrator=None,
                 migration_configuration=None,
                 dependency_list=None):
        self.static_configuration = static_configuration
        self.state = VnfState(initial_value=static_configuration.get_initial())
        self.service_package = service_package
        self.topology = topology
        self.orchestrator = orchestrator
        self.migration_configuration = migration_configuration
        self.connection_points = []
        self.dependency_list = dependency_list
        self.list_affected_vnf = []

    def get_dependency_list(self):
        return self.dependency_list

    def get_connection_points(self):
        return self.connection_points

    def add_affected_vfn(self, vnf):
        self.list_affected_vnf.append(vnf)

    def migration_vnf(self):
        return self.migration_configuration.get_migration_vnf()

    def topology_migration_vnf(self):
        return self.migration_configuration.get_topology_migration_vnf()

    def get_topology(self):
        return self.topology

    def delay(self):
        return self.topology.get_delay()

    def bandwidth(self):
        return self.topology.get_bandwidth()

    def loss(self):
        return self.topology.get_loss()

    def jitter(self):
        return self.topology.get_jitter()

    def get_orchestrator(self):
        return self.orchestrator

    def get_state(self):
        return self.state

    def host(self):
        return self.static_configuration.get_host()

    def port(self):
        return self.static_configuration.get_port()

    def name(self):
        return self.static_configuration.get_vnf_name()

    def get_orchestrator(self):
        return self.orchestrator

    def orchestrator_host(self):
        return self.orchestrator.host

    def orchestrator_port(self):
        return self.orchestrator.port

    def print_state_vnf(self):
        log.info(''.join(["VNF name: ", self.name(), " is running!"]))
        log.info(''.join(["Delay: ", str(self.delay())]))
        log.info(''.join(["Bandwidth: ", str(self.bandwidth())]))
        log.info(''.join(["Loss: ", str(self.loss())]))
        log.info(''.join(["Jitter: ", str(self.jitter())]))
        log.info(''.join(["Orchestrator: ",
                          self.orchestrator_host(),
                          " ",
                          str(self.orchestrator_port())]))
        for vnf in self.list_affected_vnf:
            print(vnf)
        log.info("Queue P: ")
        for d in self.get_state().get_p():
            log.info(''.join([str(d), " "]))

