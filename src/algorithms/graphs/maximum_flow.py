from src.structures import DirectedGraph
from typing import Dict
import sys


def ford_fulkerson(graph: DirectedGraph, source, sink):
    """
    In optimization theory, maximum flow problems involve finding a feasible flow through a
    single-source, single-sink flow network that is maximum.
    """

    # Store the current flows in a dict
    flows = {edge: 0 for edge in graph.get_all_edges()}
    max_flow = 0

    while True:
        # Find a path with capacity from source to sink and stop is none is available
        next_path = find_path_with_capacity_dfs(graph, source, sink, set(), flows)

        if next_path is None:
            break

        # Calculate the max flow for the current path
        current_max_flow = sys.maxsize
        start = source
        for edge in next_path:
            if edge.a == start:
                current_max_flow = min(current_max_flow, edge.weight - flows[edge])
                start = edge.b
            else:
                current_max_flow = min(current_max_flow, flows[edge])
                start = edge.a

        # Add this flow to the found path
        start = source
        for edge in next_path:
            if edge.a == start:
                flows[edge] += current_max_flow
                start = edge.b
            else:
                flows[edge] -= current_max_flow
                start = edge.a

        max_flow += current_max_flow

    # Return the optimal flows per edge and the total max flow
    return flows, max_flow


def find_path_with_capacity_dfs(graph: DirectedGraph, current_node, end_node, visited, flows: Dict):
    """
    Finds a path with available capacity from current node to end node
    Returns none if no such paths exist
    """
    visited.add(current_node)

    for edge in graph.get_edges(current_node):

        origin, destination = (edge.a, edge.b) if edge.a == current_node else (edge.b, edge.a)

        if (edge.weight > flows[edge] and edge.a == current_node) or (0 < flows[edge] and edge.b == current_node):

            if destination in visited:
                continue

            if destination == end_node:
                return [edge]

            result = find_path_with_capacity_dfs(graph, destination, end_node, visited, flows)

            if result:
                return [edge] + result

    visited.remove(current_node)



