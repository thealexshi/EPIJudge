from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    print(x)
    res = []
    is_neg = x < 0
    
    x = abs(x)
    if x == 0:
        res.append('0')

    while x > 0:
        digit = x % 10
        res.append(chr(ord('0') + digit))
        x //= 10

    if is_neg:
        res.append('-')

    res.reverse()
    return ''.join(res)


def string_to_int(s: str) -> int:
    """
    Needs to handle +314
    """
    res = 0
    is_neg = s[0] == '-'

    place = 0
    for c in reversed(s):
        if c == '+' or c == '-':
            continue
        res += (10**place)*(ord(c) - ord('0'))
        place += 1

    return res*-1 if is_neg else res


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
