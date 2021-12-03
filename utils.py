def dist(x, y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5


def random_graph(n):
    from random import randint
    graph = []
    for i in range(n):
        graph.append((randint(0, 9), randint(0, 9)))
    return graph
