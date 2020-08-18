from utilities.random_integer_generation import generate_random_integer, generate_unique_identifier


class VNFDefinitionConfiguration:

    def __init__(self, operation, server, port, orchestrator, queue_number, constraints):
        self.id = generate_unique_identifier()
        self.operation = operation
        self.server = server
        self.port = port
        self.orchestrator = orchestrator
        self.queue_p = queue_number
        self.queue_q = queue_number + 1
        self.queue_r = queue_number + 2
        self.delay = None
        self.bandwidth = None
        self.loss = None
        self.jitter = None
        self.migration_vnf_ip = None
        self.entry_connection_point = None
        self.exit_connection_point = None
        self.parameters = None
        self.add_constraints(constraints)

    # TODO: Here add real random with no relation because all VNFs have the same constraints
    def add_constraints(self, constraints):
        self.delay = generate_random_integer(0, constraints.delay)
        self.bandwidth = generate_random_integer(0, constraints.delay)
        self.loss = generate_random_integer(0, constraints.loss)
        self.jitter = generate_random_integer(0, constraints.jitter)

    def add_migration_ip(self, ip):
        self.migration_vnf_ip = ip

    def connection_points(self, entry_connection_point, exit_connection_point):
        self.entry_connection_point = entry_connection_point
        self.exit_connection_point = exit_connection_point

    # def add_constraints(self, constraints):
    #     self.delay = constraints.delay
    #     self.bandwidth = constraints.bandwidth
    #     self.loss = constraints.loss
    #     self.jitter = constraints.jitter
