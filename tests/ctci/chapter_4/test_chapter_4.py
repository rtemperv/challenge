import unittest
from src.structures import BinaryNode, DirectedGraph
from src.ctci.chapter_4.question_2 import points_are_connected

class TestChapter4(unittest.TestCase):

    def test_question_1(self):

        tree_1 = BinaryNode.from_array([1, 2 ,3, 4, 5, 6, 7])

        assert tree_1.is_balanced()

        leaf_node = next(tree_1.get_leaf_nodes())

        leaf_node.rnode = BinaryNode(0)
        leaf_node.rnode.rnode = BinaryNode(0)

        assert not tree_1.is_balanced()

    def test_question_2(self):

        directed = DirectedGraph()
        directed.add_edge(1, 2, 2)
        directed.add_edge(1, 3, 6)
        directed.add_edge(2, 3, 3)
        directed.add_edge(2, 4, 1)
        directed.add_edge(3, 4, 1)
        directed.add_edge(3, 5, 4)
        directed.add_edge(4, 5, 6)

        assert points_are_connected(directed, 1, 5)

        assert not points_are_connected(directed, 5, 1)
