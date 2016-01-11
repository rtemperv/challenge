from src.algorithms.graphs.bfs_cyclical import contains_cycle
from src.structures import FibonacciHeap
from src.structures import UndirectedGraph


def kruskal(graph: UndirectedGraph) -> UndirectedGraph:
    """
    Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight
    that connects any two trees in the forest. It is a greedy algorithm in graph theory as it finds a minimum
    spanning tree for a connected weighted undirected graph adding increasing cost arcs at each step.
    """
    spanning_tree = UndirectedGraph()

    edges = graph.get_all_edges()

    heap = FibonacciHeap(map(lambda x: (x.weight, x), edges))

    while not heap.is_empty():

        weight, edge = heap.pop()
        spanning_tree.add_edge(*edge)

        if contains_cycle(spanning_tree):
            spanning_tree.delete_edge(edge.a, edge.b)

    return spanning_tree



