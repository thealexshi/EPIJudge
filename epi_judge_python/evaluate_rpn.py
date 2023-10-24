from test_framework import generic_test
from collections import deque


def evaluate(expression: str) -> int:
    """
    ex: 3, 4, +, 2, x, 1 + = (3+4)*2+1


    """
    stack = []
    operators = {
        '+': lambda y, x: y + x,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x*y,
        '/': lambda y, x: x // y
    }

    for token in expression.split(','):
        if token in operators:
            stack.append(operators[token](stack.pop(), stack.pop()))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
