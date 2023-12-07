class Map:
    def __init__(self, input_start, output_start, span):
        self.input_start = input_start
        self.output_start = output_start
        self.span = span

    def output(self, val: int) -> int:
        if val < self.input_start or val > self.input_start + self.span - 1:
            return -1

        return val - self.input_start + self.output_start

    def __repr__(self):
        return f'Map(input_start={self.input_start}, output_start={self.output_start}, span={self.span})'

    def __eq__(self, o):
        return self.input_start == o.input_start and \
            self.output_start == o.output_start and \
            self.span == o.span


def build_map(line: str) -> Map:
    elms = list(filter(None, line.split(' ')))
    assert len(elms), 3

    return Map(int(elms[1]), int(elms[0]), int(elms[2]))


class Mapper:
    def __init__(self, name: str):
        self.name = name
        self.maps: list[Map] = []

    def add(self, map: Map):
        self.maps.append(map)
        self.maps.sort(key=lambda m: m.input_start)
        return self

    def output(self, val: int) -> int:
        for m in self.maps:
            # TODO improve
            out = m.output(val)
            if out != -1:
                return out
        return val


def build_mapper(line: str) -> Mapper:
    elms = list(filter(None, line.split(' ')))
    assert len(elms), 2

    return Mapper(elms[0])


class Almanac:
    def __init__(self):
        self.mappers = []

    def add(self, mapper: Mapper):
        self.mappers.append(mapper)
        return self

    def calc_location(self, seed: int) -> int:
        for m in self.mappers:
            seed = m.output(seed)
        return seed


class AlmanacDataParser:
    def __init__(self):
        self.almanac = Almanac()
        self.mapper = None

    def process_line(self, line):
        if len(line) > 0:
            if self.mapper is None:
                self.mapper = build_mapper(line)
                self.almanac.add(self.mapper)
            else:
                self.mapper.add(build_map(line))
        else:
            self.mapper = None

    def build(self) -> tuple[Almanac, list[str]]:
        almanac = self.almanac
        self.almanac = None
        self.mapper = None
        return almanac
