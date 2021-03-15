def dfile_rename_gps(input_files):
    """
    Make a copy of the data-files with the correct UTC timestamp
    as extracted from the first GPS string

    :param file_extension: File extension in dot format
        Default is .d
    :return:
    """
    from .d_name_utc import d_name_utc
    # from .get_file import get_file
    from shutil import copyfile
    from os import listdir
    # file_path = get_file(input)
    # new_files = []
    # path = file_path.rsplit("\\", 1)[0]
    # files = listdir(path)
    input_files = [i for i in input_files if i.endswith(file_extension.replace("*", ""))]
    input_files = [(path + '\\' + i) for i in input_files]
    # files = [f for f in os.listdir('./my_dir') if f.endswith('.txt')]
    for file in input_files:
        file_time = int(file.rsplit("\\", 1)[1].replace(".", "")[5:9])
        utc = 9999
        with open(file, 'r') as infile:
            data = infile.read().split('\n')
        for index, row in enumerate(data):
            row_split = row.split(",")
            if row.startswith('$GPGGA'):
                utc = int(row_split[1][0:4])
                new_files.append(d_name_utc(utc))
                break
            # if utc == (file_time):
            if (file_time - 10) <= utc <= (file_time + 10):
                new_files.append(d_name_utc(utc))
                break
            if utc < 9999:
                new_files.append(d_name_utc(utc))
                break
        if utc == 9999:
            new_files.append(d_name_utc(utc))

    output_file_name = input_files[0].rsplit('\\', 1)[0] + "\\file_list.txt"
    file_write = open(output_file_name, 'w')
    file_write.write("{} Files converted:\n".format(len(input_files)))

    for index, file in enumerate(input_files):
        copyfile(file, (file.rsplit('\\', 1)[0] + "\\" + new_files[index]))
        print(file.rsplit('\\', 1)[1] + " -> " + new_files[index])
        file_write.write(file.rsplit('\\', 1)[1] + " -> " +
                         new_files[index] + '\n')

    file_write.close()
