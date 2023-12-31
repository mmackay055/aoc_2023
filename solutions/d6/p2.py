import sys
from solutions.d6 import common


def parse_line(line):
    vals = line.split(":")[1].strip()
    nums = vals.split()
    return int("".join(nums))


def solve(file):
    time = None
    distance = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            if time is None:
                time = parse_line(line)
            elif distance is None:
                distance = parse_line(line)
            else:
                raise Exception(f'unexpected line: {line}')
    r = common.calc_win_range(time, distance)
    return common.calc_range_len(r)


if __name__ == '__main__':
    print(solve(sys.argv[1]))
