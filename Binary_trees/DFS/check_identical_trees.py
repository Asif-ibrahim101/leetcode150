def dfs(node1, node2):
    if node1 == None and node2 == None:
        return True
    
    if node1 == None or node2 == None:
        return False
    
    if node1.val != node2.val:
        return False
    

    left = dfs(node1.left, node2.left)
    right = dfs(node1.right, node2.right)

    return left and right

