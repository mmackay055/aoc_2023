class Item:
    def __init__(self, val: str, start: int, end: int):
        self.val = val
        self.start = start
        self.end = end

    def to_address(self, line_no: int) -> str:
        return f'{line_no}:{self.start}:{self.end}'

    def is_symbol(self) -> str:
        return is_symbol(self.val)

    def __repr__(self) -> str:
        return f'Item(val={self.val}, start={self.start}, end={self.end})'

    def __eq__(self, o):
        return self.val == o.val and self.start == o.start and self.end == o.end


def is_symbol(e: str):
    return (not e.isnumeric()) and e != "."

