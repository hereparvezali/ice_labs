def floyd_warshall(adj_matrix):
    vertex = len(adj_matrix)
    INF = float('inf')

    dist = [row[:] for row in adj_matrix]

    for k in range(vertex):
        for i in range(vertex):
            for j in range(vertex):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


adjacency_matrix = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

result = floyd_warshall(adjacency_matrix)

for row in result:
    print(row)
