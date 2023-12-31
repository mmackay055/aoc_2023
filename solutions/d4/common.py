def parse_card(line) -> tuple[list[int], list[int]]:
    card_lists = line.split(' | ')
    return (parse_card_list(card_lists[0].strip()),
            parse_card_list(card_lists[1].strip()))


def parse_card_list(card_list: str) -> list[int]:
    return list(map(int, card_list.split()))


def get_match_count(card_list0: list[int], card_list1: list[int]) -> int:
    list0 = set()
    for c in card_list0:
        list0.add(c)

    count = 0
    for c in card_list1:
        if c in card_list0:
            count += 1

    return count
