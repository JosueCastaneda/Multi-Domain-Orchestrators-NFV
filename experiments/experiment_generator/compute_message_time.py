import os
import statistics


def main():
    list_names = ['vnf_ROTATE',
                  'vnf_CROP',
                  'vnf_PAINTING',
                  'vnf_RESIZE',
                  'vnf_BLACK_WHITE',
                  'vnf_ANNOTATE',
                  'vnf_MIRROR_X',
                  'vnf_INVERT_COLORS',
                  'vnf_FADE_OUT',
                  'vnf_SPEED_UP',
                  'vnf_FADE_IN',
                  'vnf_COMPOSITE',
                  'vnf_MIRROR_Y']

    list_times = []

    for name in list_names:
        complete_name = 'time_update_' + name + '.txt'
        if os.path.isfile(complete_name):
            with open(complete_name, 'r') as f:
                times = [line.strip() for line in f]
                str_list = list(filter(None, times))
                for entry in str_list:
                    list_times.append(float(entry))
    mean_time = statistics.mean(list_times)
    std_time = statistics.stdev(list_times)
    var_time = statistics.variance(list_times)
    print("Mean is :", mean_time)
    print("StD is :", std_time)
    print('Variance: ', var_time)


if __name__ == main():
    main()
