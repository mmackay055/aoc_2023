class Map:
    def __init__(self, input_start: int, output_start: int, span: int):
        self.input_start = input_start
        self.output_start = output_start
        self.span = span

    def output(self, val: tuple[int, int]) -> tuple[int, int]:
        val_0 = val[0]
        val_1 = val[1]

        if val_0 < self.input_start or self.input_start > val_1:
            (-1, -1)

        out_0 = val_0 - self.input_start + self.output_start
        if out_0 < self.output_start:
            out_0 = self.output_start

        out_1 = val_1 - self.input_start + self.output_start
        if out_1 > self.output_start + self.span:
            out_1 = self.output_start + self.span

        return (out_0, out_1)

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

    def output(self, val: tuple[int, int]) -> list[tuple[int, int]]:
        v0 = val[0]
        v1 = val[1]
        vals: list[tuple[int, int]] = []

        for m in self.maps:

            s0 = v0
            s1 = v1

            if v0 < m.input_start and v1 >= m.input_start:
                vals.append((v0, m.input_start - 1))
                s0 = m.input_start
            elif v1 < m.input_start or v0 > v1:
                break
            elif v0 > m.input_start + m.span - 1:
                break

            if v1 > m.input_start + m.span - 1:
                s1 = m.input_start + m.span - 1

            v0 = m.input_start + m.span
            vals.append(m.output((s0, s1)))

        if v0 <= v1:
            vals.append((v0, v1))

        return vals


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

    def calc_location(self, seed_range: tuple[int, int]) -> list[tuple[int, int]]:
        ranges: list[tuple[int, int]] = [seed_range]
        for m in self.mappers:
            new_ranges: list[tuple[int, int]] = []
            for r in ranges:
                new_ranges = new_ranges + m.output(r)
            ranges = new_ranges

        ranges.sort(key=lambda m: m[0])
        return ranges


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

    def build(self) -> Almanac:
        almanac = self.almanac
        self.almanac = None
        self.mapper = None
        return almanac
