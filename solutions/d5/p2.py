import sys
from solutions.d5.common import AlmanacDataParser


def parse_seeds(line):
    start = -1

    seed_ranges = []
    seeds = list(map(int, filter(None, line.split(' ')[1:])))

    for s in seeds:
        if start < 0:
            start = int(s)
        else:
            seed_ranges.append((start, int(s) + start))
            start = -1

    return seed_ranges


def solve(file):
    builder = AlmanacDataParser()
    seeds = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            if seeds is None:
                seeds = parse_seeds(line)
            else:
                builder.process_line(line)

    almanac = builder.build()

    locations = []
    for sr in seeds:
        for s in range(sr[0], sr[1]):
            locations.append(almanac.calc_location(s))
    return min(locations)


if __name__ == '__main__':
    print(solve(sys.argv[1]))
