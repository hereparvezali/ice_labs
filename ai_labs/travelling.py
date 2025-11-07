from itertools import permutations

# Brute Force TSP Solver (Asymmetric Distances)


def tsp_brute_force(graph, start):
    n = len(graph)
    vertices = list(range(n))
    vertices.remove(start)
    min_path = float('inf')
    best_path = []

    # Generate all possible tours
    for perm in permutations(vertices):
        current_pathweight = 0
        k = start
        for j in perm:
            current_pathweight += graph[k][j]  # Distance from k to j
            k = j
        current_pathweight += graph[k][start]  # Return to the starting point

        if current_pathweight < min_path:
            min_path = current_pathweight
            best_path = [start] + list(perm) + [start]

    return min_path, best_path


# Example graph (Asymmetric Adjacency Matrix)
graph = [[100, 100, 100, 100, 100, 100, 100, 0], [100, 100, 1, 4, 100, 100, 100, 0], [100, 1, 100, 1, 2, 1, 100, 0], [100, 4, 1, 100, 100, 100, 1, 2], [
    100, 100, 2, 100, 100, 100, 100, 0], [100, 100, 1, 100, 100, 100, 100, 0], [100, 100, 100, 1, 100, 100, 100, 0], [100, 100, 100, 2, 100, 100, 100, 0]]
start_node = 1
min_path_cost, best_path = tsp_brute_force(graph, start_node)
print("Minimum path cost:", min_path_cost)
print("Path:", best_path)
