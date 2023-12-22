import sys
from solutions.d6 import common


def parse_line(line):
    vals = line.split(":")[1].strip()
    nums = list(map(int, filter(None, vals.split(" "))))
    return nums


def solve(file):
    result = 0
    times = None
    distances = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            if times is None:
                times = parse_line(line)
            elif distances is None:
                distances = parse_line(line)
            else:
                raise Exception(f'unexpected line: {line}')

    assert len(times) == len(distances)

    for i in range(len(times)):
        r = common.calc_range_len(
            common.calc_win_range(times[i], distances[i]))
        if result == 0:
            result = r
        else:
            result *= r

    return result


if __name__ == '__main__':
    print(solve(sys.argv[1]))
