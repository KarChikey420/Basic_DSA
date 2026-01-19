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
        
        if data < node.data:
            node.left=self.insert_node(data,node.left)
        else:
            node.right=self.insert_node(data,node.right)

        return node

if __name__=="__main__":
     
     tree=Tree()
     
     root=None
     
     values=[1,2,3,4,5,6] 
     for i in values:
         root=tree.insert_node(i,root)