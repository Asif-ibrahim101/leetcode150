class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def postOrder(node):
        if node == node:
            return
        
        dfs(node.left)
        dfs(node.right)

        #we do the logic after we have reached the leaf node
        print(node.val)
