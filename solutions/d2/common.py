def parse_game(game) -> list[str]:
    games = game.split(";")
    return list(map(str.strip, games))


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
