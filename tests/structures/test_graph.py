from src.structures import Graph


def test_graph():
    g = Graph()

    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 1, 2)

    assert len(g.adjacency_list) == 3

    for vertex, edges in g.adjacency_list.items():
        assert len(edges) == 2


