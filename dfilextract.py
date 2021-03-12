def dfilextract(data):
    """
    Extract data fields from d-files loaded into list
    line by line

    See data_out_list.txt for all parameters extracted

    :param data: Data in list format
    :return: List of data
    """
    from math import floor
    from .distance import distance
    height1 = '0'
    lat1 = 0
    lon1 = 0
    row_write = 0
    data_out = [[] for i in range(40)]
    for index, row in enumerate(data):
        row_split = row.split(",")
        if row.startswith('$TD_VZ'):
            if (len(row_split) > 45) and (row_split[15] != "nan"):
                data_out[15].append(row_split[15])  # srz15
                data_out[16].append(row_split[24])  # srz24
                data_out[17].append(row_split[33])  # srz33
                data_out[18].append(row_split[44])  # srz44
        elif row.startswith('$TD_BZ'):
            if (len(row_split) > 45) and (row_split[15] != "nan"):
                data_out[19].append(row_split[15])  # brz15
                data_out[20].append(row_split[24])  # brz24
                data_out[21].append(row_split[33])  # brz33
                data_out[22].append(row_split[44])  # brz44
        elif row.startswith('$TD_VX'):
            if (len(row_split) > 45) and (row_split[15] != "nan"):
                data_out[23].append(row_split[15])  # srx15
                data_out[24].append(row_split[24])  # srx24
                data_out[25].append(row_split[33])  # srx33
                data_out[26].append(row_split[44])  # srx44
        elif row.startswith('$TD_VY'):
            if (len(row_split) > 45) and (row_split[15] != "nan"):
                data_out[27].append(row_split[15])  # sry15
                data_out[28].append(row_split[24])  # sry24
                data_out[29].append(row_split[33])  # sry33
                data_out[30].append(row_split[44])  # sry44
        elif row.startswith('$TD_RF'):
            if (len(row_split) > 45) and (row_split[15] != "nan"):
                data_out[31].append(row_split[15])  # rf15
                data_out[32].append(row_split[24])  # rf24
                data_out[33].append(row_split[33])  # rf33
                data_out[34].append(row_split[44])  # rf44
        elif row.startswith('$TD_PKV'):
            if row_split[1] != "nan":
                data_out[11].append(row_split[1])       # pkvr
                data_out[14].append(row_split[2])       # pksz
                if len(row_split) > 3:  # TODO check without Y ch
                    data_out[12].append(row_split[3])   # pksx
                if len(row_split) > 4:  # TODO check without Y ch
                    data_out[13].append(row_split[4])   # pksy
        elif row.startswith('$TD_PKI'):
            if row_split[1] != "nan":
                data_out[7].append(row_split[1])        # pkir
                data_out[10].append(row_split[2])       # pkbz
                if len(row_split) > 3:  # TODO check without Y ch
                    data_out[8].append(row_split[3])    # pkbx
                if len(row_split) > 4:  # TODO check without Y ch
                    data_out[9].append(row_split[4])    # pkby
        elif row.startswith('$PWL'):
            data_out[35].append(row_split[1])  # pwl
        elif row.startswith('$LINE'):
            data_out[1].append(row_split[1])  # lno
        elif row.startswith('$RDALT'):
            data_out[6].append(row_split[1])  # ralt
        elif row.startswith('$GRD4A'):
            if len(row_split) > 2:
                data_out[36].append(row_split[1])  # mag1
                data_out[37].append(row_split[2])  # mag2
        elif row.startswith('$GRDI'):
            if len(row_split) > 2:
                data_out[36].append(row_split[2])  # mag1
        elif row.startswith('$MG'):
            if len(row_split) > 2:
                data_out[36].append(row_split[1])  # mag1
        elif row.startswith('$GPGGA'):
            if row_split[1] != '' and len(row_split) == 15:
                data_out[0].append(row_split[1])  # utc
                lati = row_split[2]
                data_out[2].append(row_split[2])  # lat
                lat_directioni = row_split[3]
                loni = row_split[4]
                data_out[3].append(row_split[4])  # lon
                lon_directioni = row_split[5]
                data_out[5].append(row_split[7])  # nosats
                data_out[4].append(row_split[9])  # height
                crate = (float(row_split[9]) - float(height1)) * 1000
                if crate > 5000 or crate < -5000:
                    crate = "0"
                data_out[39].append(int(crate))  # crate
                height1 = row_split[9]
                # convert latitude
                if lati.strip():
                    lati = round(floor(float(lati) / 100)
                                 + (float(lati) % 100) / 60, 6)
                    if lat_directioni == 'S':
                        lati = lati * -1
                # convert logitude
                if loni.strip():
                    loni = round(floor(float(loni) / 100)
                                 + (float(loni) % 100) / 60, 6)
                    if lon_directioni == 'W':
                        loni = loni * -1
                speed = distance(lati, loni, lat1, lon1) / 0.1
                if float(speed) > 200 or float(speed) < -200:
                    speed = "0"
                data_out[38].append(speed)  # speed
                lat1 = lati
                lon1 = loni

    total_lines = index
    return data_out
