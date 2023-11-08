from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    """
    Example: [1, 0, 0]

    - Add one to the last digit in the array
    - Go through the array from back to front
      - If current digit is 10, replace it with 0 and add one to the next digit. If next digit doesn't exist,
      append 1. 
      - Else, break.
    """

    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
