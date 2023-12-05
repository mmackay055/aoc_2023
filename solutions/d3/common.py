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
