class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end="")
    inorder(root.right)
    return root

def preorder(root):
    if root is None:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.data, end="")
    return root

def postorder(root):
    if root is None:
        return
    print(root.data, end="")
    postorder(root.left)
    postorder(root.right)
    return root     

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)

inorder(root)
preorder(root)
postorder(root)