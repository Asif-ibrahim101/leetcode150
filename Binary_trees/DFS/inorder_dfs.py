def dfs(node):
    if node == None:
        return
    
    dfs(node.left)

    #we call the left side than perform loggic in the current node than go to the right side
    print(node.val)
    dfs(node.right)

    return