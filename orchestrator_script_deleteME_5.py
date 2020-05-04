import getopt
import sys

from communication_entities.orchestrator import Orchestrator


def main(argv):
    orchestrator_index = '0'
    experiment_index = '0'
    debug = True

    if debug:
        orchestrator_index = '4'
        experiment_index = '0'
    try:
        opts, args = getopt.getopt(argv, "i:e:", ["service_id=", "experiment_id="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--service_id"):
            orchestrator_index = arg
        elif opt in ("-e", "--experiment_id"):
            experiment_index = arg

    orchestrator = Orchestrator(experiment_index=experiment_index, orchestrator_index=orchestrator_index)
    orchestrator.serve_clients()


if __name__ == "__main__":
    main(sys.argv[1:])
