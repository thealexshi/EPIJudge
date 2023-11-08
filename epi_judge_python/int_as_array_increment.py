from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    res = []

    carry = True
    for i in reversed(range(len(A))):
        digit = A[i]
        if carry:
            next_ = digit + 1
        else:
            next_ = digit
        res.append(next_ % 10)
        carry = next_ >= 10
    
    if carry:
        res.append(1)

    res.reverse()
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
