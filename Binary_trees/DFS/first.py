# #typical way to traverse a linkdlist
# def get_sum(head):
#     sum = 0

#     while head:
#         sun += head.val
#         head = head.next
    
#     return sun

# def dfs(node):
#     if node == None:
#         return 0
    

#     left = dfs(node.left)
#     right = dfs(node.right)
#     max_depth = max(left, right) + 1

#     return max_depth

# Write a DFS function that returns the sum of all node values in a binary tree. Empty tree returns 0.
def dfs(node):
    if node == None:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)

    return (node.val + left + right)
    