import unittest

from src.algorithms.graphs.bfs_cyclical import contains_cycle

from src.algorithms.graphs.kruskal import kruskal
from src.structures import UndirectedGraph, Edge


class TestKruskal(unittest.TestCase):
    def setUp(self):
        g = UndirectedGraph()

        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 4, 9)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 5, 6)

        self.graph = g

    def test_kruskal(self):
        graph = kruskal(self.graph)

        assert not contains_cycle(graph)

        assert {Edge(2, 1, 2), Edge(1, 3, 4), Edge(3, 2, 3), Edge(4, 3, 5)} == set(graph.get_all_edges())

        assert len(graph.get_all_edges()) == len(graph.get_vertices()) - 1

