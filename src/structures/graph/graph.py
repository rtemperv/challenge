from collections import namedtuple
from itertools import chain
import abc
Edge = namedtuple("Edge", ['weight', 'a', 'b'])


class Graph(object, metaclass=abc.ABCMeta):
    """
    Weighted directed graph implementation based on an adjacency list
    """

    # Todo: adjacency matrix implementation (2 dimensional vertices array)
    # Todo: incidence matrix implementation (2 dimensional vertices/edges array)

    def __init__(self, directed=True):
        self.adjacency_list = {}
        self.directed = True

    def _add_edge(self, a, b, weight):
        edge = Edge(weight, a, b)
        self.adjacency_list[a].append(edge)
        self.adjacency_list[b].append(edge)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    @abc.abstractmethod
    def edge_exists(self, a, b):
        pass

    def add_edge(self, a, b, weight):
        self.add_vertex(a)
        self.add_vertex(b)

        if not self.edge_exists(a, b):
            self._add_edge(a, b, weight)

    @abc.abstractmethod
    def get_adjacent_vertices(self, vertex):
        pass

    def get_edges(self, vertex):
        return list(self.adjacency_list[vertex])

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_all_edges(self):
        return list(set(chain(*map(lambda x: self.get_edges(x), self.get_vertices()))))

    @abc.abstractmethod
    def delete_edge(self, a, b):
        pass
    

class DirectedGraph(Graph):
    """
    Directed Graph implementation
    """
    def __init__(self):
        super(DirectedGraph, self).__init__()

    def get_adjacent_vertices(self, vertex):
        return [edge.b for edge in self.adjacency_list[vertex] if edge.a == vertex]

    def edge_exists(self, a, b):
        if a not in self.adjacency_list:
            return False

        return any(filter(lambda x: x.a == a and x.b == b, self.get_edges(a)))

    def delete_edge(self, a, b):
        if a in self.adjacency_list and b in self.adjacency_list:
            self.adjacency_list[a] = list(filter(lambda x: x.a != a or x.b != b, self.adjacency_list[a]))
            self.adjacency_list[b] = list(filter(lambda x: x.a != a or x.b != b, self.adjacency_list[b]))
    
    def has_incoming_edge(self, vertex):
        return any(filter(lambda x: x.b == vertex, self.adjacency_list[vertex]))


class UndirectedGraph(Graph):
    """
    Undirected graph implementation
    """
    def __init__(self):
        super(UndirectedGraph, self).__init__()

    def get_adjacent_vertices(self, vertex):
        return [edge.b if edge.a == vertex else edge.a for edge in self.adjacency_list[vertex]]

    def edge_exists(self, a, b):
        if a not in self.adjacency_list:
            return False

        return any(filter(lambda x: (x.a == a and x.b == b) or (x.b == a and x.a == b), self.get_edges(a)))

    def delete_edge(self, a, b):
        if a in self.adjacency_list and b in self.adjacency_list:
            self.adjacency_list[a] = list(filter(lambda x: x.a != b and x.b != b, self.get_edges(a)))
            self.adjacency_list[b] = list(filter(lambda x: x.a != a and x.b != a, self.get_edges(b)))
