#for most of the cases covert the edge list to a adjaceny list


#for undirected graphs
edge = [[0, 1], [1, 2], [2, 3]]
n = 4

adjaceny_list = [[] for _ in range(n)]

for u, v in edge:
    edge[u].append(v)
    edge[v].append(u)


#for directed graphs
adjaceny_list_1 = [[] for _ in range(n)]

for u, v in range(edge):
    edge[u].append(v
    )
