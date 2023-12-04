import sys
from typing import TypeAlias

# TODO delete?
# class Item:
#    def __init__(self, symbol: bool, index_start: int, index_end: int):
#        self.symbol = symbol
#        self.index_start = index_start
#        self.index_end = index_end

Item: TypeAlias = tuple[bool, int, int]


# if number found check previous
# if symbol found check current line and previous
# ensure duplicates are not added
def process_line(line: str, prev_line: str, prev_items: list[Item]) -> tuple[list[int], list[Item]]:
    items = parse_items(line)

    eng_nums = []

    eng_num_items = find_eng_num_same_line(items)
    for en in eng_num_items:
        eng_nums.append(to_eng_num(en, line))

    if prev_items is None:
        return (eng_nums, items)

    eng_num_items = find_eng_num_diff_line(items, prev_items, len(line) - 1)
    for en in eng_num_items:
        eng_nums.append(to_eng_num(en, line))

    eng_num_items = find_eng_num_diff_line(prev_items, items, len(line) - 1)
    for en in eng_num_items:
        eng_nums.append(to_eng_num(en, prev_line))

    return (eng_nums, items)


def parse_items(line: str) -> list[Item]:
    items: list[Item] = []
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


def to_eng_num(item: Item, line: str) -> int:
    return int(line[item[1]:item[2] + 1])


def find_eng_num_same_line(items: list[Item]) -> list[Item]:
    nums: list[Item] = []

    # check same line
    for i in range(len(items)):
        if not items[i][0]:
            if i > 0 and (items[i - 1])[0] and is_engnum_same_line(items[i], items[i - 1]):
                nums.append(items[i])
            elif i < len(items) - 1 and items[i + 1][0] and is_engnum_same_line(items[i], items[i + 1]):
                nums.append(items[i])

    return nums


def is_engnum_same_line(num: Item, symbol: Item) -> bool:
    n_0 = num[1]
    n_1 = num[2]
    s_0 = symbol[1]
    s_1 = symbol[2]

    return (n_0 - 1 == s_1) or (n_1 + 1 == s_0)


def get_next(i: int, items: list[Item]) -> Item:
    if i >= len(items):
        return items[len(items) - 1]
    return items[i]


def find_eng_num_diff_line(items: list[Item], symbols: list[Item], max_i: int) -> list[Item]:
    nums: list[Item] = []

    # TODO save where left off in search
    for item in items:
        if not item[0]:
            for symbol in symbols:
                if symbol[0] and is_engnum_diff_line(item, symbol, max_i):
                    nums.append(item)
                    break

    return nums


def is_engnum_diff_line(num: Item, symbol: Item, max_i: int) -> bool:
    n_0 = num[1]
    n_1 = num[2]

    if symbol[1] > 0:
        s_0 = symbol[1] - 1
    else:
        s_0 = symbol[1]

    if symbol[2] < max_i:
        s_1 = symbol[2] + 1
    else:
        s_1 = symbol[2]

    return (n_0 >= s_0 and n_0 <= s_1) or (n_1 >= s_0 and n_1 <= s_1)


def is_symbol(e: str):
    return (not e.isnumeric()) and e != "."


def solve(file):
    sum = 0
    index = set()
    prev_items = None
    prev_line = None
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            (eng_nums, prev_items) = process_line(line, prev_line, prev_items)
            prev_line = line
            for en in eng_nums:
                index.add(en)

    for i in index:
        sum += i
    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
