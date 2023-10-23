from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    """
    Need to keep track of max.

    O(1) push and pop
    Option 1: Search for max through underlying array each time, Time: Add, remove - O(1) Max - O(N) Space: O(1)
    Option 2: Have another array with elements in order. Each time you add another element add it in the right spot.
    Each time you remove an element, remove it from the max_array. Time: Add, remove - O(N) Max - O(1) Space O(N)
    Option 3: Keep another array tracking largest element at or below particular spot. 

    Duplicates?

    top: 5, 6, 6, 4, 2
    arr: 6 6 6 4 2
    Time: add, remove O(1), max O(1)

    """

    def __init__(self):
        # Track tuples consisting of (item, max)
        self.stack = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        return self.stack[-1][1]

    def pop(self) -> int:
        return self.stack.pop()[0]

    def push(self, x: int) -> None:
        next_ = (x, max(x, self.max()) if len(self.stack) > 0 else x)
        self.stack.append(next_)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
