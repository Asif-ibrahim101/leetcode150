#for undirected not weighted graph

# vertex, edges = map(int, input().split())

# adj_mat = [[False] * vertex for _ in range(vertex)]

# for _ in range(edges):
#     u, v = map(int, input().split())
#     adj_mat[u][v] = True
#     adj_mat[v][u] = True

# for row in adj_mat:
#     print(' '.join(str(int(cell)) for cell in row))

#for undirected weighted graph
# vertex, edges = map(int)

# adj_mat = [[False] * vertex for _ in range(vertex)];

# for _ in range(edges):
#     u, v, w = map(int)
#     adj_mat[u][v] = w
#     adj_mat[v][u] = w

# for row in adj_mat:
#     print(row)

#for directed weighted graph
# vertex, edges = map(int)

# adj_mat = [[False] * vertex for _ in range(vertex)];

# for _ in range(edges):
#     u, v, w = map(int)
#     adj_mat[u][v] = w

# for row in adj_mat:
#     print(row)