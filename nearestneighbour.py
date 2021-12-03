

"""
taverse shortest path euclidean distance using nearest neighbour algorithm
"""
from utils import *


def nearest_neighbour(graph, start):
    visited = []
    visited.append(start)
    path = [start]
    while len(visited) < len(graph):
        min_dist = float('inf')
        for node in graph:
            if node not in visited:
                if dist(node, start) < min_dist:
                    min_dist = dist(node, start)
                    min_node = node
        visited.append(min_node)
        path.append(min_node)
        start = min_node
    return path


if __name__ == '__main__':
    import time
    graph = []
    start = time.time()
    # with open('data.txt') as f:

    #     for line in f.readlines()[1:]:
    #         graph.append(list(map(int, line.split())))
    graph = random_graph(10)
    tsp = nearest_neighbour(graph, graph[0])
    # print(tsp)
    print(f'Time taken: {time.time()-start}')
    print(f'Total distance: {sum(dist(x, y) for x, y in zip(tsp, tsp[1:]))}')
    print(f'number of nodes: {len(tsp)}')
    print(f'number of edges: {len(tsp)-1}')
