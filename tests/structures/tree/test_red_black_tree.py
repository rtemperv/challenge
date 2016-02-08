from src.structures import RedBlackTree
import unittest


class TestRedBlackTree(unittest.TestCase):

    def test_insert(self):
        tree = RedBlackTree()

        for i in range(10):
            tree.insert(i, str(i))

        tree.root.pretty_print()
        assert False
