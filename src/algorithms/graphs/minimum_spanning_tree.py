from src.structures import FibonacciHeap
from src.structures import UndirectedGraph
from src.structures import UnionFind


def kruskal(graph: UndirectedGraph) -> UndirectedGraph:
    """
    Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight
    that connects any two trees in the forest. It is a greedy algorithm in graph theory as it finds a minimum
    spanning tree for a connected weighted undirected graph adding increasing cost arcs at each step.
    Time complexity: O(E log V)
    """
    spanning_tree = UndirectedGraph()

    union_find = UnionFind(max(graph.get_vertices()) + 1)

    heap = FibonacciHeap(graph.get_all_edges())

    while not heap.is_empty():

        edge = heap.pop()

        # Only add the edge if it will not create a cycle
        if union_find.find(edge.a) != union_find.find(edge.b):
            spanning_tree.add_edge(edge.a, edge.b, edge.weight)
            union_find.union(edge.a, edge.b)

    return spanning_tree


def prim(graph: UndirectedGraph) -> UndirectedGraph:
    """
    Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    This means it finds a subset of the edges that forms a tree that includes every vertex
    O(E + V log V)
    """
    current_vertex = graph.get_vertices()[0]

    new_graph = UndirectedGraph()

    heap = FibonacciHeap(map(lambda x: (x, current_vertex), graph.get_outgoing_edges(current_vertex)))

    vertices = {current_vertex}

    while not heap.is_empty():

        edge, current_vertex = heap.pop()

        next_vertex = edge.a if edge.a != current_vertex else edge.b

        if next_vertex in vertices:
            continue

        # Add edge to the minimum spanning tree
        vertices.add(next_vertex)
        new_graph.add_edge(current_vertex, next_vertex, edge.weight)

        # Add all edges from this new point to the heap
        [heap.insert((edge, next_vertex)) for edge in graph.get_outgoing_edges(next_vertex)]

    return new_graph




