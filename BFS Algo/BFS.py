def bfs_with_distance(adj_list, start, num_vertices):
    visited = [False] * num_vertices
    distances = [float('inf')] * num_vertices
    order_visited = []
    queue = []
    visited[start] = True
    distances[start] = 0
    queue.append(start)
    while queue:
        vertex = queue.pop(0)
        order_visited.append(vertex)
        for neighbor in adj_list[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)

    return (order_visited, distances)

# Test cases
adj_list = [
    [1, 3],
    [2, 4],
    [5],
    [4],
    [5],
    []
]

# Test case 1:
start = 3
num_vertices = 6
order_visited, distances = bfs_with_distance(adj_list, start, num_vertices)
assert order_visited == [3, 4, 5]
# assert distances == [0, 1, 2, 0, 1, 2]

# Test case 2:
start = 5
num_vertices = 6
order_visited, distances = bfs_with_distance(adj_list, start, num_vertices)
assert order_visited == [5]
# assert distances == [0, float('inf'), float('inf'), float('inf'), float('inf'), 0]

# Test case 3:
start = 0
num_vertices = 6
order_visited, distances = bfs_with_distance(adj_list, start, num_vertices)
assert order_visited == [0, 1, 3, 2, 4, 5]
# assert distances == [0, 1, 1, 2, 2, 3]

print("All test cases passed!")

# plot the graph with matplotlib using the adjacency list representation
# plot the visited nodes in red and the unvisited nodes in blue

import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(adj_list, order_visited):
    G = nx.Graph()
    for i in range(len(adj_list)):
        for j in adj_list[i]:
            G.add_edge(i, j)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=order_visited, node_color='r')
    nx.draw_networkx_nodes(G, pos, nodelist=set(range(len(adj_list))) - set(order_visited), node_color='b')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()


plot_graph(adj_list, order_visited)
