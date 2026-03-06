# Write a DFS function that returns the minimum value in a binary tree (not a BST — values can be anywhere). Assume the tree is non-empty.
# Hint: same template — base case, recursive calls, combine. The only thing that changes is the combine step.

def dfs(node):
    #base case
    if node == None:
        return float('inf')#we will return float(inf) for the minimum problems and flaot(-inf) for the max problems

    #recurssive functions
    left = dfs(node.left)
    right = dfs(node.right)

    min_vale = min(node.val, left, right)

    return min_vale

# Write a DFS function that takes a binary tree and a target integer, 
# and returns `True` if **any root-to-leaf path** has a sum equal to the target.
#  This is the classic **Path Sum** problem.

# Example: target = 8 on this tree returns True because 5 → 3 = 8.

def dfs(node, target):
   if node == None:
        return False
    
    if node.left == None and node.right == None:
        return node.val == target
    

    left = dfs(node.left, target - node.val)
    right = dfs(node.right, target- node.val)

    return left or right





