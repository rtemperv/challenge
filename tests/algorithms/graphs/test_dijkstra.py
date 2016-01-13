import unittest
import sys
import random
from src.algorithms.graphs.dijkstra import dijkstra
from src.structures import DirectedGraph


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        g = DirectedGraph()

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

        distance, path = dijkstra(g, 1, 5)

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

