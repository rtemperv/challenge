import sys
from typing import Iterator, Optional, List
from src.structures import Queue


class BinaryNode(object):
    """
    Binary node data structure
    """

    def __init__(self, value, *, lnode=None, rnode=None):
        # These will be set by the properties
        self.parent = None
        self.previous_node = None
        self._lnode = None
        self._rnode = None

        # Left and right node and the value of the node
        self.lnode = lnode
        self.rnode = rnode
        self.value = value

    @property
    def lnode(self) -> Optional['BinaryNode']:
        return self._lnode

    @lnode.setter
    def lnode(self, node: Optional['BinaryNode']):
        if node and not isinstance(node, self.__class__):
            raise ValueError('node should be an instance of the Node class')

        if node:
            node.parent = self

        self._lnode = node

    @property
    def rnode(self) -> Optional['BinaryNode']:
        return self._rnode

    @rnode.setter
    def rnode(self, node: Optional['BinaryNode']):
        if node and not isinstance(node, self.__class__):
            raise ValueError('node should be an instance of the Node class')

        if node:
            node.parent = self

        self._rnode = node

    @property
    def min_value(self):
        """
        Get the minimum value of the current node and all the children
        :rtype: int
        """
        return min(self.value,
                   self.lnode.min_value if self.lnode else sys.maxsize,
                   self.rnode.min_value if self.rnode else sys.maxsize)

    @property
    def max_value(self):
        """
        Get the maximum value of the current node and all the children
        :rtype: int
        """
        return max(self.value,
                   self.lnode.max_value if self.lnode else -sys.maxsize,
                   self.rnode.max_value if self.rnode else -sys.maxsize)

    def get_leaf_nodes(self) -> Iterator['BinaryNode']:
        """
        Get an iterator of all the children of this node which are also leaf nodes
        """
        if not self.lnode and not self.rnode:
            yield self
        else:
            if self.lnode: yield from self.lnode.get_leaf_nodes()
            if self.rnode: yield from self.rnode.get_leaf_nodes()

    def get_internal_nodes(self) -> Iterator['BinaryNode']:
        """
        Get an iterator of all the children of this node which are not leaf nodes
        """
        if self.lnode or self.rnode:
            yield self
        if self.lnode: yield from self.lnode.get_internal_nodes()
        if self.rnode: yield from self.rnode.get_internal_nodes()

    def in_order_traversal(self) -> Iterator['BinaryNode']:
        """
        Returns an iterator which traverses this subtree in-order
        """
        if self.lnode: yield from self.lnode.in_order_traversal()
        yield self
        if self.rnode: yield from self.rnode.in_order_traversal()

    def breadth_first_traversal(self) -> Iterator['BinaryNode']:
        """
        Returns an iterator which traverses this subtree breadth first
        """

        q = Queue([self])

        while not q.is_empty():
            node = q.dequeue()
            yield node
            if node.lnode: q.enqueue(node.lnode)
            if node.rnode: q.enqueue(node.rnode)

    def __repr__(self) -> str:
        return "{}(value={}, lnode={}, rnode={}, parent={})".format(self.__class__.__name__, self.value,
                                                                    self.lnode.value if self.lnode else None,
                                                                    self.rnode.value if self.rnode else None,
                                                                    self.parent.value if self.parent else None)

    def __len__(self):
        return 1 + (len(self.lnode) if self.lnode else 0) + (len(self.rnode) if self.rnode else 0)

    def pretty_print(self, padding=""):
        print('{} {}'.format(padding, self.value))
        if self.lnode: self.lnode.pretty_print(padding + ">>")
        if self.rnode: self.rnode.pretty_print(padding + ">>")

    def get_max_child(self) -> Optional['BinaryNode']:
        """
        Returns the child with the maximum value
        """
        if self.lnode and self.rnode:
            return self.lnode if self.lnode.value > self.rnode.value else self.rnode
        if self.lnode:
            return self.lnode
        if self.rnode:
            return self.rnode

    def get_min_child(self) -> Optional['BinaryNode']:
        """
        Returns the child with the minimum value
        """
        if self.lnode and self.rnode:
            return self.lnode if self.lnode.value < self.rnode.value else self.rnode
        if self.lnode:
            return self.lnode
        if self.rnode:
            return self.rnode

    @classmethod
    def from_array(cls, a: List) -> 'BinaryNode':
        """
        Return a complete binary tree from an array
        """
        if not a:
            return None

        # Push first element as root on the queue
        q = Queue()
        root_node = cls(a[0])
        q.enqueue(root_node)

        #
        for i in a[1:]:
            node = cls(i)
            parent = q.peek()
            if not parent.lnode:
                parent.lnode = node
                q.enqueue(node)

            else:
                parent.rnode = node
                q.enqueue(node)
                q.dequeue()

        return root_node


class BinarySearchNode(BinaryNode):
    """
    Extend BinaryNode to enforce binary search tree ordering
    """

    def __init__(self, value, *, lnode=None, rnode=None):
        super().__init__(value, lnode=lnode, rnode=rnode)

    # Overload the lnode and rnode properties to check if the constraints are not violated

    @property
    def lnode(self) -> Optional['BinaryNode']:
        return BinaryNode.lnode.fget(self)

    @lnode.setter
    def lnode(self, node: Optional['BinaryNode']):
        lower_bound = self.get_lower_bound()
        if isinstance(node, BinarySearchNode) and (
                (lower_bound and node.min_value < lower_bound) or node.max_value >= self.value):
            raise ValueError('Binary search tree constraints violated')

        BinaryNode.lnode.fset(self, node)

    @property
    def rnode(self) -> Optional['BinaryNode']:
        return BinaryNode.rnode.fget(self)

    @rnode.setter
    def rnode(self, node: Optional['BinaryNode']):
        upper_bound = self.get_upper_bound()
        if isinstance(node, BinarySearchNode) and (
                (upper_bound and node.max_value >= upper_bound) or node.min_value < self.value):
            raise ValueError('Binary search tree constraints violated')

        BinaryNode.rnode.fset(self, node)

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
