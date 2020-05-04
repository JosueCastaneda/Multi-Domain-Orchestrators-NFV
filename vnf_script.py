import getopt
import sys

from communication_entities.generic_vnf import GenericVNF


def main(argv):
    debug = True
    orchestrator_index = 0
    vnf_index = 0
    experiment_index = 0

    if debug:
        orchestrator_index = 0
        vnf_index = 1
        experiment_index = 0

    try:
        opts, args = getopt.getopt(argv, "i:e:o:", ["vnf_id=", "experiment_id=", "orchestrator_id="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--vnf_id"):
            vnf_index = arg
        elif opt in ("-e", "--experiment_id"):
            experiment_index = arg
        elif opt in ("-o", "--orchestrator_id"):
            orchestrator_index = arg

    vnf = GenericVNF(experiment_index=experiment_index,
                     orchestrator_index=orchestrator_index,
                     vnf_index=vnf_index)
    vnf.serve_clients()


if __name__ == "__main__":
    main(sys.argv[1:])
