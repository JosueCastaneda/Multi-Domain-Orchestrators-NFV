class VNFDefinition:

    def __init__(self, configuration):
        self.operation = configuration.operation
        self.server = configuration.server
        self.port = configuration.port
        self.queue_p = configuration.queue_p
        self.queue_q = configuration.queue_q
        self.queue_r = configuration.queue_r
        self.delay = configuration.delay
        self.bandwidth = configuration.bandwidth
        self.type = 'VNF'
        self.loss = configuration.loss
        self.jitter = configuration.jitter
        self.orchestrator_id = configuration.orchestrator
        self.migration_vnf_ip = configuration.migration_vnf_ip
        self.entry_connection_point = configuration.entry_connection_point
        self.exit_connection_point = configuration.exit_connection_point
        self.id = configuration.id
        self.parameters = configuration.parameters

    def create_dictionary_specification(self):
        new_vnf = dict()
        new_vnf['bandwidth'] = self.bandwidth
        new_vnf['delay'] = self.delay
        new_vnf['entry_connection_point'] = self.entry_connection_point
        new_vnf['exit_connection_point'] = self.exit_connection_point
        new_vnf['id'] = self.id
        new_vnf['jitter'] = self.jitter
        new_vnf['loss'] = self.loss
        new_vnf['migration_vnf_ip'] = self.migration_vnf_ip
        new_vnf['operation'] = self.operation
        new_vnf['orchestrator'] = self.orchestrator_id
        new_vnf['parameters'] = self.parameters
        new_vnf['port'] = self.port
        new_vnf['queue_p'] = self.queue_p
        new_vnf['queue_q'] = self.queue_q
        new_vnf['queue_r'] = self.queue_r
        new_vnf['server'] = self.server
        new_vnf['type'] = self.type
        return new_vnf
