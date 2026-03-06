# **Practice Question 6:**

# Given a binary tree, write a DFS function that returns its **diameter**. The diameter is the length of the **longest path between any two nodes** in the tree. This path may or may not pass through the root.

# The length is measured in **number of edges** (not nodes).
# ```
#       1
#      / \
#     2    3
#    / \
#   4    5

def diameterOfBinaryTree(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter

        if node == None:
            return 0
        

        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter, left + right)

        return max(left, right) + 1
    
    dfs(root)
    return diameter