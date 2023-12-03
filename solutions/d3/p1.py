import sys


# if number found check previous
# if symbol found check current line and previous
# ensure duplicates are not added
def process_line(line: str, prev_line: str, prev_items: list[tuple[bool, int, int]]) -> tuple[list[int], list[tuple[bool, int, int]]]:
    items = parse_items(line)

    if prev_items is None:
        return ([], items)

    eng_nums = calc_eng_num(line, items, prev_line, prev_items)
    return (eng_nums, items)


def parse_items(line: str) -> list[tuple[bool, int, int]]:
    items: list[tuple[bool, int, int]] = []
    n_start = -1
    n_end = -1
    for i in range(len(line)):
        c = line[i]

        if is_symbol(c):
            if n_start > 0 and n_end > 0:
                items.append((False, n_start, n_end))
                n_start = -1
                n_end = -1
            items.append((True, i, i))
        elif c.isnumeric():
            if n_start < 0:
                n_start = i
            n_end = i
        elif n_start >= 0 and n_end >= 0:
            items.append((False, n_start, n_end))
            n_start = -1
            n_end = -1

    return items


def calc_eng_num(line: str, items: list[tuple[bool, int, int]], prev_line: str, prev_items: list[tuple[bool, int, int]]) -> list[int]:
    nums: list[int] = []

    for i in items:
        if i[0]:
            # symbol
            pass
        else:
            # number
            pass
    return nums


def is_adjacent(item: tuple[bool, int, int], other: tuple[bool, int, int], max_i) -> bool:
    i_0 = item[1]
    i_1 = item[2]

    if other[1] > 0:
        o_0 = other[1] - 1
    else:
        o_0 = other[1]

    if other[2] < max_i:
        o_1 = other[2] + 1
    else:
        o_1 = other[2]



def number_is_pn(start: int, end: int, line: str, prev_line: str):
    pass


def get_adjacent_symbols(symbol_loc: int, line: str, prev_line: str):
    pass


def is_symbol(e: str):
    return (not e.isalnum()) and e != "."


def solve(file):
    sum = 0
    index = {}
    prev_items = None
    prev_line = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            (eng_nums, prev_items) = process_line(line, prev_line, prev_items)
            prev_line = line
            for en in eng_nums:
                index.add(en)

    sum = sum(index)
    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
