import unittest
from src.algorithms.graphs.maximum_flow import find_path_with_capacity_dfs, ford_fulkerson
from src.structures import DirectedGraph


class TestMaximumFlow(unittest.TestCase):
    def setUp(self):
        g = DirectedGraph()

        g.add_edge(1, 2, 2)
        g.add_edge(1, 3, 6)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 4, 1)
        g.add_edge(3, 4, 1)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 5, 6)

        self.graph = g

        g = DirectedGraph()

        g.add_edge(1, 2, 1000)
        g.add_edge(1, 3, 1000)
        g.add_edge(2, 3, 1)
        g.add_edge(2, 4, 1000)
        g.add_edge(3, 4, 1000)

        self.graph2 = g

    def test_find(self):

        flows = {edge: 0 for edge in self.graph.get_all_edges()}

        path = find_path_with_capacity_dfs(self.graph, 1, 5, set(), flows)

        assert path[0].a == 1
        assert path[-1].b == 5

        for edge_a, edge_b in zip(path, path[1:]):
            assert edge_a.b == edge_b.a

    def test_flow(self):

        flows, max_flow = ford_fulkerson(self.graph, 1, 5)

        self.__check_flow_constraints(1, 5, flows, self.graph)

        assert max_flow == 6

    def test_flow2(self):

        flows, max_flow = ford_fulkerson(self.graph2, 1, 4)

        self.__check_flow_constraints(1, 4, flows, self.graph2)

        assert max_flow == 2000

    @staticmethod
    def __check_flow_constraints(source, sink, flows, graph):

        # All incoming flows should equal all outgoing flows
        for vertex in graph.get_vertices():
            if vertex not in [source, sink]:
                assert sum([-flows[x] for x in flows.keys() if x.a == vertex]) + \
                       sum([flows[x] for x in flows.keys() if x.b == vertex]) == 0

        # The flow in each edge should not exceed the capacity
        for edge in graph.get_all_edges():
            assert 0 <= flows[edge] <= edge.weight

        # The source output and sink input should be the same
        assert sum([-flows[x] for x in flows.keys() if x.a == source]) + \
               sum([flows[x] for x in flows.keys() if x.b == sink]) == 0
