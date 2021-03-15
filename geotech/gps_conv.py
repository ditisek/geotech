def gps_conv(value):
    from math import floor
    answer = round(floor(float(value) / 100)
                   + (float(value) % 100) / 60, 6)
    return answer
