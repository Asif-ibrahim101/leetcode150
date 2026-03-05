# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case for recurssion
        if root == None:
            return 0
        
        #process the dfs we will to down left and right until we find a leaf node
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        maxNode = max(left, right) + 1 #this is the maximum depth

        return maxNode