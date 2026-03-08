from collections import deque

def bfs(root):
    if root is None:
        return
    
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
    
    return result