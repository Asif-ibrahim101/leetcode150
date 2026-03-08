# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

from collections import deque

def bfs(root):
    if root is None:
        return []
    
    queue = deque([root])
    result = []
    left_to_right = True

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
        
        if left_to_right:
            result.append(level)
        else:
            result.append(level[::-1])
        
        left_to_right = not left_to_right

    return result