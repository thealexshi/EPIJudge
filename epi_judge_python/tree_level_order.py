from typing import List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if tree == None:
        return []

    current_depth_nodes = [tree]

    res = []
    while current_depth_nodes:
        res.append([c.data for c in current_depth_nodes])
        next_level = []
        for c in current_depth_nodes:
            if c.left:
                next_level.append(c.left)
            if c.right:
                next_level.append(c.right)
        current_depth_nodes = next_level

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
