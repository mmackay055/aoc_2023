import sys
from solutions.common import parse_line_id
from solutions.d4 import common


def process_line(line):
    (id, line) = parse_line_id(line)
    (card_list0, card_list1) = common.parse_card(line)

    return common.get_match_count(card_list0, card_list1)


def count_wins(i, wins: int, limit: int, wins_list: list[int]) -> int:
    if i >= len(wins_list) or i > limit:
        return wins

    wins += wins_list[i]
    i += 1
    if i < len(wins_list):
        return count_wins(i, wins, i + wins_list[i], wins_list)

    return wins


def add_copies(count, copies, start, end):
    amount = add_to_copies(start, copies, 1)
    for i in range(start + 1, start + count + 1):
        if i < end:
            add_to_copies(i, copies, amount)
        else:
            break
    return copies


def add_to_copies(i, copies_list, amount):
    if i >= len(copies_list):
        copies_list.append(amount)
    else:
        copies_list[i] += amount
    return copies_list[i]


def solve(file):
    matches = []
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            matches.append(process_line(line))

    copies = []
    for i in range(len(matches)):
        copies = add_copies(matches[i], copies, i, len(matches))

    sum = 0
    for c in copies:
        sum += c
    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
