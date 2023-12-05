import sys
from solutions.common import parse_line_id
from solutions.d4 import common


def process_line(line):
    (id, line) = parse_line_id(line)
    (card_list0, card_list1) = common.parse_card(line)

    list0 = set()
    for c in card_list0:
        list0.add(c)

    points = 0
    for c in card_list1:
        if c in list0:
            if points < 1:
                points = 1
            else:
                points *= 2

    return points


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
