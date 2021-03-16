def gpsfile_rename_gps(input_files):
    import datetime
    from shutil import copyfile
    import os

    data_bin = b''
    SYNC_BYTES = bytes.fromhex(' aa 44 12 ')
    filenameformat = "%02d_%02d %02d_%02d_%02d"
    message_header = input_files[0][0:2]

    bin_files = input_files

    message_header = bin_files[0].rsplit('\\', 1)[1][0:2]

    gps_week = [0] * len(bin_files)
    gps_second = [0] * len(bin_files)
    # days = [0] * len(bin_files)
    # seconds = [0] * len(bin_files)
    new_date = [0] * len(bin_files)

    for no, file in enumerate(bin_files):
        data_bin = open(file, 'rb').read()
        data_lines = data_bin.split(SYNC_BYTES)

        gps_week[no] = 1
        for data in data_lines:
            if gps_week[no] == int.from_bytes(data[11:13], "little"):
                # print('yes')
                break
            gps_week[no] = int.from_bytes(data[11:13], "little")
            gps_second[no] = int.from_bytes(data[13:18], "little") / 1000

    print()

    epoch_raw = datetime.datetime(year=1980, month=1, day=6)

    days_from_epoch = [i * 7 for i in gps_week]
    years_from_epoch = [int(i / 365) for i in days_from_epoch]
    for no, day in enumerate(days_from_epoch):
        new_date[no] = epoch_raw + datetime.timedelta(days=day,
                                                      seconds=gps_second[no])

    path = bin_files[0].rsplit('\\', 1)[0]

    file_name_new = [path + '\\' + message_header + ' ' +
                     filenameformat % (i.month, i.day, i.hour, i.minute, i.second) +
                     '.log' for i in new_date]

    for no, file in enumerate(bin_files):
        with open(path + '\\filelist.txt', 'a') as text_file:
            print(f"{file} -> {file_name_new[no]}", file=text_file)

        print(f"{file} to {file_name_new[no]}")
        # if not os.path.exists(file_name_new[no]) or not filecmp.cmp(file, file_name_new[no]):
        if not os.path.exists(file_name_new[no]):
            copyfile(file, file_name_new[no])
            print('file created')
        else:
            print('file exists!!')

    print()
