#find lowest common ancestor

#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

def dfs(node, p, q):
    #this is the base case
    #check of the main node extits or not in the first place
    if node == None:
        return 0
    
    #check if the nodes are p and q or not
    if node == q or node == p:
        return root
    
    #now get the left and right
    left = dfs(node.left, p, q)
    right = dfs(node.right, p, q)

    if left and right:
        return root 
    
    return left if left else right