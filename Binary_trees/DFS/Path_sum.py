# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

class solution:
    def hasPathSum(self, root: optional[TreeNode], targetSum: int) ->bool:
       def dfs(node, currSum):
        #the base case
        if node == None:
            return False
        
        if node.left == None and node.right == None:
            return (node.val + currSum) == targetSum
        
        currSum += node.val
        left = dfs(node.left, currSum)
        right = dfs(node.right, currSum)

        return left or right
    
    return dfs(root, 0)