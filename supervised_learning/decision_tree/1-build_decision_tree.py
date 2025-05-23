#!/usr/bin/env python3
"""
Build decision tree
"""

import numpy as np


class Node:
    """
    node
    """
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
        Calculates the maximum depth of all nodes below this node,
        including leaf nodes.

        This method works recursively, searching for child nodes and
        calculating their depth. Then it returns the maximum depth value
        among the child nodes, incremented by 1 for the current node.

        Returns:
        int: The maximum depth of all nodes below this node.
        """
        if self.is_leaf:
            return self.depth
        if self.left_child:
            left_depth = self.left_child.max_depth_below()
        else:
            return 0
        if self.right_child:
            right_depth = self.right_child.max_depth_below()
        else:
            return 0
        depth = max(right_depth, left_depth)
        return depth

    def count_nodes_below(self, only_leaves=False):
        """
        Counts the number of nodes below this node, including internal nodes
        and leaves. If only_leaves is True, only counts the leaf nodes.

        This method works recursively, counting nodes in the left and right
        subtrees, and returns the total number of nodes.

        Attributes:
        only_leaves (bool): Whether to count only
        leaf nodes (default is False).

        Returns:
        int: The number of nodes below this node.
        """
        if self.is_leaf:
            return 1
        count = 0
        if self.left_child:
            count += self.left_child.count_nodes_below(only_leaves)
        if self.right_child:
            count += self.right_child.count_nodes_below(only_leaves)
        if not only_leaves:
            count += 1
        return count


class Leaf(Node):
    """
    leaf
    """
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """ max depth below """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """ count nodes below """
        return 1


class Decision_Tree:
    """
    decision tree
    """
    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """ depth """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """ count nodes """
        return self.root.count_nodes_below(only_leaves=only_leaves)
