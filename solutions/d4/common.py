def parse_card(line) -> tuple[list[int], list[int]]:
    card_lists = line.split(' | ')
    return (parse_card_list(card_lists[0].strip()), parse_card_list(card_lists[1].strip()))


def parse_card_list(card_list: str) -> list[int]:
    items = filter(None, card_list.split(' '))
    return list(map(int, items))
