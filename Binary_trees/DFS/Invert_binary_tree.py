# Write a DFS function that inverts a binary tree (mirror it). 
# Every left child becomes the right child and vice versa, for every node in the tree. 
# Return the root.

def dfs(node):
    if node == None:
        return 0
    
    left = dfs(node.left)
    right = dfs(node.right)

    #swap the vales
    node.left, node.right = node.right, node.left

    return node

