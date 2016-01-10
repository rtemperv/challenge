from src.structures import DirectedGraph, UndirectedGraph
import unittest


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.undirected = UndirectedGraph()
        self.undirected.add_edge(1, 2, 2)
        self.undirected.add_edge(1, 3, 6)
        self.undirected.add_edge(2, 3, 3)
        self.undirected.add_edge(2, 4, 1)
        self.undirected.add_edge(3, 4, 1)
        self.undirected.add_edge(3, 5, 4)
        self.undirected.add_edge(4, 5, 6)

        self.directed = DirectedGraph()
        self.directed.add_edge(1, 2, 2)
        self.directed.add_edge(1, 3, 6)
        self.directed.add_edge(2, 3, 3)
        self.directed.add_edge(2, 4, 1)
        self.directed.add_edge(3, 4, 1)
        self.directed.add_edge(3, 5, 4)
        self.directed.add_edge(4, 5, 6)

    def test_get_edges(self):
        assert self.undirected.get_all_edges() == self.directed.get_all_edges()
        assert self.undirected.get_vertices() == self.directed.get_vertices()

    def test_directed_graph(self):

        assert len(self.directed.get_adjacent_vertices(4)) == 1

        assert len(self.undirected.get_adjacent_vertices(4)) == 3

        assert self.undirected.edge_exists(4, 3)
        assert not self.directed.edge_exists(4, 3)

        self.directed.delete_edge(4, 3)
        self.undirected.delete_edge(4, 3)

        assert len(self.directed.get_all_edges()) == len(self.undirected.get_all_edges()) + 1

    def test_undirected_graph(self):
        g = UndirectedGraph()


