from collections import deque

def level_order_traversal(root):
    ans=[]
    
    if root is None:
        return ans
    
    q=deque([root])
    
    while q:
        l=len(q)
        level=[]
        
        for _ in range(l):
            node=q.popleft()
            level.append(node.data)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans