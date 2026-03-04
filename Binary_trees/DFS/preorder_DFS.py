def dfs(node):
    if node == None:
        return
    
    #the logic is done on the current node bofore we move to the childern
    print(node.val)

    dfs(node.left)
    dfs(node.right)
    return