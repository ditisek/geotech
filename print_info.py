def print_info(data):
    """
    Terminal print system info from line extracted d-file

    :param data: List of d-file data
    :return:
    """
    l = '-' * 22
    print('{0}\n System Information :\n{0}\nSample Rate :\t\t{1:>6}\n'
          'No of Channels :\t{2:>6}\nSoftware Version :\t{3:>6}\n'
          'Loop diameter :\t\t{4:>6}\nSystem Type :\t\t{5:>6}\n'
          'Serial No :\t\t\t{6:>6}\nSystem Gain :\t\t{7:>6}\n'
          'Base Frequency :\t{8:>6}\nDuty Cycle :\t\t{9:>6}\n'
          'Voltage :\t\t\t{10:>6}\nNo Mags :\t\t\t{11:>6}\n'
          'Power Monitor :\t\t{12:>6}\n'
          .format(l, data[0], data[1], data[6], data[2],
                  data[4], data[5], data[3], data[7],
                  data[8], data[9], data[12], data[11]))
