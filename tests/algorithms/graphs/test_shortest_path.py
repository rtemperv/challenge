import unittest
import sys
import random
from src.algorithms import dijkstra, floyd_warshal
from src.structures import UndirectedGraph, DirectedGraph


class TestShortestPath(unittest.TestCase):

    def setUp(self):
        g = DirectedGraph()

        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 4, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 5, 6)
        self.directed_graph = g

        g = UndirectedGraph()

        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 4, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 5, 6)
        self.undirected_graph = g

    def test_dijkstra_directed(self):

        distance, path = dijkstra(self.directed_graph, 1, 5)

        assert distance == 9

        assert path == [2, 4, 5]

    def test_dijkstra_undirected(self):

        distance, path = dijkstra(self.undirected_graph, 1, 5)

        assert distance == 8

        assert path == [2, 4, 3, 5]

    def test_dijkstra_2(self):
        g = DirectedGraph()

        for i in range(200):
            g.add_vertex(i)

        for _ in range(500):
            a = random.randint(1, 200)
            b = random.randint(1, 200)
            if a != b:
                g.add_edge(a, b, random.randint(1, 100))

        distance, path = dijkstra(g, 1, 199)

        if path:
            cur_dist = 0
            start = 1
            for i in path:
                for edge in g.adjacency_list[start]:
                    if edge.b == i:
                        cur_dist += edge.weight
                        break
                start = i

            if cur_dist == 0:
                cur_dist = sys.maxsize

            assert cur_dist == distance

    def test_floyd_warshal_directed(self):
        distances = floyd_warshal(self.directed_graph)
        assert (1, 5, 9) in distances

        assert not any(filter(lambda x: x[0] > x[1], distances))

    def test_floyd_warshal(self):
        distances = floyd_warshal(self.undirected_graph)
        assert (1, 5, 8) in distances

        assert (5, 1, 8) in distances

