from src.algorithms.graphs.bfs_cyclical import contains_cycle
from src.structures import FibonacciHeap
from src.structures import UndirectedGraph
from src.structures import UnionFind


def kruskal(graph: UndirectedGraph) -> UndirectedGraph:
    """
    Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight
    that connects any two trees in the forest. It is a greedy algorithm in graph theory as it finds a minimum
    spanning tree for a connected weighted undirected graph adding increasing cost arcs at each step.
    """
    spanning_tree = UndirectedGraph()

    union_find = UnionFind(max(graph.get_vertices()) + 1)

    heap = FibonacciHeap(map(lambda x: (x.weight, x), graph.get_all_edges()))

    while not heap.is_empty():

        weight, edge = heap.pop()

        # Only add the edge if it will not create a cycle
        if union_find.find(edge.a) != union_find.find(edge.b):
            spanning_tree.add_edge(*edge)
            union_find.union(edge.a, edge.b)

    return spanning_tree



