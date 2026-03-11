from collections import deque

def bfs(graph, start):
    visited = set() #it tracks what we have seen
    queue = deque([start]) #here we start the queue with the starting node

    #here we have to mark the start as visited when we add it to the queue
    visited.add(start)

    #we keep going until the end of the queueu [there is nothing left to look]
    while queue:
        node = queue.popleft() #take the node form the front of the queue it generanteds the level by levle order of the bfs
        print(node)

        for neighbour in graph[node]: #here we check all the neighbours of the curr node
            if neighbour not in visited: #only add the unvisited nodes if the curr node already visited

                #here mark the node visited and also add to the queue together
                visited.add(neighbour)
                queue.append(neighbour)
