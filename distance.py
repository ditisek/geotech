def distance(lat1, lng1, lat2, lng2):
    """
    Calculate distance between two gps co-ordinates

    :param lat1: Latitude from first point
    :param lng1: Longitude from first point
    :param lat2: Latitude from second point
    :param lng2: Longitude from second point
    :return: Distance between points
    """
    # return distance as meter if you want km distance, remove "* 1000"
    from math import sin, cos, atan2, sqrt, pi

    radius = 6371 * 1000

    dLat = (lat2-lat1) * pi / 180
    dLng = (lng2-lng1) * pi / 180

    lat1 = lat1 * pi / 180
    lat2 = lat2 * pi / 180

    val = sin(dLat/2) * sin(dLat/2) + sin(dLng/2) * \
          sin(dLng/2) * cos(lat1) * cos(lat2)
    ang = 2 * atan2(sqrt(val), sqrt(1-val))
    return radius * ang
