import sys
from typing import TypeAlias

# TODO delete?
# class Item:
#    def __init__(self, symbol: bool, index_start: int, index_end: int):
#        self.symbol = symbol
#        self.index_start = index_start
#        self.index_end = index_end

Item: TypeAlias = tuple[str, int, int]
EngItem: TypeAlias = tuple[str, int]


# if number found check previous
# if symbol found check current line and previous
# ensure duplicates are not added
def process_line(line: str, line_no: int, prev_line: str, prev_items: list[Item]) -> tuple[list[EngItem], list[Item]]:
    items = parse_items(line)

    eng_nums = []

    eng_num_items = find_eng_num_same_line(items)
    for en in eng_num_items:
        eng_nums.append(to_eng_item(en, line_no))

    if prev_items is None:
        return (eng_nums, items)

    eng_num_items = find_eng_num_diff_line(items, prev_items, len(line) - 1)
    for en in eng_num_items:
        eng_nums.append(to_eng_item(en, line_no))

    eng_num_items = find_eng_num_diff_line(prev_items, items, len(prev_line) - 1)
    for en in eng_num_items:
        eng_nums.append(to_eng_item(en, line_no - 1))

    return (eng_nums, items)


def to_eng_item(item: Item, line_no: int) -> EngItem:
    return (f'{line_no}:{item[1]}:{item[2]}', to_eng_num(item))


def parse_items(line: str) -> list[Item]:
    items: list[Item] = []
    n_start = -1
    n_end = -1
    for i in range(len(line)):
        c = line[i]

        if is_symbol(c):
            if n_start >= 0 and n_end >= 0:
                items.append((line[n_start: n_end + 1], n_start, n_end))
                n_start = -1
                n_end = -1
            items.append((None, i, i))
        elif c.isnumeric():
            if n_start < 0:
                n_start = i
            n_end = i
        elif n_start >= 0 and n_end >= 0:
            items.append((line[n_start: n_end + 1], n_start, n_end))
            n_start = -1
            n_end = -1

    if n_start >= 0 and n_end >= 0:
        items.append((line[n_start: n_end + 1], n_start, n_end))

    return items


def to_eng_num(item: Item) -> int:
    return int(item[0])


def find_eng_num_same_line(items: list[Item]) -> list[Item]:
    nums: list[Item] = []

    # check same line
    for i in range(len(items)):
        if not item_is_symbol(items[i]):
            if i > 0 and item_is_symbol(items[i - 1]) and is_engnum_same_line(items[i], items[i - 1]):
                nums.append(items[i])
            elif i < (len(items) - 1) and item_is_symbol(items[i + 1]) and is_engnum_same_line(items[i], items[i + 1]):
                nums.append(items[i])

    return nums


def item_is_symbol(item: Item) -> bool:
    return item[0] is None


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
        if not item_is_symbol(item):
            for symbol in symbols:
                if item_is_symbol(symbol) and is_engnum_diff_line(item, symbol, max_i):
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
    index = {}
    prev_items = None
    prev_line = None
    line_no = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            (eng_items, prev_items) = process_line(line, line_no, prev_line, prev_items)
            prev_line = line
            line_no += 1
            for ei in eng_items:
                if ei[0] in index and index[ei[0]] != ei[1]:
                    raise Exception('duplicate entry with differing value')
                index[ei[0]] = ei[1]

    for val in index.values():
        sum += val
    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
