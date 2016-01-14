import unittest
from src.algorithms.graphs.strongly_connected_components import tarjan
from src.structures import DirectedGraph


class TestTarjan(unittest.TestCase):
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

    def test_tarjan(self):
        scc = tarjan(self.graph)

        # Detect if there are cycles
        assert not any(map(lambda x: len(x) > 1, scc))

        # Add an edge which creates a cycle
        self.graph.add_edge(3, 2, 1)
        scc = tarjan(self.graph)
        assert {2, 3} in scc

        # Add another cycle
        self.graph.add_edge(5, 4, 1)
        scc = tarjan(self.graph)
        assert {4, 5} in scc

        # Connect the two cycles
        self.graph.add_edge(4, 3, 1)
        scc = tarjan(self.graph)
        assert {2, 3, 4, 5} in scc


