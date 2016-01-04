import sys

from code.structures import Stack
from heapq import heappop, heappush


def find_shortest_path(graph, start_node, end_node):
    """

    :param G: graph object
    :type G: Graph
    :type start_node:
    :type end_node:
    """

    # Min heap
    pq = [(0, start_node)]

    # Final distances and paths from the start node
    distances = {key: sys.maxsize for key in graph.get_vertices()}
    paths = {key: [] for key in graph.get_vertices()}

    # Finished nodes
    visited_nodes = set()

    # Set start node distance to 0
    distances[start_node] = 0

    while pq:
        distance, vertex = heappop(pq)

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

                heappush(pq, (distance + outgoing_edge.weight, outgoing_edge.b))

        visited_nodes.add(vertex)

    return distances[end_node], paths[end_node]

def find_cycles(graph):

    vertices = set(graph.get_vertices())

    start = vertices.pop()

    stack = Stack()

    def _find_cycles(graph, stack, current_vertex):
        for av in graph.get_adjacent_vertices(current_vertex):
            if av in stack:
                # Found a cycle
                pass