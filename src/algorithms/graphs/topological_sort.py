from src.structures import DirectedGraph, Queue
from typing import List
import copy


def topological_sort(graph: DirectedGraph) -> List:
    """
    Called Kahns algorithm
    Sorts the vertices of a graph in a topological order
    or raises an exception when the graph is cyclical
    :param graph: The graph to be sorted toplogically
    """

    graph = copy.deepcopy(graph)

    sorted_nodes = []
    nodes = Queue()

    # Add the nodes without incoming edges to the starting nodes
    for vertex in graph.get_vertices():
        if not graph.has_incoming_edge(vertex):
            nodes.enqueue(vertex)

    while not nodes.is_empty():
        node = nodes.dequeue()
        sorted_nodes.append(node)

        for edge in graph.get_edges(node)[:]:
            graph.delete_edge(edge.a, edge.b)
            if not graph.has_incoming_edge(edge.b):
                nodes.enqueue(edge.b)

    if len(list(graph.get_all_edges())):
        raise RuntimeError('Graph is cyclical')

    return sorted_nodes



