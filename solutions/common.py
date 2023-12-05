def parse_line_id(line: str) -> tuple[int, str]:
    line_index = line.find(":")
    line_elm = line[:line_index]

    line_id = int(list(filter(None, line_elm.split(' ')))[1])

    return (line_id, line[line_index + 1:].strip())
