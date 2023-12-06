import sys


class Map:
    def __init__(self, input_start, output_start, span):
        self.input_start = input_start
        self.output_start = output_start
        self.span = span

    def output(self, intput: int) -> int:
        return -1


def build_map(line: str) -> Map:
    pass


class Mapper:
    def __init__(self, name: str):
        self.name = name
        self.maps: list[Map] = []

    def add(self, map: Map):
        # sort

        return self


    def output(self, intput: int) -> int:
        return -1


class Almanac:
    def __init__(self):
        self.mappers = []

    def add(self, mapper: Mapper):
        self.mappers.append(mapper)
        return self

    def calc_location(self, seed: int) -> int:
        return -1


def process_line(line):
    pass


def solve(file):
    sum = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            val = process_line(line)
            sum += val
    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
