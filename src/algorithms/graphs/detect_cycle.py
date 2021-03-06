from src.structures import UndirectedGraph, Queue
import copy


def contains_cycle(graph: UndirectedGraph) -> bool:
    """
    Simple breadth first cycle detection for Undirected graphs
    """
    graph = copy.deepcopy(graph) # type: Graph

    visited_nodes = set()

    queue = Queue()
    queue.enqueue(graph.get_vertices()[0])

    while not queue.is_empty():
        vertex = queue.dequeue()

        for neighbour in graph.get_successive_vertices(vertex):
            if neighbour in visited_nodes:
                return True
            visited_nodes.add(neighbour)
            queue.enqueue(neighbour)
            graph.delete_edge(vertex, neighbour)

    return False




