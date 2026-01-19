class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Tree:
    def create_node(self,data):
        return Node(data)
    
    def insert_node(self,data,node):
        if node is None:
            return self.create_node(data)
        
        if data< node.data:
            node.left=self.insert_node(data,node.left)
        else:
            node.right=self.insert_node(data,node.right)
        
        return node 
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,"->")
            self.inorder(root.right)
    
    def preorder(self,root):
        if root:
            print(root.data,"->")
            self.preorder(root.left)
            self.preorder(root.right)
    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,"->")

if __name__=="__main__":
    tree=Tree()
    
    root=None
    
    values=[1,2,3,4,5,6]
    for i in values:
        root=tree.insert_node(i,root)
        
    print("Inorder Traversal:\n")
    tree.inorder(root)
    
    print("Preorder Traversal:\n")
    tree.preorder(root)
    
    print("Postorder Traversal:\n")
    tree.postorder(root)
            
        