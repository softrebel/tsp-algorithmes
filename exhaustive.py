'''
 tsp tour exhaustive algorithm that tries all permutations of nodes
'''

from utils import *


def tsp_exhaustive(graph):
    from itertools import permutations
    # get the number of nodes
    n = len(graph)
    # create a list of all possible permutations
    perms = permutations(graph)
    # minimum distance
    min_distance=float('inf')
    for perm in perms:
        sum_distance=0
        # create a tour
        tour = [perm[0]]
        # add the rest of the nodes
        for i in range(1, n):
            # get the distance between the current node and the next node
            distance = dist(tour[-1], perm[i])
            sum_distance += distance
            # add the next node to the tour
            tour.append(perm[i])
        # if distance is minimum then update the minimum distance and the tour
        if sum_distance < min_distance:
            min_distance = sum_distance
            shortest_tour = tour
    # return the shortest tour
    return shortest_tour



    

if __name__ == '__main__':
    import time
    graph = []
    start = time.time()
    # with open('data.txt') as f:
    #     for line in f.readlines()[1:]:
    #         graph.append(list(map(int, line.split())))
    graph = random_graph(10)
    tsp = tsp_exhaustive(graph)
    # print(tsp)
    print(f'Time taken: {time.time()-start}')
    print(f'Total distance: {sum(dist(x, y) for x, y in zip(tsp, tsp[1:]))}')
    print(f'number of nodes: {len(tsp)}')
    print(f'number of edges: {len(tsp)-1}')
