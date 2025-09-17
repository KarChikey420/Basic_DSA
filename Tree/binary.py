class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Binary_Tree(root,key):
    if root is None:
        return Node(key)
    if key<root.data:
        root.left=Binary_Tree(root.left,key)
    else:
        root.right=Binary_Tree(root.right,key)
    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end='')        
        inorder(node.right)
        
def preoder(node):
    if node:
        print(node.data,end='')
        preoder(node.left)
        preoder(node.right)
        
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data,end='')
        
number=[1,2,3,4,5,6,7,8]
root=None
for num in number:
    root=Binary_Tree(root,num)

print('inorder')
inorder(root)
print('\npreorder')
preoder(root)
print('\npostorder')
postorder(root)