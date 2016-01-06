from src.structures import Graph
from src.topcoder.dynamic.dijkstra import find_shortest_path
import unittest
import random


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        g = Graph()

        g.add_edge(1, 2, 2)
        g.add_edge(2, 1, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(3, 1, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(3, 2, 3)
        g.add_edge(2, 4, 1)
        g.add_edge(4, 2, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(4, 3, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(5, 3, 4)
        g.add_edge(4, 5, 6)
        g.add_edge(5, 4, 6)

        distance, path = find_shortest_path(g, 1, 5)

        assert distance == 8

        assert path == [2, 4, 3, 5]

    def test_dijkstra_2(self):
        g = Graph()

        for i in range(200):
            g.add_vertex(i)

        for _ in range(500):
            a = random.randint(1, 200)
            b = random.randint(1, 200)
            if a != b:
                g.add_edge(a, b, random.randint(1, 100))

        distance, path = find_shortest_path(g, 1, 199)
