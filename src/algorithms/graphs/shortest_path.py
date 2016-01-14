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

        outgoing_edges = filter(lambda x: x.a == vertex, graph.get_edges(vertex))

        for outgoing_edge in outgoing_edges:
            if outgoing_edge in visited_nodes:
                continue

            if distance + outgoing_edge.weight < distances[outgoing_edge.b]:
                distances[outgoing_edge.b] = distance + outgoing_edge.weight
                paths[outgoing_edge.b] = paths[outgoing_edge.a] + [outgoing_edge.b]

                pq.insert((distance + outgoing_edge.weight, outgoing_edge.b))

        visited_nodes.add(vertex)

    return distances[end_node], paths[end_node]


