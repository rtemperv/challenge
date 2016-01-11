import unittest

from src.algorithms.graphs.bfs_cyclical import contains_cycle
from src.structures import UndirectedGraph, DirectedGraph


class TestCyclical(unittest.TestCase):
    def setUp(self):
        self.undirected = UndirectedGraph()

        self.undirected.add_edge(1, 2, 2)
        self.undirected.add_edge(1, 3, 6)
        self.undirected.add_edge(2, 4, 1)
        self.undirected.add_edge(3, 5, 4)

    def test_topological_sort(self):
        assert not contains_cycle(self.undirected)
        self.undirected.add_edge(4, 5, 6)
        assert contains_cycle(self.undirected)
