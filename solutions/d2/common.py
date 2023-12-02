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


def get_minimum_hand(hands):
    blue = 0
    green = 0
    red = 0

    for h in hands:
        b = h['blue']
        if b > blue:
            blue = b
        r = h['red']
        if r > red:
            red = r
        g = h['green']
        if g > green:
            green = g

    return {'blue': blue, 'red': red, 'green': green}
