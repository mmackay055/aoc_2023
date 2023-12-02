import sys


def process_line(line):

    dig_1 = None
    dig_2 = None
    for c in line:
        if c.isdigit():
            if dig_1 is None:
                dig_1 = c
                dig_2 = c
            else:
                dig_2 = c

    return int(dig_1 + dig_2)


def solve(file):

    sum = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            cali_val = process_line(line)
            sum += cali_val

    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
