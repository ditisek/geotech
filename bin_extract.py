def bin_extract():
    import struct
    import wx

    def get_path(wildcard):
        app = wx.App(None)
        style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        else:
            path = None
        dialog.Destroy()
        return path


    # Open the file for reading.
    with open(get_path('*.bin'), 'rb') as infile:
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
