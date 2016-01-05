import sys
import itertools


class BaseNode(object):
    def __init__(self, value, *, value_type=None):
        self.value_type = value_type
        self.value = value
        self.parent = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.value_type and value and not isinstance(value, self.value_type):
            raise ValueError('value should be of type {}'.format(self.value_type))
        self._value = value


class BinaryNode(BaseNode):
    """
    Binary node data structure
    """

    def __init__(self, value, *, value_type=None, lnode=None, rnode=None):
        super().__init__(value, value_type=value_type)
        self.lnode = lnode
        self.rnode = rnode

    @property
    def lnode(self):
        return self._lnode

    @lnode.setter
    def lnode(self, node):
        if node and not isinstance(node, self.__class__):
            raise ValueError('node should be an instance of the Node class')

        if node:
            node.parent = self

        self._lnode = node

    @property
    def rnode(self):
        return self._rnode

    @rnode.setter
    def rnode(self, node):
        if node and not isinstance(node, self.__class__):
            raise ValueError('node should be an instance of the Node class')

        if node:
            node.parent = self

        self._rnode = node

    @property
    def min_value(self):
        return min(self.value,
                   self.lnode.min_value if self.lnode else sys.maxsize,
                   self.rnode.min_value if self.rnode else sys.maxsize)

    @property
    def max_value(self):
        return max(self.value,
                   self.lnode.max_value if self.lnode else -sys.maxsize,
                   self.rnode.max_value if self.rnode else -sys.maxsize)

    def get_leaf_nodes(self):
        if not self.lnode and not self.rnode:
            yield self
        else:
            if self.lnode: yield from self.lnode.get_leaf_nodes()
            if self.rnode: yield from self.rnode.get_leaf_nodes()


class BinarySearchNode(BinaryNode):
    """
    Extend BinaryNode to enforce binary search tree ordering
    """

    def __init__(self, value, *, value_type=None, lnode=None, rnode=None):
        super().__init__(value, value_type=value_type)

    @property
    def lnode(self):
        return BinaryNode.lnode.fget(self)

    @lnode.setter
    def lnode(self, node):
        lower_bound = self.get_lower_bound()
        if isinstance(node, BinarySearchNode) and (
            (lower_bound and node.min_value < lower_bound) or node.max_value >= self.value):
            raise ValueError('Binary search tree constraints violated')

        BinaryNode.lnode.fset(self, node)

    @property
    def rnode(self):
        return BinaryNode.rnode.fget(self)

    @rnode.setter
    def rnode(self, node):
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

    def __repr__(self):
        return "{}(value={}, lnode={}, rnode={})".format(self.__class__.__name__, self.value,
                                                         self.lnode.value if self.lnode else None,
                                                         self.rnode.value if self.rnode else None)


class NarySearchNode(BaseNode):
    def __init__(self, values, value, children=None):
        if len(values) != children - 1:
            raise ValueError('Number of children should be 1 more than the number of values')
        super().__init__(values)
