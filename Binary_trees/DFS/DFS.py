def DFS(node):
    #base case cause we use recurssion for DFS
    if node == None:
        return

    DFS(node.left)
    DFS(node.right)

    return