def parse_line_id(line) -> tuple[int, str]:
    line_index = line.find(":")
    line_elm = line[:line_index]
    line_id = int(line_elm.split(' ')[1])

    return (line_id, line[line_index + 1:].strip())
