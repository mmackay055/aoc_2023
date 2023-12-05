import sys
from typing import TypeAlias
from solutions.d3 import common
from solutions.d3.common import Item


def to_eng_num(item: Item) -> int:
    return int(item.val)


EngItem: TypeAlias = tuple[str, int]


def process_line(line: str, line_no: int, prev_line: str, prev_items: list[Item]) -> tuple[list[EngItem], list[Item]]:
    items = common.parse_items(line, line_no)

    eng_nums = []

    eng_num_items = common.find_eng_num_same_line(items)
    for pair in eng_num_items:
        eng_nums.append(to_eng_item(pair[1]))

    if prev_items is None:
        return (eng_nums, items)

    eng_num_items = common.find_eng_num_diff_line(items, prev_items, len(line) - 1)
    for pair in eng_num_items:
        eng_nums.append(to_eng_item(pair[1]))

    eng_num_items = common.find_eng_num_diff_line(prev_items, items, len(prev_line) - 1)
    for pair in eng_num_items:
        eng_nums.append(to_eng_item(pair[1]))

    return (eng_nums, items)


def to_eng_item(item: Item) -> EngItem:
    return (f'{item.to_address()}', to_eng_num(item))


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
