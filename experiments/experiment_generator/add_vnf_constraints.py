import json

from utilities.random_integer_generation import generate_random_integer


class AddVNFConstraints:

    def __init__(self, experiment_path, delay, bandwidth, loss, jitter):
        self.experiment_path = experiment_path
        self.list_vnf = []
        self.list_vnf_constraints = []
        self.delay_low = delay[0]
        self.delay_high = delay[1]
        self.bandwidth_low = bandwidth[0]
        self.bandwidth_high = bandwidth[1]
        self.loss_low = loss[0]
        self.loss_high = loss[1]
        self.jitter_low = jitter[0]
        self.jitter_high = jitter[1]

    def add_constraints(self):
        print('Adding constraints')
        self.load_vnfs()
        for vnf in self.list_vnf:
            constraints = self.generate_constraints()
            vnf['delay'] = constraints['delay']
            vnf['bandwidth'] = constraints['bandwidth']
            vnf['loss'] = constraints['loss']
            vnf['jitter'] = constraints['jitter']
            self.list_vnf_constraints.append(vnf)
        self.save_file()

    def save_file(self):
        with open(self.experiment_path + 'vnf_info.json', 'w') as json_file:
            vnf_data = dict()
            vnf_data['vnf'] = self.list_vnf_constraints
            json.dump(vnf_data, json_file)

    def generate_constraints(self):
        topology = dict()
        topology['delay'] = generate_random_integer(self.delay_low, self.delay_high)
        topology['bandwidth'] = generate_random_integer(self.bandwidth_low, self.bandwidth_high)
        topology['loss'] = generate_random_integer(self.loss_low, self.loss_high)
        topology['jitter'] = generate_random_integer(self.jitter_low, self.jitter_high)
        return topology

    def load_vnfs(self):
        print('Loading VNFs')
        with open('vnf_info.json') as json_file:
            raw_data = json.load(json_file)
            self.list_vnf = raw_data['vnf']


def main():
    length_of_vnfs = 4
    video_definition = 480

    delay = [0, 20]
    bandwidth = [0, 70]
    loss = [0, 10]
    jitter = [0, 10]

    experiment_path = '../first/' + str(video_definition) + '/exp_1_' + str(length_of_vnfs) + '/experiments/'

    exp_gen = AddVNFConstraints(experiment_path, delay, bandwidth, loss, jitter)
    exp_gen.add_constraints()

    with open(experiment_path + 'vnf_info.json') as jsonfile:
        parsed = json.load(jsonfile)
    print(json.dumps(parsed, indent=2, sort_keys=True))

    print('Finish setting up experiment!')


if __name__ == main():
    main()
