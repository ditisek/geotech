def get_file(wildcard="*.d"):
    """
    Open a wx FileDialog to select a file for usage

    :param wildcard: Wildcard with file extension
    :return: Filename selected in string
    """
    import wx
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    # dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style | wx.FD_MULTIPLE)
    if dialog.ShowModal() == wx.ID_OK:
        # path = dialog.GetPath()
        path = dialog.GetPaths()
    else:
        path = None
    dialog.Destroy()
    return path
