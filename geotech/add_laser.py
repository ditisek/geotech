def add_laser(laser_files, data_file):
    # import pandas as pd
    from pandas import read_csv, merge

    path = laser_files[0].rsplit("\\", 1)[0]

    laser_raw = []
    for file_name in laser_files:
        laser_raw += [line.rstrip('\n') for line in open(file_name)]

    laser_data = [i for i in laser_raw if i.startswith('$LALT')]
    laser_gps_data = [i for i in laser_raw if i.startswith('$GPGGA')]

    laser_combine = []

    for no in range(len(laser_data)):
        laser_combine.append(str(laser_gps_data[no].split(",")[1]) + ','
                             + str(laser_data[no].split(",")[1]))

    print()

    with open(path + '\\gyro.csv', 'w') as file_gyro:
        print('UTC,laser', file=file_gyro)
        for item in laser_combine:
            print(item, file=file_gyro)

    # data_csv_filename = get_file("*.csv")[0]

    laser_csv = read_csv(path + '\\gyro.csv')
    # data_csv = pd.read_csv(geo.get_file("*.csv")[0])
    data_csv = read_csv(data_file)

    path_out = data_file.rsplit("\\", 1)[0]

    merged = merge(data_csv, laser_csv, how="left", on='UTC')
    merged.to_csv(path_out + "\\VTEMExtractedLaser.csv",
                  index=False, header=True)
