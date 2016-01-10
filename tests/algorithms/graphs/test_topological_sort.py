import unittest

from src.algorithms.graphs.topological_sort import topological_sort
from src.structures import DirectedGraph


class TestTopologicalSort(unittest.TestCase):

    def setUp(self):
        g = DirectedGraph()

        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 4, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 5, 6)

        self.graph = g

    def test_topological_sort(self):

        assert topological_sort(self.graph) == [1, 2, 3, 4, 5]

    def test_topological_sort2(self):
        self.graph.add_edge(5, 1, 2)
        with self.assertRaises(RuntimeError):
            topological_sort(self.graph)

    def test_topological_sort3(self):
        self.graph.add_edge(4, 2, 2)
        with self.assertRaises(RuntimeError):
            topological_sort(self.graph)

    def test_topological_sort4(self):
        self.graph.add_edge(0, 4, 2)
        assert type(topological_sort(self.graph)) == list
