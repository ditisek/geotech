def dfileinfo(data: str) -> list:
    """
    Return system info when valid extracted d-file
    data is parsed to function

    :param data: Data extracted in line format
        from d-files
    :return: A list of twelve variables containing
        the system information
    """
    data_out = [[] for i in range(13)]
    for index, row in enumerate(data):
        if row.startswith('$TDINFO'):
            row_split = row.split(",")
            data_out[0] = row_split[1]    # SamplR
            data_out[1] = row_split[2]    # Chan
            data_out[2] = row_split[3]    # loopd
            data_out[3] = row_split[7]    # gain
            data_out[4] = row_split[9]    # stype
            data_out[5] = row_split[10]   # sn
        elif row.startswith('$TDTDEM'):
            row_split = row.split(",")
            data_out[6] = row_split[1]   # Ver
            data_out[7] = row_split[2]   # basef
            data_out[8] = row_split[3]   # dc
            data_out[9] = row_split[4]   # volt
            data_out[10] = row_split[5]  # noch
            data_out[11] = row_split[9]  # pmon
            data_out[12] = row_split[11] # nomags

    return data_out
