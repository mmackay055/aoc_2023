import math


def calc_win_range(time, distance):
    c = -1 * (distance + 1)
    adder = math.sqrt((time * time) - (4 * -1 * c))
    x1 = math.ceil((time * -1 + adder) / -2)
    x2 = math.floor((time * -1 - adder) / -2)
    return (x1, x2)


def calc_range_len(r):
    return r[1] - r[0] + 1
