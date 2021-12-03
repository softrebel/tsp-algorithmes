
import time
from utils import *
from nearestneighbour import nearest_neighbour, random_graph
from exhaustive import tsp_exhaustive

graph = []

with open('data.txt') as f:
    for line in f.readlines()[1:]:
        graph.append(list(map(int, line.split())))
# graph = random_graph(11)
start = time.time()
tsp = nearest_neighbour(graph, graph[0])
print("nearestneighbour:")
print(tsp)
print(f'Time taken: {time.time()-start}')
print(f'Total distance: {sum(dist(x, y) for x, y in zip(tsp, tsp[1:]))}')
start = time.time()
print("exhaustive:")
tsp = tsp_exhaustive(graph)
print(tsp)
print(f'Time taken: {time.time()-start}')
print(f'Total distance: {sum(dist(x, y) for x, y in zip(tsp, tsp[1:]))}')
