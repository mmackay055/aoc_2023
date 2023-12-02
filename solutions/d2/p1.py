import sys

from solutions.d2 import common


main_hand_limit = {"red": 12, "green": 13, "blue": 14}


def hand_is_possible(hand, hand_limit) -> bool:
    return hand_color_in_limit('blue', hand, hand_limit) and hand_color_in_limit('red', hand, hand_limit) and hand_color_in_limit('green', hand, hand_limit)


def hand_color_in_limit(color, hand, hand_limit) -> bool:
    hand_color = hand[color]
    hand_limit_color = hand_limit[color]
    return hand_color <= hand_limit_color


def process_line(line) -> int:
    (game_id, game) = common.parse_game_id(line)
    hands_raw = common.parse_game(game)
    hands = list(map(common.parse_hand, hands_raw))

    for h in hands:
        if not hand_is_possible(h, main_hand_limit):
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
