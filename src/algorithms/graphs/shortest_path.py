import sys
from typing import List
from src.structures import FibonacciHeap
from src.structures import Graph
from itertools import count
import sys

def dijkstra(graph: Graph, start_node, end_node) -> (int, List):
    """
    Dijkstras shortest path algorithm implementation
    Works for directed and undirected graphs with non negative weights
    Time complexity: O(EV + V^2 * logV)
    :return Returns a tuple of the distance of the shortest path and the nodes to reach the shortest path
    """

    # Min heap
    pq = FibonacciHeap()
    pq.insert((0, start_node))

    # Final distances and paths from the start node
    distances = {key: sys.maxsize for key in graph.get_vertices()}
    paths = {key: [] for key in graph.get_vertices()}

    # Finished nodes
    visited_nodes = set()

    # Set start node distance to 0
    distances[start_node] = 0

    while not pq.is_empty():
        distance, vertex = pq.pop()

        if distance == sys.maxsize or end_node in visited_nodes:
            # Only unconnected vertices are left or we found the minimal distance
            break

        for outgoing_edge in graph.get_outgoing_edges(vertex):

            next_vertex = outgoing_edge.a if outgoing_edge.a != vertex else outgoing_edge.b

            if next_vertex in visited_nodes:
                continue

            if distance + outgoing_edge.weight < distances[next_vertex]:
                distances[next_vertex] = distance + outgoing_edge.weight
                paths[next_vertex] = paths[vertex] + [next_vertex]

                pq.insert((distance + outgoing_edge.weight, next_vertex))

        visited_nodes.add(vertex)

    return distances[end_node], paths[end_node]


def floyd_warshal(g: Graph):
    """
    the Floyd–Warshall algorithm is an algorithm for finding shortest paths in a weighted graph with positive
    or negative edge weights (but with no negative cycles). A single execution of the algorithm will find the
    lengths (summed weights) of the shortest paths between all pairs of vertices, though it does not return details
    of the paths themselves.
    Time complexity: O(V^3)
    """

    vertices_mapping = dict(zip(g.get_vertices(), count()))

    # Build V*V matrix initialized to sys.maxsize
    matrix = [[sys.maxsize] * len(vertices_mapping) for _ in range(len(vertices_mapping))]

    # Set distance to itself to zero
    for vertex in g.get_vertices():
        matrix[vertices_mapping[vertex]][vertices_mapping[vertex]] = 0

    # Set distance for all edges
    for vertex in g.get_vertices():
        for edge in g.get_outgoing_edges(vertex):
            succesive_vertex = edge.a if edge.a != vertex else edge.b
            matrix[vertices_mapping[vertex]][vertices_mapping[succesive_vertex]] = edge.weight

    # Main loop
    for k in g.get_vertices():
        for i in g.get_vertices():
            for j in g.get_vertices():
                matrix[vertices_mapping[i]][vertices_mapping[j]] = min(matrix[vertices_mapping[i]][vertices_mapping[k]] + \
                    matrix[vertices_mapping[k]][vertices_mapping[j]], matrix[vertices_mapping[i]][vertices_mapping[j]])

    return [(a, b, matrix[vertices_mapping[a]][vertices_mapping[b]]) for a in g.get_vertices() for b in g.get_vertices() if
            matrix[vertices_mapping[a]][vertices_mapping[b]] != sys.maxsize]
