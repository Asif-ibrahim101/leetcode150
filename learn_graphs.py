#path sum
# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

def dfs(root, targetSum):
    #base case
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return (root.val + curr_sum) == targetSum
    

    curr_sum += root.val
    left = dfs(root.left, curr_sum)
    right = dfs(root.right, curr_sum)

    return left or right


