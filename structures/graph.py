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
        self.adjacency_list[a].append(edge)
        self.adjacency_list[b].append(edge)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

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

    def get_adjacent_vertices(self, vertex):

        if vertex not in self.adjacency_list:
            raise RuntimeError('Vertex not present')

        return [edge.b for edge in self.adjacency_list[vertex] if edge.a == vertex]

    def get_edges(self, vertex):

        if vertex not in self.adjacency_list:
            raise RuntimeError('Vertex not present')

        return list(self.adjacency_list[vertex])

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def delete_edge(self, a, b):
        if a in self.adjacency_list and b in self.adjacency_list:
            self.adjacency_list[a] = filter(lambda x: x.a != a or x.b != b, self.adjacency_list[a])
            self.adjacency_list[b] = filter(lambda x: x.a != a or x.b != b, self.adjacency_list[b])

