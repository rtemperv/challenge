import unittest

from src.algorithms.graphs.bfs_cyclical import contains_cycle

from src.algorithms.graphs.kruskal import minimal_spanning_tree
from src.structures import UndirectedGraph


class TestKruskal(unittest.TestCase):
    def setUp(self):
        g = UndirectedGraph()

        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 4, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 5, 6)

        self.graph = g

    def test_kruskal(self):
        graph = minimal_spanning_tree(self.graph)

        assert not contains_cycle(graph)

        assert len(graph.get_all_edges()) == len(graph.get_vertices()) - 1

