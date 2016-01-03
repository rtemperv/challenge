import sys
from heapq import heappop, heappush

def find_shortest_path(G, start_node, end_node):

    pq = [(0, start_node)]

    distances = {key: sys.maxsize for key in G.iterkeys()}

    # Set start node distance to 0
    distances[start_node] = 0

    while pq:
        

