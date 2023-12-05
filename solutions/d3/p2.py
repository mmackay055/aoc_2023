from solutions.d3 import common
from solutions.d3.common import Item, SymbolEngNumPair

import sys


def process_line(line: str, line_no: int, prev_line: str, prev_items: list[Item]) -> tuple[list[SymbolEngNumPair], list[Item]]:
    items = common.parse_items(line, line_no)

    eng_nums = []

    eng_num_items = common.find_eng_num_same_line(items)
    for pair in eng_num_items:
        eng_nums.append(pair)

    if prev_items is None:
        return (eng_nums, items)

    eng_num_items = common.find_eng_num_diff_line(items, prev_items, len(line) - 1)
    for pair in eng_num_items:
        eng_nums.append(pair)

    eng_num_items = common.find_eng_num_diff_line(prev_items, items, len(prev_line) - 1)
    for pair in eng_num_items:
        eng_nums.append(pair)

    return (eng_nums, items)


def solve(file):
    sum = 0
    index = {}
    prev_items = None
    prev_line = None
    line_no = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            (pairs, prev_items) = process_line(line, line_no, prev_line, prev_items)
            prev_line = line
            line_no += 1
            for p in pairs:
                address = p[0].to_address()
                if address in index:
                    items = index[address]
                    if len(items) > 3:
                        raise Exception('Found element {items} with too many elements')
                    items.append(p[1])
                    index[address] = items
                else:
                    index[address] = [p[0], p[1]]

    for val in index.values():
        if len(val) == 3 and val[0].val == "*":
            sum += int(val[1].val) * int(val[2].val)

    return sum




if __name__ == '__main__':
    print(solve(sys.argv[1]))
