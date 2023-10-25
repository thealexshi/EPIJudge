from typing import List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree == None:
        return []

    q = deque([(tree, 1)])

    res = []
    while q:
        node, level = q.popleft()
        if len(res) < level:
            res.append([])
        res[level - 1].append(node.data)
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
