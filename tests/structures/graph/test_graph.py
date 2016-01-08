from src.structures import Graph
import unittest


class TestGraph(unittest.TestCase):
    def test_graph(self):
        g = Graph()

        g.add_edge(1, 2, 1)
        g.add_edge(2, 3, 4)
        g.add_edge(3, 1, 2)

        assert len(g.adjacency_list) == 3

        for vertex, edges in g.adjacency_list.items():
            assert len(edges) == 2


