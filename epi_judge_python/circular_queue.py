from test_framework import generic_test
from test_framework.test_failure import TestFailure

"""
Use an array to implement a queue

enqueue and dequeue must be O(1)

Most obvious solution: enqueue elements at back of array, dequeue elements at front of array. but each
time you dequeue, you need to shift elements forward which is O(N)
"""


class Queue:
    def __init__(self, capacity: int) -> None:
        self.arr = [0]*capacity
        # index of the first element
        self.head = 0
        # index of the next place to put element
        self.tail = 0
        self.num_elements = 0

    def enqueue(self, x: int) -> None:
        if self.num_elements == len(self.arr):
            entries = self.arr[self.head:] + self.arr[:self.head]
            self.arr = (entries) + [0]*(self.num_elements*2)
            self.head, self.tail = 0, self.num_elements
        self.arr[self.tail] = x
        self.tail = (self.tail + 1) % len(self.arr)
        self.num_elements += 1

    def dequeue(self) -> int:
        val = self.arr[self.head]
        self.head = (self.head + 1) % len(self.arr)
        self.num_elements -= 1
        return val

    def size(self) -> int:
        return self.num_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
