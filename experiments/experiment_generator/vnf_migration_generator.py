import json
import os
import random

from utilities.random_integer_generation import generate_random_integer


class VNFMigrationGenerator:

    def __init__(self, delay, bandwidth, loss, jitter, orchestrators, experiment_path):
        self.delay_low = delay[0]
        self.delay_high = delay[1]
        self.bandwidth_low = bandwidth[0]
        self.bandwidth_high = bandwidth[1]
        self.loss_low = loss[0]
        self.loss_high = loss[1]
        self.jitter_low = jitter[0]
        self.jitter_high = jitter[1]
        self.orchestrator_low = orchestrators[0]
        self.orchestrator_high = orchestrators[1]
        self.path = experiment_path
        random.seed(5)

    def create_vnfs(self):
        print('Begin creation')

        running_queue = 150
        vnf_list = []

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        for i in range(150, 255):
            new_vnf = dict()
            new_vnf['operation'] = "UNKNOWN"
            new_vnf['server'] = "10.0.0." + str(i)
            new_vnf['queue_p'] = [running_queue]
            new_vnf['queue_q'] = [running_queue + 1]
            new_vnf['queue_r'] = [running_queue + 2]
            new_vnf['delay'] = generate_random_integer(self.delay_low, self.delay_high)
            new_vnf['bandwidth'] = generate_random_integer(self.bandwidth_low, self.bandwidth_high)
            new_vnf['loss'] = generate_random_integer(self.loss_low, self.loss_high)
            new_vnf['jitter'] = generate_random_integer(self.jitter_low, self.jitter_high)
            new_vnf['orchestrator'] = generate_random_integer(self.orchestrator_low, self.orchestrator_high)
            running_queue += 3
            vnf_list.append(new_vnf)
        with open(self.path + 'migration_vnfs' + '.json', 'w') as json_file:
            json.dump(vnf_list, json_file)


# TODO: Put constants instead of magic numbers
def main():
    delay = [0, 20]
    bandwidth = [0, 70]
    loss = [0, 10]
    jitter = [0, 10]
    orchestrator = [1, 4]
    length_of_vnfs = 4
    video_definition = 480
    experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'
    exp_gen = VNFMigrationGenerator(delay, bandwidth, loss, jitter, orchestrator, experiment_path)
    exp_gen.create_vnfs()
    with open(experiment_path + 'migration_vnfs.json') as json_file:
        parsed = json.load(json_file)
    print(json.dumps(parsed, indent=2, sort_keys=True))
    print('Finish creating up experiment!')


if __name__ == "__main__":
    main()
