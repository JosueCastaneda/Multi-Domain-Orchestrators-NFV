import getopt
import pickle
import socket
import sys

sys.path.append('../')


from entities.message_generator import MessageGenerator
from entities.command_package import CommandPackage
from utilities.logger import log


def main(argv):
    command = read_parameters(argv)
    # file = 'experiments/first/1920/exp_1_3/parameters.json'
    # file = 'experiments/first/480/exp_1_4/experiments/experiment_0.json'
    # file = 'experiments/first/1920/exp_1_5/parameters.json'
    #file = 'experiments/first/1920/exp_1_6/parameters.json'
    # print('Filename:', file)
    if command.is_valid():
        messages = generate_messages(command)
        if isinstance(messages, list):
            log.info(''.join(["Number of messages", str(len(messages))]))
            # send_message(command, messages[0])
            for m in messages:
                send_message(command, m)
        else:
            send_message(command, messages)
    else:
        print(command.help_message)


def generate_messages(command):
    m = MessageGenerator(command, command.experiment)
    return m.generate_message()


def send_message(command, message):
    send_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Host: ', command.host, ' Port: ', command.port)
    send_channel.connect((command.host, command.port))
    log.info('Connected!')
    data_string = pickle.dumps(message)
    log.info('Data string created!')
    send_channel.send(data_string)
    log.info('Sent!')
    send_channel.close()
    log.info('Closing channel!')


def read_parameters(argv):
    command = CommandPackage()
    debug = False

    try:
        opts, args = getopt.getopt(argv, "t:h:p:n:m:v:w:e",
                                   ["type=",
                                    "host=",
                                    "port=",
                                    "name=",
                                    "new_name=",
                                    "vnf_host=",
                                    "vnf_port=",
                                    "experiment="])
    except getopt.GetoptError:
        print(command.help_message)
        sys.exit(2)
    for opt, arg in opts:
        if debug:
            print("Option: ", opt, " Argument: ", arg)
        if opt in ("-h", "--host"):
            command.host = arg
        elif opt in ("-p", "--port"):
            command.port = int(arg)
        elif opt in ("-n", "--name"):
            command.name = arg
        elif opt in ("-m", "--new_name"):
            command.new_name = arg
        elif opt in ("-t", "--type"):
            command.message_type = arg
        elif opt in ("-v", "--vnf_host"):
            command.vnf_host = arg
        elif opt in ("-w", "--vnf_port"):
            command.vnf_port = arg
        elif opt in ("-e", "--experiment"):
            str_exp = 'experiments/first/480/exp_1_4/experiments/experiment_' + arg +'.json'
            command.experiment = str_exp
    return command


if __name__ == "__main__":
    main(sys.argv[1:])
