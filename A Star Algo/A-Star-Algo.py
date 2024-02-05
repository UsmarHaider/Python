graph = {
    0: {1: 4, 2: 2},
    1: {2: 5, 3: 10},
    2: {1: 1, 3: 2},
    3: {0: 7, 3: 3}
}

source = 0
destination = 3


def heuristic(node):
    return abs(node - destination)


def a_star(graph, source, destination):
    open_list = [source]

    closed_list = []
    parent = {}
    g = {}
    f = {}
    g[source] = 0
    f[source] = heuristic(source)
    while open_list:
        current = open_list[0]
        for node in open_list:
            if f[node] < f[current]:
                current = node
        if current == destination:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            path.reverse()
            return (path, g[destination])
        closed_list.append(current)
        open_list.remove(current)
        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue
            if neighbor not in open_list:
                open_list.append(neighbor)
            g_value = g[current] + graph[current][neighbor]
            if g_value < g.get(neighbor, float('inf')):
                parent[neighbor] = current
                g[neighbor] = g_value
                f[neighbor] = g_value + heuristic(neighbor)
    return (None, None)


path, weight = a_star(graph, source, destination)
print("Shortest path: {}".format(path))
print("Total weight: {}".format(weight))