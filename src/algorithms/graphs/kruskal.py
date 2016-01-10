from src.algorithms.graphs.cyclical import contains_cycle
from src.structures import FibonacciHeap
from src.structures import UndirectedGraph


def minimal_spanning_tree(graph: UndirectedGraph):

    spanning_tree = UndirectedGraph()

    edges = graph.get_all_edges()

    heap = FibonacciHeap(map(lambda x: (x.weight, x), edges))

    while not heap.is_empty():

        weight, edge = heap.pop()
        spanning_tree.add_edge(*edge)

        if contains_cycle(spanning_tree):
            spanning_tree.delete_edge(edge.a, edge.b)

    return spanning_tree



