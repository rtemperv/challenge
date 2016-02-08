from .binary_search_tree import BinarySearchNode, BinarySearchTree


class RedBlackTreeNode(BinarySearchNode):
    """
    Single node in a red black tree
    """
    def __init__(self, value, lnode=None, rnode=None, payload=None):
        super(RedBlackTreeNode, self).__init__(value, lnode=lnode, rnode=rnode, payload=payload)

        self.is_red = False


class RedBlackTree(BinarySearchTree):

    def __init__(self):
        super(RedBlackTree, self).__init__()

        self._nil = RedBlackTreeNode(None)

        self.root = self._nil

    def _rotate_left(self, node: RedBlackTreeNode):
        """
        Rotate the node and it's right node to the left
        """
        if not node.rnode:
            return

        right_node = node.rnode

        # Make the left subtree of the right node the right subtree of the parent node
        node.rnode = right_node.lnode

        # Make the parent node the left node of the right node
        right_node.lnode = node

        # Make the parent's parent node point to the right node
        parent = node.parent
        if parent:
            if parent.rnode == node:
                parent.rnode = right_node
            else:
                parent.lnode = right_node

    def _rotate_right(self, node: RedBlackTreeNode):
        """
        Rotate the node and it's right node to the left
        """

        if not node.lnode:
            return

        left_node = node.lnode

        # Make the left subtree of the right node the right subtree of the parent node
        node.rnode = left_node.rnode

        # Make the parent node the left node of the right node
        left_node.rnode = node

        # Make the parent's parent node point to the right node
        parent = node.parent
        if parent:
            if parent.rnode == node:
                parent.rnode = left_node
            else:
                parent.lnode = left_node

    def _insert(self, node):

        y = self._nil

        x = self.root

        while x != self._nil:
            y = x
            x = x.lnode if node.value < x.value else x.rnode

        node.parent = y
        if y == self._nil:
            self.root = node
        elif node.value < y.value:
            y.lnode = node
        else:
            y.rnode = node

    def insert(self, value, payload):
        node = RedBlackTreeNode(value, payload=payload)
        node.is_red = True
        node.rnode = self._nil
        node.lnode = self._nil

        # Fix the coloring of the tree
        while node.parent.is_red:
            parent = node.parent
            if node.parent.parent:
                grandparent = node.parent.parent
                # parent is a left node so uncle is right
                if grandparent.lnode == parent:
                    uncle = grandparent.rnode
                    # Uncle is a red node
                    if uncle.is_red:
                        parent.is_red = False
                        uncle.is_red = False
                        grandparent.is_red = True

                        node = grandparent
                    # Uncle is a black node
                    else:
                        if node == parent.rnode:
                            node = parent
                            self._rotate_left(node)
                        else:
                            parent.is_red = False
                            grandparent.is_red = True
                            self._rotate_right(grandparent)

                # parent is a right node so uncle is left
                elif grandparent.rnode == parent:
                    uncle = grandparent.lnode
                    # Uncle is a red node
                    if uncle.is_red:
                        parent.is_red = False
                        uncle.is_red = False
                        grandparent.is_red = True

                        node = grandparent
                    # Uncle is a black node
                    else:
                        if node == parent.lnode:
                            node = parent
                            self._rotate_right(node)
                        else:
                            parent.is_red = False
                            grandparent.is_red = True
                            self._rotate_left(grandparent)
        self.root.is_red = False
