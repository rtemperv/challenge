from .binary_tree import BinaryNode
from typing import Optional


class BinarySearchNode(BinaryNode):
    """
    Extend BinaryNode to enforce binary search tree ordering
    """

    def __init__(self, value, *, lnode=None, rnode=None, payload=None):
        super().__init__(value, lnode=lnode, rnode=rnode, payload=payload)

    def get_upper_bound(self):
        """
        Find the lower bound for the right child of this node
        """
        node = self.parent
        old_node = self
        while node:
            if node.lnode == old_node:
                return node.value
            old_node = node
            node = old_node.parent

    def get_lower_bound(self):
        """
        Find the lower bound for the left child of this node
        """
        node = self.parent
        old_node = self
        while node:
            if node.rnode == old_node:
                return node.value
            old_node = node
            node = old_node.parent


class BinarySearchTree(object):
    """
    Wrapper around a binary search node with insert search and remove instructions
    """

    def __init__(self):
        self.root = None

    def _insert(self, node: BinarySearchNode):
        """
        Insert a node in the binary search tree
        """
        if not self.root:
            self.root = node
            return

        parent_node = None
        next_node = self.root
        is_smaller = False

        while next_node:
            if node.value >= next_node.value:
                parent_node, next_node, is_smaller = next_node, next_node.rnode, False
            else:
                parent_node, next_node, is_smaller = next_node, next_node.lnode, True

        if is_smaller:
            parent_node.lnode = node
        else:
            parent_node.rnode = node

    def insert(self, value, payload):
        self._insert(BinarySearchNode(value, payload=payload))

    def _search(self, value):

        if not self.root:
            raise IndexError('Value not present in binary tree')

        current_node = self.root

        while current_node and current_node.value != value:
            current_node = current_node.lnode if current_node.value > value else current_node.rnode

        if current_node:
            return current_node

        raise IndexError('Value not present in binary tree')

    def search(self, value):

        return self._search(value).payload


