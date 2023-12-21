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
        if result == 0:
            result = len(common.calc_wins(times[i], distances[i]))
        else:
            result *= len(common.calc_wins(times[i], distances[i]))

    return result


if __name__ == '__main__':
    print(solve(sys.argv[1]))
