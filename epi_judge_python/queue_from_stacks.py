from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Using 2 stacks:


"""


class Queue:
    def __init__(self):
        self.backwards = []
        self.inorder = []

    def enqueue(self, x: int) -> None:
        self.backwards.append(x)
        return

    def dequeue(self) -> int:
        if self.inorder:
            return self.inorder.pop()
        while len(self.backwards) > 1:
            self.inorder.append(self.backwards.pop())
        return self.backwards.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
