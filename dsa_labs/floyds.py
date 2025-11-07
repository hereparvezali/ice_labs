
INF = float('inf')

def floyds_algo(graph):
	l = len(graph)

	# Initializing a the distance matrix with the given graph
	dist = graph
	# for all the given value if there is -1 that will be replaced as infinity distance
	for row in dist:
		for ij in row:
			if ij==-1:
				ij=INF

	# Main algorithm loop
	for i in range(l):
		for j in range(l):
			for k in range(l):
				dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

	return dist


n = int(input("Enter the size of adjacency matrix: "))
# Example graph as an adjacency matrix
graph = []
# taking input one by one row of the matrix from the user
# give -1 if unreachable 
for row in range(n):
	graph.append(list(map(int, input(f"Enter the {row+1}th row: ").split())))


result = floyds_algo(graph)
for row in result:
	print(row)
