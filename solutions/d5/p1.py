import sys
from solutions.d5.common import AlmanacDataParser


def solve(file):
    builder = AlmanacDataParser()
    seeds = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            if seeds is None:
                seeds = list(map(int, filter(None, line.split(' ')[1:])))
            else:
                builder.process_line(line)

    almanac = builder.build()
    locations = [almanac.calc_location(seed) for seed in seeds]
    return min(locations)


if __name__ == '__main__':
    print(solve(sys.argv[1]))
