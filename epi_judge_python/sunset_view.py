from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    """
    EAST TO WEST ORDER

    Building at position i can view sunset if:
    - all buildings from positions 0 to i-1 have a height <= sequence[i]

    Option 1: For each building, scan all previous buildings to make sure heights are less than or equal to 
    current. Time: O(N^2). 
    Option 2: Scan right to left, keep track of running max which you compare to each position. Time: O(N)

    1 3 2
    max = 3

    """
    """
    My solution (more optimal)
    """
    # max_ = float('-inf')
    # res = []

    # for index in range(len(sequence)-1, -1, -1):
    #     height = sequence[index]
    #     if height > max_:
    #         res.append(index)
    #     max_ = max(max_, height)

    # return res

    """
    Book's solution
    """
    res = []

    for index, height in enumerate(sequence):
        # Do we need to pop elements off first?
        while res and sequence[res[-1]] <= height:
            res.pop()
        res.append(index)

    res.reverse()
    return res


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
