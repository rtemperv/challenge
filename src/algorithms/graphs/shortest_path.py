import sys
from typing import List
from src.structures import FibonacciHeap
from src.structures import Graph


def dijkstra(graph: Graph, start_node, end_node) -> (int, List):
    """
    Dijkstras shortest path algorithm implementation
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


