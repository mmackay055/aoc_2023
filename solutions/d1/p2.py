import sys


def calc_digit(word):
    if word == 'one':
        return '1'
    if word == 'two':
        return '2'
    if word == 'three':
        return '3'
    if word == 'four':
        return '4'
    if word == 'five':
        return '5'
    if word == 'six':
        return '6'
    if word == 'seven':
        return '7'
    if word == 'eight':
        return '8'
    if word == 'nine':
        return '9'
    return None


def starts_with(word):
    if 'one'.startswith(word):
        return word
    if 'two'.startswith(word):
        return word
    if 'three'.startswith(word):
        return word
    if 'four'.startswith(word):
        return word
    if 'five'.startswith(word):
        return word
    if 'six'.startswith(word):
        return word
    if 'seven'.startswith(word):
        return word
    if 'eight'.startswith(word):
        return word
    if 'nine'.startswith(word):
        return word
    return None


def ends_with(word):
    if 'one'.endswith(word):
        return word
    if 'two'.endswith(word):
        return word
    if 'three'.endswith(word):
        return word
    if 'four'.endswith(word):
        return word
    if 'five'.endswith(word):
        return word
    if 'six'.endswith(word):
        return word
    if 'seven'.endswith(word):
        return word
    if 'eight'.endswith(word):
        return word
    if 'nine'.endswith(word):
        return word
    return None


def process_line(line):
    digs1 = find_forward(line)
    digs2 = find_reverse(line)

    return int(digs1 + digs2)


def find_forward(line):
    word = ''
    for i in range(len(line)):
        c = line[i]
        if c.isdigit():
            return c
        word += c
        check = starts_with(word)
        if check is not None:
            dig = calc_digit(check)
            if dig is not None:
                return dig
        else:
            while len(word) > 0 and starts_with(word) is None:
                word = word[1:]


def find_reverse(line):
    word = ''
    for i in range(len(line) - 1, -1, -1):
        c = line[i]
        if c.isdigit():
            return c
        word = c + word
        check = ends_with(word)
        if check is not None:
            dig = calc_digit(check)
            if dig is not None:
                return dig
        else:
            while len(word) > 0 and ends_with(word) is None:
                word = word[:-1]


def solve(file):

    sum = 0
    with open(file) as f:
        for line in f:
            linez = line.rstrip()
            sum += process_line(linez)
    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
