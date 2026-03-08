# Given the root of a binary tree, return the sum of values of its deepest leaves.
 

# Example 1:


# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = []
        
        while queue:
            curr_level = len(queue)
            level = []
            
            for _ in range(curr_level):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            result.append(level)
        
        return sum(result[-1])
                
            
        