from collections import namedtuple

Edge = namedtuple("Edge", ['a', 'b', 'weight'])


class Graph(object):
    """
    Weighted directed graph implementation based on an adjacency list
    """

    # Todo: adjacency matrix implementation (2 dimensional vertices array)
    # Todo: incidence matrix implementation (2 dimensional vertices/edges array)

    def __init__(self):
        self.adjacency_list = {}

    def _add_edge(self, a, b, weight):
        edge = Edge(a, b, weight)
        self.adjacency_list[a].add(edge)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()

    def edge_exists(self, a, b):
        if a not in self.adjacency_list[a]:
            return False

        edges = self.adjacency_list[a]

        return bool(filter(lambda x: x.a == a and x.b == b, edges))

    def add_edge(self, a, b, weight):
        self.add_vertex(a)
        self.add_vertex(b)

        if not self.edge_exists(a, b):
            self._add_edge(a, b, weight)



