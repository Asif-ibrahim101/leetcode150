#basic dfs in graphs
def dfs(graph, node, visited):
    #before doing anything we check that have we seen it before
    #prevents infinite loop in graph cycle
    if node in visited:
        return
    
    visited.add(node) #here we mark the node as seen
    print(node) #here we process the node as the question

    for neighbour in graph[node]: #here we look at everyone the node is connected to
        dfs(graph, neighbour, visited) #here we recursively dive into each neighbour
