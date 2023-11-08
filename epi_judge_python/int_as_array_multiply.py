from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    """
    Figure out which sign it is
    Convert num to positive



    """
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    

    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
