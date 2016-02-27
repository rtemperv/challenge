from src.structures import Graph


def points_are_connected(graph:Graph, a, b, visited_points=None):
    if not visited_points:
        visited_points = set()

    if a == b:
        return True

    visited_points.add(a)

    for i in graph.get_successive_vertices(a):
        if i not in visited_points:
            if points_are_connected(graph, i, b, visited_points):
                return True
    return False
