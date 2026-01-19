class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def create_node(self,data):
        return Node(data)
    
    def insert_node(self,root,data):
        if root is None:
            return self.create_node(data)
        
        if data < root.data:
            root.left=self.insert_node(root.left,data)
        else:
            root.right=self.insert_node(root.right,data)
        return root