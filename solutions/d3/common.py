class Item:
    def __init__(self, val: str, line_no: int, start: int, end: int):
        self.val = val
        self.line_no = line_no
        self.start = start
        self.end = end

    def to_address(self) -> str:
        return f'{self.line_no}:{self.start}:{self.end}'

    def is_symbol(self) -> str:
        return is_symbol(self.val)

    def __repr__(self) -> str:
        return f'Item(val={self.val}, line_no={self.line_no}, start={self.start}, end={self.end})'

    def __eq__(self, o):
        return self.val == o.val and self.line_no == o.line_no and self.start == o.start and self.end == o.end


def is_symbol(e: str):
    return (not e.isnumeric()) and e != "."


def parse_items(line: str, line_no: int) -> list[Item]:
    items: list[Item] = []
    n_start = -1
    n_end = -1
    for i in range(len(line)):
        c = line[i]

        if is_symbol(c):
            if n_start >= 0 and n_end >= 0:
                items.append(Item(line[n_start: n_end + 1], line_no, n_start, n_end))
                n_start = -1
                n_end = -1
            items.append(Item(line[i: i + 1], line_no, i, i))
        elif c.isnumeric():
            if n_start < 0:
                n_start = i
            n_end = i
        elif n_start >= 0 and n_end >= 0:
            items.append(Item(line[n_start: n_end + 1], line_no, n_start, n_end))
            n_start = -1
            n_end = -1

    if n_start >= 0 and n_end >= 0:
        items.append(Item(line[n_start: n_end + 1], line_no, n_start, n_end))

    return items


def find_eng_num_same_line(items: list[Item]) -> list[Item]:
    nums: list[Item] = []

    # check same line
    for i in range(len(items)):
        if not items[i].is_symbol():
            if i > 0 and items[i - 1].is_symbol() and is_engnum_same_line(items[i], items[i - 1]):
                nums.append(items[i])
            elif i < (len(items) - 1) and items[i + 1].is_symbol() and is_engnum_same_line(items[i], items[i + 1]):
                nums.append(items[i])

    return nums


def is_engnum_same_line(num: Item, symbol: Item) -> bool:
    return (num.start - 1 == symbol.end) or (num.end + 1 == symbol.start)


def find_eng_num_diff_line(items: list[Item], symbols: list[Item], max_i: int) -> list[Item]:
    nums: list[Item] = []

    # TODO save where left off in search
    for item in items:
        if not item.is_symbol():
            for symbol in symbols:
                if symbol.is_symbol() and is_engnum_diff_line(item, symbol, max_i):
                    nums.append(item)
                    break

    return nums


def is_engnum_diff_line(num: Item, sym: Item, max_i: int) -> bool:
    n_0 = num.start
    n_1 = num.end

    if sym.start > 0:
        s_0 = sym.start - 1
    else:
        s_0 = sym.start

    if sym.end < max_i:
        s_1 = sym.end + 1
    else:
        s_1 = sym.end

    return (n_0 >= s_0 and n_0 <= s_1) or (n_1 >= s_0 and n_1 <= s_1)
