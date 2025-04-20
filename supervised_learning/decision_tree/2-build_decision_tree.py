#!/usr/bin/env python3
"""
Build decision tree
"""

import numpy as np


def left_child_add_prefix(text):
    """
    Add the left child prefix to the text representation of a subtree
    """
    lines=text.split("\n")
    new_text="    +--"+lines[0]+"\n"
    for x in lines[1:] :
        new_text+=("    |  "+x)+"\n"
    return (new_text)


def right_child_add_prefix(text):
    """
    Add the right child prefix to the text representation of a subtree
    """
    lines=text.split("\n")
    new_text="    +--"+lines[0]+"\n"
    for x in lines[1:] :
        new_text+=("       "+x)+"\n"
    return (new_text)


class Node:
    """
    Class representing a decision node in the tree
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
        Calculates the maximum depth of all nodes below this node

        Returns:
            int: Maximum depth
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
        Counts the number of nodes below this node

        Args:
            only_leaves (bool): If True, counts only leaf nodes

        Returns:
            int: Count of nodes
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

    def __str__(self):
        """
        String representation of the node and its children
        """
        if self.is_root:
            output = f"root [feature={self.feature}, threshold={self.threshold}]"
        else:
            output = f"node [feature={self.feature}, threshold={self.threshold}]"

        if self.left_child:
            output += "\n" + left_child_add_prefix(str(self.left_child).rstrip())
        if self.right_child:
            output += "\n" + right_child_add_prefix(str(self.right_child).rstrip())

        return output


class Leaf(Node):
    """
    Class representing a leaf node in the decision tree
    """
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
        Returns depth for leaf

        Returns:
            int: Depth
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
        Returns count for leaf

        Returns:
            int: Always 1
        """
        return 1

    def __str__(self):
        """
        String representation of the leaf
        """
        return f"-> leaf [value={self.value}]"


class Decision_Tree:
    """
    Class representing a decision tree
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
        """
        Returns max depth of tree

        Returns:
            int: Tree depth
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
        Count total number of nodes in tree

        Args:
            only_leaves (bool): If True, only count leaves

        Returns:
            int: Count of nodes
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """
        String representation of the entire tree
        """
        return self.root.__str__()
