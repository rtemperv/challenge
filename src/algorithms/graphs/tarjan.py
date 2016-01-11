from src.structures.graph import DirectedGraph
from src.structures.stack import Stack
import copy


def tarjan(graph: DirectedGraph):
    """
    Tarjan's Algorithm is an algorithm in graph theory for
    finding the strongly connected components of a directed graph.
    It runs in linear time, matching the time bound for
    alternative methods including Kosaraju's algorithm and
    the path-based strong component algorithm.
    """

    graph = copy.deepcopy(graph)

    stack = Stack()

    node_visited = {}
    node_lowlinks = {}
    node_indices = {}

    SCC = []

    index = 0

    # Recursive strong connect function
    def strong_connect(current_node):
        nonlocal index

        node_visited[current_node] = True
        node_indices[current_node] = index
        node_lowlinks[current_node] = index
        index += 1
        stack.push(current_node)

        for vertex in graph.get_adjacent_vertices(current_node):
            if vertex not in node_indices:
                strong_connect(vertex)
                node_lowlinks[current_node] = min(node_lowlinks[current_node], node_lowlinks[vertex])
            elif vertex in node_visited:
                node_lowlinks[current_node] = min(node_lowlinks[current_node], node_indices[vertex])

        # If current node is root of SCC pop the SCC
        if node_lowlinks[current_node] == node_indices[current_node]:
            current_scc = set()
            while stack.peek() != current_node:
                node = stack.pop()
                node_visited[node] = False
                current_scc.add(node)
            current_scc.add(stack.pop())
            SCC.append(current_scc)

    for i in graph.get_vertices():
        if i not in node_indices:
            strong_connect(i)

    return SCC





