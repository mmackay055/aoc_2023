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


def check_word(word):
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


def solve(file):

    sum = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip()

            dig_1 = None
            dig_2 = None
            word = ''
            for c in line:
                if c.isdigit():
                    if dig_1 is None:
                        dig_1 = c
                        dig_2 = c
                    else:
                        dig_2 = c
                    word = ''
                else:
                    word += c
                    check = check_word(word)
                    if check is not None:
                        dig = calc_digit(check)
                        if dig is not None:
                            if dig_1 is None:
                                dig_1 = dig
                                dig_2 = dig
                            else:
                                dig_2 = dig
                            word = ''
                    else:
                        word = word[1:]

            cali_val = int(dig_1 + dig_2)
            sum += cali_val

    return sum


if __name__ == '__main__':
    print(solve(sys.argv[1]))
