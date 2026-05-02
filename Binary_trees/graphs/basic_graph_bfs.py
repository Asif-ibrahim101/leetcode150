#Good nodes in a tree

#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#Return the number of good nodes in the binary tree.

def dfs(node, max_node):
    if node == None:
        return 0
    

    left = dfs(node.left, max(max_node, node.val))
    right = dfs(node.right, max(max_node, node.val))

    ans = left + right
    if node.val >= max_node_far:
        ans += 1
            
        return ans
        
    return dfs(root, float("-inf"))
