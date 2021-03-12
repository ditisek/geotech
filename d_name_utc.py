def d_name_utc(data):
    """
    Create new d-file name with today's date

    :param data: UTC extracted from GPS
    :return: File name with date and UTC start at begging of file
    """
    from datetime import date
    data = str(data)
    f_name = date.today().strftime("%d.%m") + " " + data[0:2] + \
             "." + data[2:4] + ".00.d"
    return f_name
