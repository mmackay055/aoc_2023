import sys

# need to parse out
# 'Game x:' is the header
#   - where x and be multiple digits

# need to parse game
#  - ',' separates color
#  - ';' separates sets


main_hand_limit = {"red": 12, "green": 13, "blue": 14}


# return game id if it would have been possible 0 if not
def process_line(line) -> int:
    (game_id, game) = parse_game_id(line)
    hands_raw = parse_game(game)
    hands = list(map(parse_hand, hands_raw))

    for h in hands:
        if not hand_is_possible(h, main_hand_limit):
            return 0

    return game_id


# return single integer and remaining line
def parse_game_id(line) -> tuple[int, str]:

    game_index = line.find(":")
    game_elm = line[:game_index]
    game_id = int(game_elm.split(' ')[1])

    return (game_id, line[game_index + 1:].strip())


# return game list of hands
def parse_game(game) -> list[str]:
    games = game.split(";")
    return list(map(str.strip, games))


# return dic of colors
def parse_hand(hand_raw) -> dict[str, int]:
    color_raw_elms = list(map(str.strip, hand_raw.split(",")))
    color_elms = list(map(parse_color, color_raw_elms))
    return repair_map(dict(color_elms))


def repair_map(color_map) -> dict[str, int]:
    if 'blue' not in color_map:
        color_map['blue'] = 0
    if 'red' not in color_map:
        color_map['red'] = 0
    if 'green' not in color_map:
        color_map['green'] = 0
    return color_map


def parse_color(color_raw) -> tuple[str, int]:
    elms = color_raw.split(' ')
    return (elms[1], int(elms[0]))


def hand_is_possible(hand, hand_limit) -> bool:
    return hand_color_in_limit('blue', hand, hand_limit) and hand_color_in_limit('red', hand, hand_limit) and hand_color_in_limit('green', hand, hand_limit)


def hand_color_in_limit(color, hand, hand_limit) -> bool:
    hand_color = hand[color]
    hand_limit_color = hand_limit[color]
    return hand_color <= hand_limit_color


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
