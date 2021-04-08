class OrchestratorDefinition:

    def __init__(self, data):
        self.waiting_time = data['waiting_time']
        self.probability_repeated_message = data['probability_repeated_messages']
        self.experiment_name = 'experiment_' + data['experiment_index']
        self.experiment_index = data['experiment_index']
        self.name = 'orch_' + data['orchestrator_index']
        self.orchestrator_index = data['orchestrator_index']
        self.orchestrator_counter = 0
        self.directory_path = 'experiments/experiment_' + self.experiment_index + '/'
        self.id = ''
        self.location = ''
        self.orchestrators_ids = []
        self.ip = data['server_host']
        self.port = data['server_port']
        self.topology = None
        self.inconsistencies = 0
        self.messages_sent = 0
        self.causal_delivery = data['causal_delivery']
        self.random_seed = data['random_seed']
        self.pending_operations_repetitions = 0
        self.time_elapsed_in_reconfiguration = 0.0
        self.algorithm_type = data['algorithm_type']
        self.total_time_for_experimentation = 0.0
