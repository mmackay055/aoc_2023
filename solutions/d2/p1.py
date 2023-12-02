import sys

from solutions.d2 import common

# need to parse out
# 'Game x:' is the header
#   - where x and be multiple digits

# need to parse game
#  - ',' separates color
#  - ';' separates sets


main_hand_limit = {"red": 12, "green": 13, "blue": 14}


# return game id if it would have been possible 0 if not
def process_line(line) -> int:
    (game_id, game) = common.parse_game_id(line)
    hands_raw = common.parse_game(game)
    hands = list(map(common.parse_hand, hands_raw))

    for h in hands:
        if not common.hand_is_possible(h, main_hand_limit):
            return 0

    return game_id


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
