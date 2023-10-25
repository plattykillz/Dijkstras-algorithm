import sys

def dijkstra(graph, source):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    distances = [sys.maxsize] * num_nodes
    distances[source] = 0

    for _ in range(num_nodes):
        min_dist = sys.maxsize
        min_node = None

        for v in range(num_nodes):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                min_node = v

        visited[min_node] = True

        for v in range(num_nodes):
            if not visited[v] and graph[min_node][v] > 0:
                new_dist = distances[min_node] + graph[min_node][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist

    return distances

# Example!!!
if __name__ == "__main__":
    graph = [
        [0, 4, 0, 0, 2, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 2, 7, 0, 4, 14, 0, 6, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [9, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 61, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]

    source_node = 0
    shortest_distances = dijkstra(graph, source_node)

    for i, dist in enumerate(shortest_distances):
        print(f"Shortest distance from node {source_node} to node {i}: {dist}")
