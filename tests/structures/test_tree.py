from code.structures import BinarySearchNode
import unittest


class TestTree(unittest.TestCase):
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

        print(a.max_value)


    def test_get_leafs(self):
        leafs = list(self.tree.get_leaf_nodes())
        assert len(leafs) == 2, "Incorrect amount of leafs"
        assert {i.value for i in leafs} == {2, 4.99}, "Incorrect leaf values"

    def test_max_value(self):
        assert self.tree.max_value == 5, "Incorrect maximum value"

    def test_min_value(self):
        assert self.tree.min_value == 1, "Incorrect minimum value"
