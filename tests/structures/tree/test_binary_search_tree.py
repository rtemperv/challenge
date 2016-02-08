from src.structures import BinarySearchNode, BinarySearchTree
import unittest


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        a = BinarySearchNode(1)
        b = BinarySearchNode(2)
        c = BinarySearchNode(5)
        d = BinarySearchNode(3)
        e = BinarySearchNode(4.99)
        f = BinarySearchNode(2)

        a.rnode = b
        b.rnode = c
        c.lnode = d
        d.rnode = e
        d.lnode = f
        self.tree = a

    def test_get_leafs(self):
        leafs = list(self.tree.get_leaf_nodes())
        assert len(leafs) == 2, "Incorrect amount of leafs"
        assert {i.value for i in leafs} == {2, 4.99}, "Incorrect leaf values"

    def test_max_value(self):
        assert self.tree.max_value == 5, "Incorrect maximum value"

    def test_min_value(self):
        assert self.tree.min_value == 1, "Incorrect minimum value"

    def test_in_order_traversal(self):
        assert list(map(lambda x: x.value, self.tree.in_order_traversal())) == [1, 2, 2, 3, 4.99, 5]

    def test_binary_search_tree(self):

        tree = BinarySearchTree()
        tree.insert(4, payload="four")
        tree.insert(7, payload="seven")
        tree.insert(1, payload="one")
        tree.insert(9, payload="nine")
        tree.insert(0, payload="zero")
        tree.insert(3, payload="three")
        tree.insert(6, payload="six")

        assert [node.value for node in tree.root.in_order_traversal()] == [0, 1, 3, 4, 6, 7, 9]

        assert tree.search(6) == "six"
