def bin_extract(input_file):
    import struct

    # Open the file for reading.
    with open(input_file, 'rb') as infile:
        data = infile.read()  # Read the contents of the file into memory.
        sbet_data = infile.read()
        print(infile.name)

    FName = infile.name.split('\\')[-1:][0].rsplit('.', 1)[0]
    print(FName + ".txt")

    no_chan = int(len(data) / 1536000)
    # print(len(sbet_data))

    if no_chan == 2:
        struct_fmt = 'll'
    elif no_chan == 3:
        struct_fmt = 'lll'
    elif no_chan == 4:
        struct_fmt = 'llll'

    struct_len = struct.calcsize(struct_fmt)
    print("{} channels detected".format(int(struct_len / 4)))
    struct_unpack = struct.Struct(struct_fmt).unpack_from

    results = []

    fout = open(infile.name + '.txt', 'w')
    with open(infile.name, "rb") as f:
        while True:
            data = f.read(struct_len)
            if not data: break
            s = struct_unpack(data)
            fout.write(', '.join(map(str, s)) + '\n')
            results.append(s)

    fout.close()
