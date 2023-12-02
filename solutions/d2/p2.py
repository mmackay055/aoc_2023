import sys
from solutions.d2 import common

main_hand_limit = {"red": 12, "green": 13, "blue": 14}


# return game id if it would have been possible 0 if not
def process_line(line) -> int:
    (game_id, game) = common.parse_game_id(line)
    hands_raw = common.parse_game(game)
    hands = list(map(common.parse_hand, hands_raw))

    min_hand = get_minimum_hand(hands)

    cube = 1

    for v in min_hand.values():
        cube *= v

    return cube


def get_minimum_hand(hands):
    blue_min = 0
    green_min = 0
    red_min = 0

    for h in hands:
        blue_min = get_required_blocks(h, 'blue', blue_min)
        red_min = get_required_blocks(h, 'red', red_min)
        green_min = get_required_blocks(h, 'green', green_min)

    return {'blue': blue_min, 'red': red_min, 'green': green_min}


def get_required_blocks(hand, color, cur_min):
    min = hand[color]
    if min > cur_min:
        return min
    return cur_min


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
