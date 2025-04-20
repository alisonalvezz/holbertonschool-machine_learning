#!/usr/bin/env python3
"""
Build decision tree
"""

import numpy as np


def left_child_add_prefix(text):
    """
    Add the left child prefix to the text representation of a subtree
    """
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += ("    |  " + x) + "\n"
    return new_text


def right_child_add_prefix(text):
    """
    Add the right child prefix to the text representation of a subtree
    """
    lines = text.split("\n")
    new_text = "    +--" + lines[0] + "\n"
    for x in lines[1:]:
        new_text += ("       " + x) + "\n"
    return new_text


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
        self.lower = {}
        self.upper = {}

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

    def get_leaves_below(self):
        """
        Retrieves all leaf nodes under this node

        Returns:
            list: List of leaf nodes (Leaf instances)
        """
        leaves = []
        if self.left_child:
            leaves += self.left_child.get_leaves_below()
        if self.right_child:
            leaves += self.right_child.get_leaves_below()
        return leaves

    def update_bounds_below(self):
        """
        Recursively update lower and upper bounds for each node in the tree.
        The bounds are stored in dictionaries self.lower and self.upper.
        """
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -1*np.inf}

        if self.left_child:
            self.left_child.lower = self.lower.copy()
            self.left_child.upper = self.upper.copy()
            self.left_child.lower[self.feature] = self.threshold

        if self.right_child:
            self.right_child.lower = self.lower.copy()
            self.right_child.upper = self.upper.copy()
            self.right_child.upper[self.feature] = self.threshold

        for child in [self.left_child, self.right_child]:
            if child:
                child.update_bounds_below()

    def update_indicator(self):
        """
        Updates the indicator function for the current node.
        The indicator function is stored in the 'indicator' attribute.
        """
        def is_large_enough(x):
            """
            Checks if the features of individuals are
            greater than the lower bounds
            for each feature.

            Args:
                x (np.ndarray): 2D array of shape

            Returns:
                np.ndarray: 1D array of booleans indicating whether each
                individual satisfies the lower bounds.
            """
            return np.array([np.greater(x[:, key], self.lower[key])
                             for key in self.lower.keys()]).all(axis=0)

        def is_small_enough(x):
            """
            Checks if the features of individuals are less than or equal
            to the upper bounds
            for each feature.

            Args:
                x (np.ndarray): 2D array of shape (n_individuals, n_features)

            Returns:
                np.ndarray: 1D array of booleans indicating
                        whether each individual
                            satisfies the upper bounds.
            """
            return np.array([np.less_equal(x[:, key], self.upper[key])
                             for key in self.upper.keys()]).all(axis=0)

        self.indicator = lambda x: np.all(np.array(
            [is_large_enough(x), is_small_enough(x)]), axis=0)


    def __str__(self):
        """
        String representation of the node and its children
        """
        if self.is_root:
            output = f"root [feature={self.feature},\
                threshold={self.threshold}]"
        else:
            output = f"node [feature={self.feature},\
                threshold={self.threshold}]"

        if self.left_child:
            output += "\n" +\
                left_child_add_prefix(str(self.left_child).rstrip())
        if self.right_child:
            output += "\n" +\
                right_child_add_prefix(str(self.right_child).rstrip())

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
        self.lower = {}
        self.upper = {}

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

    def get_leaves_below(self):
        """
        Returns self as the only leaf below

        Returns:
            list: A list containing this leaf
        """
        return [self]

    def update_bounds_below(self):
        """
        Leaf does not have children, so nothing to update.
        """
        pass

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

    def get_leaves(self):
        """
        Retrieves all leaf nodes in the tree

        Returns:
            list: List of all leaves in the tree
        """
        return self.root.get_leaves_below()

    def update_bounds(self):
        """
        Initiate bounds computation for the entire tree from the root.
        """
        self.root.update_bounds_below()

    def __str__(self):
        """
        String representation of the entire tree
        """
        return self.root.__str__()
