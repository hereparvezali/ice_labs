def welsh_powell(adj):
	V = len(adj)

	def deg(v): return len(adj[v])

	color = [-1] * V

	for v, _ in sorted(enumerate(adj), key=lambda x: -deg(x[0])):
		available_colors = set(range(V)) - {color[adj_v] for adj_v in adj[v]}
		color[v] = next(iter(available_colors))

	return color

adj_list = [[1,2],[0,2,3],[0,1,3],[1,2,4],[3,5,6],[4,6],[4,5]]

print(*enumerate(welsh_powell(adj_list)))
