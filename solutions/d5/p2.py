import sys
from solutions.d5.common import AlmanacDataParser


def parse_seeds(line):
    start = -1

    seed_ranges = []
    seeds = list(map(int, line.split()[1:]))

    for s in seeds:
        if start < 0:
            start = int(s)
        else:
            seed_ranges.append((start, int(s) + start))
            start = -1

    return seed_ranges


def solve(file):
    builder = AlmanacDataParser()
    seed_ranges = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            if seed_ranges is None:
                seed_ranges = parse_seeds(line)
            else:
                builder.process_line(line)

    almanac = builder.build()

    min = -1
    for sr in seed_ranges:
        loc = almanac.calc_location(sr)
        if min < 0 or loc[0][0] < min:
            min = loc[0][0]
    return min


if __name__ == '__main__':
    print(solve(sys.argv[1]))
