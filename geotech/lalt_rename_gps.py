def lalt_rename_gps(input_files, new_date):
    """
    Make a copy of the data-files with the correct UTC timestamp
    as extracted from the first GPS string

    :param file_extension: File extension in dot format
        Default is .log
    :return:
    """
    from shutil import copyfile

    new_files = []
    for file in input_files:
        file_time = int(file.rsplit("\\", 1)[1].replace("_", "")[5:9])
        utc = 9999
        with open(file, 'r') as infile:
            data = infile.read().split('\n')
        for index, row in enumerate(data):
            row_split = row.split(",")
            if row.startswith('$GPGGA'):
                utc = row_split[1][0:4]
                new_files.append('LALT ' + new_date + " " + str(utc)[0:2] + \
                                 "_" + str(utc)[2:4] + "_00.log")
                break
            if (file_time - 10) <= utc <= (file_time + 10):
                new_files.append('LALT ' + new_date + " " + str(utc)[0:2] + \
                                 "_" + str(utc)[2:4] + "_00.log")
                break
            if utc < 9999:
                new_files.append('LALT ' + new_date + " " + str(utc)[0:2] + \
                                 "_" + str(utc)[2:4] + "_00.log")
                break
        if utc == 9999:
            new_files.append('LALT ' + new_date + " " + str(utc)[0:2] + \
                             "_" + str(utc)[2:4] + "_00.log")

    output_file_name = input_files[0].rsplit('\\', 1)[0] + "\\file_list.txt"
    file_write = open(output_file_name, 'w')
    file_write.write("{} Files converted:\n".format(len(input_files)))

    for index, file in enumerate(input_files):
        copyfile(file, (file.rsplit('\\', 1)[0] + "\\" + new_files[index]))
        print(file.rsplit('\\', 1)[1] + " -> " + new_files[index])
        file_write.write(file.rsplit('\\', 1)[1] + " -> " +
                         new_files[index] + '\n')

    file_write.close()
